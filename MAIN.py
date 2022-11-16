import pandas as pd #Biblioteca pra ler arquivos CSV, Execel e etc...
import matplotlib.pyplot as plt #BiBlioteca pra criar os Graficos
import PySimpleGUI as sg #Biblioteca para criar as janelas
from PIL import Image #Biblioteca para inserir imagem
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator #Biblioteca para criar a nuvem de palavras 

#Criando janela e selecionando arquivo CSV
Caminho = sg.popup_get_file('Chosse a CSV file:', sg.theme('Dark Amber'))
CSV = pd.read_csv(Caminho)
CSV_I = pd.read_csv(Caminho)
CSV_DT = pd.DataFrame(CSV)

#Removendo colunas não utilizadas na criação de Graficos
CSV_DT.drop(["Carimbo de data/hora",
        "3. Informe os 7 últimos dígitos do seu RA: (109nnnxxxxxxx)",
        "7. Agora vamos falar sobre sua idade:Em qual dia você nasceu?", 
        "7-1. Em qual mês você nasceu?"], inplace=True, axis=1)

#inserindo coluna de idade e subtraindo a coluna de ano de nacimento
CSV.insert(0, "Idades", 2022) 
CSV_DT["Idades"] =  CSV["Idades"] - CSV_DT["7-2. Em qual ano você nasceu?"]

#
summary = CSV_DT.dropna(subset=["42. Escreva algumas linhas sobre sua história e seus sonhos de vida."], axis = 0) ["42. Escreva algumas linhas sobre sua história e seus sonhos de vida."]

all_summary = " ".join(s for s in summary)

print("Quantidade de Palavras; {}".format(len(all_summary)))

stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "voce", "de", "Um", "uma","eu","que","na","o","como","e","minha","para","sou","não","meus"])

wordcloud = WordCloud(stopwords=stopwords,
                background_color= "black", width=1600, height=800).generate(all_summary)


list = CSV_DT.columns[0:]
list2 = CSV_DT[CSV_DT.columns[-2]]

print(list2)
def janela_Graficos():
    sg.theme('Dark Amber')

    layout_inicio = [
        [sg.Text('Selecione o grafico á ser exibido')],
        [sg.LB(values=list[0:], key='opc', bind_return_key=True, enable_events=True, no_scrollbar=False,  s=(60, 4))],
         [sg.LB(values=list[-2:], key='opc2', bind_return_key=True, enable_events=True,  s=(60, 1))]
        ]

    window = sg.Window('Gráficos', layout_inicio, finalize=True,  keep_on_top=False)

    return window

window = janela_Graficos()


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'opc':
            CalcularCSV = values[event]
            contCSV = CSV_DT[CalcularCSV]
            Grafico = CalcularCSV[0]
            GraficoValor = contCSV.value_counts()

            explode = (0.1,0,0,0)
            plt.pie(GraficoValor,  shadow=True,  startangle=90)#, colors= ['y','r'])
            plt.title(Grafico)
            plt.legend(GraficoValor.index, ncol=1, loc="upper right", bbox_to_anchor=(1.2,1), prop={'size': 8}) #, loc="lower left")
            plt.axis("equal")
            plt.tight_layout()
            plt.show()
    elif event == 'opc2':
            fig, ax = plt.subplots(figsize=(10,6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.set_axis_off()

            plt.imshow(wordcloud)
            wordcloud.to_file("FATEC_123.png")
        
window.close()
