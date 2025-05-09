from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CompanyInformationSerializer
from .model.convert_to_json import generate_chatbot_training_data
from .model.create_json import create_json
from .model.train import train_bot


epochList = [1000]

class CompanyInformationAPI(APIView):
    def post(self, request):
        serializer = CompanyInformationSerializer(data=request.data)
        if serializer.is_valid():
            json_data = request.data

            userEnteredEpoch = request.data.get("epoch")
            epochList.insert(0,userEnteredEpoch)
            for_training_data = generate_chatbot_training_data(json_data)
            create_json(for_training_data)
            
            serializer.save()

            return Response({"message": "Company information saved and training data created.", "data": serializer.data})
        return Response(serializer.errors)


class TrainBotAPI(APIView):
    def post(self, request):
        try:
            userEnteredEpoch = epochList[0]
            train_bot(userEnteredEpoch)
            return Response({"message": "Bot training initiated successfully. Progress updates will be sent via WebSocket."})
        except Exception as e:
            print(f"Error during bot training: {str(e)}")
            return Response({"error": str(e)}, status=500)
