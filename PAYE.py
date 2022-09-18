
def staff_salary_details():
    '''
    This function collects tax payer's details and returns annual taxable income.

    '''
    user_annual_gross = float(input("Enter Your Annual Gross Earnings: "))
    user_annual_B = float(input("Enter Percentage of Basic Salary: "))
    user_annual_H = float(input("Enter Percentage of Housing Salary: "))
    user_annual_T = float(input("Enter Percentage of Transport Salary: "))
    user_annual_Leave_allowance = float(input("Enter Annual Leave Allowance: "))
    user_annual_13th_month = float(input("Enter 13th Month Allowance: "))
    user_NHF = input(" Do You Have NHF? 'Yes or No': ").upper()
    
    user_annual_basic = user_annual_B / 100
    user_annual_housing = user_annual_H / 100
    user_annual_transport = user_annual_T /100

    if user_NHF == ('YES'):
        NHF = (2.5/100) * (user_annual_gross * user_annual_basic)
    else:
        NHF = 0
    # print(NHF)

    total_income = user_annual_gross + user_annual_Leave_allowance + user_annual_13th_month

    pension = (8/100) * ((user_annual_gross * user_annual_basic) + ( user_annual_gross* user_annual_housing) + 
                         (user_annual_gross * user_annual_transport))

    base_allowance = 200000

    allowed_percentage = 20/100


    TCRA = base_allowance + (allowed_percentage * (total_income - pension - NHF))
    taxable_income = total_income - TCRA - pension - NHF
    return taxable_income

# Tax Computation functioning as expected
taxable_income = staff_salary_details() # used function to collect tax payer's details

rate_1 =0.07
if taxable_income > 0 and taxable_income <= 300000:
    previous_tax_0 = 0
    band_1_tax = (taxable_income * rate_1) + previous_tax_0
    tax = band_1_tax

rate_2 = 0.11
if taxable_income > 300000 and taxable_income <= 600000:
    previous_tax_1 = rate_1 * 300000
    band_2_tax = ((taxable_income - 300000) * rate_2) + previous_tax_1
    tax = band_2_tax


rate_3 = 0.15
if taxable_income >600000 and taxable_income <= 1100000:
    previous_tax_2 = (rate_1 * 300000) + (rate_2 * 300000)
    band_3_tax = ((taxable_income - 300000 - 300000) * rate_3)+ previous_tax_2
    tax = band_3_tax

rate_4 = 0.19
if taxable_income >1100000 and taxable_income <= 1600000:
    previous_tax_3 = (rate_1 * 300000) + (rate_2 * 300000) + (rate_3 *500000)
    band_4_tax = ((taxable_income - 300000 - 300000 - 500000) * rate_4)+ previous_tax_3
    tax = band_4_tax
    
rate_5 = 0.21
if taxable_income >1600000 and taxable_income <= 3200000:
    previous_tax_4 = (rate_1 * 300000) + (rate_2 * 300000) + (rate_3 *500000) + (rate_4 * 500000)
    band_5_tax = ((taxable_income - 300000 - 300000 - 500000 - 500000) * rate_5) + previous_tax_4
    tax = band_5_tax
    
rate_6 = 0.24
if taxable_income >3200000:
    previous_tax_5 = (rate_1 * 300000) + (rate_2 * 300000) + (rate_3 *500000) + (rate_4 * 500000) + (rate_5 * 1600000)
    band_6_tax = ((taxable_income - 300000 - 300000 - 500000 - 500000 - 1100000) * rate_6) + previous_tax_5 - 120000
    tax = band_6_tax

print(tax/12)
