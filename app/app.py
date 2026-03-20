from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "NimboLingo API is running"}

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    target = data.get("target", "es")

    return jsonify({
        "original_text": text,
        "translated_text": f"{text} (translated to {target})"
    })

@app.route("/load", methods=["GET"])
def load():
    total = 0
    for i in range(5000000):  # simulate CPU load
        total += i
    return {"status": "load simulated"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)