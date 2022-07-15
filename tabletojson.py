import json
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def html_to_json(content, indent=None):
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find_all("tr")
    
    headers = {}
    thead = soup.find("thead")
    if thead:
        thead = thead.find_all("th")
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()
    data = []
    for row in rows:
        cells = row.find_all("td")
        if thead:
            items = {}
            if len(cells) > 0:
                for index in headers:
                    items[headers[index]] = cells[index].text
        else:
            items = []
            for index in cells:
                items.append(index.text.strip())
        if items:
            data.append(items)
    return json.dumps(data, indent=indent)

if __name__ == "__main__":
    content = "<table> <thead> <th>ID</th> <th>Vendor</th> <th>Product</th> </thead> <tr> <td>1</td> <td>Intel</td> <td>Processor</td> </tr> <tr> <td>2</td> <td>AMD</td> <td>GPU</td> </tr> <tr> <td>3</td> <td>Gigabyte</td> <td>Mainboard</td> </tr></table>"
    content_no_thead = "<table> <tr> <td>1</td> <td>Intel</td> <td>Processor</td> </tr> <tr> <td>2</td> <td>AMD</td> <td>GPU</td> </tr> <tr> <td>3</td> <td>Gigabyte</td> <td>Mainboard</td> </tr></table>"
    content_head_no_td = '<table id="statementTable" class="fncGrid" width="100%" cellspacing="0px" cellpadding="0px"><thead><tr class="columnTitles"><th class="AlignTextLeft" index="0"><span style="cursor:pointer">Date</span><img src="/fnc/1/Content/FASTNETC/Style/Images/column_sort_desc.gif" border="0" width="18" height="14"></th><th class="AlignTextLeft" index="1"><span style="cursor:pointer">Transaction Description</span></th><th class="AlignTextRight" index="2"><span style="cursor:pointer">Debit/Cheque</span></th><th class="AlignTextRight" index="3"><span style="cursor:pointer">Credit/Deposit</span></th><th class="AlignTextRight  noTableHeader" index="4"><span>Balance</span></th></tr></thead><tbody><tr class=""><td class="AlignTextLeft">13 Jul 2022</td><td class="AlignTextLeft">SOME WORKPLACE<br>Salary</td><td class="AlignTextRight"></td><td class="AlignTextRight">$3,509.30</td><td class="AlignTextRight"><font color="red">OD </font>$1,725.53</td></tr><tr class=""><td class="AlignTextLeft">12 Jul 2022</td><td class="AlignTextLeft">ATM DEPOSIT<br>CARD 1605</td><td class="AlignTextRight"></td><td class="AlignTextRight">$400.00</td><td class="AlignTextRight"><font color="red">OD </font>$5,234.83</td></tr><tr class=""><td class="AlignTextLeft">11 Jul 2022</td><td class="AlignTextLeft">Another Transaction<br>Another Transaction</td><td class="AlignTextRight"></td><td class="AlignTextRight">$104.00</td><td class="AlignTextRight"><font color="red">OD </font>$5,634.83</td></tr><tr class=""><td class="AlignTextLeft">11 Jul 2022</td><td class="AlignTextLeft">MB TRANSFER<br>TO XX-XXXX-XXXXXXX-51</td><td class="AlignTextRight">$4.50</td><td class="AlignTextRight"></td><td class="AlignTextRight"><font color="red">OD </font>$5,738.83</td></tr></tbody></table>'
    print(html_to_json(content))
    # returns list of objects as header is present
    # [{"id": "1", "vendor": "Intel", "product": "Processor"}, {"id": "2", "vendor": "AMD", "product": "GPU"}, {"id": "3", "vendor": "Gigabyte", "product": "Mainboard"}]
    
    print(html_to_json(content_no_thead, indent=4))
    # autodetects if thead is there, returns list of list
    # [["1", "Intel", "Processor"], ["2", "AMD", "GPU"], ["3", "Gigabyte", "Mainboard"]]
    
    print(html_to_json(content_head_no_td, indent=4))
    # [{"date": "13 Jul 2022", "transaction description": "SOME WORKPLACESalary", "debit/cheque": "", "credit/deposit": "$3,509.30", "balance": "OD $1,725.53"}, {"date": "12 Jul 2022", "transaction description": "ATM DEPOSITCARD 1605", "debit/cheque": "", "credit/deposit": "$400.00", "balance": "OD $5,234.83"}, {"date": "11 Jul 2022", "transaction description": "Another TransactionAnother Transaction", "debit/cheque": "", "credit/deposit": "$104.00", "balance": "OD $5,634.83"}, {"date": "11 Jul 2022", "transaction description": "MB TRANSFERTO XX-XXXX-XXXXXXX-51", "debit/cheque": "$4.50", "credit/deposit": "", "balance": "OD $5,738.83"}]
