class Ustun:
    def __init__(self, ichimlik_nomi, ichimlik_soni) -> None:
        self._ichimlik_nomi = ichimlik_nomi
        self._ichimlik_soni = ichimlik_soni
    
    @property
    def ichimlik_nomi(self):
        return self._ichimlik_nomi
    
    @property
    def ichimlik_soni(self):
        return self._ichimlik_soni
    
    @ichimlik_nomi.setter
    def ichimlik_nomi(self, value):
        self._ichimlik_nomi = value

    @ichimlik_soni.setter
    def ichimlik_soni(self, value):
        self._ichimlik_soni += value

    def sell_beverage(self):
        self._ichimlik_soni -= 1