from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    bmi = ''
    weight = ''
    height = '' 
    
    if request.method == 'POST' and 'userweight' in request.form:
        weight = float(request.form.get('userweight'))
        height = float(request.form.get('userheight'))

        bmi = round(weight / ((height/100)**2),2)

    return  render_template('index.html', weight = weight, height = height, bmi = bmi)

app.run()


