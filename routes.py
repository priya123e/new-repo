from flask import Flask, render_template						
app = Flask(__name__)

@app.route("/")
@app.route("/login", methods=['GET'])
def hello():
    print("hello")
    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
