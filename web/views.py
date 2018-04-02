from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response  #render_to_response是什么
import json
# Create your views here.

def Login(request):
     if request.method=='GET':
          result={}
          username = request.GET.get('username')
          mobile = request.GET.get('mobile')
          data = request.GET.get('data')
          result['user'] = username
          result['mobileNum'] = mobile
          result['data'] = data
          result = json.dumps(result)
          return HttpResponse(result,content_type='application/json')
     else:
          return render_to_response('login.html')