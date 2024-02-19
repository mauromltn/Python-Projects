from abc import ABC, abstractmethod
# Si vuole implementare un’applicazione che permetta ad un concessionario auto di poter gestire il proprio parco auto.
# i veicoli hanno le seguenti caratteristiche: targa, marca, modello, numero di posti, prezzo di base.

# guardare il metodo instance() per capire come si può fare per creare un'istanza di una classe a partire da un dizionario

class Veicolo(ABC):
    def __init__(self, targa, marca, modello, numero_posti, prezzo_base):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.numero_posti = numero_posti
        self.prezzo_base = prezzo_base

    @abstractmethod
    def calcola_prezzo(self):
        pass

class Auto(Veicolo):
    def __init__(self, targa, marca, modello, numero_posti, prezzo_base, numero_porte):
        super().__init__(targa, marca, modello, numero_posti, prezzo_base)
        self.num_porte = numero_porte

    def calcola_prezzo(self):
        return self.prezzo_base  # il prezzo varia in base al numero di porte

class Camion(Veicolo):
    def __init__(self, targa, marca, modello, numero_posti, prezzo_base, capacita_massima):
        super().__init__(targa, marca, modello, numero_posti, prezzo_base)
        self.capacita_massima = capacita_massima  # in quintali

    def calcola_prezzo(self):
        return self.prezzo_base  # il prezzo varia in base alla capacità massima

class Moto(Veicolo):
    def __init__(self, targa, marca, modello, numero_posti, prezzo_base):
        super().__init__(targa, marca, modello, numero_posti, prezzo_base)

    def calcola_prezzo(self):
        return self.prezzo_base