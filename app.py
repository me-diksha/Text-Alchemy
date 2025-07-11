from flask import Flask, render_template, request
from project_text import summarizer
from project_trans import detect1, translate1,language

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum1')
def sum():
    return render_template('sum1.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary , og_txt, len_og_txt, len_summary=summarizer(rawtext)
    return render_template('summary.html',summary=summary, og_txt= og_txt,len_og_txt=len_og_txt,len_summary=len_summary)   

@app.route('/translate')
def translate():
    ln=language()
    return render_template('translate.html',ln=ln)

@app.route('/translat',methods=['GET','POST']) 
def translat():
    if request.method=='POST':
        text= request.form['rawtext']
        lang=request.form['dest']
        print('text :',text,'lang:',lang)
        dt= detect1(text)
        trans=translate1(text,lang)
        tr=trans.text
        return render_template('translated.html',dt=dt,tr=tr)
            

if __name__ == "__main__":
    app.run(debug=True)