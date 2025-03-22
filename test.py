from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')  # This serves the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
   # return f"Hello, {name}! \n ,  your password, {password}"  # Displays the submitted name

   # simple validation
    if username == 'sabbir' and password == '123456':
         return f"Welcome, {username}!"
    else:
         return "Invalide credentails, try again !"
if __name__ == '__main__':
    app.run(debug=True)


