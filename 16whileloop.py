atm_pin  = '1234'
user_pin =''
attempt =0

while atm_pin !=user_pin:  ## statement true vayasi yesko talako code run hunxa(atm pin ra user pin equal xaina vaneko xa so its true) 
    if attempt>0:          ## statement false vayo so yo talako code run vayana .
        print(f"Invalid pin code. Total Attemnt {attempt}")
    user_pin = input("Enter ATM pin: ")
    attempt = attempt+1

print("Access Granted.")