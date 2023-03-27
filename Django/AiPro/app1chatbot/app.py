'''from flask import Flask, request, render_template
from aichat import generate_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']
        response = generate_response(message)
        return render_template('chatbot/home.html', response=response, message=message)
    else:
        return render_template('chatbot/home.html')

if __name__ == '__main__':
    app.run(debug=True)
'''