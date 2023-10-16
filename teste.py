from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'titulo': 'os 3 mosqueteiros',
        'autor': 'alexandre dumas'
    },
    {
        'id': 2,
        'titulo': 'harry potter e a pedra filosofal',
        'autor': 'j. k howlink'
    },   
     {
        'id': 3,
        'titulo': 'james clear',
        'autor': 'habitos aatomicos'
    }   
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(books)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    book_changed = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(book_changed)
            return jsonify(books[indice])

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    new_book =  request.get_json()
    books.append(new_book)
    return jsonify(books)



app.run(port=5000, host='localhost', debug=True)