from flask import Flask, render_template, request
from collections import defaultdict
import json


with open("data.json", "r") as f:
    data = json.load(f)

classes = defaultdict(list, data)
# classes = data
# classes = json.loads(data)
# classes["math"].append("homework")

app = Flask(__name__)
tasks = []
# currentclass = 'math'

@app.route("/")
def home():
    global currentclass
    currentclass = request.args.get('classname', 'math').strip()
    return render_template('contact.html', classes=classes, tasks=classes[currentclass])

@app.route('/display', methods=['GET', 'POST'])
def task():
    global currentclass


    if request.method == 'GET':
        fname = (request.args.get("fname") or "").strip()
        newclass = (request.args.get('newclass') or '').strip()

        if newclass:
            classes[newclass]

        if fname:
            classes[request.args.get('classname') or ""].append(fname)




    if request.method == 'POST':
        selected = request.form.get('sclass')
        remove = request.form.get('remove')
        removeclass = request.form.get('removeclass')

        if remove:
            classes[currentclass].remove(request.form.get('remove'))

        if selected:
            currentclass = selected

        if removeclass:
            classes.pop(removeclass)

    tasks = classes[currentclass]

    save = json.dumps(classes, indent=4)
    with open("data.json", "w") as f:
        f.write(save)

    return render_template('contact.html', classes=classes, tasks=tasks, currentclass = currentclass)

# @app.route("/di", methods=['GET', 'POST'])





if __name__ == "__main__":
    app.run(debug=True)

