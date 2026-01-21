from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User, Department, Semester, Section


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    department_name = serializers.SerializerMethodField(read_only=True)
    semester_number = serializers.SerializerMethodField(read_only=True)
    section_name = serializers.SerializerMethodField(read_only=True)
    
    def get_department_name(self, obj):
        return obj.department.name if obj.department else None
    
    def get_semester_number(self, obj):
        return obj.semester.number if obj.semester else None
    
    def get_section_name(self, obj):
        return obj.section.name if obj.section else None
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'role', 'department', 'semester', 'section', 
            'is_active', 'date_joined', 'last_login',
            'department_name', 'semester_number', 'section_name'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                attrs['user'] = user
            else:
                raise serializers.ValidationError('Invalid credentials.')
        else:
            raise serializers.ValidationError('Must include username and password.')

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'password', 'password_confirm', 'role', 'department'
        ]
        read_only_fields = ['id']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm', None)

        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match.')

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user