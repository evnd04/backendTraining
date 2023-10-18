from userDAO import UserDAO
from flask import Flask, request, jsonify

class User:
    
    def addNewUser(self, request):
        # Ensure all required fields are present in the request data
        required_fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email_address', 'password']
        if not all(field in request for field in required_fields):
            return jsonify({"message": "Missing required fields"}), 400

        # Call the UserDAO method to create the user
        UserDAO().addNewUser(request)

        return jsonify({"message": "User created successfully"}), 201
    
    def getUserByEmail(self, email_adress):
        user = UserDAO().getUserByEmail(email_adress)
        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "User not found"}), 404
        
    def getUserById(self, user_id):
        user = UserDAO().getUserById(user_id)
        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "User not found"}), 404

    