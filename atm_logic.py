"""
         Atm Bussiness Logic
this script only contain logic seprate form input
"""

class AtmModel():
				def __init__(self, balance=1000):
								self.balance = balance
				
				def deposit(self, ammount):
								if ammount <= 0:
												return "Invalid ammount"
												
								self.balance += ammount
								return True
				
				def withdraw(self, ammount):
								if ammount > self.balance:
												return "Lower balance than ammount try again"
								else:
												self.balance -= ammount
								return True

				def check_balance(self):
								return self.balance


								






