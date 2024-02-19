from flask import Flask


FAI=Flask(__name__)

@FAI.route('/StringResponse')
def StringResponse():
    return 'This is my first project  by using flask'



@FAI.route('/SecondStringResponse')
def SecondStringResponse():
    return 'This is my Second String Response project  by using flask'


if __name__=='__main__':
    FAI.run(debug=True)