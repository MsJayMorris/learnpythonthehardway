from sys import argv

script, price, taxes, insurance = argv


def mortgage_payment_calculator(price, taxes, insurance):
    mort_payment = int(price) / 360
    print "Your monthly mortgage payment will be: %d" % mort_payment
    tax_payment = int(taxes) / 12
    print "Your monthly tax payment will be: %d" % tax_payment
    ins_payment = int(insurance) / 12
    print "Your monthly insurance payment will be: %d" % ins_payment
    total = mort_payment + tax_payment + ins_payment
    print "Your total payment will be: %d" % total
    
    
mortgage_payment_calculator(153000, 6000, 775)

mortgage_payment_calculator(price, taxes, insurance)

home_price = int(raw_input("Enter the purchase price of the house: "))
yearly_taxes = int(raw_input("Enter the yearly tax amount: "))
yearly_insurance = int(raw_input("Enter the yearly insurance premium: "))




