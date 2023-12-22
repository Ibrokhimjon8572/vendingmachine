class Card:
    def __init__(self, card_id, card_credit) -> None:
        self.id = card_id
        self.credit = card_credit

    @property
    def id(self):
        return self.id
    
    @property
    def credit(self):
        return self.credit