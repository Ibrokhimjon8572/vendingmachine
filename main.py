from ichimlik import Ichimlik
from vending_machine import VendingMachine


ichimlik1 = Ichimlik('Pepsi', 16000)

print(ichimlik1)

vendingmachine = VendingMachine()
vendingmachine.addbeverage(ichimlik1)
print(vendingmachine.ichimliklar)
print(vendingmachine.get_prise('Pepsi'))
# print(vendingmachine.get_prise('Cola'))
vendingmachine.recharge_card(1, 20000)
# vendingmachine.recharge_card(1, 2000)
# vendingmachine.recharge_card(2, 2000)

# print(vendingmachine.cards)

# print(vendingmachine.get_card(1))

# print(vendingmachine.get_card(3))
# print(vendingmachine.ustun_list[0].ichimlik_soni, vendingmachine.ustun_list[0].ichimlik_nomi)

vendingmachine.refill_column(1, "Pepsi", 16)
# vendingmachine.refill_column(1, "Cola", 16)
# vendingmachine.refill_column(1, "Cola", 16)

# vendingmachine.refill_column(1, "Fola", 16)

# print(vendingmachine.ustun_list[0].ichimlik_soni, vendingmachine.ustun_list[0].ichimlik_nomi)

# vendingmachine.refill_column(1, "Cola", 16)
# vendingmachine.refill_column(3, "Cola", 10)
# print(vendingmachine.ustun_list[0].ichimlik_soni, vendingmachine.ustun_list[0].ichimlik_nomi)

# print(vendingmachine.available('Cola'))

# print("ustun -->", vendingmachine.sell(1, 'fanta'), " dan kamaytirildi")
# print(vendingmachine.get_card(1))
# print(vendingmachine.ustun_list[0].ichimlik_soni)
print(vendingmachine.sell(1000, "Pepsi"))

