print("welcome to abc bank!!!!")
pin=2412
chances=3
balance=50000
while chances !=0:
    user_pin = int(input("please enter the four digit pin"))
    if user_pin != pin:
        chances -=1
        print("wrong pin number")
        print(f"you have{2}chances left")
    else:
        user_choice = input("B:balance,D:deposit,W:withdraw")
        if user_choice == "B":
            print(f"your total balance is Rs.{balance}")
        if user_choice == "D":
            deposit_user = int(input("enter the amount that you would like to deposit"))
            total_balance = deposit_user + balance
            print(f"you have deposited Rs.{deposit_user}")
            print(f"your total balanca is Rs.{total_balance}")
        if user_choice== "W":
            withdraw_user = int(input("enter the amount you want to withdraw"))
            total_balance =  balance -  withdraw_user
            print(f"your total balance is Rs.{total_balance}")
    user_exit = input("would you like to exit?  yes/no")
    if user_exit == "yes":
        print("thankyou for using ABC bank!!")
        break
    else:
        continue
