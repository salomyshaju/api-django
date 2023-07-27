from django.shortcuts import render
from .models import premium,prem,products
from .serializers import premiumSerializer,premSerializer,pairSerializer,productSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def premiumfn(request):
    if request.method=="POST":
        serializer=premiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data saved successfully"})
@api_view(['POST'])
def premm(request):
    if request.method=="POST":
        serializer=premSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
        
            serializer.save()
            return Response({"msg":"data saved successfully"})
   
@api_view(['POST'])
def pairr(request):
    if request.method=="POST":
        serializer=pairSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
        
            serializer.save()
            return Response({"msg":"data saved successfully"})

@api_view(['GET'])
def pro(request):
    prod = products.objects.all()
    serializer = productSerializer(prod,many=True,context={'request':request})
    return Response(serializer.data)