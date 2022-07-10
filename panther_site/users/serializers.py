from rest_framework import serializers

from . import models


class TgUserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TgUser
        fields = [
            'username',
            'password',
            'chat_id',
            'first_name',
            'last_name',
            'tg_username'
        ]

    last_name = serializers.CharField(max_length=255, allow_null=True)

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(
                "Password should consists of 8 or more characters")

    def create(self, validated_data):
        for key in validated_data:
            if validated_data[key] == 'None':
                validated_data[key] = None
        validated_data['chat_id'] = int(validated_data['chat_id'])
        user = models.TgUser.objects.create_user(**validated_data)
        user.save()
        return user


class TgUserChatIdSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()
    is_exist = serializers.BooleanField()
