from django.shortcuts import render
import requests;
from myapp.forms import Cform;
# Create your views here.
def index(request):
    #appid="a0d5659a015c8b72076e37f18fb9b18b";
    if request.method=="POST":
            form=Cform(request.POST);
            if form.is_valid():
                city=form.cleaned_data.get('name');
                url="http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=a0d5659a015c8b72076e37f18fb9b18b";
                response=requests.get(url.format(city));
                json_response=response.json();
                if response.status_code==200 and json_response['list']:
                        # response=response.json();
                        # if response['list']:
                        # response=response.json();

                            name=json_response['list'][0]['name'];
                            temp=json_response['list'][0]['main']['temp'];
                            des=json_response['list'][0]['weather'][0]['description'];
                            icon=json_response['list'][0]['weather'][0]['icon'];
                            wind=json_response['list'][0]['wind']['speed'];
                            country=json_response['list'][0]['sys']['country'];
                            rain=json_response['list'][0]['rain'];
                            snow=json_response['list'][0]['snow'];
                            weather={
                                "city":name,"temp":temp,
                                "des":des,"icon":icon,"wind":wind,"country":country,"rain":rain,"snow":snow
                            };
                            return render(request,"index.html",{"weather":weather,"form":form,"valid":True});
                        # else:
                        #     return render(request,"index.html",{"valid":False,"touser":"Please Be Sure Of City Name And Spelling","form":form})
                else:
                        return render(request,"index.html",{"valid":False,"touser":"Please Be Sure Of City Name And Spelling","form":form})
                
    
    form=Cform();
    return render(request,"index.html",{"form":form});
