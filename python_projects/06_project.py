# EMI Calculator in pyhton

loan_amount = float(input("Enter Loan Amount: "))
annual_interest = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))

monthly_rate = annual_interest / (12 * 100)
months = years * 12

emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print(f"\nMonthly EMI = ₹{emi:.2f}")