from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_attribute(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        response = ""
        if not username and not password:
            response = 'Both username and password are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username:
            response = 'Username is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password:
            response = 'Password is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate_attribute(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        email = attrs.get('email')
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')

        response = ""

        # Missing all values
        if not username and not password and not email and not first_name and not last_name:
            response = 'Username, password, email, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')

        # Missing 4 values
        elif not username and not password and not email and not first_name:
            response = 'Username, password, email, and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not password and not email and not last_name:
            response = 'Username, password, email, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not password and not first_name and not last_name:
            response = 'Username, password, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not email and not first_name and not last_name:
            response = 'Username, email, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not email and not first_name and not last_name:
            response = 'Password, email, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')

        # Missing 3 values
        elif not username and not password and not email:
            response = 'Username, password, and email are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not password and not first_name:
            response = 'Username, password, and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not password and not last_name:
            response = 'Username, password, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not email and not first_name:
            response = 'Username, email, and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not email and not last_name:
            response = 'Username, email, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not first_name and not last_name:
            response = 'Username, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not email and not first_name:
            response = 'Password, email, and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not email and not last_name:
            response = 'Password, email, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not first_name and not last_name:
            response = 'Password, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not email and not first_name and not last_name:
            response = 'Email, first name, and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')

        # Missing 2 values
        elif not username and not password:
            response = 'Username and password are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not email:
            response = 'Username and email are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not first_name:
            response = 'Username and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not username and not last_name:
            response = 'Username and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not email:
            response = 'Password and email are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not first_name:
            response = 'Password and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password and not last_name:
            response = 'Password and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not email and not first_name:
            response = 'Email and first name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not email and not last_name:
            response = 'Email and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not first_name and not last_name:
            response = 'First name and last name are required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        
        # Missing 1 value
        elif not username:
            response = 'Username is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not password:
            response = 'Password is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not email:
            response = 'Email is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not first_name:
            response = 'First name is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')
        elif not last_name:
            response = 'Last name is required.'
            raise serializers.ValidationError({'response': response}, code='authorization')