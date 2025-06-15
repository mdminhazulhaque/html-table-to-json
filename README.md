# html-table-to-json

Convert HTML Table (with no rowspan/colspan) to JSON using Python

## Features

✅ **Smart Header Detection** - Automatically detects headers in `<thead>` or first row with `<th>` elements  
✅ **Flexible Output Format** - Returns list of dictionaries (when headers exist) or list of lists  
✅ **Robust HTML Parsing** - Handles complex nested HTML content within cells  
✅ **Error Handling** - Comprehensive input validation and error reporting  
✅ **Type Safety** - Full type hints for better development experience  
✅ **Multiple Utility Functions** - Various conversion methods for different use cases  

## Installation

```bash
pip install beautifulsoup4
```

## Usage

### Basic Usage

```python
from tabletojson import html_to_json

# Convert HTML table to JSON
html_content = "<table>...</table>"
json_result = html_to_json(html_content, indent=2)
print(json_result)
```

### Advanced Usage

```python
from tabletojson import (
    html_to_json,
    html_table_to_dict_list,
    html_table_to_list_of_lists,
    validate_html_table
)

# Validate table first
if validate_html_table(html_content):
    # Force dictionary output (with auto-generated headers if needed)
    dict_result = html_table_to_dict_list(html_content)
    
    # Force list of lists output (ignores headers)
    list_result = html_table_to_list_of_lists(html_content)
```

## Examples

### Example 1: Table with Headers

**Input:**

<table>
    <thead>
        <th>ID</th>
        <th>Vendor</th>
        <th>Product</th>
    </thead>
    <tr>
        <td>1</td>
        <td>Intel</td>
        <td>Processor</td>
    </tr>
    <tr>
        <td>2</td>
        <td>AMD</td>
        <td>GPU</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Gigabyte</td>
        <td>Mainboard</td>
    </tr>
</table>

## Output

```json
[
    {
        "product": "Processor", 
        "vendor": "Intel", 
        "id": "1"
    }, 
    {
        "product": "GPU", 
        "vendor": "AMD", 
        "id": "2"
    }, 
    {
        "product": "Mainboard", 
        "vendor": "Gigabyte", 
        "id": "3"
    }
]
```

### Example 2: Table without Headers

**Input:**

<table>
    <tr>
        <td>1</td>
        <td>Intel</td>
        <td>Processor</td>
    </tr>
    <tr>
        <td>2</td>
        <td>AMD</td>
        <td>GPU</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Gigabyte</td>
        <td>Mainboard</td>
    </tr>
</table>

**Output:**

```json
[
  [
    "1",
    "Intel",
    "Processor"
  ],
  [
    "2",
    "AMD",
    "GPU"
  ],
  [
    "3",
    "Gigabyte",
    "Mainboard"
  ]
]
```

### Example 3: Complex Table with tbody and Nested Content

**Input:**

<table id="statementTable" class="fncGrid" width="100%" cellspacing="0px" cellpadding="0px">
<thead>
    <tr class="columnTitles">
                    <th class="AlignTextLeft" index="0"><span style="cursor:pointer">Date</span><img src="/fnc/1/Content/FASTNETC/Style/Images/column_sort_desc.gif" border="0" width="18" height="14"></th>
                    <th class="AlignTextLeft" index="1"><span style="cursor:pointer">Transaction Description</span></th>                
                    <th class="AlignTextRight" index="2"><span style="cursor:pointer">Debit/Cheque</span></th>                
                    <th class="AlignTextRight" index="3"><span style="cursor:pointer">Credit/Deposit</span></th>
                    <th class="AlignTextRight  noTableHeader" index="4"><span>Balance</span></th>
    </tr>
</thead>
<tbody>
       <tr class="">
                    <td class="AlignTextLeft">
                        13 Jul 2022
                    </td>
                    <td class="AlignTextLeft">
                        SOME WORKPLACE<br>Salary
                    </td>
                    <td class="AlignTextRight">
                    </td>
                    <td class="AlignTextRight">
                        $3,509.30
                    </td>
                    <td class="AlignTextRight">
                        <font color="red">OD </font>$1,725.53
                    </td>
       </tr>
       <tr class="">
                    <td class="AlignTextLeft">
                        12 Jul 2022
                    </td>
                    <td class="AlignTextLeft">
                        ATM DEPOSIT<br>CARD 1605
                    </td>
                    <td class="AlignTextRight">
                    </td>
                    <td class="AlignTextRight">
                        $400.00
                    </td>
                    <td class="AlignTextRight">
                        <font color="red">OD </font>$5,234.83
                    </td>
       </tr>
       <tr class="">
                    <td class="AlignTextLeft">
                        11 Jul 2022
                    </td>
                    <td class="AlignTextLeft">
                        Another Transaction<br>Another Transaction
                    </td>
                    <td class="AlignTextRight">
                    </td>
                    <td class="AlignTextRight">
                        $104.00
                    </td>
                    <td class="AlignTextRight">
                        <font color="red">OD </font>$5,634.83
                    </td>
       </tr>
       <tr class="">
                    <td class="AlignTextLeft">
                        11 Jul 2022
                    </td>
                    <td class="AlignTextLeft">
                        MB TRANSFER<br>TO XX-XXXX-XXXXXXX-51
                    </td>
                    <td class="AlignTextRight">
                        $4.50
                    </td>
                    <td class="AlignTextRight">
                    </td>
                    <td class="AlignTextRight">
                        <font color="red">OD </font>$5,738.83
                    </td>
       </tr>
       <tr class="">
       </tr>
</tbody>
</table>

**Output:**
```json
[
    {
        "date": "13 Jul 2022",
        "transaction description": "SOME WORKPLACESalary",
        "debit/cheque": "",
        "credit/deposit": "$3,509.30",
        "balance": "OD $1,725.53"
    },
    {
        "date": "12 Jul 2022",
        "transaction description": "ATM DEPOSITCARD 1605",
        "debit/cheque": "",
        "credit/deposit": "$400.00",
        "balance": "OD $5,234.83"
    },
    {
        "date": "11 Jul 2022",
        "transaction description": "Another TransactionAnother Transaction",
        "debit/cheque": "",
        "credit/deposit": "$104.00",
        "balance": "OD $5,634.83"
    },
    {
        "date": "11 Jul 2022",
        "transaction description": "MB TRANSFERTO XX-XXXX-XXXXXXX-51",
        "debit/cheque": "$4.50",
        "credit/deposit": "",
        "balance": "OD $5,738.83"
    }
]
```

## Improvements Made

### 🐛 **Bug Fixes**
- Fixed header detection logic that was incorrectly searching for `th` elements
- Fixed data structure handling for consistent output format
- Fixed handling of tables with `tbody` elements
- Fixed text extraction from nested HTML elements (preserves spaces)

### ✨ **New Features**
- **Type Safety**: Added comprehensive type hints for better IDE support
- **Input Validation**: Robust error handling with descriptive error messages
- **Multiple Output Formats**: New utility functions for different use cases
- **Smart Header Detection**: Detects headers in `<thead>` or first row with `<th>` elements
- **Empty Row Handling**: Automatically skips empty rows
- **Flexible Cell Handling**: Handles mismatched column counts gracefully

### 🚀 **Performance & Code Quality**
- **Modular Design**: Split functionality into focused helper functions
- **Better Error Handling**: Comprehensive exception handling with context
- **Documentation**: Added detailed docstrings and usage examples
- **Test Coverage**: Enhanced test cases covering edge cases and error scenarios

### 📋 **New API Functions**
- `html_to_json()` - Main conversion function (improved)
- `html_table_to_dict_list()` - Force dictionary output with auto-generated headers
- `html_table_to_list_of_lists()` - Force list of lists output
- `validate_html_table()` - Validate HTML table structure

## TODO

- [ ] Support for nested table
- [x] ~~Support for buggy HTML table (ie. `td` instead of `th` in `thead`)~~ ✅ **Fixed**
- [x] ~~Improve error handling~~ ✅ **Added comprehensive error handling**
- [x] ~~Add type hints~~ ✅ **Added full type safety**
- [x] ~~Better text extraction from nested elements~~ ✅ **Improved HTML parsing**
- [ ] Support for rowspan/colspan attributes
- [ ] Add support for custom header mappings
- [ ] Add CSV export functionality
