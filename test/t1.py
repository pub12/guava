from flask import *
app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("t1.html")

@app.route("/", methods=["GET", "POST"])
def home():
    breakpoint()
    if request.method == "POST":
        
        print(request.form["name"])
        print(request.form["email"])
        return 'posted'
    return render_template("t1.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4572)