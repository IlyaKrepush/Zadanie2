from flask import Flask,render_template,request

app = Flask(__name__, static_folder="static")

@app.route('/', methods=['GET', 'POST'])
def main():
    cifru="0123456789"
    stroka_data = request.form.get("text")
    if stroka_data is not None:
        count=0
        for i in stroka_data:
            if i in cifru:
                count+=1
    return render_template("1.html",count=count)

if __name__ == '__main__':
    app.run(debug=True)
