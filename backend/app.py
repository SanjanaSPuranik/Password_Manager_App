from flask import Flask, request, jsonify
from flask_cors import CORS

from storage import (
    save_password,
    get_password,
    delete_password
)

app = Flask(__name__)
CORS(app)


# LOGIN API
@app.route('/login', methods=['POST'])
def login():

    data = request.json

    password = data.get('password')

    if password == "MASTER@2026":

        return jsonify({
            "success": True
        })

    else:

        return jsonify({
            "success": False
        })


# ADD PASSWORD API
@app.route('/add', methods=['POST'])
def add_password():

    data = request.json

    site = data.get('site')
    username = data.get('username')
    password = data.get('password')

    success = save_password(
        site,
        username,
        password
    )

    if success:

        return jsonify({
            "success": True,
            "message": "Password saved successfully"
        })

    else:

        return jsonify({
            "success": False,
            "message": "Website already exists"
        })


# VIEW PASSWORD API
@app.route('/view/<site>', methods=['GET'])
def view_password(site):

    result = get_password(site)

    if result:

        return jsonify({
            "success": True,
            "site": site,
            "username": result[0],
            "password": result[1]
        })

    else:

        return jsonify({
            "success": False,
            "message": "No password found"
        })


# DELETE PASSWORD API
@app.route('/delete/<site>', methods=['DELETE'])
def remove_password(site):

    success = delete_password(site)

    if success:

        return jsonify({
            "success": True,
            "message": "Password deleted successfully"
        })

    else:

        return jsonify({
            "success": False,
            "message": "Website not found"
        })


if __name__ == '__main__':
    app.run(debug=True)