# Assignment 1: Programing Basics
# Final Revision 02/07/23
# Nick Dimarzo

# This program was designed for Global Green Energy(GGE) a utility company in Canada.
# This program is a calculator that will produce a customers total monthly utility bill,
# depending on the customers utility plans and the amount of resources used for the specified month.
# This program operates in 3 steps:
# Step 1: The program takes the inputs from the customer and calculates the electricity plan costs before taxes.
# Step 2: The program takes the inputs from the customer and calculates the natural gas plan casts before taxes.
# Step 3: The program combines the electricity plan total, the natural gas plan total and the additional fees
# before adding the provincial sales tax for the customers final monthly total owed.

# Program begins
print("Welcome to the Global Energy bill calculator!")

# customer inputs
account_number = input("Enter your account number:")
month_number = int(input("Enter the month number (e.g., for January, enter 1):"))

# customer electricity plan inputs
electricity_plan = (input("Enter your electricity plan (EFIR or ELFR):"))
kwh_used = int(input("Enter the amount of electricity you used in the selected month (in kWh):"))

# electricity plan cost calculations
electricity_fixed_rate = (kwh_used * 0.0836)
electricity_fixed_rate_plus = (1000 * 0.0836) + ((kwh_used - 1000) * 0.0941)
electricity_floating_rate = (kwh_used * 0.0911)

if electricity_plan == 'EFIR' and kwh_used < 1000:
    electricity_cost = electricity_fixed_rate
elif electricity_plan == 'EFIR' and kwh_used > 1000:
    electricity_cost = electricity_fixed_rate_plus
else:
    electricity_cost = electricity_floating_rate

# customer natural gas plan inputs
natural_gas_plan = input("Enter your gas plan (GFIR or GFLR):")
gj_used = int(input("Enter the amount of gas you used in the selected month (in GJ):"))

# natural gas plan cost calculations
natural_gas_fixed_rate = (gj_used * 0.0456)
natural_gas_fixed_rate_plus = (950 * 0.456) + ((gj_used - 950) * 0.586)
natural_gas_floating_rate = (gj_used * 0.0393)

if natural_gas_plan == 'GFIR' and gj_used < 950:
    natural_gas_cost = natural_gas_fixed_rate
elif natural_gas_plan == 'GFIR' and gj_used > 950:
    natural_gas_cost = natural_gas_fixed_rate_plus
else:
    natural_gas_cost = natural_gas_floating_rate

# additional monthly fees
fixed_monthly_fee = 120.62
fixed_monthly_transaction_fee = 1.32
additional_fees = (fixed_monthly_fee + fixed_monthly_transaction_fee)

# total before provincial taxes
cost_before_provincial_taxes = (electricity_cost + natural_gas_cost + additional_fees)

# customer province input
province = input("Enter the abbreviation for your province of residence (two letters):")

# total cost calculations
if province == 'AB' or 'BC' or 'MB' or 'NT' or 'NU' or 'QC' or 'SK' or 'YT':
    total_cost = (cost_before_provincial_taxes * 1.05)
elif province == 'NB' or 'NL' or 'NS' or 'PE':
    total_cost = (cost_before_provincial_taxes * 1.13)
else:
    total_cost = (cost_before_provincial_taxes * 1.15)

# Program ends
print("Thank you! Your total amount due now is: $" + str(total_cost))
