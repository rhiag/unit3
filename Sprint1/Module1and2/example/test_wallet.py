"""an example of a more intense pytest"""
import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    """Testing balance is zero"""
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    """Testing constructor initial balance"""
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    """Testing add_cash method in wallet object"""
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100
    
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    """Test proper exception is raised when spend cash exceed balance"""
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)