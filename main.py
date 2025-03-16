from flask import Flask, request, jsonify, render_template
from controller import *
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error in home : {str(e)}")
        return jsonify({ 
                "Error":str(e),
                "statusCode":500
            })

@app.route('/result', methods=['POST','GET'])
def result():
    try:
        data = request.form.to_dict()
        response = validateData(data)
        statusCode=response['statusCode']
        if statusCode ==200:
            try :
                data=response['data']
                return render_template('result.html', result=data)
            except Exception as e:
                return render_template('error.html')
        else:
            return render_template('error.html')
    except Exception as e:
        print(f"Error in result: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            })    

if __name__ == "__main__":
    app.run(debug=True , port="8080",host="0.0.0.0")