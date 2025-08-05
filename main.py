from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # lógica del bot
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
