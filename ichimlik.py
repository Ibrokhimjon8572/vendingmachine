class Ichimlik:
    def __init__(self, nomi, narxi) -> None:
        self._nomi = nomi
        self._narxi = narxi


        
    @property
    def nomi(self):
        return self._nomi
    @property
    def narxi(self):
        return self._narxi
    def __str__(self) -> str:
        return f"Nomi: {self.nomi} --> {self.narxi} som"
