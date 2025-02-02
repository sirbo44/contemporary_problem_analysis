from django.shortcuts import render, HttpResponse
import json
import requests


def map_view(request):
    return render(request, 'map.html')


def api(request):
    # res = requests.get('https://opensky-network.org/api/states/all')
    # data = json.loads(res.text)
    f = open("C:\\Users\\stsir\\OneDrive\\Υπολογιστής\\New folder\\myWebApp\\flight\\templates\\test.json")
    data = json.load(f)
    mydict = []
    for d in data['states']:
        if (d[5]!=None and d[6]!=None): 
            mylist = [d[0],d[5],d[6]]
            mydict.append(mylist)
    f.close()
    f = open("api.json", "w+")
    mydict = sorted(mydict, key=lambda x:(float(x[1]), x[2]))
    json.dump(mydict, f)
    f.close()    
    
    return render(request, 'api.json')