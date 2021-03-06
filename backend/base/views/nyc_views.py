from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from base.models import Ny17Mediandata,Ny17Table1
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
        print(threshold)

        if table == 'ny17_table':
            data = pd.DataFrame(list(Ny17Mediandata.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()

        else: 
            data = None

        if data.size<2:#data.count() <2:
            pass
                
        tare = gage_id.get('tare')
        scalar = gage_id.get('scalar')
        if tare is None:
            tare = 0.0
        if scalar is None:
            scalar =1.0
            # print(f'tare: {tare}')
        if threshold:
            data = data[data[gage] > threshold[0]]
            data = data[data[gage] < threshold[1]]
        y= data[gage]*float(scalar)-float(tare)

        min_y, max_y = get_min_max_y(y, min_y, max_y)
        y = (y).values.tolist()
        x = data['tmstamp'].dt.to_pydatetime().tolist()
        
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

    return traces,min_y,max_y

#
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gage(request):
    data = request.data   #JSONParser().parse(request)
    # print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist'].get('secondary')
    title = data['gagelist'].get('title')
    y_axis_label = data['gagelist'].get('y_axis_label')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]

    min_y = -1
    max_y = 1
    min_y2 = -1
    max_y2 = 1



    traces,min_y,max_y= get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary=False)
    if gagelist2 is not None:
        traces2,min_y2,max_y2= get_gage_data(gagelist2,from_date,to_date,min_y2,max_y2,secondary=True)
        traces = traces +traces2

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