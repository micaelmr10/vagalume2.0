

import tkinter as tk
from googletrans import translator
from gtts import gTTS
import os

def traduzir():
    texto = entrada.get("1.0", tk.END)
    tradutor = translator()
    traducao = tradutor.translate(texto,dest='pt')
    saida.delete("1.0",tk.END)
    saida.insert(tk.END,traducao.text)

def sintetizar():
    texto = saida.get("1.0",tk.END)
    voz = gTTS(texto, lang='pt')
    voz.save("traducacao.mp3")
    os.system("start traducao.mp3")

def salvar():
    texto = saida.get("1.0",tk.END)
    with open("traducao.txt,""w") as arquivo:
        arquivo.write(texto)

janela = tk.Tk()
janela.title("Vagalume 2.0")

entrada = tk.Text(janela, height=10, width=40)
entrada.pack()

botao_traduzir = tk.Button(janela,text="traduzir", command=traduzir)
botao_traduzir.pack()

saida = tk.Text(janela,height=10, width=40)
saida.pack()

botao_sintetizar = tk.Button(janela,text="Sintetizar", command=sintetizar)
botao_sintetizar.pack()

botao_salvar = tk.Button(janela, text="salvar", command=salvar)
botao_salvar.pack()

janela.mainloop()




















































