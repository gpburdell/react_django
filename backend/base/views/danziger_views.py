from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User


from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status
from base.models import Ladotd500MainDtldata,Ladotd502EEvent502,Ladotd502EMonitor502,Ladotd502EZero502,Ladot501WEvent501,Ladot501WMonitor501,Ladot501WZero501,Ladot601WMonitor601,Ladot601WEvent601,Ladot601WZero601,Ladot602EMonitor602,Ladot602EEvent602,Ladot602EZero602
from datetime import datetime, date, timedelta
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import numpy as np

import json

# @api_view(['GET'])
# def onegage(request,gage):
#     data = Lulling1Table1.objects.using('lndb').values('tmstamp',gage)
#     context = {
#     'x': [i['tmstamp'] for i in data],
#     'y': [i[gage] for i in data]
#     }
#     #print(context)
#     return Response(context)
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

@api_view(['GET'])
def getCurrentData(request):
    data = request.data 
    from_date='2022-02-07 00:00:00'
    to_date='2022-02-14 00:00:00'
    
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

    traces = []
    min_y = 1
    max_y = -1
    min_y2 = 1
    max_y2 = -1
    def get_min_max_y(values,min_y,max_y):
        min_y =min_y
        max_y=max_y
        for p in values:
            if p != None :
                if p > max_y:
                    max_y = p
                if p < min_y:
                    min_y = p
        return min_y, max_y

    dan502_gagelist = ['lne_med','tne_med','vne_med','se_shoe_avg','ne_shoe_avg','tilt_about_ns_med','tilt_about_ew_med','e_joint_laser_avg']

    #-----------501W
    for index,gage in enumerate(dan502_gagelist):
        print('********************dan502********************')
    
        print(gage)


        data = Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        print('here')
        if data.count() >1:
            
            print(data.count())
            y_values =[i[gage] for i in data]

            min_y, max_y = get_min_max_y(y_values,min_y,max_y)

            traces += {
                "uid": index,
                "mode": "line",
                "name": gage,
                "type": "scatter",
                # "yaxis": 'yaxis',
                "x": [i['tmstamp'] for i in data],
                "y": y_values,
                "line": {
                "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
                },
            },

    dan602_gagelist = ['lse_med','tse_med','vse_med','temp_ambient_avg','lne_ultra_in_med','tne_ultra_in_med','lse_ultra_in_med','tse_ultra_in_med']

    #-----------501W
    for index,gage in enumerate(dan602_gagelist):
        print('*******************************************')
        print(gage)


        data = Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)

        if data.count() >1:
            y_values =[i[gage] for i in data]

            min_y, max_y = get_min_max_y(y_values,min_y,max_y)
            traces += {
                "uid": index,
                "mode": "line",
                "name": gage,
                "type": "scatter",
                # "yaxis": 'yaxis',
                "x": [i['tmstamp'] for i in data],
                "y": y_values,
                "line": {
                "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
                },
            },

    

    ###############################################################

    context = {
    
    
    "layout": {
        "title": gage,
        "showlegend": "true",
        "width": 600,
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
                min_y,
                max_y
            ],
            "title": "Strain",
            "autorange": "true"
        },
        "yaxis2": {
            "type": "linear",
            "range": [
                min_y2,
                max_y2
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
def gage(request):
    data = request.data   #JSONParser().parse(request)
    print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist']['secondary']
    title = data['gagelist'].get('title')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]


    min_y = 1
    max_y = -1
    min_y2 = 1
    max_y2 = -1
    def get_min_max_y(values,min_y,max_y):
        min_y =min_y
        max_y=max_y
        for p in values:
            if p != None :
                if p > max_y:
                    max_y = p
                if p < min_y:
                    min_y = p
        return min_y, max_y

    def get_min_max_y2(values,min_y2,max_y2):
        min_y2 =min_y2
        max_y2 =max_y2
        for p in values:
            if p != None :
                if p > max_y2:
                    max_y2 = p
                if p < min_y2:
                    min_y2 = p
        return min_y2, max_y2
    traces2=[]
    for index,gage_id in enumerate(gagelist2):
        print('g2*******************************************')
        gage = gage_id.get('gage')
        print(gage)
        table = gage_id.get('table')

        if table == 'Dan502':
            data = Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'Dan602':
            data = Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)

        elif table == 'Dan501':
            data = Ladot501WMonitor501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)

        elif table == 'Dan601':
            data = Ladot601WMonitor601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = None

        if data.count() <2:
            pass
        y_values =[i[gage] for i in data]
        min_y2_=np.percentile(np.array(y_values),1)*1.2
        max_y2_=np.percentile(np.array(y_values),99)*1.2
        if min_y2_ < min_y2:
            min_y2 = min_y2_
        if max_y2_ > max_y2:
            max_y2 = max_y2_

        # min_y2, max_y2 = get_min_max_y(y_values,min_y2,max_y2)
        traces2 += {
            "uid": 100+index,
            "mode": "line",
            "name": gage_id.get('name'),
            
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
    for index,gage_id in enumerate(gagelist):
        print('g1*******************************************')
        gage = gage_id.get('gage')
        print(gage)
        table = gage_id.get('table')

        if table == 'Dan502':
            data = Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'Dan602':
            data = Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)

        elif table == 'Dan501':
            data = Ladot501WMonitor501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)

        elif table == 'Dan601':
            data = Ladot601WMonitor601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = None
        
        if data.count() <2:
            pass
       
        y_values =np.array([i[gage] for i in data])


        y_values =[i[gage] for i in data]
        min_y_=np.percentile(np.array(y_values),1)*1.2
        max_y_=np.percentile(np.array(y_values),99)*1.2
        if min_y_ < min_y:
            min_y=min_y_
        if max_y_ > max_y:
            max_y=max_y_

        # min_y2, max_y2 = get_min_max_y(y_values,min_y2,max_y2)
        traces += {
            "uid": index,
            "mode": "line",
            "name": gage_id.get('name'),
            "type": "scatter",
            # "yaxis": 'yaxis',
            "x": [i['tmstamp'] for i in data],
            "y": y_values,
            "line": {
            "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
            },
        },


    traces = traces +traces2

    ###############################################################

    context = {
    
    
    "layout": {
        "title": title,
        "showlegend": "true",
        "legend": {
		    "orientation": "v",
		    "x": 1.2,
            "xanchor": 'left',
		    "y": 1,
		    "font": {
            "size": 9
            },
		"borderwidth": 1
        },
        "width": 500,
        "height": 300,
        "autosize": "true",
        "margin":{"l":80,"r":100},
        "yaxis": {
            "type": "linear",
            "automargin": "true",
            "range": [
                min_y,
                max_y
            ],
            "title": "Strain",
            "autorange": "true"
        },
        "yaxis2": {
            "type": "linear",
            "range": [
                min_y2,
                max_y2
            ],
            "automargin": "true",
            "side": 'right',
            "title": "Temperature",
            "autorange": "true",
            "overlaying": 'y',
        },

    },
    "frames": []
    }
    
    
    context.update({"data": traces})

    return Response(context)

@api_view(['POST'])
def gage_old(request):
    import json
    print('1----------------------------------')
  
    data = request.data   #JSONParser().parse(request)
    print(f'data: {data}')

 
    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist']['secondary']
    
    date_range = data['dateRange']['dateRange']
    # from_date = request.data['from_date']

    from_date = date_range[0]
    to_date = date_range[1]
    table = data['table']
    print('table')

    




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
    min_y = 1
    max_y = -1
    min_y2 = 1
    max_y2 = -1
    def get_min_max_y(values,min_y,max_y):
        min_y =min_y
        max_y=max_y
        for p in values:
            if p != None :
                if p > max_y:
                    max_y = p
                if p < min_y:
                    min_y = p
        return min_y, max_y

    def get_min_max_y2(values,min_y2,max_y2):
        min_y2 =min_y2
        max_y2 =max_y2
        for p in values:
            if p != None :
                if p > max_y2:
                    max_y2 = p
                if p < min_y2:
                    min_y2 = p
        return min_y2, max_y2
    traces2=[]
    for index,gage in enumerate(gagelist2):
        print('*******************************************')
        print(gage)

        if table == 'Dan502':
            data = Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'Dan602':
            data = Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = None
        if data.count() <2:
            pass
        y_values =[i[gage] for i in data]
 

        min_y2, max_y2 = get_min_max_y(y_values,min_y2,max_y2)
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
        if table == 'Dan502':
            data = Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'Dan602':
            data = Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = None
        
        if data.count() <2:
            pass
        

        y_values =[i[gage] for i in data]
 

        min_y, max_y = get_min_max_y(y_values,min_y,max_y)
        traces += {
            "uid": index,
            "mode": "line",
            "name": gage,
            "type": "scatter",
            # "yaxis": 'yaxis',
            "x": [i['tmstamp'] for i in data],
            "y": y_values,
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
                min_y,
                max_y
            ],
            "title": "Strain",
            "autorange": "true"
        },
        "yaxis2": {
            "type": "linear",
            "range": [
                min_y2,
                max_y2
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
