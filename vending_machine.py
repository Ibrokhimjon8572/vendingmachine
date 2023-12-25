from ichimlik import Ichimlik
from card import Card
from ustun import Ustun

class VendingMachine:

    def __init__(self) -> None:
        self.ichimliklar:list[Ichimlik] = []
        self.cards = {}
        self.ustun_list:list[Ustun] = [Ustun(None, 0) for i in range(4)]

    def addbeverage(self, ichimlik:Ichimlik):
        self.ichimliklar.append(ichimlik)
        print("ichimlik qo'shildi", ichimlik)

    def get_prise(self, ichimlik_nomi):
        for ichimlik in self.ichimliklar:
            if ichimlik.nomi == ichimlik_nomi:
                return ichimlik.narxi
        return -1.0
    
    def recharge_card(self, card_id, credit):
        if card_id in self.cards.keys():
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def get_card(self, card_id):
        if card_id in self.cards.keys():
            return self.cards[card_id]
        else:
            return -1.0
        
    def refill_column(self, ustun_soni, ichimlik_nomi, ichimlik_soni):
        ustun = self.ustun_list[ustun_soni - 1]
        if ustun.ichimlik_nomi == None or ustun.ichimlik_nomi == ichimlik_nomi and ustun.ichimlik_soni + ichimlik_soni < 40:
            ustun.ichimlik_soni = ichimlik_soni
            ustun.ichimlik_nomi = ichimlik_nomi
        else:
            print("Afsuski qo'shilayotgan ichimlik bir turda emas yoki limit tugadi")
        

    def available(self, ichimlik_nomi):
        number_of_beverage = 0
        for ustun in self.ustun_list:
            if ustun.ichimlik_nomi == ichimlik_nomi:
                number_of_beverage += ustun.ichimlik_soni
        return number_of_beverage
    
    def sell(self, card_id, ichimlik_nomi):
        number_column = 0
        if card_id not in self.cards.keys() or self.get_prise(ichimlik_nomi) == -1.0:
            return -1.0
        narxi = self.get_prise(ichimlik_nomi)
        if self.cards[card_id] - narxi < 0:
            return -1.0
        self.cards[card_id] -= narxi
        for ustun in self.ustun_list:
            number_column += 1
            if ustun.ichimlik_nomi == ichimlik_nomi and ustun.ichimlik_soni >= 1:
                ustun.sell_beverage()
                return number_column



        




