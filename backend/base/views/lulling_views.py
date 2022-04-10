from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from base.models import Lulling3Table1, Lulling2Table1,Lulling1Table1
from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status

from django.utils import timezone
import numpy as np
import pandas as pd
import datetime as dt
import json


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

def get_min_max_y(values,min_y,max_y):
    min_y = min_y
    max_y= max_y
    if values.min() <min_y:
        min_y = values.min()
    if values.max() > max_y:
        max_y = values.max()
    return min_y, max_y


def get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary):
    traces =[]
    for index,gage_id in enumerate(gagelist):
        print('ggd*******************************************')
        gage = gage_id.get('gage')
        print(gage)
        table = gage_id.get('table')
        threshold = gage_id.get('threshold')
        smooth = gage_id.get('smooth')

        if table == 'L1':
            data = pd.DataFrame(list(Lulling1Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        elif table == 'L2':
            data = pd.DataFrame(list(Lulling2Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        elif table == 'L3':
            data = pd.DataFrame(list(Lulling3Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        else: 
            data = None

        if data.size<2:#data.count() <2:
            pass
        
        tare = gage_id.get('tare')
        scalar = gage_id.get('scalar')
        # if threshold:
        #     data = data[data[gage] > threshold[0]]
        #     data = data[data[gage] < threshold[1]]
         
        if tare is None:
            tare = 0.0
        if scalar is None:
            scalar =1.0
            # print(f'tare: {tare}')
        
        data = data.set_index('tmstamp')
        
        # smooth =10

        if smooth is not None:
            data = data.rolling(smooth).std()
            #data = data.resample('5T').sum().median()
        data = data.reset_index()
        data = data.dropna()


        data[gage]= data[gage]*float(scalar)-float(tare)

        if threshold:
            data = data[data[gage] > threshold[0]]
            data = data[data[gage] < threshold[1]]
        y= data[gage]

        min_y, max_y = get_min_max_y(y, min_y, max_y)
        y = (y).values.tolist()

        
#
        x = data['tmstamp'].dt.to_pydatetime().tolist()

        #x = data.index.values.dt.to_pydatetime().tolist()
        #data.to_csv('data3.csv')
        if secondary==True:
            line =  {
                    "color": "rgba(180, 180, 180, 1.0)",#colors[index],
                    "width": 1,
                    'dash': 'dash',
                },
            yaxis= 'y2'
        else:
            line= {
            "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
            },
            yaxis= 'y'

        traces += {
            "uid": index,
            "mode": "line",
            "name": gage_id.get('name'),
            "type": "scatter",
            # "yaxis": 'yaxis',
            # "x": [i['tmstamp'] for i in data],
            # "y": y_values,
            "x":x,
            "y":y,
            "line": line,
            "yaxis":yaxis
        },
    #print(traces)
    return traces,min_y,max_y


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def onegage(request,gage):
    data = Lulling1Table1.objects.using('lndb').values('tmstamp',gage)
    context = {
    'x': [i['tmstamp'] for i in data],
    'y': [i[gage] for i in data]
    }
    #print(context)
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gage(request):
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

        if table == 'L1':
            data = Lulling1Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'L2':
            data = Lulling2Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = Lulling3Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        
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
        if table == 'L1':
            data = Lulling1Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        elif table == 'L2':
            data = Lulling2Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        else: 
            data = Lulling3Table1.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage)
        
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gage2(request):
    data = request.data   #JSONParser().parse(request)
    # print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist'].get('secondary')
    title = data['gagelist'].get('title')
    #y_axis_label = data['gagelist'].get('y_axis_label')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]

    # y_axes_label = data.get('config').get('y_axes_label')
    if (data.get('config') is not None):
        y_axis_label = data['config'].get('y_axis_label')



    min_y = -1
    max_y = 1
    min_y2 = -1
    max_y2 = 1



    traces,min_y,max_y= get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary=False)
    if gagelist2 is not None:
        traces2,min_y2,max_y2= get_gage_data(gagelist2,from_date,to_date,min_y2,max_y2,secondary=True)
        traces = traces +traces2

    if (data.get('config') is not None):
        y_axes_range = data['config'].get('y_axes_range')
        min_y = y_axes_range[0]
        max_y = y_axes_range[1]
      
    
  
    context = {
 
    "layout": {
        "title": title,
        "showlegend": "true",
        "legend": {
		    "orientation": "h",
		    # "x": 1.2,
            "xanchor": 'bottom',
		    "y": -0.2,
		    "font": {
            "size": 8
            },

		"borderwidth": 1
        },
        "modebar": {
            "orientation": 'v',
            #"bgcolor": 'salmon',
            # "color": 'white',
            "activecolor": '#9ED3CD'
        },
        "width": 500,
        "height": 300,
        "autosize": "false",
        "margin":{"l":80,"r":80,"t":50,"b":100},
        "yaxis": {
            "type": "linear",
            "automargin": "true",
            "range": [
                min_y,
                max_y
            ],
            "title": y_axis_label,
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


