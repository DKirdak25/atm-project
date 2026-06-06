"""
            Atm user interface
            
this script design specilly for user interaction by seperating input and logic            
"""
from atm_logic import AtmModel

def get_user():
				while True:
								print("(A) Deposit , \n(B) Withdraw, \n(C) Check Balance, \n(D) Exit")
								user = input("Enter Your Option: ").upper()
								
								if user == "":
												print("Empty Option Not allowed try again")
												continue
								elif not user in ("A", "B", "C", "D"):
												print("Optipn npt available try again")
												continue
								else:
												return user

def get_ammount():
				while True:
								try:
												ammount = int(input("Enter ammount: "))
								except ValueError:
												print("Invalid ammount try again")
												continue
								else:
												if ammount <= 0:
																print("Invalid ammount try again")
																continue
												else:
																return ammount

def main():
				atm = AtmModel()
				while True:
								user = get_user()
								if user == "A":
												ammount = get_ammount()
												success = atm.deposit(ammount)
												if success is True:
																print("Deposite Successfull")
												else:
																print(successs)
								elif user == "B":
												ammount = get_ammount()
												success = atm.withdraw(ammount)
												if success is True:
																print("Withdraw Successfull")
												else:
																print(successs)
								elif user == "C":
												balance = atm.check_balance()
												print("Current Balance", balance)
								else:
												break


if __name__ == "__main__":
    main()
								