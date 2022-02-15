from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "not4you"

#@app.route('/second')
#def second():
#    return render_template("second.html")
# "second" on lines 9 and 10 and 11 are independent of each other
# 9 on the web address
#10 it's the function name, won't really use this
#11  name of the html file

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/surveyIn', methods=["POST"])
def survey_post():
    print ("entering surveyIn")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print ("session info")
    print (session)
    return redirect("/afterPost")

@app.route('/afterPost',)
def from_post():
    print ("afterPost, rendering the final screen")
    return render_template("/second.html")

if __name__=="__main__":
    app.run(debug=True, port=5000)