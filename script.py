from flask import Flask, render_template, request
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"
debug = DebugToolbarExtension(app)

@app.route("/")
def ask():
    prompts = story.prompts
    return render_template("submit.html", prompts = prompts)

@app.route("/story")
def storyPost():
    text = story.generate(request.args)
    return render_template("index.html", text = text)