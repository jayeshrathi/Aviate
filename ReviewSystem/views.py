from json import loads

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ReviewSystem.models import Candidate
from ReviewSystem.serializers import CandidateSerializer


@api_view(['GET'])
def candidate_list(request):
    if request.method == "GET":
        try:
            candites = Candidate.objects.values('id', 'name', 'status')
        except:
            return Response("Error while fetching data")
        return Response(candites)



@api_view(['GET', 'PUT'])
def candidate_detailed(request,id):
    if request.method == "GET":
        try:


            candidate = Candidate.objects.get(id=id)
            candidate_serializer = CandidateSerializer(candidate)
        except:
            return Response("Error while fetching data")

        return Response(candidate_serializer.data)
    elif request.method == "PUT":

        candidate = Candidate.objects.get(id=id)
        candidate_serializer = CandidateSerializer(candidate, partial=True, data=request.data)
        if candidate_serializer.is_valid():
            candidate_serializer.save()
            return Response("candidate updated successfully")
        return Response(candidate_serializer.errors)

@api_view(["POST"])
def candidate_create(request):
    if request.method=="POST":
        serilizer = CandidateSerializer(data=request.data)

        if serilizer.is_valid():

            serilizer.save()
            return Response("candidate created successfully")
        print(serilizer.errors)
        return Response(serilizer.errors)

