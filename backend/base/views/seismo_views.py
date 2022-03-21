from optparse import Values
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User


from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status
from base.seismo_models import HistoBe13501,HistoBe13658, HistoBe13833, HistoBe13835, HistoBe13836,\
    HistoBe13868,HistoBe14054,HistoBe19849,HistoMp12625,HistoMp12897,\
    HistoUm10307,HistoUm10308,HistoUm10374,HistoUm12302,HistoUm12319,\
    HistoUm12616,HistoUm14474,HistoUm16265,HistoUm16427,HistoUm16428,\
    HistoUm16429,HistoUm16433,HistoUm16435,HistoUm16455,HistoUm6377,\
    HistoUm6378,HistoUm6379,HistoUm6380,SeismoWaveforms
from datetime import datetime, date, timedelta
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import numpy as np
import pandas as pd
import datetime as dt
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gage(request):
    data = request.data   #JSONParser().parse(request)
    # print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    # gagelist2= data['gagelist']['secondary']
    title = data['gagelist'].get('title')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]


    min_y = -.001
    max_y = .001
    min_y2 = -.001
    max_y2 = .001

  
    # traces2,min_y2,max_y2= get_gage_data(gagelist2,from_date,to_date,min_y2,max_y2,secondary=True)
    # print(f'miny2: {min_y2} maxy2: {max_y2}')

    traces,min_y,max_y= get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary=False)
    print(f'miny: {min_y} maxy: {max_y}')
    # traces = traces +traces2
  
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
            "title": "PPV (in/s)",
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
@permission_classes([IsAuthenticated])
def gagehz(request):
    data = request.data   #JSONParser().parse(request)
    # print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    # gagelist2= data['gagelist']['secondary']
    title = data['gagelist'].get('title')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]


    min_y = -.001
    max_y = .001
    min_y2 = -.001
    max_y2 = .001

  
    # traces2,min_y2,max_y2= get_gage_data(gagelist2,from_date,to_date,min_y2,max_y2,secondary=True)
    # print(f'miny2: {min_y2} maxy2: {max_y2}')

    traces,min_y,max_y= get_gage_datahz(gagelist,from_date,to_date,min_y,max_y,secondary=False)
    print(f'miny: {min_y} maxy: {max_y}')
    # traces = traces +traces2
  
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
        "xaxis": {
            "type": "log",
            "automargin": "true",
            "range": [
                0,
                2
            ],
            "title": "PPV (in/s)",
            "autorange": "true"
        },
        "yaxis": {
            "type": "log",
            "automargin": "true",
            "range": [
                -2.5,
                1
            ],
            "title": "PPV (in/s)",
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


def get_min_max_y(values,min_y,max_y):
    min_y = min_y
    max_y= max_y
    if values.min() <min_y:
        min_y = values.min()
    if values.max() > max_y:
        max_y = values.max()
    return min_y, max_y

def get_table_data(table,from_date,to_date):
    if table == 'histo_be13501':
        data = pd.DataFrame(list(HistoBe13501.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be13658':
        data = pd.DataFrame(list(HistoBe13658.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be13833':
        data = pd.DataFrame(list(HistoBe13833.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be13835':
        data = pd.DataFrame(list(HistoBe13835.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be13836':
        data = pd.DataFrame(list(HistoBe13836.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

    elif table == 'histo_be13868':
        data = pd.DataFrame(list(HistoBe13868.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be14054':
        data = pd.DataFrame(list(HistoBe14054.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_be19849':
        data = pd.DataFrame(list(HistoBe19849.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_mp12625':
        data = pd.DataFrame(list(HistoMp12625.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_mp12897':
        data = pd.DataFrame(list(HistoMp12897.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

    elif table == 'histo_um10307':
        data = pd.DataFrame(list(HistoUm10307.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um10308':
        data = pd.DataFrame(list(HistoUm10308.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um10374':
        data = pd.DataFrame(list(HistoUm10374.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um12302':
        data = pd.DataFrame(list(HistoUm12302.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um12319':
        data = pd.DataFrame(list(HistoUm12319.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

    elif table == 'histo_um12616':
        data = pd.DataFrame(list(HistoUm12616.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um14474':
        data = pd.DataFrame(list(HistoUm14474.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16265':
        data = pd.DataFrame(list(HistoUm16265.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16427':
        data = pd.DataFrame(list(HistoUm16427.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16428':
        data = pd.DataFrame(list(HistoUm16428.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

    elif table == 'histo_um16429':
        data = pd.DataFrame(list(HistoUm16429.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16433':
        data = pd.DataFrame(list(HistoUm16433.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16435':
        data = pd.DataFrame(list(HistoUm16435.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um16455':
        data = pd.DataFrame(list(HistoUm16455.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um6377':
        data = pd.DataFrame(list(HistoUm6377.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        
    elif table == 'histo_um6378':
        data = pd.DataFrame(list(HistoUm6378.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um6379':
        data = pd.DataFrame(list(HistoUm6379.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    elif table == 'histo_um6380':
        data = pd.DataFrame(list(HistoUm6380.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
    else: 
        data = None
    return data



def get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary):
    traces =[]
    for index,gage_id in enumerate(gagelist):
        print('ggd*******************************************')
        gage = gage_id.get('gage')
        print(gage)
        table = gage_id.get('table')
        threshold = gage_id.get('threshold')

        #data = get_table_data(table,from_date,to_date)
        if table == 'histo_be13501':
            data = pd.DataFrame(list(HistoBe13501.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be13658':
            data = pd.DataFrame(list(HistoBe13658.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be13833':
            data = pd.DataFrame(list(HistoBe13833.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be13835':
            data = pd.DataFrame(list(HistoBe13835.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be13836':
            data = pd.DataFrame(list(HistoBe13836.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

        elif table == 'histo_be13868':
            data = pd.DataFrame(list(HistoBe13868.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be14054':
            data = pd.DataFrame(list(HistoBe14054.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_be19849':
            data = pd.DataFrame(list(HistoBe19849.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_mp12625':
            data = pd.DataFrame(list(HistoMp12625.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_mp12897':
            data = pd.DataFrame(list(HistoMp12897.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

        elif table == 'histo_um10307':
            data = pd.DataFrame(list(HistoUm10307.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um10308':
            data = pd.DataFrame(list(HistoUm10308.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um10374':
            data = pd.DataFrame(list(HistoUm10374.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um12302':
            data = pd.DataFrame(list(HistoUm12302.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um12319':
            data = pd.DataFrame(list(HistoUm12319.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

        elif table == 'histo_um12616':
            data = pd.DataFrame(list(HistoUm12616.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um14474':
            data = pd.DataFrame(list(HistoUm14474.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16265':
            data = pd.DataFrame(list(HistoUm16265.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16427':
            data = pd.DataFrame(list(HistoUm16427.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16428':
            data = pd.DataFrame(list(HistoUm16428.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()

        elif table == 'histo_um16429':
            data = pd.DataFrame(list(HistoUm16429.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16433':
            data = pd.DataFrame(list(HistoUm16433.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16435':
            data = pd.DataFrame(list(HistoUm16435.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um16455':
            data = pd.DataFrame(list(HistoUm16455.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um6377':
            data = pd.DataFrame(list(HistoUm6377.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
            
        elif table == 'histo_um6378':
            data = pd.DataFrame(list(HistoUm6378.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um6379':
            data = pd.DataFrame(list(HistoUm6379.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        elif table == 'histo_um6380':
            data = pd.DataFrame(list(HistoUm6380.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values('timestamp',gage))).dropna()
        else: 
            data = None

        if data.size<2:#data.count() <2:
            pass
                
        tare = gage_id.get('tare')
        scalar = gage_id.get('scalar')
        if threshold:
            data = data[data[gage] > threshold[0]]
            data = data[data[gage] < threshold[1]]
        if tare is None:
            tare = 0.0
        if scalar is None:
            scalar =1.0
            # print(f'tare: {tare}')
        y= data[gage]*float(scalar)-float(tare)

        min_y, max_y = get_min_max_y(y, min_y, max_y)
        y = (y).values.tolist()
        x = data['timestamp'].dt.to_pydatetime().tolist()
        
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
            "mode": "markers",
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


    return traces,min_y,max_y

    
def get_gage_datahz(gagelist,from_date,to_date,min_y,max_y,secondary):
    traces =[]
    for index,gage_id in enumerate(gagelist):
        print('ggd*******************************************')
        gage = gage_id.get('gage')
        freq = gage_id.get('freq')
        print(gage)
        table = gage_id.get('table')
        threshold = gage_id.get('threshold')

        #data = get_table_data(table,from_date,to_date)
        if table == 'histo_be13501':
            data = pd.DataFrame(list(HistoBe13501.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be13658':
            data = pd.DataFrame(list(HistoBe13658.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be13833':
            data = pd.DataFrame(list(HistoBe13833.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be13835':
            data = pd.DataFrame(list(HistoBe13835.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be13836':
            data = pd.DataFrame(list(HistoBe13836.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()

        elif table == 'histo_be13868':
            data = pd.DataFrame(list(HistoBe13868.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be14054':
            data = pd.DataFrame(list(HistoBe14054.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_be19849':
            data = pd.DataFrame(list(HistoBe19849.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_mp12625':
            data = pd.DataFrame(list(HistoMp12625.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_mp12897':
            data = pd.DataFrame(list(HistoMp12897.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()

        elif table == 'histo_um10307':
            data = pd.DataFrame(list(HistoUm10307.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um10308':
            data = pd.DataFrame(list(HistoUm10308.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um10374':
            data = pd.DataFrame(list(HistoUm10374.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um12302':
            data = pd.DataFrame(list(HistoUm12302.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um12319':
            data = pd.DataFrame(list(HistoUm12319.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()

        elif table == 'histo_um12616':
            data = pd.DataFrame(list(HistoUm12616.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um14474':
            data = pd.DataFrame(list(HistoUm14474.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16265':
            data = pd.DataFrame(list(HistoUm16265.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16427':
            data = pd.DataFrame(list(HistoUm16427.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16428':
            data = pd.DataFrame(list(HistoUm16428.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()

        elif table == 'histo_um16429':
            data = pd.DataFrame(list(HistoUm16429.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16433':
            data = pd.DataFrame(list(HistoUm16433.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16435':
            data = pd.DataFrame(list(HistoUm16435.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um16455':
            data = pd.DataFrame(list(HistoUm16455.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um6377':
            data = pd.DataFrame(list(HistoUm6377.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
            
        elif table == 'histo_um6378':
            data = pd.DataFrame(list(HistoUm6378.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um6379':
            data = pd.DataFrame(list(HistoUm6379.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        elif table == 'histo_um6380':
            data = pd.DataFrame(list(HistoUm6380.objects.using('seismo').filter(timestamp__range=[from_date, to_date]).values(freq,gage))).dropna()
        else: 
            data = None

        if data.size<2:#data.count() <2:
            pass
                
        tare = gage_id.get('tare')
        scalar = gage_id.get('scalar')
        if threshold:
            data = data[data[gage] > threshold[0]]
            data = data[data[gage] < threshold[1]]
        if tare is None:
            tare = 0.0
        if scalar is None:
            scalar =1.0
            # print(f'tare: {tare}')
        y= data[gage]*float(scalar)-float(tare)

        min_y, max_y = get_min_max_y(y, min_y, max_y)
        y = (y).values.tolist()
        x = data[freq].tolist()
        
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
            "mode": "markers",
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


    return traces,min_y,max_y

