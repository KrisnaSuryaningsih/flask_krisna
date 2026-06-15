from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello Krisna!</h1>
    <p>Web Flask berhasil berjalan.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)