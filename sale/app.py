from flask import Flask, render_template,request

import pickle
import numpy as np

# object creation
app=Flask(__name__)  


with open("sales_model.pkl","rb") as f:
    model=pickle.load(f) 
# create the routing
@app.route('/') 
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict",methods=['POST'])
def predict():
   
    if request.method=='POST':
        day=float(request.form.get('day'))
        month=float(request.form.get('month'))
        year=float(request.form.get('year'))
        store=float(request.form.get('store'))
        fuel=float(request.form.get('fuel'))
        cpi=float(request.form.get('cpi'))
        unemploy=float(request.form.get('unemploy'))

        lst=[day,month,year,store,fuel,cpi,unemploy]
        print(lst)
        lst_pr=np.array([lst])
        pr=model.predict(lst_pr)
        output=pr
       
        print(output)
        
        
       
   
        
    return render_template('predict.html',op=output)
    


if __name__=='__main__':
    app.run(debug=True)

