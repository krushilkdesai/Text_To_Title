import urlToTitle as uTl
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_word():
    text = None
    description = 'No available..'
    if request.method == 'POST':
        url = request.form['url']
    
        if not url:
            text = 'Enter valid URL'
        else:
            print(url)
            url = url
            text,description = uTl.get_title_from_url(url)

    return render_template('index.html', text=text, description=description)

if __name__ == '__main__':
    app.run(debug=True)

