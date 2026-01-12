SBI_Nithin = {"Name": "Nithin",
             "mobile": "1234567890",
             "ATM PIN" : "1234",
             "Balance" : 25000,
             "Transaction History" : []}     #this is the user data
print("please insert your ATM card")
remaining_attempts = 3
while remaining_attempts >0:
    user_pin = input("Enter your 4 digit pin: ")
    if len(user_pin) ==4:
        if user_pin in SBI_Nithin['ATM PIN'] :
            print("welcome to SBI ATM")
            user_input = int(input("enter \n1.Deposit money \n2.Withdraw money \n3.Check balance \n4.change pin \n5.Transaction History"))
            if user_input ==1:
                Deposite_money = int(input("enter amount you want to deposite into the amount: "))
                if Deposite_money >= 1000 and Deposite_money % 100 ==0 :
                   SBI_Nithin['Balance'] += Deposite_money
                   SBI_Nithin['Transaction History'].append(f"Deposited: {Deposite_money}")
                   break
                elif user_input == 2:
                    witdraw_money = int(input("enter amount you want to withdraw from the account: "))
                    if witdraw_money <= SBI_Nithin ["Balance"] and witdraw_money % 100 ==0:
                        SBI_Nithin['Balance'] -= witdraw_money
                        SBI_Nithin['Transaction History'].append(witdraw_money)
                        print(f"you have withdraw {witdraw_money} and the total balance in your acount is  {SBI_Nithin['Balance']} ")
                        break
                    else:
                        print(f"your total balance is {SBI_Nithin['ATM PIN']}and you're trying to withdraw_money {witdraw_money}")
                elif user_input == 3:
                        print(f"your total balance is {SBI_Nithin['Balance']}")
                        break
    else:
        remaining_attempts -= 1
        if remaining_attempts > 0:
            print(f"invalied pin entered and you have {remaining_attempts}only")
        else:
            print("you've run out of attempts, your card has been temporarilly blocked")
            break    
else:
        print("please enter 4 digit pin only")
        