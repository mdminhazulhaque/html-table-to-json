# html-table-to-json

Convert HTML Table (with no rowspan/colspan) to JSON using Python

## Input

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

# Output

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

## Input (Without Table Header)

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

# Output

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

## TODO

- [ ] Support for nested table
- [ ] Support for buggy HTML table (ie. `td` instead of `th` in `thead`)
