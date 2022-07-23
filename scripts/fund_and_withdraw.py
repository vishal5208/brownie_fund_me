from brownie import FundMe
from scripts.helpful_scripts import get_account

account = get_account()
fund_me = FundMe[-1]


def fund():
    print(f"Length of fund me contract : {len(FundMe)}")
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current price of Eth is {fund_me.getPrice()}")
    print(f"Entrance Fee : {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee + 50 * 10**18})


def withdraw():
    fund_me.withdraw({"from": account})


def main():
    # fund()
    withdraw()
