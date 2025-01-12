from flask import Flask

main = Flask(__name__)

@main.route('/hello')
def hello():
    return 'Hello world!'
if __name__ == '__main__':
     main.run(debug=True)

