from flask import Flask, json, jsonify, request
app=Flask(__name__)

@app.route("/")
def home():
    return "welcome flask"

@app.route("/webhook",methods=["POST"])
def get_callback():
    print(request.get_json())
    return {
  "fulfillmentMessages": [
    {
      "card": {
        "title": "Test desde webhook",
        "subtitle": "card text",
        "imageUri": "https://images-na.ssl-images-amazon.com/images/I/61tUTlPHb5L._AC_UX385_.jpg",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://example.com/path/for/end-user/to/follow"
          }
        ]
      }
    }
  ]
}



if(__name__ =="__main__"):
    app.run(debug=True)