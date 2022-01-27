import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    x = np.cumsum(range(1,11))
    last = x[-1]
    return 'The sum of 1 to 10 is {}'.format(last)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)