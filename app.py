from flask import Flask, request

app = Flask(__name__)

#Variable used to count post requests
counter = 0 
@app.route("/", methods=['POST', 'GET'])
def hello():
    global counter
    if request.method == 'POST':
        #Increment when is post request
        counter += 1 
        #Return a message when is post request
        return "Hello World!!!"
        return
    if request.method == 'GET':
        pass
    #Return counter variable as string
    return str(counter)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
