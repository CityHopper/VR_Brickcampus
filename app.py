from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

host_addr = "127.0.0.1"
port_num = "8080"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/topnav')
def topnav():
    return render_template("topnav.html")

@app.route('/escaperoom', methods=['POST', 'GET'])
def escaperoom():
    answer1 = '자연'
    message = ''
    if request.method == 'POST':
        temp = request.form.get('answ')
        if temp == answer1:
            # message = '정답이다.'
            return redirect(url_for('ursaved'))
        else:
            # message = '당신은 사망했습니다.'
            return redirect(url_for('urdead'), code=307)
    elif request.method == 'GET':
        # temp = request.args.get('answ')
        pass
        # if temp == '':
        #     pass
        # elif temp == answer1:
        #     pass
        #     # return redirect(url_for('ursaved'))
        # else:
        #     pass
        #     # return redirect(url_for('urdead'))
    else:
        pass
    return render_template('escaperoom.html')

@app.route('/ursaved')
def ursaved():
    return render_template("ursaved.html")

@app.route('/urdead', methods=['POST', 'GET'])
def urdead():
    temp = request.form.get('answ')
    return render_template("urdead.html", temp=temp)

@app.route('/storyvideo')
def storyvideo():
    return render_template("storyvideo.html")

if __name__ == '__main__':
    app.run(host=host_addr, port=port_num, debug=True)