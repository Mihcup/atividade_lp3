from flask import Flask, render_template, request
app = Flask("Minha aplicação")
lista_produtos = [
    {"nome": "Jaqueta de Couro", "descricao": "Perfeita para o inverno"},
    {"nome": "Camiseta Estampada", "descricao": "Confortável e moderna"},
    {"nome": "Calça Jeans Skinny", "descricao": "Ideal para o dia a dia"},
    {"nome": "Vestido Floral", "descricao": "Ótimo para ocasiões especiais"},
    {"nome": "Tênis Esportivo", "descricao": "Para quem ama praticar esportes"},
    {"nome": "Bolsa de Couro", "descricao": "Elegante e espaçosa"},
    {"nome": "Óculos de Sol", "descricao": "Protege dos raios UV com estilo"},
    {"nome": "Moletom Confortável", "descricao": "Perfeito para os dias mais frios"},
    {"nome": "Sandália de Verão", "descricao": "Leve e confortável para passeios"},
    {"nome": "Blusa de Tricô", "descricao": "Confortável e quentinha"},
    {"nome": "Shorts Jeans", "descricao": "Ideal para dias ensolarados"},
    {"nome": "Sapato Social", "descricao": "Elegante para ocasiões formais"},
    {"nome": "Casaco de Lã", "descricao": "Para enfrentar o frio com estilo"},
    {"nome": "Saia Midi", "descricao": "Versátil para diversas ocasiões"},
    {"nome": "Mochila Esportiva", "descricao": "Prática e resistente"},
    {"nome": "Chapéu de Sol", "descricao": "Protege do sol com charme"},
    {"nome": "Blazer Clássico", "descricao": "Perfeito para looks profissionais"},
    {"nome": "Calça Legging", "descricao": "Confortável para atividades físicas"},
    {"nome": "Camisa Polo", "descricao": "Estilo casual e confortável"}
]
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/termos_uso")
def termos_uso():
    return render_template("termos_uso.html")

@app.route("/politica_privacidade")
def politica_privacidade():
    return render_template("politica_privacidade.html")

@app.route("/como_utilizar")
def como_utilizar():
    return render_template("como_utilizar.html")

@app.route("/", methods=['POST'])
def salvar_contato(): 
    return render_template("home.html")
#aqui caso dê erro, mostra o erro em específico 
if __name__ == "__main__":
    app.run(debug=True)
