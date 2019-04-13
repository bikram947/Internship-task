from flask import Flask,render_template,request
app = Flask(__name__)
name1=""
@app.route("/")
def otd():
    return render_template('otd_main.html')
#bikram    
@app.route("/otdresult", methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        lt=[]
        for key, values in result.items():
            lt.append(values)
        import otd_data
        data=otd_data.otd(lt[0],lt[1])
        if(len(data[0])==0):
            result0="No Zero hop routes"
        else:
            result0="zero hop routes_id  are= {}".format(data[0])
        if(len(data[1])==0):
            result1="NO One hop routes present"
        else:
            result1="one hop routes_id are= {}".format(data[1])

        result=[result0,result1]
        return render_template("otd_result.html",result=result)


if __name__ == "__main__":
    app.run(debug=True)
