from optparse import Values
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django_pandas.io import read_frame

from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status

from datetime import datetime, date, timedelta
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import numpy as np
import pandas as pd
import datetime as dt
import json

from base.models import Ladotd500MainDtldata,Ladotd502EEvent502,Ladotd502EMonitor502,Ladotd502EZero502,Ladot501WEvent501,Ladot501WMonitor501,Ladot501WZero501,Ladot601WMonitor601,Ladot601WEvent601,Ladot601WZero601,Ladot602EMonitor602,Ladot602EEvent602,Ladot602EZero602
from base.analytics_model import DanzBearingEast,DanzBearingEast2,DanzBearingLimits,DanzBearingWest,DanzBearingWest2,DanzLifts,DanzResensyWide1Min,DanzUltraRaw,Resensys1HMedian,DanzBearingEast2,DanzBearingWest2


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

limits_dict = {'sensor_0_banda': {'west': 0.002, 'east': 0.0025},
 'sensor_1_banda': {'west': 0.003, 'east': 0.003},
 'sensor_2_banda': {'west': 0.0035, 'east': 0.003},
 'sensor_3_banda': {'west': 0.002, 'east': 0.0025},
 'sensor_4_banda': {'west': 0.0025, 'east': 0.0025},
 'sensor_5_banda': {'west': 0.003, 'east': 0.0035},
 'sensor_6_banda': {'west': 0.003, 'east': 0.0035},
 'sensor_7_banda': {'west': 0.002, 'east': 0.003},
 'sensor_8_banda': {'west': 0.002, 'east': 0.002},
 'sensor_9_banda': {'west': 0.004, 'east': 0.0025},
 'sensor_10_banda': {'west': 0.0035, 'east': 0.002},
 'sensor_11_banda': {'west': 0.002, 'east': 0.002},
 'sensor_12_banda': {'west': 0.002, 'east': 0.0015},
 'sensor_13_banda': {'west': 0.003, 'east': 0.0025},
 'sensor_14_banda': {'west': 0.003, 'east': 0.0025},
 'sensor_15_banda': {'west': 0.002, 'east': 0.002},
 'sensor_0_bandb': {'west': 0.003, 'east': 0.003},
 'sensor_1_bandb': {'west': 0.0045, 'east': 0.005},
 'sensor_2_bandb': {'west': 0.0045, 'east': 0.006},
 'sensor_3_bandb': {'west': 0.0025, 'east': 0.003},
 'sensor_4_bandb': {'west': 0.004, 'east': 0.004},
 'sensor_5_bandb': {'west': 0.007, 'east': 0.006},
 'sensor_6_bandb': {'west': 0.007, 'east': 0.006},
 'sensor_7_bandb': {'west': 0.004, 'east': 0.004},
 'sensor_8_bandb': {'west': 0.004, 'east': 0.003},
 'sensor_9_bandb': {'west': 0.007, 'east': 0.006},
 'sensor_10_bandb': {'west': 0.008, 'east': 0.006},
 'sensor_11_bandb': {'west': 0.0055, 'east': 0.003},
 'sensor_12_bandb': {'west': 0.002, 'east': 0.002},
 'sensor_13_bandb': {'west': 0.004, 'east': 0.004},
 'sensor_14_bandb': {'west': 0.0045, 'east': 0.004},
 'sensor_15_bandb': {'west': 0.0025, 'east': 0.003},
 'sensor_0_bandc': {'west': 0.002, 'east': 0.002},
 'sensor_1_bandc': {'west': 0.003, 'east': 0.003},
 'sensor_2_bandc': {'west': 0.003, 'east': 0.003},
 'sensor_3_bandc': {'west': 0.0016, 'east': 0.002},
 'sensor_4_bandc': {'west': 0.003, 'east': 0.003},
 'sensor_5_bandc': {'west': 0.005, 'east': 0.004},
 'sensor_6_bandc': {'west': 0.005, 'east': 0.005},
 'sensor_7_bandc': {'west': 0.004, 'east': 0.0025},
 'sensor_8_bandc': {'west': 0.0025, 'east': 0.0025},
 'sensor_9_bandc': {'west': 0.004, 'east': 0.005},
 'sensor_10_bandc': {'west': 0.0035, 'east': 0.004},
 'sensor_11_bandc': {'west': 0.003, 'east': 0.0025},
 'sensor_12_bandc': {'west': 0.002, 'east': 0.0025},
 'sensor_13_bandc': {'west': 0.0025, 'east': 0.002},
 'sensor_14_bandc': {'west': 0.0035, 'east': 0.0025},
 'sensor_15_bandc': {'west': 0.002, 'east': 0.002}}

def get_dataframe(gage,table,from_date, to_date):
            
    if table == 'Dan502':
        data = pd.DataFrame(list(Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan602':
        data = pd.DataFrame(list(Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan501':
        data = pd.DataFrame(list(Ladot501WMonitor501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan601':
        data = pd.DataFrame(list(Ladot601WMonitor601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan502_event':
        data = pd.DataFrame(list(Ladotd502EEvent502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan602_event':
        data = pd.DataFrame(list(Ladot602EEvent602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan501_event':
        data = pd.DataFrame(list(Ladot501WEvent501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'Dan601_event':
        data = pd.DataFrame(list(Ladot601WEvent601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    elif table == 'ultra':
        data = pd.DataFrame(list(DanzUltraRaw.objects.using('wjeanalytics').filter(timestamp__range=[from_date, to_date],sensorname__exact=gage).order_by('timestamp').values('timestamp','sensordata'))).dropna()
        print(data)
        data = data.rename(columns = {'timestamp':'tmstamp','sensordata':gage})

    elif table == 'resensys_1H_median':
        print('resensys')
        data = pd.DataFrame(list(Resensys1HMedian.objects.using('wjeanalytics').filter(timestamp__range=[from_date, to_date],sensorname__exact=gage).order_by('timestamp').values('timestamp','sensorvalue'))).dropna()
        
        data = data.rename(columns = {'timestamp':'tmstamp','sensorvalue':gage})

    elif table == 'DanzLifts':      
        data = pd.DataFrame(list(DanzLifts.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
    
    else: 
        data = None

    return data
        

@api_view(['GET',])
def lifts(request):
    # data = pd.DataFrame(list(DanzLifts.objects.using('wjeanalytics').values('timestamp','verified'))).dropna()
    data = DanzLifts.objects.using('wjeanalytics').values('timestamp').order_by('-timestamp')
    context = {
    'lifttime': [i['timestamp'] for i in data],
    }
    #print(context)
    return Response(context)

@api_view(['POST',])
def get_bearings_event(request):
    print('-------------get_bearings_event-------------')
    data = request.data

    date = data['dateRange']
    # print(type(json.loads(date)))
    # print(f'date: {json.loads(date)}')
    date = date
    from_date = date[0]
    print(f'fromdate: {from_date}')
    to_date = date[1]
    print(f'todate: {to_date}')
    limits =  pd.DataFrame.from_dict(limits_dict)

    # data_bearings_West = pd.DataFrame(list(DanzBearingWest2.objects.using('wjeanalytics').filter(timestamp__range=[from_date, to_date]).values('timestamp','sensor_0_banda')))
    data_bearings_West = DanzBearingWest2.objects.using('wjeanalytics').filter(timestamp__range=[from_date, to_date]).all()
    df = read_frame(data_bearings_West)
    df = df.set_index('timestamp')
    df = df.drop(['comment','valid'], axis=1)
    # print(df.columns)
    west_limit = limits.loc['west']
    for col in df.columns:
        # print(f'col: {col}')
        # print(df)
        # print(west_limit)
        # print(f'value: {df[{col}]}')
        # print(f'west_l: {west_limit[{col}]}')
        df[col] = 100 * df[col] / west_limit[col]
    df['maximum'] = df.max(axis=1)
    df = df.reset_index()
    
    print(df)
    
    context = {
        
    }
    #print(context)
    return Response(df.to_json())

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
def skew(request):
    print('--------main skew----------')
    data = request.data
    gagelist= data['gagelist']['set_one']
    title = data['gagelist'].get('title')
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]

    min_y = -1
    max_y = 1
    min_y2 = -1
    max_y2 = 1

    if (data.get('config') is not None):
        y_axes_label = data['config'].get('y_axes_label')
        y_axes_range = data['config'].get('y_axes_range')

    else:
        y_axes_label ='default'

    min_y = -.001
    max_y = .001
    min_y2 = -.001
    max_y2 = .001


    if (data.get('config') is not None):
        if (data['config'].get('longskew') is not None):
            longskew = data['config'].get('longskew')

    print(f'longskew: {longskew}\n')
    # Check to see if we need standard skew or the long skew
    if longskew == True:
        print('head to longskew function')
        traces,min_y,max_y= get_longskew_data(gagelist,from_date,to_date,min_y,max_y)
    else:

        print('head to skew function')
        traces,min_y,max_y= get_skew_data(gagelist,from_date,to_date,min_y,max_y,0)
        traces2,min_y,max_y= get_skew_data(gagelist,from_date,to_date,min_y,max_y,1)
        traces = traces + traces2


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
def gage(request):
    # Function to pull standard time history data from Danziger logger data tables
    #
    data = request.data   #JSONParser().parse(request)
    # print(f'data: {data}')

    gagelist= data['gagelist']['primary']
    gagelist2= data['gagelist'].get('secondary')
    title = data['gagelist'].get('title')
    
    date_range = data['dateRange']['dateRange']
    from_date = date_range[0]
    to_date = date_range[1]

    if (data.get('config') is not None):
        y_axis_label = data['config'].get('y_axis_label')

    min_y = -1
    max_y = 1
    min_y2 = -1
    max_y2 = 1


    traces,min_y,max_y= get_gage_data(gagelist,from_date,to_date,min_y,max_y,secondary=False)

    # Determine if there are plots to be shown on secondary axis
    if gagelist2 is not None:
        traces2,min_y2,max_y2= get_gage_data(gagelist2,from_date,to_date,min_y2,max_y2,secondary=True)
        traces = traces +traces2

    # Determine if there is a predefined range
    if (data.get('config') is not None):
        if (data['config'].get('y_axes_range') is not None):
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
        gage = gage_id.get('gage')
        print(gage)
        table = gage_id.get('table')
        threshold = gage_id.get('threshold')
        smooth = gage_id.get('smooth')

        data = get_dataframe(gage,table,from_date, to_date)

        # if table == 'Dan502':
        #     data = pd.DataFrame(list(Ladotd502EMonitor502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan602':
        #     data = pd.DataFrame(list(Ladot602EMonitor602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan501':
        #     data = pd.DataFrame(list(Ladot501WMonitor501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan601':
        #     data = pd.DataFrame(list(Ladot601WMonitor601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan502_event':
        #     data = pd.DataFrame(list(Ladotd502EEvent502.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan602_event':
        #     data = pd.DataFrame(list(Ladot602EEvent602.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan501_event':
        #     data = pd.DataFrame(list(Ladot501WEvent501.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'Dan601_event':
        #     data = pd.DataFrame(list(Ladot601WEvent601.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        # elif table == 'DanzLifts':      
        #     data = pd.DataFrame(list(DanzLifts.objects.using('lndb').filter(tmstamp__range=[from_date, to_date]).values('tmstamp',gage))).dropna()
        
        # else: 
        #     data = None

        if data.size<2:#data.count() <2:
            pass
                
        # tare = gage_id.get('tare')
        # scalar = gage_id.get('scalar')

        # if threshold:
        #     data = data[data[gage] > threshold[0]]
        #     data = data[data[gage] < threshold[1]]
        # if tare is None:
        #     tare = 0.0
        # if scalar is None:
        #     scalar =1.0
        #     # print(f'tare: {tare}')
        # y= data[gage]*float(scalar)-float(tare)

        # min_y, max_y = get_min_max_y(y, min_y, max_y)
        # y = (y).values.tolist()
        # x = data['tmstamp'].dt.to_pydatetime().tolist()
        
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
            data = data.rolling(smooth).median()
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

def get_skew_data(gagelist,from_date,to_date,min_y,max_y,index):
    print('-------------skew funtion----------')
    traces =[]

    print(gagelist)
    gage_one = gagelist[index].get('gage_one')
    # print(f'gage_one: {gage_one}')
    gage_two = gagelist[index].get('gage_two')
    # print(f'gage_two: {gage_two}')
    table_one = gagelist[index].get('table_one')
    table_two = gagelist[index].get('table_two')
    # print(f'gage_two: {gage_two}')
    
    data_one = get_dataframe(gage_one,table_one,from_date, to_date)
    
    data_two = get_dataframe(gage_two,table_two,from_date, to_date)
    
    data_one = data_one.set_index('tmstamp')
    data_two = data_two.set_index('tmstamp')
    
    data_one = data_one.resample('2S').mean()
    data_two = data_two.resample('2S').mean()
    
    skew =data_two.subtract(data_one[gage_one], axis='rows')

    skew = skew.reset_index()
    skew = skew.dropna()
    print('inside skew')
    print(skew)
    y= skew[gage_two]

    min_y, max_y = get_min_max_y(y, min_y, max_y)
    y = (y).values.tolist()

    x = skew['tmstamp'].dt.to_pydatetime().tolist()
    

    line= {
    "color": colors[index]#"rgba(55, 128, 191, 1.0)","width": 1
    },
    yaxis= 'y'

    traces += {
        "uid": index,
        "mode": "line",
        "name": gagelist[index].get('name'),
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

def get_longskew_data(gagelist,from_date,to_date,min_y,max_y):
    print('-------------longskew funtion----------')
    traces =[]

    #One side
    gage_one = gagelist[0].get('gage_one')
    gage_two = gagelist[0].get('gage_two')

    table_one = gagelist[0].get('table_one')
    table_two = gagelist[0].get('table_two')

    
    data_one = get_dataframe(gage_one,table_one,from_date, to_date)
    data_two = get_dataframe(gage_two,table_two,from_date, to_date)

    
    data_one = data_one.set_index('tmstamp')
    data_two = data_two.set_index('tmstamp')
    
    data_one = data_one.resample('2S').mean()
    data_two = data_two.resample('2S').mean()

    print(f'data1: {data_one}')
    data_east = (data_one[gage_one] + data_two[gage_two]) /2

    gage_three = gagelist[1].get('gage_one')
    gage_four = gagelist[1].get('gage_two')

    table_one = gagelist[1].get('table_one')
    table_two = gagelist[1].get('table_two')

    
    data_three = get_dataframe(gage_three,table_one,from_date, to_date)
    data_four = get_dataframe(gage_four,table_two,from_date, to_date)

    
    data_three = data_three.set_index('tmstamp')
    data_four = data_four.set_index('tmstamp')
    
    data_three = data_three.resample('2S').mean()
    data_four = data_four.resample('2S').mean()
    
    data_west = (data_three[gage_three] + data_four[gage_four]) /2

    #skew =data_east - data_west
    skew = data_east.subtract(data_west, axis='rows')
    print('inside dataeast')


    skew = skew.reset_index()
    skew = skew.dropna()

    min_y, max_y = get_min_max_y(skew[0].values, min_y, max_y)
    y = skew[0].values.tolist()

    x = skew['tmstamp'].dt.to_pydatetime().tolist()
 
    line= {
    "color": colors[0]#"rgba(55, 128, 191, 1.0)","width": 1
    },
    yaxis= 'y'

    traces += {
        "uid": 0,
        "mode": "line",
        "name": "Long. Skew",
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


@api_view(['POST'])
def gage_old(request):
    import json
    print('1----------------------------------')
  
    data = request.data   #JSONParser().parse(request)
    #print(f'data: {data}')

 
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
        print(f'datatype: ${type(data)}')

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
