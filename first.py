def calculate_net_salary(salary,tax_rate):
    if salary < 0:
        return "Invalid salary"
    if tax_rate < 0 or tax_rate > 1:
        return "Invalid tax rate"
    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount
    return net_salary
salary =float(input())
tax_rate =float(input())
result = calculate_net_salary(salary, tax_rate)
print(f"Net Salary after tax: {result:.2f}")
