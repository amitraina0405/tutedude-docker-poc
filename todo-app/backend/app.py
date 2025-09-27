from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
   item_name = request.form.get('itemName')
   item_description = request.form.get('itemDescription')
   print(f"Received: {item_name} - {item_description}")
   success_html = f"""
<html>
<head><title>Success</title></head>
<body>
<h1>Todo Item Submitted Successfully!</h1>
<p><strong>Item Name:</strong> {item_name}</p>
<p><strong>Description:</strong> {item_description}</p>
<a href="http://frontend:3000/">Go back to form</a>
</body>
</html>
   """
   return render_template_string(success_html)
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
