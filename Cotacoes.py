import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

janela = Tk()
janela.geometry("400x400")

janela.title("Cotação Moedas")
texto_orientacao = Label(janela, text="Clique no botão abaixo para pegar as cotações atualizadas das moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text="Pegar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()