#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

# Standardize Items:

item_dict = {
    'APPLE' : {
        'PHONE': [
            ('IPHONE 3GS', re.compile(r'\bIPHONE\s*3\s*GS\b')),
            ('IPHONE 3', re.compile(r'\bIPHONE\s*3\b')),
            ('IPHONE 4S', re.compile(r'\bIPHONE\s*4\s*S\b')),
            ('IPHONE 4', re.compile(r'\bIPHONE\s*4\b')),
            ('IPHONE 5C', re.compile(r'\bIPHONE\s*5\s*C\b')),
            ('IPHONE 5S', re.compile(r'\bIPHONE\s*(?:5\s*S|S5)\b')),
            ('IPHONE 5', re.compile(r'\bIPHONE\s*5\b')),
            ('IPHONE 6 PLUS', re.compile(r'\bIPHONE\s*6\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 6S PLUS', re.compile(r'\bIPHONE\s*6\s*S\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 6S', re.compile(r'\bIPHONE\s*6\s*S\b')),
            ('IPHONE 6', re.compile(r'\bIPHONE\s*6\b')),
            ('IPHONE 7 PLUS', re.compile(r'\bIPHONE\s*7\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 7', re.compile(r'\bIPHONE\s*7\b')),
            ('IPHONE 8 PLUS', re.compile(r'\bIPHONE\s*8\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 8', re.compile(r'\bIPHONE\s*8\b')),
            ('IPHONE 11 PRO MAX', re.compile(r'\bIPHONE\s*11\s*PRO\s*MAX\b')),
            ('IPHONE 11 PRO', re.compile(r'\bIPHONE\s*11\s*PRO\b')),
            ('IPHONE 11', re.compile(r'\bIPHONE\s*11\b')),
            ('IPHONE 12 PRO MAX', re.compile(r'\bIPHONE\s*12\s*PRO\s*MAX\b')),
            ('IPHONE 12 PRO', re.compile(r'\bIPHONE\s*12\s*PRO\b')),
            ('IPHONE 12 MINI', re.compile(r'\bIPHONE\s*12\s*MINI\b')),
            ('IPHONE 12', re.compile(r'\bIPHONE\s*12\b')),
            ('IPHONE 13 PRO MAX', re.compile(r'\bIPHONE\s*13\s*PRO\s*MAX\b')),
            ('IPHONE 13 PRO', re.compile(r'\bIPHONE\s*13\s*PRO\b')),
            ('IPHONE 13', re.compile(r'\bIPHONE\s*13\b')),
            ('IPHONE 14 PLUS', re.compile(r'\bIPHONE\s*14\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 14 PRO MAX', re.compile(r'\bIPHONE\s*14\s*PRO\s*MAX\b')),
            ('IPHONE 14 PRO', re.compile(r'\bIPHONE\s*14\s*PRO\b')),
            ('IPHONE 14', re.compile(r'\bIPHONE\s*14\b')),
            ('IPHONE 15 PLUS', re.compile(r'\bIPHONE\s*15\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 15 PRO MAX', re.compile(r'\bIPHONE\s*15\s*PRO\s*MAX\b')),
            ('IPHONE 15 PRO', re.compile(r'\bIPHONE\s*15\s*PRO\b')),
            ('IPHONE 15', re.compile(r'\bIPHONE\s*15\b')),
            ('IPHONE 16 PLUS', re.compile(r'\bIPHONE\s*16\s*(?:\+|PLUSS*)\b')),
            ('IPHONE 16 PRO MAX', re.compile(r'\bIPHONE\s*16\s*PRO\s*MAX\b')),
            ('IPHONE 16 PRO', re.compile(r'\bIPHONE\s*16\s*PRO\b')),
            ('IPHONE 16', re.compile(r'\bIPHONE\s*16\b')),
            ('IPHONE SE', re.compile(r'\bIPHONE\s*(?:SE|5\s*SE|8\s*SE|SE2)\b')),
            ('IPHONE XR', re.compile(r'\bIPHONE\s*XR\b')),
            ('IPHONE XS MAX', re.compile(r'\bIPHONE\s*XS\s*MAX\b')),
            ('IPHONE XS', re.compile(r'\bIPHONE\s*XS\b')),
            ('IPHONE X', re.compile(r'\bIPHONE\s*X\b')),
            ('IPHONE MODEL', re.compile(r'\bIPHONE\b'))
        ],

        'COMPUTER': [
            ('IMAC', re.compile(r'\bIMAC\b')),
            ('MACBOOK PRO', re.compile(r'\bMAC\s*BOOK\s*PRO\b')),
            ('MACBOOK AIR', re.compile(r'\bMAC\s*BOOK\s*AIR\b')),
            ('MACBOOK', re.compile(r'\bMAC\s*BOOK\b')),
            ('MAC PRO', re.compile(r'\bMAC\s*(?:PRO\s*)?(?:TOWER|PRO)\b')),
            ('UNCLASSIFIED', re.compile(r'\bMAC\b'))
        ],

        'TABLET': [
            ('IPAD (2ND GEN)', re.compile(r'\bIPAD\s*2(?:ND)?\b')),
            ('IPAD (4TH GEN)', re.compile(r'\bIPAD\s*4(?:TH)?\b')),
            ('IPAD (5TH GEN)', re.compile(r'\bIPAD\s*5(?:TH)?\b')),
            ('IPAD (6TH GEN)', re.compile(r'\bIPAD\s*6(?:TH)?\b')),
            ('IPAD (7TH GEN)', re.compile(r'\bIPAD\s*7(?:TH)?\b')),
            ('IPAD (8TH GEN)', re.compile(r'\bIPAD\s*8(?:TH)?\b')),
            ('IPAD (9TH GEN)', re.compile(r'\bIPAD\s*9(?:TH)?\b')),
            ('IPAD (10TH GEN)', re.compile(r'\bIPAD\s*10(?:TH)?\b')),
            ('IPAD AIR', re.compile(r'\bIPAD\s*AIR\b')),
            ('IPAD PRO', re.compile(r'\bIPAD\s*PRO\b')),
            ('IPAD MINI', re.compile(r'\bIPAD\s*MINI\b')),
            ('IPAD MODEL', re.compile(r'\bIPAD\b')),
        ],

        'MEDIA PLAYER': [
            ('IPOD CLASSIC', re.compile(r'\bIPOD\s*CLASSIC\b')),
            ('IPOD TOUCH', re.compile(r'\bIPOD\s*TOUCH\b')),
            ('IPOD MODEL', re.compile(r'\bIPOD\b')),
        ],

        'OTHER': [
            ('WATCH', re.compile(r'\b(?:APPLE\s*WATCH|IWATCH)\b'))
        ],
    },

    'SAMSUNG': {
        'PHONE': [
            ('GALAXY A', re.compile(r'\b(?:SAMSUNG?\s*GALAXY|SAMSUNG|GALAXY)\s*A\d{1,3}\w*\b')),
            ('GALAXY J', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*(?:SM-?J|J)\d{1,3}\w*\b')),
            ('GALAXY S', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\b.*\b(?:(SM-?)?(?:G9|S9)|I|S)(?:\d{1,3})?(?:\+|\w*)\b')),
            ('GALAXY CORE', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*(?:SM-?G36|CORE)\w*\b')),
            ('GALAXY GRAND', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*(?:SM-?G53|GRAND)\w*\b')),
            ('GALAXY NOTE', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*(?:SM-?N|N|NOTE)\s*\d{1,4}(?:\+|\w*)\b')),
            ('GALAXY Z FLIP', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*Z?\s*FLIP\s*\d?\b')),
            ('GALAZY Z FOLD', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*Z?\s*FOLD\s*\d?\b')),
            ('GALAXY MEGA', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*MEGA\b')),
            ('GALAXY EXPRESS', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*EXPRESS\b')),
            ('GALAXY ON', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\b.*\bON\s*\d{1}\b')),
            ('GALAXY XCOVER', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*XCOVER\b')),
            ('INTENSITY', re.compile(r'\b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*(?:SCH-?U|U)\d{3}\b')),
            ('UNCLASSIFIED', re.compile(r'\b(?:SAMSUNG\s*PHONE|GALAXY)\b'))
        ],

        'TABLET': [
            ('GALAXY TAB', re.compile(r"""
            \b(?:SAMSUNG\s*GALAXY|SAMSUNG|GALAXY)\s*
            (?:
                SM-?(?:T|P)\d{3,4}\w*
                |T-?\d{3}\w*
                |TAB\s*\w*
                |GT-?N
                |TABLET
                )\w*\b""", re.VERBOSE)),
        ],

        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bSAMSUNG\s*(?:CHROME(?:\s*BOOK)?|LAPTOP|NOTEBOOK|CHRONOS|NP\d{3}\w*)\b')),
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bSAMSUNG\b'))
        ]
    },

    'MICROSOFT': {
        'TABLET': [
            ('SURFACE', re.compile(r'\bMICROSOFT\s*SURFACE\s*(?:PRO|\d{1})\b')),
        ],

        'OTHER': [
            ('GAME CONSOLE', re.compile(r'\bXBOX\b')),
        ],

        'UNCLASSIFIED': [
            ('SURFACE', re.compile(r'\bMICROSOFT\s*SURFACE\b'))
        ]
    },

    'GOOGLE': {
        'PHONE': [
            ('PIXEL', re.compile(r'\bGOOGLE\s*PIXEL(?:\s*\d{1}\w*)?\b')),
            ('NEXUS', re.compile(r'\b(?:GOOGLE\s*)?NEXUS\b')),
        ],
    },

    'NOKIA': {
        'PHONE': [
            ('LUMIA', re.compile(r'\bNOKIA\b.*\bLUMIA\b')),
            ('X SERIES', re.compile(r'\bNOKIA\s*X(?:\d{3})?\b'))
        ]
    },

    'ASUS': {
        'TABLET': [
            ('TRANSFORMER', re.compile(r'\bASUS\b.*\bTF\s*\d{3}\b')),
            ('NEXUS', re.compile(r'\bASUS\b.*\bNEXUS\b')),
            ('ZENPAD', re.compile(r'\bASUS\b.*\bZENPAD\b')),
            ('UNCLASSIFIED', re.compile(r'\bASUS\s*TABLET\b'))
        ],

        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bASUS\b.*\b(?:LAPTOP|(?:NET|NOTE|CHROME|VIVO|ZEN)BOOK?)\b')),
            ('DESKTOP', re.compile(r'\bASUS\b.*\b(?:PC|ALL[\s\-]?IN[\s\-]?ONE)\b')),
        ],

        'PHONE': [
            ('ZENFONE', re.compile(r'\bASUS\b.*\b(?:PHONE|ZENFONE|ZENPHONE)\b'))
        ],

        'OTHER': [
            ('MOTHERBOARD', re.compile(r'\bASUS\b.*\bMOTHERBOARD')),
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bASUS\b'))
        ]
    },

    'CORE INNOVATION': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bCORE\s*INNOVATION\b.*\bLAPTOP\b')),
        ],
    },

    'DELL': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r"""
            \b(?:DELL\b.*\b
                (?:
                    LAPTOP
                    |CHROMEBOOK
                    |NOTEBOOK
                    |LATITUDE
                    |N\d{4}
                    |\d{2}
                    |G{1,2}
                    |PRECISION\s*(?:\d{2}|M\d{4})
                    |STUDIO\s*(?:\d{2}|XPS)
                    |XPS\s*(?:\d{2}|M\d{4})
                    |I[A-Z]+ON\s*(?:\d{2}|\d{1}5\d{2}|N\d{4})
                    |VOSTRO\s*(?!3470)(?!3670)(?!3888)\d{4}
                )
                |ALIENWARE\s*(?:\d{2}|\w\d))\b""", re.VERBOSE)),
            ('DESKTOP', re.compile(r"""
            \bDELL\b.*\b
            (?:
                DESKTOP
                |PC
                |ALL(?:\s*|-)IN(?:\s*|-)ONE
                |AIO
                |OPTIPLEX
                |DIMENSION
                |PRECISION\s*(?:T|R)\d{4}
                |STUDIO\s*ONE
                |XPS\s*8\d{3}
                |I[A-Z]+ON\s*(?:\d{3,4}|ONE)
                |VOSTRO\s*(?:\d{3}|3470|3670|3888)
                \b)""", re.VERBOSE)),
            ('UNCLASSIFIED', re.compile(r'\b(?:DELL\s*(?:COMPUTER|PRECISION|STUDIO|XPS|I[A-Z]+ON|VOSTRO)|ALIENWARE)\b'))
        ],

        'TABLET': [
            ('VENUE', re.compile(r'\bDELL\s*VEN[A-Z]{2}\b')),
            ('UNCLASSIFIED', re.compile(r'\bDELL\b.*\bTABLET'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bDELL\b')),
        ]
    },

    'HP': {
        'OTHER': [
            ('PRINTER', re.compile(r'\bHP(?:\s*PRINTER|\s*ENVY\s*PHOTO)'))
        ],

        'COMPUTER': [
            ('DESKTOP', re.compile(r"""
            \bHP\b
            (?:
                \b.*\bDESKTOP\b
                |\b.*\bPC
                |\b.*\bALL(?:\s*|-)IN(?:\s*|-)ONE\b
                |\b.*\bTOWER\b
                |\s*SLIMLINE
                |\s*ENVY\s*2\d
                |\s*PAVILION\s*2\d
                |\s*2\d{1}\b
                |\s*110
                )""", re.VERBOSE)),
            ('LAPTOP', re.compile(r"""
             \bHP
            (?:
                \b.*\bLAPTOP\b
                |\b.*\bTOUCH
                |\s*CHROMEBOOK\b
                |\s*NOTEBOOK\b
                |\s*PROBOOK\b
                |\s*ELITEBOOK\b
                |\s*STREAM\b
                |\s*SPECTRE\b
                |\s*DV
                |\s*ENVY\s*(?:1\d|X\d{3}|DM|M)
                |\s*PAVILION\s*(?:1\d|X\d{3}|DM|M)
                |\s*\d{1,4}(?:-\w+)?
                |\s*G\d{2}
                )""", re.VERBOSE)),
            ('UNCLASSIFIED', re.compile(r'\bHP\s*(?:COMPUTER|PAVILION|ENVY)\b')),
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bHP\b')),
        ],
    },

    'LG': {
        'PHONE': [
            ('FORTUNE', re.compile(r'\bLG\s*FORTUNE\b')),
            ('REVERE', re.compile(r'\bLG\s*REVERE\b')),
            ('VELVET', re.compile(r'\bLG\s*VELVET\b')),
            ('G SERIES', re.compile(r'\bLG\b.*\bG\d{1,2}\b')),
            ('K SERIES', re.compile(r'\bLG\s*K\d{1,3}\b')),
            ('V SERIES', re.compile(r'\bLG\s*V\d{2}\b')),
            ('Q SERIES', re.compile(r'\bLG\s*Q\d')),
            ('STYLO', re.compile(r'\bLG\s*(?:STYLO|STYLUS)\b.*\b\d{1,2}\b')),
            ('UNCLASSIFIED', re.compile(r'\bLG[-\s]*(?:LS|MS|VS|VN|VX|H|PHONE)\s*(?:\d{3,4})*\w*\b'))
        ],

        'TABLET': [
            ('G PAD', re.compile(r'\bLG\s*G\s*PAD\b')),
            ('UNCLASSIFIED', re.compile(r'\bLG[-\s]*VK\s*\d{3,4}\w*\b'))
        ],

        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bLG\s*(?:LAPTOP|GRAM)\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bLG\b'))
        ]
    },

    'TOSHIBA': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r"""
            \bTOSHIBA\s*
                (?:
                    LAPTOP\b
                    |NOTEBOOK\b
                    |SAT[A-Z]LLITE\b
                    |C(?:\d)?55
                    |L\d{2,3}
                    |S\d{2,3}
                    )""", re.VERBOSE))
        ],

        'TABLET': [
            ('EXCITE', re.compile(r'\bTOSHIBA\s*EXCITE\s*(?:TABLET)?\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bTOSHIBA\b'))
        ]
    },

    'LENOVO': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r"""
            \bLENOVO\s*
            (?:
                LAPTOP\b
                |CHROMEBOOK\b
                |FLEX\b
                |IDEAPAD\b
                |THINKPAD\b
                |T\d{3}\b
                |YOGA\b
                |LEGION\s*(?!T)\w+\b
                |X1\b
                |G\d
                |V\d{2})
                """, re.VERBOSE)),
            ('DESKTOP', re.compile(r"""
            \bLENOVO\s*
            (?:
                DESKTOP\b
                |PC\b
                |\b.*\bALL(?:\s*|-)IN(?:\s*|-)ONE\b
                |S\d{3}\b)
                """, re.VERBOSE))
        ],

        'TABLET': [
            ('TAB', re.compile(r'\bLENOVO\s*(?:TAB\s*(?:A|M)\d{1,2})')),
            ('UNCLASSIFIED', re.compile(r'\bLENOVO\s*TABLET\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bLENOVO\b'))
        ],
    },

    'ACER': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r"""
            \bACER\b.*\b
            (?:
                LAPTOP\b
                |CHROME(?:BOOK)?\b
                |NOTEBOOK\b
                |NITRO\b
                |ALPHA\b
                |(?:PREDATOR\b|PH\d{3}-d{2})
                |(?:SPIN\b|SP\d{3}-d{2})
                |(?:SWIFT\b|SF\d{3}-d{2})
                |ASPIRE\s*(?:SWITCH\b|[A-Z]?\d{1,2}(?:-)?|\d{4}[A-Z]?(?:-)?)
                |C\d{3}\b
                )""", re.VERBOSE)),
            ('DESKTOP', re.compile(r"""
            \bACER\b.*\b
            (?:
                DESKTOP\b
                |PC\b
                |\b.*\bALL(?:\s*|-)IN(?:\s*|-)ONE\b
                |AX\d{4}
                )""", re.VERBOSE)),
            ('UNCLASSIFIED', re.compile(r'\bACER\s*(?:ASPIRE)'))
        ],

        'TABLET': [
            ('ICONIA', re.compile(r'\bACER\s*ICONIA\b')),
            ('UNCLASSIFIED', re.compile(r'(?:ACER|TABLET)\s*(?:TABLET|ACER)'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bACER\b'))
        ]
    },

    'MOTOROLA': {
        'PHONE': [
            ('DROID', re.compile(r'\b(?:MOTO|MOTOROLA)\s*DROID\b')),
            ('EDGE', re.compile(r'\b(?:MOTO|MOTOROLA)\s*EDGE\b')),
            ('MOTOROLA ONE', re.compile(r'\b(?:MOTO|MOTOROLA)\b.*\bONE\b')),
            ('MOTO G', re.compile(r'\b(?:MOTO|MOTOROLA(?:\s*MOTO)?)\s*G(?:\s*\d{1,2}|\b)')),
            ('MOTO Z', re.compile(r'\b(?:MOTO|MOTOROLA(?:\s*MOTO)?)\s*Z(?:\s*\d{1,2}|\b)')),
            ('MOTO E', re.compile(r'\b(?:MOTO|MOTOROLA(?:\s*MOTO)?)\s*E(?:\s*\d{1,2}|\b)')),
            ('MOTO X', re.compile(r'\b(?:MOTO|MOTOROLA(?:\s*MOTO)?)\s*X(?:\s*\d{1,2}|\b)')),
            ('UNCLASSIFIED', re.compile(r'\b(?:MOTO|MOTOROLA)\s*(?:5G|XT\d{3,4}(?:-\d{1,2})?)\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\b(?:MOTO|MOTOROLA)\b'))
        ]
    },

    'EPIK': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bEPIK\b.*\bLAPTOP\b')),
        ],
    },

    'BLU': {
        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bBLU\b'))
        ]
    },

    'SONY': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bSONY\b.*\b(?:LAPTOP|NOTEBOOK|VAIO\s*VPC(?:E|F|S|Z|C)\w+)\b')),
            ('DESKTOP', re.compile(r'\bSONY\b.*\b(?:DESKTOP|PC|VAIO\s*VPC(?:J|L)\w+)\b')),
            ('UNCLASSIFIED', re.compile(r'\bSONY\s*VAIO(?!.*\bADAPT[A-Z]R)\b'))
        ],

        'PHONE': [
            ('XPERIA', re.compile(r"""
            \bSONY\s*
            (?:
                XP[A-Z]+IA
                |X(?:[A-Z]{1}(?:\w)?|10)
                |ERICSSON\s*(?:Z|C|E|M|L|X)\w{1}
                |(?:Z|C|E|M|L|X)\w{1}
                )\b""", re.VERBOSE)), # More models available
            ('UNCLASSIFIED', re.compile(r'\bSONY\s*(?:PHONE|ERICSSON)\b'))
        ],

        'OTHER': [
            ('GAME CONSOLE', re.compile(r'\b(?:SONY\s*)?(?:PLAYSTATION\s*(?:PS\s*\d|\d)?|PS\d)\b')),
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bSONY\b'))
        ]
    },

    'AMAZON': {
        'TABLET': [
            ('FIRE', re.compile(r'\bAMAZON\s*FIRE\b')),
            ('KINDLE', re.compile(r'\b(?:AMAZON)?\s*KINDLE\b')),
            ('UNCLASSIFIED', re.compile(r'(?:AMAZON|TABLET)\s*(?:TABLET|AMAZON)')) 
        ]
    },

    'HUAWEI': {
        'PHONE': [
            ('NOVA', re.compile(r'\bHUAWEI\b.*\bNOVA\b')),
            ('MATE', re.compile(r'\bHUAWEI\b.*\bMATE\s*')),
            ('NEXUS', re.compile(r'\bHUAWEI\b.*\bNEXUS\b')),
            ('HONOR', re.compile(r'\bHUAWEI\b.*\bHONOR\b'))
        ],

        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bHUAWEI\b.*\bLAPTOP\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bHUAWEI\b'))
        ]
    },

    'GATEWAY': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bGATEWAY\s*(?:LAPTOP\b|NOTEBOOK\b|GWNC|GWTN|NE|NV)')),
            ('DESKTOP', re.compile(r'\bGATEWAY\s*(?:DESKTOP|PC|TOWER|ALL(?:\s*|-)IN(?:\s*|-)ONE)\b')),
            ('UNCLASSIFIED', re.compile(r'\bGATEWAY\s*COMPUTER\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bGATEWAY\b'))
        ]
    },

    'ALCATEL': {
        'PHONE': [
            ('ONETOUCH', re.compile(r'\bALCATEL\s*(?:ONE\s*TOUCH|4\d{3}[A-Z]?)\b')),
            ('GO FLIP', re.compile(r'\bALCATEL\b.*\bFLIP\s*(?:GO)?\b')),
            ('VOLTA', re.compile(r'\bALCATEL\s*VOLTA\b'))
        ],

        'TABLET': [
            ('JOY', re.compile(r'\bALCATEL\s*JOY\s*(?:TAB|TABLET)\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bALCATEL\b'))
        ]
    },

    'T-MOBILE': {
        'PHONE': [
            ('REVVL', re.compile(r'\bT-?MOBILE\s*RE[?:V]+L\b')),
            ('UNCLASSIFIED', re.compile(r'\bT-?MOBILE\s*PHONE\b'))
        ],

        'UNCLASSIFIED': [
            ('PRODUCT', re.compile(r'\bT-?MOBILE\b')),
        ]
    },

    'MSI': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bMSI\s*(?:LAPTOP|SWORD)\b')),
            ('UNCLASSIFIED', re.compile(r'\bMSI\b')) # For consumer ownership purposes
        ]
    },

    'CYBERPOWERPC': {
        'COMPUTER': [
            ('UNCLASSIFIED', re.compile(r'\bCY(B|P)ER(POWER)?PC\b'))
        ]
    },

    'OTHER': {
        'COMPUTER': [
            ('LAPTOP', re.compile(r'\bLAPTOP[A-Z]?\b')),
            ('DESKTOP', re.compile(r'\b(?:DESKTOP|PC)\b')),
            ('UNCLASSIFIED', re.compile(r'\bCOMPUTER\b')),
        ],

        'PHONE': [
            ('UNCLASSIFIED', re.compile(r'\bPHONE\b')),
        ],

        'TABLET': [
            ('UNCLASSIFIED', re.compile(r'\bTABLET\b')),
        ],
    },

    'NOT APPLICABLE': {
        'OTHER': [
            ('ONSITE SERVICE', re.compile(r'\bON\s*SITE\b')),
            ('CUSTOM SYSTEM', re.compile(r'\bCUSTOM(?:IZED|ED)?\b.*?\b(?:SYSTEM|PC|COMPUTER|LAPTOP)\b'))
        ]
    }, 
}

exclude_words = [
    r'\bGLASS\b', r'\bRETURN\b', r'TRADE', r'\bPROBLEM\b',
    r'\bPROTECTOR\b', r'\bSIM TRAY\b', r'\bKEEP\b', r'\bBATH\b', r'\bPAID\b',
    r'\bBAND\b', r'\bDEMO\b', r'\bPICKUP\b', r'\b(?:RESTORING|RESTORE)\b', '@',
    r'\bGOOGLE\sCHROME\b', r'\bSCAN\b', r'\bCUSTOMER\b', r'\bFAILED\b',
    r'\bCORRUPTED\b', r'\bCRASH\b', r'\bSIGNAL\b', r'\bFROZE\b', r'\bSETUP\b', 
    r'\bBAR\b', r'\bADJUST\b', r'\bDISCOUNT\b', r'\bDISABLE\b', r'\bWARRANTY\b',
    r'\bNO\b', r'\bORDERED\b', r'\bGMAIL\b', r'\bCASH\b', r'\bCC\b', r'\bTEMPERED\b',
    r'\bCRASH\b'
]

services_list = [
    # 1
    ('COVER REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b.*?\b
    (?:COVER|HOUSING|CASE|BACK\s*GLASS)\b
    |
    \b(?:COVER|HOUSING|CASE|BACK\s*GLASS)\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b
    """, re.VERBOSE)),

    # 2
    ('SCREEN REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|BROKEN|FIX|NO)\b.*?\b
    (?:SCREEN|TOUCH\s*SCREEN|DIGIT(?:I)?ZE(?:R|D)?|LCD)\b
    |
    \b(?:SCREEN|TOUCH\s*SCREEN|DIGIT(?:I)?ZE(?:R|D)?|LCD)\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX|BROKEN)\b
    """, re.VERBOSE)),

    # 3
    ('BATTERY REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|INSTALL|FIX)\b.*?\b
    BATTER(?:Y)?\b
    |
    \bBATTER(?:Y)?\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|INSTALL|FIX)\b
    """, re.VERBOSE)),

    # 4
    ('POWER SUPPLY/ADAPTER REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b.*?\b
    (?:POWER\s*SUPPLY|ADAPTER)\b
    |
    \b(?:POWER\s*SUPPLY|ADAPTER)\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b
    """, re.VERBOSE)),

    # 5
    ('CHARGING PORT REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX|REATTACH|BROKEN)\b.*?\b
    CHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)\b
    |
    \bCHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX|REATTACH)\b
    """, re.VERBOSE)),

    # 6
    ('BUTTON REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b.*?\b
    BUTTON\b
    |
    \bBUTTON\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b
    """, re.VERBOSE)),

    # 7
    ('STORAGE DRIVE REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b.*?\b
    (?:HD|SSD|HDD)\b
    |
    \b(?:HD|SSD|HDD)\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b
    """, re.VERBOSE)),

    # 8
    ('MISC. HARDWARE REPLACEMENT OR REPAIR', re.compile(r"""
    \b(?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b.*?\b
    (?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |DC\s*JACK
        |HARD\s*DRIVE
        |POWER\s*CHIP
        )\b
    |
    \b(?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |DC\s*JACK
        |HARD\s*DRIVE
        |POWER\s*CHIP
        )\b.*?\b
    (?:REP[A-Z]{3,4}MENT|RE[A-Z]{3}CE(?:D)?|RE[A-Z]{3}R(?:ED)?|FIX)\b
    """, re.VERBOSE)),

     # 9
    ('MALWARE REMOVAL', re.compile(r"""
    \b(?:REMOVE|CLEAN|UNINSTALL)\b.*?\b
    (?:MALWARE|VIRUS|ADWARE)\b
    |
    \b(?:MALWARE|VIRUS|ADWARE)\b.*?\b
    (?:REMOVAL|CLEAN(?:\s*UP)?)\b
    """, re.VERBOSE)),

    # 10
    ('HARDWARE INSTALLATION OR UPGRADE', re.compile(r"""
    \b(?:INSTALL|UPGRADE|UPDATE)\b.*?\b
    (?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |HARD\s*DRIVE
        |POWER\s*CHIP
        |BUTTON
        |CHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)
        |SCREEN
        )\b
    |
    \b(?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |HARD\s*DRIVE
        |POWER\s*CHIP
        |BUTTON
        |CHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)
        |SCREEN
        )\b.*?\b
    (?:INSTALL|UPGRADE|UPDATE)\b
    """, re.VERBOSE)),

    # 11
    ('SOFTWARE INSTALLATION OR UPDATE', re.compile(r"""
    \b(?:INSTALL|UPGRADE|UPDATE)\b.*?\b
    (?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|OFFICE|FIREFOX
        |FACTORY
        |MALWAREBYTES|ANTI(?:\-|\s*)?VIRUS|ADWARE
        |PRINTER
        )\b
    |
    \b(?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|OFFICE|FIREFOX
        |FACTORY
        |MALWAREBYTES|ANTI(?:\-|\s*)?VIRUS|ADWARE
        |PRINTER
        )\b.*?\b
    (?:INSTALL|UPGRADE|UPDATE)\b
    """, re.VERBOSE)),

    # 12
    ('SOFTWARE UNINSTALLATION OR REMOVAL', re.compile(r"""
    \bREMOVE\b.*?\b
    (?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|OFFICE|FIREFOX
        |FACTORY
        |MALWAREBYTES|ANTI(?:\-|\s*)?VIRUS
        )\b
    """, re.VERBOSE)),

    # 13
    ('SOFTWARE RESTORATION', re.compile(r"""
    \b(?:REINSTALL|RESTORE|RESET|REPAIR)\b.*?\b
    (?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|FIREFOX
        |FACTORY
        |MALWAREBYTES|ANTI(?:\-|\s*)?VIRUS|ADWARE
        )\b
    |
    \b(?:
        PROGRAM(?:S)?
        |SOFTWARE
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|FIREFOX
        |FACTORY
        |MALWAREBYTES|ANTI(?:\-|\s*)?VIRUS|ADWARE
        )\b.*?\b
    (?:REINSTALL|RESTORE|RESET|REPAIR)\b
    """, re.VERBOSE)),

    # 14
    ('DEVICE OR SERVICE UNLOCK', re.compile(r"""
    \bUNLOCK\b.*?\b
    (?:(?:I)?PHONE|DEVICE|SERVICE|NETWORK|SAMSUNG|LG|FRP)\b
    |
    \b(?:(?:I)?PHONE|DEVICE|SERVICE|NETWORK|SAMSUNG|LG|FRP)\b.*?\b
    UNLOCK\b
    |
    \bREMOVE\s*FRP\b
    |
    \bUNLOCK\b
    """, re.VERBOSE)),

    # 15
    ('PERSONAL ACCOUNT SERVICE', re.compile(r"""
    \b(?:RESET|REMOVE|(?:RE)?CONFIGURE|CHECK|CLEAN|CHANGE|UPDATE|SETUP)\b.*?\b
    (?:PASSWORD|EMAIL|OUTLOOK|ACCOUNT|ACCT|YAHOO|ZOOM)\b
    """, re.VERBOSE)),

    # 16
    ('DATA RECOVERY', re.compile(r"""
    \b(?:RECOVER|RESTORE)\b.*?\b
    (?:DATA|FILE(?:S)?)\b
    |
    (?:DATA|FILE(?:S)?)\b.*?\b
    (?:RECOVER(?:Y)?|RESTORE)\b
    """, re.VERBOSE)),

    # 17
    ('STARTUP REPAIR', re.compile(r"""
    \b(?:WON(?:')?T|CAN(?:'|\s*|NO)?T|NOT|REPAIR)\b.*?\b
    (?:TURN\s*ON|(?:RE)?BOOT(?:\s*UP|ING)?|POWER\s*ON)\b
    |
    \b(?:TURN\s*ON|(?:RE)?BOOT(?:\s*UP|ING)?|POWER\s*ON)\b.*?\b
    (?:ERROR|ISSUE|PROBLEM)\b
    |
    \bCONSTANT\s*REBOOT\b
    |
    \bREBOOT\s*DEVICE\b
    |
    \bERROR\b.*?\bBOOT(?:\s*UP|ING)\b
    """, re.VERBOSE)),

    # 18
    ('SYSTEM CUSTOMIZATION', re.compile(r"""
    \bCUSTOMIZE\b.*?\b
    (?:SYSTEM|PC|WINDOWS|TABLET)\b
    """, re.VERBOSE)),

    # 19
    ('DATA TRANSFER/BACKUP', re.compile(r"""
    \b(?:
        DATA
        |FILE(?:S)?
        |INFO(?:RMATION)?
        |CONTACT(?:S)?
        |PHOTO(?:S)?
        |PIC(?:TURE|TURES|S)?
        |MUSIC
        |MOVIE(?:S)?
        |SONG(?:S)?
        )\b.*?\b
    (?:TRANSFER|BACKUP)\b
    |
    \b(?:TRANSFER|BACKUP)\b.*?\b
    (?:
        DATA
        |FILE(?:S)?
        |INFO(?:RMATION)?
        |CONTACT(?:S)?
        |PHOTO(?:S)?
        |PIC(?:TURE|TURES|S)?
        |MUSIC
        |MOVIE(?:S)?
        |SONG(?:S)?
        )\b
    |
    \bCOPY\b.*?\bDATA\s*FROM\b.*?\bTO\b
    """, re.VERBOSE)),

    # 20
    ('HARDWARE DIAGNOSTICS', re.compile(r"""
    \b(?:CLEAN|INSPECT|CHECK|SUSPECT)\b.*?\b
    (?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |HARD\s*DRIVE
        |POWER\s*CHIP
        |BUTTON
        |CHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)
        |SCREEN
        )\b
    |
    \b(?:
        LOGIC\s*BOARD
        |MOTHER\s*BOARD
        |KEY\s*BOARD
        |HDMI
        |HD|SSD|HDD
        |CPU|GPU
        |SPEAKER
        |CAMERA
        |HINGE
        |FAN
        |HEATING\sVENT
        |MICROPHONE
        |EAR\s*PIECE
        |HARD\s*DRIVE
        |POWER\s*CHIP
        |BUTTON
        |CHAR(?:G)?ING\s*(?:PORT|CONNECTOR|TIP)
        |SCREEN
        )\b.*?\b
    (?:CLEAN(?:\s*UP)?|INSPECT(?:ION)?|CHECK|ISSUE)\b
    |
    \b(?:WHITE|BLACK|BLUE)\s*SCREEN\b
    """, re.VERBOSE)),

    # 21
    ('SOFTWARE DIAGNOSTICS', re.compile(r"""
    \b(?:CLEAN|INSPECT|CHECK|SUSPECT)\b.*?\b
    (?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|FIREFOX
        |FACTORY
        |MALWAREBYTES|VIRUS|ADWARE
        |INTERNET
        )\b
    |
    \b(?:
        PROGRAM(?:S)?
        |SOFTWARE
        |DRIVERS
        |WINDOWS
        |SYSTEM
        |(?:BI|I)?OS
        |ICLOUD
        |APP(?:S)?
        |GOOGLE|CHROME|ADOBE|MS\s*(?:OFFICE|EDGE)?|MICROSOFT|FIREFOX
        |FACTORY
        |MALWAREBYTES|VIRUS|ADWARE
        |INTERNET
        )\b.*?\b
    (?:CLEAN(?:\s*UP)?|INSPECT(?:ION)?|CHECK|ISSUE)\b
    """, re.VERBOSE)),

    # 22
    ('CHARGING/POWER DIAGNOSTICS', re.compile(r"""
    \b(?:CHECK|WON(?:')?T|CAN(?:'|\s*|NO)T)\b.*?\b
    (?:CHARGE(?:R)?|POWER\s*(?:SUPPLY)?|SMC|BATTERY)\b
    |
    \b(?:CHARGE(?:R)?|POWER\s*(?:SUPPLY)?|SMC|BATTERY)\b.*?\b
    (?:CHECK|ISSUE)\b
    """, re.VERBOSE)),

    # 23
    ('GENERAL DIAGNOSTICS', re.compile(r"""
    \b(?:CLEAN|INSPECT|CHECK|SUSPECT|WON(?:')?T|CAN(?:'|\s*|NO)T|ISSUE)\b
    """, re.VERBOSE)),

    # 24
    ('UNMAPPED', re.compile(r'\bUNMAPPED\b'))
]

exclude_words_2 = [
    r'\bPROTECTOR\b', r'\bLABOR\b', r'\bPAID\b', r'\bCOURTESY\b', r'\bCOMPLIMENTARY\b',
    r'\bVOID\b', r'\bNO\s*FIX\b', r'NOT\s*FIXABLE', r'\b(?:\()?DIAGNOSTIC\s*FEE(?:\))?\b',
    r'\bNO\s*REPAIR\b', r'\bCUSTOMER\b', r'\bSCREEN\s*PROTECTOR\b', r'\bTANNSON\s*TECH\b',
    r'\bWITHOUT\s*REPAIR(?:ING)?\b', r'\bWARRANTY\b', r'\bEXPENSIVE\b', r'\bCANNOT\s*(?:REPAIR|RESTORE)\b',
    r'\bDEPOSIT\b', r'\bPRICE\b', r'\bESTIMATE\b', r'\bBALANCE\b', r'\bWANT\s*TO\b'
]


# In[ ]:




