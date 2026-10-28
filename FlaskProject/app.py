from flask import Flask, render_template, request
from collections import defaultdict

classes = defaultdict(list)
classes["math"].append("homework")

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return render_template('contact.html')

@app.route("/display", methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        classes[request.args.get('classname')].append(request.args.get('fname'))

    # return render_template('contact.html', tasks=tasks)


    if request.method == 'POST':
        tasks.remove(request.form.get('remove'))

    return render_template('contact.html', classes=classes, tasks=tasks)


def add():
    if request.method == 'GET':
        newclass = request.args.get('class+')
        classes[newclass].append("")
        classes[newclass].remove("")


if __name__ == "__main__":
    app.run(debug=True)