from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import serializers
from . import models


class RegistrationTgUser(APIView):
    def post(self, request):
        # print("NOT SERIALIZED:", request.data)
        serializer = serializers.TgUserRegistrationSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FindChatId(APIView):
    def get(self, request, chat_id):
        try:
            user = models.TgUser.objects.get(chat_id=chat_id)
            ser_answ = serializers.TgUserChatIdSerializer({
                'chat_id': user.chat_id,
                'is_exist': True})
            return Response(ser_answ.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            ser_answ = serializers.TgUserChatIdSerializer({
                'chat_id': chat_id,
                'is_exist': False})
            return Response(ser_answ.data, status=status.HTTP_200_OK)


@login_required
def profile(request):
    user = request.user
    # user = get_object_or_404(models.TgUser, username=user.username)
    tg_name = user.first_name
    if user.last_name:
        tg_name += ' ' + user.last_name
    tg_link = 'https://t.me/' + user.tg_username if user.tg_username else None
    return render(request, 'profile.html', {
        'user': user,
        'tg_link': tg_link,
        'tg_name': tg_name
    })


def index(request):
    return redirect('login')
