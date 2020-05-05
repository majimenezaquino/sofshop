from flask import Flask, json, jsonify, request
app=Flask(__name__)

@app.route("/")
def home():
    return "welcome flask"

@app.route("/webhook",methods=["POST"])
def get_callback():
    print(request.get_json())
    return "hola"



if(__name__ =="__main__"):
    app.run(debug=True)