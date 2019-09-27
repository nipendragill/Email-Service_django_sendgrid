from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


class SendEmailView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        receivers = request.data.get('receivers')
        if receivers is None or len(receivers) == 0:
            return Response({'detail':'Please eneter email id of the receiver'},
                            status=status.HTTP_400_BAD_REQUEST)

        sender = request.data.get('sender')
        if sender is None:
            return Response({'detail': 'Please eneter yout id'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        serializer_class = EmailSerializer(data=request.data)
        transaction.set_autocommit(False)
        try:
            if serializer_class.is_valid():
                serializer_class.save()
                transaction.commit()
                transaction.set_autocommit(True)

                return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
            else:
                transaction.rollback()
                transaction.set_autocommit(False)
                return Response(serializer_class.errors(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            transaction.rollback()
            transaction.set_autocommit(False)
            return Response({'detail':'Internal Server Error Occured'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
