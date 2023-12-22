from ichimlik import Ichimlik
from card import Card

class VendingMachine:

    def __init__(self) -> None:
        self.ichimliklar:list[Ichimlik] = []
        self.cards = {}

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

