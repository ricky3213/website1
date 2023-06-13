from flask import Flask, render_template, request, url_for, flash, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'caskJ8758TFDWcshdyxyayd5#570)98s'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['content']
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/')
def home():
    return render_template('home.html')





@app.route("/about")
def about():
    return render_template("about.html")

