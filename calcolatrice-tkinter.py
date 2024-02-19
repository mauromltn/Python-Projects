from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import math

class CalcolatriceScientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatrice Scientifica")

        self.operazioni = []

        # Inizializzazioni
        self.create_widgets()

    def create_widgets(self):
        # Creazione del display
        self.display = ttk.Label(self.root, font=('Arial', 14), anchor='e')
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Creazione dei bottoni
        style = ttk.Style()
        style.configure("TButton", font=('Arial', 12))
        
        # Impostazione per l'espanzione del layout
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        ttk.Button(self.root, text="(", command=lambda: self.mostra("("), style="TButton").grid(row=1, column=0, sticky="nsew")
        ttk.Button(self.root, text=")", command=lambda: self.mostra(")"), style="TButton").grid(row=1, column=1, sticky="nsew")
        ttk.Button(self.root, text="C", command=lambda: self.cancella(), style="TButton").grid(row=1, column=2, sticky="nsew")
        ttk.Button(self.root, text="MEM", command=lambda: self.memoria(), style="TButton").grid(row=1, column=4, sticky="nsew")
        ttk.Button(self.root, text='⌫', command=lambda: self.backspace(), style="TButton").grid(row=1, column=3, sticky="nsew")
        ttk.Button(self.root, text="/", command=lambda: self.mostra("/"), style="TButton").grid(row=2, column=4, sticky="nsew")
        ttk.Button(self.root, text="7", command=lambda: self.mostra("7"), style="TButton").grid(row=3, column=1, sticky="nsew")
        ttk.Button(self.root, text="8", command=lambda: self.mostra("8"), style="TButton").grid(row=3, column=2, sticky="nsew")
        ttk.Button(self.root, text="9", command=lambda: self.mostra("9"), style="TButton").grid(row=3, column=3, sticky="nsew")
        ttk.Button(self.root, text="*", command=lambda: self.mostra("*"), style="TButton").grid(row=3, column=4, sticky="nsew")
        ttk.Button(self.root, text="4", command=lambda: self.mostra("4"), style="TButton").grid(row=4, column=1, sticky="nsew")
        ttk.Button(self.root, text="5", command=lambda: self.mostra("5"), style="TButton").grid(row=4, column=2, sticky="nsew")
        ttk.Button(self.root, text="6", command=lambda: self.mostra("6"), style="TButton").grid(row=4, column=3, sticky="nsew")
        ttk.Button(self.root, text="1", command=lambda: self.mostra("1"), style="TButton").grid(row=5, column=1, sticky="nsew")
        ttk.Button(self.root, text="2", command=lambda: self.mostra("2"), style="TButton").grid(row=5, column=2, sticky="nsew")
        ttk.Button(self.root, text="3", command=lambda: self.mostra("3"), style="TButton").grid(row=5, column=3, sticky="nsew")
        ttk.Button(self.root, text="0", command=lambda: self.mostra("0"), style="TButton").grid(row=6, column=1, columnspan=2, sticky="nsew")
        ttk.Button(self.root, text=".", command=lambda: self.mostra("."), style="TButton").grid(row=6, column=3, sticky="nsew")
        ttk.Button(self.root, text="=", command=lambda: self.calcolo(), style="TButton").grid(row=6, column=4, sticky="nsew")
        ttk.Button(self.root, text="-", command=lambda: self.mostra("-"), style="TButton").grid(row=4, column=4, sticky="nsew")
        ttk.Button(self.root, text="+", command=lambda: self.mostra("+"), style="TButton").grid(row=5, column=4, sticky="nsew")

        # Creazione dei bottoni scientifici
        ttk.Button(self.root, text="^n", command=lambda: self.calcola_potenza(), style="TButton").grid(row=2, column=1, sticky="nsew")
        ttk.Button(self.root, text="na", command=lambda: self.calcola_radice_enne(), style="TButton").grid(row=2, column=2, sticky="nsew")
        ttk.Button(self.root, text="√", command=lambda: self.calcola_radice_quadrata(), style="TButton").grid(row=2, column=3, sticky="nsew")
        ttk.Button(self.root, text="sin", command=lambda: self.calcola_seno(), style="TButton").grid(row=2, column=0, sticky="nsew")
        ttk.Button(self.root, text="cos", command=lambda: self.calcola_coseno(), style="TButton").grid(row=3, column=0, sticky="nsew")
        ttk.Button(self.root, text="tan", command=lambda: self.calcola_tangente(), style="TButton").grid(row=4, column=0, sticky="nsew")
        ttk.Button(self.root, text="cot", command=lambda: self.calcola_cotangente(), style="TButton").grid(row=5, column=0, sticky="nsew")
        ttk.Button(self.root, text="sec", command=lambda: self.calcola_secante(), style="TButton").grid(row=6, column=0, sticky="nsew")

    def mostra(self, valore):
        # Implementazione della funzione mostra
        testo_attuale = self.display.cget("text")
        ultimo_carattere = testo_attuale[-1:]
        if ultimo_carattere in ['+', '-', '*', '/'] and valore in ['+', '-', '*', '/']:
            messagebox.showerror("Errore", "Operazione non valida.")
        else:
            self.display.config(text=testo_attuale + valore)
        # Verifica se il risultato è stato visualizzato e inizia un nuovo calcolo
        if self.risultato_calcolato:
            if valore in ['+', '-', '*', '/']:
                self.display.config(text=testo_attuale + valore)
                self.risultato_calcolato = False  # Memorizza che il risultato non è stato visualizzato
            else:
                self.display.config(text=valore)
                self.risultato_calcolato = False
        else:
            # Aggiunge il valore inserito al testo corrente del display
            self.display.config(text=testo_attuale + valore)

    def calcolo(self):
        # Implementazione della funzione calcolo
        try:
            espressione = self.display.cget("text")
            risultato = eval(espressione)
            self.display.config(text=str(risultato))
            self.operazioni.append(espressione + " = " + str(risultato))
            self.risultato_calcolato = True  # Memorizza che il risultato è stato visualizzato
        except ZeroDivisionError:
            messagebox.showerror("Errore", "Divisione per zero non consentita.")
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True
            
    def cancella(self):
        # Implementazione della funzione cancella
        self.display.config(text="")

    def backspace(self):
        # Implementazione della funzione backspace
        testo_attuale = self.display.cget("text")
        testo_nuovo = testo_attuale[:-1]
        self.display.config(text=testo_nuovo)

    def memoria(self):
        # Implementazione della funzione memoria
        if len(self.operazioni) > 0:
            messagebox.showinfo("Memoria", "\n".join(self.operazioni))
        else:
            messagebox.showinfo("Memoria", "Nessuna operazione memorizzata.")

    def calcola_potenza(self):
        # Implementazione della funzione calcola_potenza
        try:
            base = float(self.display.cget("text"))
            esponente = simpledialog.askfloat("Inserisci l'esponente", "Esponente:")
            risultato = base ** esponente
            self.display.config(text=str(risultato))
            self.operazioni.append(f'{base}^{esponente} = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True
    
    def calcola_radice_enne(self):
        # Implementazione della funzione calcola_radice_enne
        try:
            numero = float(self.display.cget("text"))
            n = simpledialog.askfloat("Inserisci l'indice della radice", "Indice:")
            risultato = numero ** (1 / n)
            self.display.config(text=str(risultato))
            self.operazioni.append(f'({numero})^(1/{n}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_radice_quadrata(self):
        # Implementazione della funzione calcola_radice_quadrata
        try:
            numero = float(self.display.cget("text"))
            risultato = math.sqrt(numero)
            self.display.config(text=str(risultato))
            self.operazioni.append(f'sqrt({numero}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_seno(self):
        # Implementazione della funzione calcola_seno
        try:
            angolo = float(self.display.cget("text"))
            risultato = math.sin(math.radians(angolo))
            self.display.config(text=str(risultato))
            self.operazioni.append(f'sin({angolo}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_coseno(self):
        # Implementazione della funzione calcola_coseno
        try:
            angolo = float(self.display.cget("text"))
            risultato = math.cos(math.radians(angolo))
            self.display.config(text=str(risultato))
            self.operazioni.append(f'cos({angolo}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_tangente(self):
        # Implementazione della funzione calcola_tangente
        try:
            angolo = float(self.display.cget("text"))
            risultato = math.tan(math.radians(angolo))
            self.display.config(text=str(risultato))
            self.operazioni.append(f'tan({angolo}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_cotangente(self):
        # Implementazione della funzione calcola_cotangente
        try:
            angolo = float(self.display.cget("text"))
            risultato = 1 / math.tan(math.radians(angolo))
            self.display.config(text=str(risultato))
            self.operazioni.append(f'cot({angolo}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

    def calcola_secante(self):
        # Implementazione della funzione calcola_secante
        try:
            angolo = float(self.display.cget("text"))
            risultato = 1 / math.cos(math.radians(angolo))
            self.display.config(text=str(risultato))
            self.operazioni.append(f'sec({angolo}) = {risultato}')
            self.risultato_calcolato = True
        except Exception as e:
            messagebox.showerror("Errore", "Errore durante il calcolo.")
            self.risultato_calcolato = True

# Esecuzione del programma
root = Tk()
app = CalcolatriceScientifica(root)
root.mainloop()