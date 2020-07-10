from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')
def hello_world():
    return render_template('index.html', phrase='hello', times=5)

@app.route('/<name>/<times>/<color>')
def hello_person(name, times, color):
        print('*'*80)
        print('in hello_person function')
        print(name)
        return render_template('index.html', 
        some_name=name, 
        num_times=int(times),
        box_color=color)  

# @app.route('/<name>/<times>/<color>')
# def hello_person(name, times, color):
#         print('*'*80)
#         print('in hello_person function')
#         print(name)
#         return render_template('index.html', some_name=name, 
#         num_times=int(times), box_color=color)        
      
if __name__=="__main__":       
    app.run(debug=True)    