from flask import Flask , jsonify

app = Flask(__name__)


tech_stack = ["Python", "Flask", "JSON", "SQLAlchemy"]


@app.route('/',methods=['GET'])
def get_dict():
  
    response_envelope = {
    "status": "success",
    "message": "Technologies fetched successfully",
    "total_count": len(tech_stack),
    "data": tech_stack
    }

    return jsonify(response_envelope) , 200


if __name__ == '__main__':
    app.run(debug=True)
