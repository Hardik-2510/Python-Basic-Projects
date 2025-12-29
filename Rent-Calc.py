rent = int(input("Enter your flat rent : "))
food = int(input("Enter the amount of food :"))
electricity_spend = int(input("Enter the total of electricity spend :"))
charge_per_unit = int(input("Enter the charge per unit :"))
persons = int(input("Enter the number of person : "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill)// persons
print("Each Person will have to pay : ", output)