# Float Precision – Net Salary Calculation Using Python

The program calculates the net salary after tax deduction and prints the result with 2 decimal precision.

1.Store salary and tax rate in variables

2.Use a function to calculate net salary

3.Validate salary and tax rate values

4.Print the output formatted to 2 decimal places


<img width="1110" height="558" alt="Screenshot 2026-05-28 185826" src="https://github.com/user-attachments/assets/5c88b648-31f1-4eb4-88e7-f851f46c3a82" />

# Code:
```
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

```

# Output:
<img width="662" height="177" alt="image" src="https://github.com/user-attachments/assets/0acaef60-e0cb-4fca-bb93-47c0c8a128b4" />

# Conclusion:

This program demonstrates how floating-point operations can be handled efficiently in Python using functions, validation techniques, and formatted outputs. It improves code readability, accuracy, and reliability in salary-based calculations.


