from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
   data = request.get_json()
   item_name = data.get('itemName')
   item_description = data.get('itemDescription')
   print(f"Received: {item_name}, {item_description}")
   # Here you can save to database
   return jsonify({"message": "Todo item submitted successfully!"})
if __name__ == '__main__':
   app.run(debug=True)
