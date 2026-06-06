"""
           Atm Test 
This script cantain only test of atm 
"""

from unittest.mock import patch
from atm_interface import get_ammount, get_user
from atm_logic import AtmModel

def test_deposit():
				atm = AtmModel()
				result = atm.deposit(500)
				
				assert result is True
				assert atm.balance == 1500

def test_withdraw():
				atm = AtmModel()
				result = atm.withdraw(300)
				
				assert result is True
				assert atm.balance == 700

def test_overwithdraw():
				atm = AtmModel()
				result = atm.withdraw(5000)
				
				assert result == "Lower balance than ammount try again"
				assert atm.balance == 1000

def test_invalid_deposit():
				atm = AtmModel()
				result = atm.deposit(-100)
				
				assert result == "Invalid ammount"
				assert atm.balance == 1000
				
def test_check_balance():
				atm = AtmModel()
				
				assert atm.check_balance() == 1000    
				
def test_get_ammount():
				with patch("builtins.input", return_value="500"):
								result = get_ammount()
				assert result == 500

def test_invalide_ammount_then_valid():
				with patch("builtins.input", side_effect = ["abc", "", "100"]):
								result = get_ammount()
				assert result == 100

def test_get_user():
				with patch("builtins.input", return_value= "A"):
								result = get_user()
				assert result == "A"

def test_invalid_user_then_valid():
				with patch("builtins.input", side_effect = ["X", "", "B"]):
								result = get_user()
				assert result == "B"