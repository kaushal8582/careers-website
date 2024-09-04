from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'sala': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Gurgao, India',
        'sala': 'Rs. 2,00,000'
    },
    {
        'id': 3,
        'title': 'Python Developer',
        'location': 'Mumbai, India',
        'sala': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Fronted Developer',
        'location': 'Gugrat, India',
        'sala': 'Rs. 5,00,000'
    },
   
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS);

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)