#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd

# Exclude obvious non-key words:
exclude_words = [
    'paid', 'total', 'tax', 'free', 'discount',
    r'\d{4}-\d{2}-\d{2}', 'problem', 'solution', 'customer', 
    'imei', 'diagnostic', 'model', 'serial', 'deposit',
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',
    r'^SN:\s?[A-Z0-9]{4,20}$', 'password',
]

# Find item keys: (Include Playstation? PS4? Onsite?)
items = [
    'iphone', 'samsung', 'lg', 'asus', 'acer',
    'dell', 'hp', 'macbook', 'epik', 'moto',
    'ipad', 'galaxy', 'lenov', 'imac', 'sony', 
    'google', 'mac', 'xbox', 'kindle', 'core innovation',
    'gateway', 'ipod', 'toshiba', 'metropcs', 'nexus',
    'alcatel', 'fujitsu', 'watch', 'michael kors', 'amazon',
    'msi', 'oneplus', 'alienware', 'huawei', 'microsoft', 
    'kazuna', 'seagate', r't-?mobile', 'droid', 'nokia', 
    'notebook', 'rca', 'ps5', 'ps4', 'steam', 
    'tablet', 'laptop', 'desktop', 'earbuds', 'system',
    'onsite', 'playstation', 'pc', 'computer', 'phone',
    'razer'
]

# Find service keys:
services = [
    'replace', 'repair', 'install', 'reinstall', 'remove',
    'restore', 'resolve', 'update', 'upgrade', 'change', 
    'fix', 'reset', 'reconfigure', 'configure', 'recover', 
    'clean', 'transfer', 'unlock', 'set', 'enable', 
    'check', 'reattach', 'solution', 'customize', 'make',
    'swap', 'issue', 'boot', 'wont', 'screen',
    'button', 'labor', 'void', 'courtesy', 'refresh',
]

service_keys = '|'.join(services)
item_keys = '|'.join(items)
# item_keys = rf'^(?!.*\b(?:{service_keys})\b).*?(?:{item_keys})'

filter_out = exclude_words + items + services

conditions = '|'.join(filter_out)

def assign_data(df, file):
    """Assign data from each df to appropriate column by extracting the first valid value in each category."""
    # Standardize free text
    df.loc[:, 'Text'] = df['Text'].str.strip().str.upper()

    # Extract date string and convert to datetime object
    date = pd.to_datetime(df['Text'], errors='coerce').dropna()

    # Substitute missing dates with last modified date of file
    timestamp = pd.to_datetime(os.path.getmtime(file), unit='s')
    date = null_date(date, timestamp)

    # Extract item(s) of concern based on keys in item key list
    items = df.loc[df['Text'].str.contains(item_keys, case=False, na=False, regex=True), 'Text']

    # Extract service(s) performed based on keys in service key list
    services = df.loc[df['Text'].str.contains(service_keys, case=False, na=False), 'Text']

    # Get price for each service performed
    prices = df.loc[services.index, 'Numeric'].dropna()

    # Extract payment method
    payment = df.loc[df['Text'].str.contains('paid|diagnostic', case=False, na=False), 'Text']

    # Extract subtotal
    subtotal = df.loc[df['Text'].str.contains(r'^sub-total$', case=False, na=False, regex=True), 'Numeric'].dropna()

    # Extract tax
    tax = df.loc[df['Text'].str.contains(r'\bnj\b.*?\btax$', case=False, na=False), 'Numeric'].dropna()

    # Extract discount
    discount = df.loc[df['Text'].str.contains('discount', case=False, na=False), 'Numeric'].dropna()

    if discount.size == 1:
        discount = float(discount.iloc[0])
    else:
        discount = 0

    # Extract total
    total = df.loc[df['Text'].str.contains(r'^total$', case=False, na=False, regex=True), 'Numeric'].dropna()

    # Get refund value, if any
    refund = df.loc[df['Text'].str.contains('refund|return payment|return cash', case=False, na=False), 'Numeric'].dropna()

    # Check for key word matches & valid numeric vals
    text_s = [items, services, payment]
    float_s = [subtotal, tax, total, refund]

    text_list = []
    float_list = []

    for s in text_s:
        s = fallback_text(s)
        text_list.append(s)

    for s in float_s:
        s = fallback_float(s)
        float_list.append(s)

    items = text_list[0]
    services = text_list[1]
    payment = text_list[2]
    subtotal = float_list[0]
    tax = float_list[1]
    total = float_list[2]
    refund = float_list[3]
    prices = fallback_price(prices, subtotal)

    # Capture any service not in service key words
    if not services:
        services = 'OTHER'

    # Return structured df
    o_details = pd.DataFrame([{
        'Date': date,
        'Item': items,
        'Service': services,
        'Price': prices
    }])

    m_details = pd.DataFrame([{
        'Date': date,
        'Payment Method': payment,
        'Subtotal': subtotal,
        'Discount': discount,
        'Tax': tax,
        'Total': total,
        'Refund Amt': refund
    }])

    return o_details, m_details

def null_date(date, timestamp):
    """Substitute missing date with the file's last modified date."""
    if len(date) == 1:
        return date.iloc[0]

    return timestamp

def fallback_text(text_s):
    """
    Return the sole value if there is only one match.
    Return a list of all values if there is more than one match.
    Otherwise, return empty list.
    """
    if len(text_s) == 1:
        return text_s.iloc[0]
    elif len(text_s) > 1:
        return list(text_s)
    return None

def fallback_float(float_s):
    """
    Return the float value if available.
    Otherwise, return None.
    """
    float_s = pd.to_numeric(float_s, errors='coerce').dropna()
    if len(float_s) > 0:
        return float(float_s.iloc[0])
    return None

def fallback_price(prices, subtotal):
    """
    Return float price(s) if available.
    Return subtotal if subtotal is not null.
    Otherwise, return an empty list.
    """
    prices = pd.to_numeric(prices, errors='coerce').dropna()
    if len(prices) == 1:
        return float(prices.iloc[0])
    elif len(prices) > 1:
        return [float(p) for p in prices]
    elif pd.notna(subtotal):
        return subtotal
    return None

def main():
    """Execute main test code."""
    # Load raw file
    main_df = pd.read_csv(r'C:\Users\shuju\Desktop\Tannson_Tech_Project\raw_data.csv', names=['Text', 'Quantity', 'Numeric'], skiprows=1)
    pd.set_option('display.max.rows', 5000)

    # TEST FUNCTION:
    main_df['Text'] = main_df['Text'].str.strip().str.upper() # Standardize raw data
    unique_text = pd.Series(main_df['Text'].unique()) # Extract unique instances
    test = unique_text[~unique_text.str.contains(conditions, case=False, na=False)] # Filter test
    print("Current length:", test.size)

    test = main_df.iloc[17045:17058,] # 'D:\INVOICE\P GREGORY JEAN EXANTUS.xls'
    return assign_data(test, r'D:\INVOICE\P AARON JOHNSON.xls') # File info different from test info

# o_df, m_df = main()

