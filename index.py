from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "✅ Success! The server is running. The error was in the scraper code."

if __name__ == '__main__':
    app.run(debug=True)
