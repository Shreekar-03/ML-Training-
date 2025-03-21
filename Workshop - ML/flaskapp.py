from flask import Flask,jsonify, request

app = Flask(__name__)

items = [
    {"id":1,"name":"Item 1","price":10.11},
    {"id":2,"name":"Item 2","price":9.11}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# @app.route('/items/<int:item_id>', methods=['GET'])
# def get_items(item_id):

#     return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)