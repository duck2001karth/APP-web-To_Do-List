from asyncio import tasks
from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)

url = "https://api-todo-list-arquitectura.herokuapp.com/api/tasks"

@app.route("/")
def home():
    try:
       tasks = requests.get(url).json()["tasks"]
       print(tasks)
    except:
       print("Error!..")
       tasks = [ ] 
    
    response = {"tasks": tasks, "counter":len(tasks)}
    
    return render_template("index.html", response =response)

if __name__ == "__main__":
    app.run(debug=True)