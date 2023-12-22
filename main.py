from ichimlik import Ichimlik
from vending_machine import VendingMachine


ichimlik1 = Ichimlik('Pepsi', '16000')

print(ichimlik1)

vendingmachine = VendingMachine()
vendingmachine.addbeverage(ichimlik1)
print(vendingmachine.ichimliklar)
print(vendingmachine.get_prise('Pepsi'))
print(vendingmachine.get_prise('Cola'))
vendingmachine.recharge_card(1, 10000)
vendingmachine.recharge_card(1, 2000)
vendingmachine.recharge_card(2, 2000)

print(vendingmachine.cards)

print(vendingmachine.get_card(1))

print(vendingmachine.get_card(3))