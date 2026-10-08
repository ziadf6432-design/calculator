def read_file(filename):
    with open('sales_data.txt', 'r') as file:
        sales = file.readlines()
        sales = [float(sale.strip()) for sale in sales]
    return sales
def write_report(sales, report_filename):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    with open(report_filename, 'w') as file:
        file.write(f'Total Sales: {total_sales}\n')
        file.write(f'Average Sales: {average_sales}\n')
sales = read_file('sales_data.txt')
write_report(sales, 'sales_report.txt')
    