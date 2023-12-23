# здесь все из констультации с Лизой
from flask import Flask, render_template, request
from control_analysis_for_flask import analysis

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/next')
def next_one(name=None):
    some_text = analysis(request.args.get('TEXT'))
    # 3 потому что 2 написала стремный
    return render_template('index3.html', name=name, some_text=some_text)


if __name__ == '__main__':
    app.run(debug=False)
