from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to College ERP System</h1>"

@app.route("/attendance")
def attendance():
    return "<h2>Student Attendance</h2>"

@app.route("/results")
def results():
    return "<h2>Examination Results</h2>"

@app.route("/notices")
def notices():
    return "<h2>College Notices</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
