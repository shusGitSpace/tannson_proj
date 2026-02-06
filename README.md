Status: In-Progress

The following scripts contain the data preprocessing pipeline for Tannson Tech, a computer and phone repair store located in Egg Harbor Township, New Jersey (https://www.tannsontech.com/). The company has been in business for over a decade, and, though successful, has yet to establish a definitive system for deriving financial or service metrics. Per routine practice, all invoices are stored in individual Excel files as free text, which makes it more difficult to identify business performance.

The objective of this project is to design a data preprocessing pipeline that extracts available key metrics from yearly invoice data, such as revenue and most-utilized service categories, so that a more comprehensible overview of performance can be attained.

For the company's convenience, the pipeline should
1. not alter any part of Tannson Tech's current business operations
2. allow the company to continue using the same Excel template as usual
3. be reusable as long as similarly-structured data is used.

Upon the completion of this project, a data visualization using PowerBI would be created to communicate insights.

Files included:
* test.ipynb and tannson_fnc.py extract key data from each invoice
* export_extracts.ipynb transforms each invoice into a Pandas DataFrame row
* order_details.json contains each invoice's order details, including date of transaction, item in need of service, and service
* monetary_details.json contains each invoice's financial details, including revenue, tax, and payment method
* regex.ipynb and tannson_re.py standardize free text
* main.ipynb houses the main data pipeline
* convert_to_py.ipynb converts code in Jupyter notebooks to Python files
