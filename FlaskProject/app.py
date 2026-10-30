from flask import Flask, render_template, request
from collections import defaultdict

classes = defaultdict(list)
classes["math"].append("homework")

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    currentclass = request.args.get('classname', 'math').strip()
    return render_template('contact.html', classes=classes, tasks=classes[currentclass])

@app.route("/display", methods=['GET', 'POST'])
def task():
    global currentclass


    if request.method == 'GET':
        fname = (request.args.get("fname") or "").strip()
        newclass = (request.args.get('newclass') or '').strip()

        if newclass:
            classes[newclass].append("")
            classes[newclass].remove("")

        if fname:
            classes[request.args.get('classname')].append(fname)




    if request.method == 'POST':
        currentclass = request.form.get('sclass')
        classes[currentclass].remove(request.form.get('remove'))

    tasks = classes[currentclass]
    return render_template('contact.html', classes=classes, tasks=tasks)

# @app.route("/di", methods=['GET', 'POST'])





if __name__ == "__main__":
    app.run(debug=True)
