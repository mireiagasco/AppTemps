from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk          
import requests
from tkinter import messagebox

#funció que obté el clima
def obtenir_clima(ciutat, et_nom, et_icona, et_temp, et_desc, et_realfeel, icones):
    #creem les variables amb les dades que ens calen per accedir al servidor
    api_key = "7f2fb91cddee2e58c5056c046d7f6046"
    url = "http://api.openweathermap.org/data/2.5/weather"
    dic_param = {"AppID" : api_key, "q" : ciutat, "units" : "metric", "lang" : "sp"}

    #accedim al servidor i en desem la resposta en format json
    resposta = requests.get(url, params = dic_param)
    clima = resposta.json()

    #comprovem que s'ha pogut obtenir la ciutat
    if clima.get("cod", "404") == "404":
        et_desc["text"] = "No s'ha pogut trobar la ciutat"
    else:
        #mostrem les dades que ens interessen
        et_nom["text"] = "{}, {}".format(clima["name"], clima["sys"]["country"])
        et_desc["text"] = clima["weather"][0]["description"].title()
        et_temp["text"] = "{}ºC".format(clima["main"]["temp"])
        et_realfeel["text"] = "Real Feel: {}ºC".format(clima["main"]["feels_like"])
        
        info = clima["weather"][0]["icon"]
        num_icona = info[0:2]
        et_icona["image"] = icones[num_icona]


    
class AppTemps:

    def __init__(self):
        #creem la finestra principal
        self.finestra_principal = tk.ThemedTk()
        self.finestra_principal.get_themes()
        self.finestra_principal.set_theme("breeze")
        self.finestra_principal.title("App del Temps")
        self.finestra_principal.iconbitmap(r"icona_apptemps.ico")

        #creem els marcs que utilitzarem
        self.marc_esquerre = Frame(self.finestra_principal, height = 400, width = 350)
        self.marc_esquerre.grid(row = 0, column = 0)

        self.marc_central = Frame(self.finestra_principal)
        self.marc_central.grid(row = 0, column = 1, padx = 20)

        self.marc_dret = Frame(self.finestra_principal, height = 400, width = 350)
        self.marc_dret.grid(row = 0, column = 2)

        #creem l'etiqueta de benvinguda
        self.etiq_benv = ttk.Label(self.marc_esquerre, text = "Benvingut/da!", font = "Gabriola 20 bold")
        self.etiq_benv.pack(pady = 15, padx = 15)

        #creem l'etiqueta que ens indica què fer
        self.etiq_instruccions = ttk.Label(self.marc_esquerre, text = "Introdueixi el nom de la ciutat que vulgui:", font = "Gabriola 15")
        self.etiq_instruccions.pack(pady = 10, padx = 10)

        #creem l'entrada de text
        self.entrada_ciutat = ttk.Entry(self.marc_esquerre, justify = "center")
        self.entrada_ciutat.pack(pady = 5, padx = 10)

        #creem la línia de separació entre els dos marcs
        self.canvas_linia = Canvas(self.marc_central, width = 10)
        self.canvas_linia.grid(row = 0, column = 0)
        self.linia = self.canvas_linia.create_line(0,0,0,400, width = 7, fill = "light blue")

        #creem l'etiqueta que mostrarà el nom de la ciutat
        self.nom = ttk.Label(self.marc_dret, font = "Gabriola 20")
        self.nom.grid(row = 0, column = 0, columnspan = 2, pady = 15)

        #creem l'etiqueta que mostrarà la icona i carreguem el diccionari amb les possibles icones
        self.icona = ttk.Label(self.marc_dret)
        self.icona.grid(row = 1, column = 0, pady = 10, padx = 10)

        sol = PhotoImage(file = r"icones\sol.png")
        algun_nuvol = PhotoImage(file = r"icones\algun_núvol.png")
        sol_nuvol = PhotoImage(file = r"icones\sol&núvol.png")
        sol_pluja = PhotoImage(file = r"icones\sol&núvols&pluja.png")
        molts_nuvols = PhotoImage(file = r"icones\molts_núvols.png")
        boira = PhotoImage(file = r"icones\boira.png")
        neu = PhotoImage(file = r"icones\neu.png")
        tempesta = PhotoImage(file = r"icones\tempesta.png")
        pluja = PhotoImage(file = r"icones\pluja.png")
        
        icones = {"01" : sol, "02" : sol_nuvol, "03" : algun_nuvol, "04" : molts_nuvols, "09" : pluja, "10" : sol_pluja, "11" : tempesta, "13" : neu, "50" : boira}

        #creem l'etiqueta que mostrarà la temperatura
        self.temperatura = ttk.Label(self.marc_dret, font = "Gabriola 25")
        self.temperatura.grid(row = 1, column = 1, pady = 10, padx = 10)

        #creem l'etiqueta que mostrarà la descripció
        self.descripcio = ttk.Label(self.marc_dret, font = "Gabriola 15")
        self.descripcio.grid(row = 2, column = 0, pady = 10, padx = 10)

        #creem l'etiqueta que mostrarà el real feel
        self.real_feel = ttk.Label(self.marc_dret, font = "Gabriola 15")
        self.real_feel.grid(row = 2, column = 1, pady = 10, padx = 10)

        #creem el botó per obtenir el clima
        self.boto_clima = ttk.Button(self.marc_esquerre, text = "Obtenir predicció", command = lambda : obtenir_clima(self.entrada_ciutat.get(), self.nom, self.icona, self.temperatura, self.descripcio, self.real_feel, icones))
        self.boto_clima.pack(pady = 5, padx = 10)

    def iniciar_app(self):
        self.finestra_principal.mainloop()
    

    


