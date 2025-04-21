from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

text = ""
deleted = False

@app.route('/share', methods=['POST', 'GET'])
def share():
    if request.method == "POST":
        global text, deleted
        text = request.form.get("txt")
        if text:
            return render_template("txt_view.html", text=text, deleted = deleted)
        else:
            return render_template("txt_view.html", text="Nothing to show" )
    return render_template("txt_view.html", text=text, deleted = deleted)
    
       

@app.route("/updatefortoday", methods=['GET', 'POST'])
def updatefortoday():
    if request.method == "GET":
        global deleted
        deleted = False
        return """
        <html><head>
        <title>Notepad</title>
        <style>
        
        </style></head>
        <body>
        <form action = "/share" method = "POST">
       
        Enter Text: <textarea type="textbox" name="txt" placeholder="Enter Update here" /></textarea>
        
        <br/>
        <input type="submit" name = "form-submit">
        </form>
        </body>
        </html>"""
    

@app.route("/clearnotepadtxt", methods=['GET'])
def clearnotepadtxt():
        if request.method == "GET":
            global text
            global deleted
            text = ""
            deleted = True
            return redirect(url_for('share'))
    

if __name__ == '__main__':
    app.run() 


