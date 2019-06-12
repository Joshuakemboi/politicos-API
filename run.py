from flask import Flask, request, jsonify

app = Flask(__name__)

users= []

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users', methods=['POST'])
def create_users():
    response = request.get_json()
    if not response:
        return jsonify(
            {
                "status": 400,
                "message": "Please provide json data"
            }
        ), 400
    else:

        first_name = response['first_name']

        newuser = {
            "first_name":first_name,
        }
        users.append(newuser)
        return jsonify({
            "status":201,
            "message":"created succesfuly",
            "data":newuser
        })
    
    # if not first_name or not last_name  or not email  or not username  or not passport or not other_name or not phone_number or not password:
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "Please fill all the fields"
    #         }
    #     ), 400
    #     abort
    # if not password !=password(password):
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "invalid password"
    #         }
    #     ), 400
    #     abort 
    # if not email !=email(email):
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "invalid email"
    #         }
    #     ), 400
    #     abort
    # if not phone_number .startswith('07') email(email):
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "wrong phone format"
    #         }
    #     ), 400
    #     abort       
    # if taken_username(username):
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "The username is already taken"
    #         }
    #     ), 400
    #     abort
    # if len(password) < 6:
    #     return jsonify(
    #         {
    #             "status": 400,
    #             "message": "Please provide a valid password"
    #         }
    #     ), 400
    #     abort
    
# @app.route('/users', methods=['GET'])
# def create_users():
#     return jsonify({
#         "status": 201,
#         "message": "Users successfully created",
#         "data": users
#     }), 200

if __name__ == '__main__':
    app.run(debug=True)