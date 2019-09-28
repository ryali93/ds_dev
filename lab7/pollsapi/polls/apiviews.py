from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


#class PollList(APIView):
#    def get(self, request):
#        polls = Poll.objects.all()[:10]
#        data = PollSerializer(polls, many=True).data
#        return Response(data)

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


#class PollDetail(APIView):
#    def get(self, request, pk):
#        poll = get_object_or_404(Poll, pk=pk)
#        data = PollSerializer(poll).data
#        return Response(data)


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
