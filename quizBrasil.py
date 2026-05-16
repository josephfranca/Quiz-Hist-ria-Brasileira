import tkinter as tk
from tkinter import messagebox

#Variáveis para controle
score = 0
perguntaAtual = 0

#Array e dicionário, o dicionário está dentro do array pq facilita para manipular
perguntas = [
    {
        "pergunta": "Em que ano Pedro Álvares Cabral chegou ao Brasil?",
        "opcoes": ["1492", "1500", "1534", "1822"],
        "correta": "1500"
    },
    {
        "pergunta": "Quem proclamou a Independência do Brasil em 1822?",
        "opcoes": ["Dom João VI", "Pedro Álvares Cabral", "Dom Pedro I", "Marechal Deodoro"],
        "correta": "Dom Pedro I"
    },
    {
        "pergunta": "Qual foi o primeiro presidente do Brasil?",
        "opcoes": ["Getúlio Vargas", "Prudente de Morais", "Floriano Peixoto", "Deodoro da Fonseca"],
        "correta": "Deodoro da Fonseca"
    },
    {
        "pergunta": "Em que ano começou a ditadura militar?",
        "opcoes": ["1912", "1500", "1972", "1964"],
        "correta": "1964"
    },
    {
        "pergunta": "O lema '50 anos em 5' foi a marca de qual presidente:",
        "opcoes": ["Getúlio Vargas", "Juscelino Kubitschek", "Castelo Branco", "Jânio Quadros"],
        "correta": "Juscelino Kubitschek"
    },
    {
        "pergunta": "O movimento das 'Diretas já' em 1984, reivindicava:",
        "opcoes": ["O fim imediato da escravidão", "Eleições diretas para presidência", "O direito de voto para as mulheres", "Eleições diretas para governador"],
        "correta": "Eleições diretas para presidência"
    }
]

def verificarResposta(indiceEscolhido):
    #Acessando variáveis do escopo global
    global score, perguntaAtual
    
    #Rastreando a pergunta do momento baseado na posição do array
    dados_perguntas = perguntas[perguntaAtual]
    #Rastreando a resposta baseado no dado do dicionário e levando em base o indíce
    escolha = dados_perguntas["opcoes"][indiceEscolhido]
    
    if escolha == dados_perguntas["correta"]:
        score += 1
        messagebox.showinfo("Sucesso", "Você acertou!")
    else:
        messagebox.showerror("Erro", f"Incorreto! A resposta era: {dados_perguntas['correta']}")
        
    perguntaAtual += 1
    atualizarInterface()
    
def atualizarInterface():
    global perguntaAtual
    
    #Verificação do número de peguntas, menor que o len para não continuar rodando dps da última pergunta
    if perguntaAtual < len(perguntas):
        #Usa o dicionário para para pegar a pergunta da vez
        dados = perguntas[perguntaAtual]
        #Altera os textos ao invés de criar novos
        labelPergunta.config(text=dados["pergunta"])
        
        #Laço for para atualizar o texto dos botões
        for i in range(4):
            botoesOpcoes[i].config(text=dados["opcoes"][i])
            
            labelScore.config(text=f"Pontuação: {score}")
    else:
        messagebox.showinfo("Fim", f"Quiz terminado! Score:{score} " )
        janela.destroy()
        
janela = tk.Tk()
janela.title("Quiz História do Brasil")
janela.geometry("480x640")

labelPergunta = tk.Label(janela, text="", font=("Arial", 12, "bold"), wraplength=350, pady=20)
labelPergunta.pack()

botoesOpcoes = []

for i in range(4):
    btn = tk.Button(janela, text="", width=25,pady=5, command=lambda x=i: verificarResposta(x))
    #lambda salva qual botão foi clicado e leva um tempo pra ativar a função que verifica a resposta
    btn.pack(pady=5)
    botoesOpcoes.append(btn)
    
labelScore = tk.Label(janela, text=f"Pontuação: {score}", font=("Arial", 10, "italic"), pady=20)
labelScore.pack()

atualizarInterface()

janela.mainloop()