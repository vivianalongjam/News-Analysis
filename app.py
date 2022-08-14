from flask import Flask, render_template
app = Flask(__name__)

with open("sentiment", "r") as f:
  text = f.read().strip()

color = ""
if text.split(" ")[-1] == "POSITIVE":
  color = "green"
elif text.split(" ")[-1] == "NEGATIVE":
  color = "red"
else:
  color = "yellow"

@app.route('/')
def page():
  return render_template("page.html", text=text,color=color)