from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subjects = request.form['subject']
        message = request.form['message']
        
        return f"Your Name:  {name}\nYour Email:  {email}\nThe Subject:  {subjects}\nMessage:  {message} "
        
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
