from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from base.models import Cr1000FtlaudMonitor, Ny17Table1
from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status


@api_view(['GET'])
def cr1000(request):
    data = Cr1000FtlaudMonitor.objects.using('lndb').all()
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    serializer = CR1000_Serializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def csi(request):
    data = Cr1000FtlaudMonitor.objects.using('lndb').values('tmstamp','measure_avg')
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    context = {
    'tmstamp': [i['tmstamp'] for i in data],
    'measure_avg': [i['measure_avg'] for i in data]
    }
    #print(context)
    return Response(context)

@api_view(['GET'])
def ny17(request):
    data = Ny17Table1.objects.using('lndb').values('tmstamp','laser_18_avg')
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    context = {
    'tmstamp': [i['tmstamp'] for i in data],
    'laser_18_avg': [i['laser_18_avg'] for i in data]
    }
    #print(context)
    return Response(context)

@api_view(['GET'])
def ny17onegage(request,gage):
    data = Ny17Table1.objects.using('lndb').values('tmstamp',gage)
    context = {
    'x': [i['tmstamp'] for i in data],
    'y': [i[gage] for i in data]
    }
    #print(context)
    return Response(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ny17gage(request):
    import json
    print('1----------------------------------')
  
    data = request.data   #JSONParser().parse(request)
    print(f'data: {data}')
    #print(type(data))
    # print(request.POST.get('gagelist'))
    # data = json.loads(request.POST.get('gagelist'))
    # print(type(data))
    # data2 = json.loads(request.data.get['gagelist'])
    #gagelist= data.get('gagelist').get('primary')
    # print('data2')
    # print(type(data2))

    # gagelist = json.loads(data)
    # gagelist = print(f'dict: {data}')
    # print(type(data))
    # #data['gagelist'].strip('[]').split(',')
    # print(data.get('primary'))
    # gagelist = data.get('primary')
    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist']['secondary']
    date_range = data['dateRange']['dateRange']
    # from_date = request.data['from_date']
    from_date = date_range[0]

    from datetime import datetime, date, timedelta
    from django.utils.dateparse import parse_datetime
    from django.utils import timezone

    # for gage in gagelist:
    #     print('*******************************************')
    #     print(f'gage: {gage}')
    colors =[
    '#1f77b4',  # muted blue
    '#ff7f0e',  # safety orange
    '#2ca02c',  # cooked asparagus green
    '#d62728',  # brick red
    '#9467bd',  # muted purple
    '#8c564b',  # chestnut brown
    '#e377c2',  # raspberry yogurt pink
    '#7f7f7f',  # middle gray
    '#bcbd22',  # curry yellow-green
    '#17becf'   # blue-teal
    ]
    traces2=[]
    for index,gage in enumerate(gagelist2):
        print('*******************************************')
        print(gage)
        data = Ny17Table1.objects.using('lndb').filter(tmstamp__range=[from_date, "2022-01-31"]).values('tmstamp',gage)
        
        traces2 += {
            "uid": 100+index,
            "mode": "line",
            "name": gage,
            
            "type": "scatter",
            "x": [i['tmstamp'] for i in data],
            "y": [i[gage] for i in data],
            "line": {
                "color": "rgba(180, 180, 180, 1.0)",#colors[index],
                "width": 1,
                'dash': 'dash',
            },
            "yaxis": 'y2',
        },
    traces=[]
    for index,gage in enumerate(gagelist):
        print('*******************************************')
        print(gage)
        data = Ny17Table1.objects.using('lndb').filter(tmstamp__range=[from_date, "2022-01-31"]).values('tmstamp',gage)
        traces += {
            "uid": index,
            "mode": "line",
            "name": gage,
            "type": "scatter",
            # "yaxis": 'yaxis',
            "x": [i['tmstamp'] for i in data],
            "y": [i[gage] for i in data],
            "line": {
            "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
            },
        },


    traces = traces +traces2

    ###############################################################

    context = {
    
    
    "layout": {
        "title": gage,
        "showlegend": "true",
        "width": 800,
        # "xaxis": {
            # "type": "date",

            # "title": "Source: <a href=\"http://www.scribblrs.com/\">Scribblrs</a><br>Source: <a href=\"http://www.internetlivestats.com/total-number-of-websites/\">Internet Live Stats</a>",
            # "showgrid": "false",
            # "autorange": "true",
            # "tickformat": "%y/%m"
        # },
        "yaxis": {
            "type": "linear",
            "range": [
                -0,
                1666
            ],
            "title": "Displacement",
            "autorange": "true"
        },
        "yaxis2": {
            "type": "linear",
            "range": [
                0,
                100
            ],
            "side": 'right',
            "title": "Temperature",
            "autorange": "true",
            "overlaying": 'y',
        },
        "height": 500,
        "autosize": "true"
    },
    "frames": []
    }
    
    
    context.update({"data": traces})

    return Response(context)

@api_view(['POST'])
def ny17gage_old(request):

    data = request.data
    gage = data['gage']
    from_date = data['from_date']

    from datetime import datetime, date, timedelta
    from django.utils.dateparse import parse_datetime
    from django.utils import timezone

    # the datetime value passed to make_aware() can be any datetime
    # you could even use datetime.strptime() if you want
    # (as mentioned in the accepted anwser)
    # there are more ways to make datetime aware
    # but this was simplest to me
    aware_datetime = timezone.make_aware(datetime.now())

    # storing the two dates for easier reading
    start_date = aware_datetime - timedelta(days=1)
    end_date = aware_datetime + timedelta(days=7)

    start_date = '2022-01-01 00:00:00'
    end_date = '2022-02-01 00:00:00'


    data = Ny17Table1.objects.using('lndb').filter(tmstamp__range=[from_date, "2022-01-31"]).values('tmstamp',gage)
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    trace1 =        {
            "uid": "aaabbb",
            "mode": "line",
            "name": "Trace1",
            "type": "scatter",
            "x": [i['tmstamp'] for i in data],
            "y": [i[gage] for i in data],
            "line": {
            "color": "rgba(55, 128, 191, 1.0)","width": 1
            },
        },
    trace2= {
            "uid": "bbbbaaa",
            "mode": "line",
            "name": "Trace2",
            "type": "scatter",
            "x": [i['tmstamp'] for i in data],
            "y": [i[gage] *2 for i in data],
            "line": {
            "color": "rgba(255, 0, 0, 1.0)","width": 1
            },
        },
    context = {
    
    
    "layout": {
        "title": gage,
        "showlegend": "true",
        "width": 800,
        "xaxis": {
            "type": "date",

            # "title": "Source: <a href=\"http://www.scribblrs.com/\">Scribblrs</a><br>Source: <a href=\"http://www.internetlivestats.com/total-number-of-websites/\">Internet Live Stats</a>",
            "showgrid": "false",
            "autorange": "true",
            "tickformat": "%Y"
        },
        "yaxis": {
            "type": "linear",
            "range": [
                -1500,
                1666
            ],
            "title": "",
            "autorange": "true"
        },
        "height": 500,
        "autosize": "false"
    },
    "frames": []
    }
    
    
    context.update({"data": trace1+trace2})
    #context["data"]={[trace1,trace2]}
    #print(context)
    return Response(context)