import json
from typing import Optional, Union, List, Dict, Any
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def html_to_json(content: str, indent: Optional[int] = None) -> str:
    """
    Convert HTML table to JSON format.
    
    Args:
        content (str): HTML string containing table
        indent (Optional[int]): JSON indentation level
        
    Returns:
        str: JSON string representation of the table data
        
    Raises:
        ValueError: If content is empty or invalid
        Exception: If HTML parsing fails
    """
    if not content or not content.strip():
        raise ValueError("Content cannot be empty")
    
    try:
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find("table")
        
        if not table:
            raise ValueError("No table found in the provided HTML content")
        
        # Find headers
        headers = _extract_headers(table)
        
        # Extract data rows
        data = _extract_data_rows(table, headers)
        
        return json.dumps(data, indent=indent, ensure_ascii=False)
        
    except Exception as e:
        raise Exception(f"Failed to parse HTML table: {str(e)}")


def _extract_headers(table) -> Optional[List[str]]:
    """
    Extract headers from table.
    
    Args:
        table: BeautifulSoup table element
        
    Returns:
        Optional[List[str]]: List of header names or None if no headers found
    """
    headers = []
    
    # Try to find headers in thead
    thead = table.find("thead")
    if thead:
        header_cells = thead.find_all(["th", "td"])
        headers = [cell.get_text(strip=True).lower() for cell in header_cells]
    
    # If no thead, check if first row contains th elements
    if not headers:
        first_row = table.find("tr")
        if first_row:
            header_cells = first_row.find_all("th")
            if header_cells:
                headers = [cell.get_text(strip=True).lower() for cell in header_cells]
    
    return headers if headers else None


def _extract_data_rows(table, headers: Optional[List[str]]) -> List[Union[Dict[str, str], List[str]]]:
    """
    Extract data rows from table.
    
    Args:
        table: BeautifulSoup table element
        headers: List of header names or None
        
    Returns:
        List[Union[Dict[str, str], List[str]]]: List of dictionaries (if headers exist) or list of lists
    """
    data = []
    
    # Find all rows
    tbody = table.find("tbody")
    if tbody:
        rows = tbody.find_all("tr")
    else:
        rows = table.find_all("tr")
    
    # Skip header row if it exists and we have headers
    start_index = 0
    if headers and rows:
        first_row = rows[0]
        # Check if first row contains th elements (header row)
        if first_row.find_all("th"):
            start_index = 1
        # Or if we found headers in thead, we still process all tr rows
        elif table.find("thead"):
            start_index = 0
    
    for row in rows[start_index:]:
        cells = row.find_all(["td", "th"])
        
        # Skip empty rows
        if not cells:
            continue
            
        # Extract cell text
        cell_data = []
        for cell in cells:
            # Handle line breaks and nested elements
            text = cell.get_text(separator=" ", strip=True)
            cell_data.append(text)
        
        # Skip rows with no meaningful data
        if not any(cell.strip() for cell in cell_data):
            continue
        
        # Create row data based on whether we have headers
        if headers:
            row_dict = {}
            for i, header in enumerate(headers):
                # Handle cases where row has fewer cells than headers
                value = cell_data[i] if i < len(cell_data) else ""
                row_dict[header] = value
            data.append(row_dict)
        else:
            data.append(cell_data)
    
    return data

def html_table_to_dict_list(content: str) -> List[Dict[str, Any]]:
    """
    Convert HTML table to a list of dictionaries (always uses headers).
    
    Args:
        content (str): HTML string containing table
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries representing table rows
    """
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    
    if not table:
        raise ValueError("No table found in the provided HTML content")
    
    headers = _extract_headers(table)
    
    # If no headers found, create generic ones
    if not headers:
        first_row = table.find("tr")
        if first_row:
            cells = first_row.find_all(["td", "th"])
            headers = [f"column_{i+1}" for i in range(len(cells))]
    
    if not headers:
        return []
    
    data_rows = _extract_data_rows(table, headers)
    return data_rows


def html_table_to_list_of_lists(content: str) -> List[List[str]]:
    """
    Convert HTML table to a list of lists (ignores headers).
    
    Args:
        content (str): HTML string containing table
        
    Returns:
        List[List[str]]: List of lists representing table rows
    """
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    
    if not table:
        raise ValueError("No table found in the provided HTML content")
    
    data_rows = _extract_data_rows(table, None)
    return data_rows


def validate_html_table(content: str) -> bool:
    """
    Validate if the provided HTML content contains a valid table.
    
    Args:
        content (str): HTML string to validate
        
    Returns:
        bool: True if valid table found, False otherwise
    """
    try:
        if not content or not content.strip():
            return False
            
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find("table")
        
        if not table:
            return False
            
        # Check if table has at least one row
        rows = table.find_all("tr")
        return len(rows) > 0
        
    except Exception:
        return False


def main():
    """Main function to test the html_to_json functionality."""
    
    # Test case 1: Table with thead
    content_with_thead = """
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
    """
    
    # Test case 2: Table without thead
    content_no_thead = """
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
    """
    
    # Test case 3: Complex table with tbody and nested content
    content_complex = '''
    <table id="statementTable" class="fncGrid" width="100%" cellspacing="0px" cellpadding="0px">
        <thead>
            <tr class="columnTitles">
                <th class="AlignTextLeft" index="0">
                    <span style="cursor:pointer">Date</span>
                    <img src="/fnc/1/Content/FASTNETC/Style/Images/column_sort_desc.gif" border="0" width="18" height="14">
                </th>
                <th class="AlignTextLeft" index="1">
                    <span style="cursor:pointer">Transaction Description</span>
                </th>
                <th class="AlignTextRight" index="2">
                    <span style="cursor:pointer">Debit/Cheque</span>
                </th>
                <th class="AlignTextRight" index="3">
                    <span style="cursor:pointer">Credit/Deposit</span>
                </th>
                <th class="AlignTextRight noTableHeader" index="4">
                    <span>Balance</span>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr class="">
                <td class="AlignTextLeft">13 Jul 2022</td>
                <td class="AlignTextLeft">SOME WORKPLACE<br>Salary</td>
                <td class="AlignTextRight"></td>
                <td class="AlignTextRight">$3,509.30</td>
                <td class="AlignTextRight"><font color="red">OD </font>$1,725.53</td>
            </tr>
            <tr class="">
                <td class="AlignTextLeft">12 Jul 2022</td>
                <td class="AlignTextLeft">ATM DEPOSIT<br>CARD 1605</td>
                <td class="AlignTextRight"></td>
                <td class="AlignTextRight">$400.00</td>
                <td class="AlignTextRight"><font color="red">OD </font>$5,234.83</td>
            </tr>
            <tr class="">
                <td class="AlignTextLeft">11 Jul 2022</td>
                <td class="AlignTextLeft">Another Transaction<br>Another Transaction</td>
                <td class="AlignTextRight"></td>
                <td class="AlignTextRight">$104.00</td>
                <td class="AlignTextRight"><font color="red">OD </font>$5,634.83</td>
            </tr>
            <tr class="">
                <td class="AlignTextLeft">11 Jul 2022</td>
                <td class="AlignTextLeft">MB TRANSFER<br>TO XX-XXXX-XXXXXXX-51</td>
                <td class="AlignTextRight">$4.50</td>
                <td class="AlignTextRight"></td>
                <td class="AlignTextRight"><font color="red">OD </font>$5,738.83</td>
            </tr>
            <tr></tr>
        </tbody>
    </table>
    '''
    
    print("=== Test Case 1: Table with thead ===")
    try:
        result1 = html_to_json(content_with_thead, indent=2)
        print(result1)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n=== Test Case 2: Table without thead ===")
    try:
        result2 = html_to_json(content_no_thead, indent=2)
        print(result2)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n=== Test Case 3: Complex table with tbody ===")
    try:
        result3 = html_to_json(content_complex, indent=2)
        print(result3)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n=== Additional Utility Function Tests ===")
    
    # Test validation function
    print(f"Valid table check: {validate_html_table(content_with_thead)}")
    print(f"Invalid content check: {validate_html_table('<div>Not a table</div>')}")
    print(f"Empty content check: {validate_html_table('')}")
    
    # Test dict list conversion
    print("\n--- Force dict output (with auto-generated headers) ---")
    try:
        dict_result = html_table_to_dict_list(content_no_thead)
        print(json.dumps(dict_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Test list of lists conversion
    print("\n--- Force list of lists output ---")
    try:
        list_result = html_table_to_list_of_lists(content_with_thead)
        print(json.dumps(list_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Test error handling
    print("\n=== Error Handling Tests ===")
    
    test_cases = [
        ("", "Empty content"),
        ("<div>No table here</div>", "No table found"),
        ("<table></table>", "Empty table"),
        ("invalid html", "Invalid HTML")
    ]
    
    for test_content, description in test_cases:
        print(f"\n--- {description} ---")
        try:
            result = html_to_json(test_content)
            print(f"Success: {result}")
        except Exception as e:
            print(f"Expected error: {e}")


if __name__ == "__main__":
    main()
