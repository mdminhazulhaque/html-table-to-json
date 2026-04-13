#!/usr/bin/env python3
"""
Example usage of the improved html-table-to-json converter.
This file demonstrates various use cases and features.
"""

from tabletojson import (
    html_to_json,
    html_table_to_dict_list,
    html_table_to_list_of_lists,
    validate_html_table
)

def demo_basic_usage():
    """Demonstrate basic usage with different table types."""
    print("=" * 60)
    print("BASIC USAGE DEMONSTRATION")
    print("=" * 60)
    
    # Simple table with headers
    table_with_headers = """
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>30</td>
                <td>New York</td>
            </tr>
            <tr>
                <td>Jane Smith</td>
                <td>25</td>
                <td>Los Angeles</td>
            </tr>
        </tbody>
    </table>
    """
    
    print("🔹 Table with headers:")
    result = html_to_json(table_with_headers, indent=2)
    print(result)
    print()

def demo_utility_functions():
    """Demonstrate utility functions."""
    print("=" * 60)
    print("UTILITY FUNCTIONS DEMONSTRATION")
    print("=" * 60)
    
    table_no_headers = """
    <table>
        <tr><td>Product A</td><td>$10.99</td><td>In Stock</td></tr>
        <tr><td>Product B</td><td>$15.50</td><td>Out of Stock</td></tr>
        <tr><td>Product C</td><td>$8.75</td><td>In Stock</td></tr>
    </table>
    """
    
    print("🔹 Original table (no headers):")
    print(html_to_json(table_no_headers, indent=2))
    print()
    
    print("🔹 Force dictionary output (auto-generated headers):")
    dict_result = html_table_to_dict_list(table_no_headers)
    import json
    print(json.dumps(dict_result, indent=2))
    print()
    
    print("🔹 Force list of lists output:")
    list_result = html_table_to_list_of_lists(table_no_headers)
    print(json.dumps(list_result, indent=2))
    print()

def demo_error_handling():
    """Demonstrate error handling capabilities."""
    print("=" * 60)
    print("ERROR HANDLING DEMONSTRATION")
    print("=" * 60)
    
    test_cases = [
        ("", "Empty string"),
        ("<div>No table here</div>", "No table in HTML"),
        ("<table></table>", "Empty table"),
        ("Not even HTML", "Invalid HTML"),
    ]
    
    for content, description in test_cases:
        print(f"🔹 Testing: {description}")
        print(f"   Valid table: {validate_html_table(content)}")
        try:
            result = html_to_json(content)
            print(f"   Result: {result}")
        except Exception as e:
            print(f"   Error: {e}")
        print()

def demo_complex_table():
    """Demonstrate handling of complex HTML tables."""
    print("=" * 60)
    print("COMPLEX TABLE DEMONSTRATION")
    print("=" * 60)
    
    complex_table = """
    <table class="data-table" style="width: 100%;">
        <thead style="background: #f0f0f0;">
            <tr>
                <th style="padding: 10px;">
                    <strong>Order ID</strong>
                </th>
                <th style="padding: 10px;">
                    <span>Customer<br/>Information</span>
                </th>
                <th style="padding: 10px;">
                    <em>Total Amount</em>
                </th>
                <th style="padding: 10px;">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr class="row-odd">
                <td style="text-align: center;">
                    <a href="#order-1001">#1001</a>
                </td>
                <td>
                    <div>
                        <strong>Alice Johnson</strong><br/>
                        <small>alice@email.com</small><br/>
                        <span style="color: gray;">Premium Customer</span>
                    </div>
                </td>
                <td style="text-align: right;">
                    <span style="color: green; font-weight: bold;">$299.99</span>
                </td>
                <td>
                    <span class="status shipped" style="color: blue;">Shipped</span>
                </td>
            </tr>
            <tr class="row-even">
                <td style="text-align: center;">
                    <a href="#order-1002">#1002</a>
                </td>
                <td>
                    <div>
                        <strong>Bob Williams</strong><br/>
                        <small>bob@email.com</small><br/>
                        <span style="color: gray;">Regular Customer</span>
                    </div>
                </td>
                <td style="text-align: right;">
                    <span style="color: green; font-weight: bold;">$157.50</span>
                </td>
                <td>
                    <span class="status pending" style="color: orange;">Pending</span>
                </td>
            </tr>
        </tbody>
    </table>
    """
    
    print("🔹 Complex table with nested HTML and styling:")
    result = html_to_json(complex_table, indent=2)
    print(result)
    print()

if __name__ == "__main__":
    print("🚀 HTML Table to JSON Converter - Enhanced Version")
    print("This demonstrates the improved functionality and robustness.\n")
    
    demo_basic_usage()
    demo_utility_functions()
    demo_error_handling()
    demo_complex_table()
    
    print("=" * 60)
    print("✅ All demonstrations completed successfully!")
    print("=" * 60)
