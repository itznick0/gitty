class Salvadanaio:
    def __init__(self):
        self.totale = 0
    def aggiungi(self, somma):
        if somma > 0:
            self.totale += somma
        else:
            print("La somma deve essere positiva.")
    def mostra_saldo(self):
        print(f"Saldo attuale: {self.totale}€")
    def svuota(self):
        self.totale = 0
        print("Il salvadanaio è stato svuotato.")
class Fratello:
    def __init__(self, nome, cognome, salvadanaio):
        self.nome = nome
        self.cognome = cognome
        self.salvadanaio = salvadanaio
    def metti_soldi(self, somma):
        self.salvadanaio.aggiungi(somma)
        print(f"{self.nome} ha aggiunto {somma}€.")
    def controlla_risparmi(self):
        self.salvadanaio.mostra_saldo()
salvadanaio_famiglia = Salvadanaio()
mario = Fratello("Mario", "Rossi", salvadanaio_famiglia)
luigi = Fratello("Luigi", "Rossi", salvadanaio_famiglia)
mario.metti_soldi(10)
luigi.metti_soldi(15)
mario.controlla_risparmi()
luigi.svuota_salvadanaio = salvadanaio_famiglia.svuota()
mario.controlla_risparmi()