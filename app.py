import pandas as pd
df = pd.read_csv('https://theweatherpartner.xyz/projects/c102/Miscelanea/ensembles_data.csv')
list_time = list(dict.fromkeys(list((df.Time))))

colors = {'bg':'#94c2ff',
         'elem_bg':'#23a1db',
         'letter':'#ffffff',
         'title':'#4867f0'}
font = {'family':'system-ui'}

import plotly.express as px
import plotly.graph_objs as go

mapbox_access_token = 'pk.eyJ1IjoibWFydGFub2luZXJjaWFsIiwiYSI6ImNrdXdwNXRxczJydWkydnFydWhuZTAybTMifQ.dTpq64f-nPO3L1GLmla9Aw'
px.set_mapbox_access_token(mapbox_access_token)

import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(show_undo_redo=False)

server = app.server
app.title = 'Meteo-Panama'

app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    id='general-title',
                    children= [
                        html.Img(src="https://theweatherpartner.com/wp-content/uploads/2021/01/logo-twp-nw.png",
                                style={
                                    "position":'absolute',
                                    'top':'2%',
                                    'left':'1%',
                                    'width':'90px',
                                    'height':'90px'
                                }
                                ),
                        html.H1("Ensembles"),
                        html.Img(src="https://www.hidromet.com.pa/images/logo_etesa_hidromet.png",
                                style={
                                    "position":'absolute',
                                    'top':'2%',
                                    'right':'1%',
                                    'width':'250px',
                                    'height':'90px'
                                })
                    ],
                    style={'outline-color':colors['bg'],
                           'outline-style':'solid',
                           'display':'inline-block',
                           'width':'98%',
                           'height':'23%',
                           'backgroundColor':colors['title'],
                           'padding':'1%',
                           'outline-width':'5px',
                           'font-family':font['family'],
                           'color':colors['letter'],
                           'text-align':'center'}),
                html.Div(
                    className="two-main-columns",
                    children=[
                        html.Div(id='left-column-precip',
                                 children=[
                                     html.Div(
                                         id='lat-lon-row',
                                         children=[
                                                 html.Div(
                                                        id='title-precip',
                                                        children=[html.H2('Precipitacion Acumulada')],
                                                        style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'width':'98%',
                                                               'height':'23%',
                                                               'backgroundColor':colors['title'],
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),                                             
                                         ],
                                     ),
                                     html.Div(
                                         id='precip-map-row',
                                         children=[
                                             dcc.Graph(id='precip-map',
                                                       figure = {
                                                           'data':[go.Scattermapbox(lat=df[df['Time']==list_time[0]].Latitude,
                                                                lon=df[df['Time']==list_time[-1]].Longitude,
                                                                hoverinfo=["lon", "lat"], opacity=0.8,
                                                                mode = 'markers',
                                                                marker=go.Marker(
                                                                        color =df[df['Time']==list_time[-1]].PrecipitacionAcumulada_e1,
                                                                        colorscale= 'PuBu',
                                                                        opacity=0.7,
                                                                        showscale=False,
                                                                        symbol = 'circle'))],
                                                          'layout':go.Layout(mapbox=dict(accesstoken=mapbox_access_token,
                                                                         center=dict(lat=8.6995,lon=-80.25),
                                                                         zoom = 6),
                                                                             paper_bgcolor=colors['elem_bg'],
                                                                             plot_bgcolor=colors['elem_bg'])
                                      },style={'outline-color':colors['bg'],
                                               'outline-style':'solid',
                                               'display':'inline-block',
                                               'width':'98%',
                                               'height':'78%',
                                               'backgroundColor':colors['elem_bg'],
                                               'padding':'1%',
                                               'outline-width':'5px',
                                              'font-family':font['family'],
                                               'color':colors['letter']})
                                         ],
                                     ),
                                     html.Div(
                                         id='row1-indicador',
                                         children=[
                                             html.Div(
                                                children=[html.Br(),
                                                    html.H5("Selecciona la latitud:"),
                                                    html.Div(dcc.RangeSlider(min=6.9, max=9.7,
                                                                    marks={7:7,8:8,9:9},
                                                                    value=[6.9, 9.7],
                                                                    dots=False,
                                                                    step=0.01,
                                                                    updatemode='drag',
                                                                      id='lat-slider'
                                                                   )),
                                                    html.H5("Selecciona la longitude:"),
                                                    html.Div(dcc.RangeSlider(min=-83.1, max=-77.1,
                                                                    marks={-83:-83,-81:-81,-80:-80,-79:-79,-78:-78},
                                                                    value=[-83.1, 9.7],
                                                                    dots=False,
                                                                    step=0.01,
                                                                    updatemode='drag',
                                                                    id='lon-slider'
                                                                   )),
                                                    html.Br(),
                                                ],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',                                              
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'top': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                             html.Div(
                                                id='precip-e1',
                                                children=[html.Br(),html.Br(),html.Br(),
                                                          html.H4('Ensemble 1:'),
                                                          html.H2('-'),
                                                          html.H4('l/m2'),
                                                          html.Br()],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',                                              
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'top': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                             html.Div(
                                                id='precip-e2',
                                                children=[html.Br(),html.Br(),html.Br(),
                                                          html.H4('Ensemble 2:'),
                                                          html.H2('-'),
                                                          html.H4('l/m2'),
                                                          html.Br()],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',                                              
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'height': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                         ],
                                     ),
                                     html.Div(
                                         id='row2-indicador',
                                         children=[
                                             html.Div(
                                                id='precip-e3',
                                                children=[html.H4('Ensemble 3:'),
                                                          html.H2('-'),
                                                          html.H4('l/m2'),
                                                          html.Br()],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'height': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                             html.Div(
                                                id='precip-e4',
                                                children=[html.H4('Ensemble 4:'),
                                                          html.H2('-'),
                                                          html.H4('l/m2'),
                                                          html.Br()],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',                                              
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'height': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                             html.Div(
                                                id='precip-e5',
                                                children=[html.H4('Ensemble 5:'),
                                                          html.H2('-'),
                                                          html.H4('l/m2'),
                                                          html.Br()],
                                                style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'min-height':'30%',                                              
                                                               'backgroundColor':colors['elem_bg'],
                                                               'width':'31.2%',
                                                               'height': '30%',
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'}),
                                         ],
                                     ),
                                     html.Div(
                                         id='precip-graph',
                                         children = [
                                             dcc.Graph(id='precip-scatter_chart',
                                                  figure= {'layout':go.Layout(title='Precipitacion acumulada',
                                                              xaxis={'title':'Tiempo', 'color':colors['letter']},
                                                              yaxis={'title':'Precipitacion acumulada (l/m2)',
                                                                     'range':[0,df.PrecipitacionAcumulada_e1.max()],
                                                                     'color':colors['letter']},
                                                              paper_bgcolor=colors['elem_bg'],
                                                              plot_bgcolor=colors['elem_bg'], 
                                                              font={'color':colors['letter'], 'family':font['family']},
                                                              )},
                                                 style={'outline-color':colors['bg'],
                                                        'outline-style':'solid',
                                                        'display':'inline-block',
                                                        'width':'98%',
                                                        'height':'48%',
                                                        'backgroundColor':colors['elem_bg'],
                                                        'padding':'1%',
                                                        'outline-width':'5px',
                                                       'font-family':font['family'],
                                                        'color':colors['letter']}),
                                                         ],
                                     ),
                                     
                                 ],
                                style={
                                     'width':'50%',
                                     'display':'inline',
                                    'float':'left'
                                 }
                                ),
                        html.Div(id='right-column',
                                 children=[
                                     html.Div(
                                         children = [
                                                 html.Div(
                                                        id='title-temp',
                                                        children=[html.H2('Temperatura')],
                                                        style={'outline-color':colors['bg'],
                                                               'outline-style':'solid',
                                                               'display':'inline-block',
                                                               'width':'98%',
                                                               'height':'23%',                                                
                                                               'backgroundColor':colors['title'],
                                                               'padding':'1%',
                                                               'outline-width':'5px',
                                                               'font-family':font['family'],
                                                               'color':colors['letter'],
                                                               'text-align':'center'})]),
                                         html.Div(
                                         id='temp-map-row',
                                         children=[
                                             dcc.Graph(id='temp-map',
                                                       figure = {
                                                           'data':[go.Scattermapbox(lat=df[df['Time']==list_time[0]].Latitude,
                                                                lon=df[df['Time']==list_time[-1]].Longitude,
                                                                hoverinfo=["lon", "lat"], opacity=0.8,
                                                                mode = 'markers',
                                                                marker=go.Marker(
                                                                        color =df[df['Time']==list_time[-1]].Temperatura_e1,
                                                                        colorscale= 'Turbo',
                                                                        opacity=0.7,
                                                                        showscale=False,
                                                                        symbol = 'circle'))],
                                                          'layout':go.Layout(mapbox=dict(accesstoken=mapbox_access_token,
                                                                         center=dict(lat=8.6995,lon=-80.25),
                                                                         zoom = 6),
                                                                             paper_bgcolor=colors['elem_bg'],
                                                                             plot_bgcolor=colors['elem_bg'])
                                      },style={'outline-color':colors['bg'],
                                               'outline-style':'solid',
                                               'display':'inline-block',
                                               'width':'98%',
                                               'height':'78%',
                                               'backgroundColor':colors['elem_bg'],
                                               'padding':'1%',
                                               'outline-width':'5px',
                                              'font-family':font['family'],
                                               'color':colors['letter']})
                                         ],
                                     ),
                                     html.Div(
                                         id='temp-graph',
                                         children = [
                                             dcc.Graph(id='temp-scatter_chart',
                                                  figure= {'layout':go.Layout(title='Temperatura en (lon='+', lat='')',
                                                              xaxis={'title':'Tiempo', 'color':colors['letter']},
                                                              yaxis={'title':'Temperatura (ºC)',
                                                                     'range':[10,df.Temperatura_e1.max()],
                                                                     'color':colors['letter']},
                                                              paper_bgcolor=colors['elem_bg'],
                                                              plot_bgcolor=colors['elem_bg'], 
                                                              font={'color':colors['letter'], 'family':font['family']},
                                                              )},
                                                 style={'outline-color':colors['bg'],
                                                        'outline-style':'solid',
                                                        'display':'inline-block',
                                                        'width':'98%',
                                                        'height':'48%',
                                                        'backgroundColor':colors['elem_bg'],
                                                        'padding':'1%',
                                                        'outline-width':'5px',
                                                       'font-family':font['family'],
                                                        'color':colors['letter']}),
                                                         ],
                                     ),
                                 ],
                                 style={
                                     'width':'50%',
                                     'display':'inline',
                                     'float':'left'
                                 }
                                ),
                    ],
                ),
                html.Div(
                    id='title-flow',
                    children=[html.H2('Caudal')],
                    style={'outline-color':colors['bg'],
                           'outline-style':'solid',
                           'display':'inline-block',
                           'height':'23%',
                           'width':'98%',
                           'backgroundColor':colors['title'],
                           'padding':'1%',
                           'outline-width':'5px',
                           'font-family':font['family'],
                           'color':colors['letter'],
                           'text-align':'center'}),
                html.Div(
                    id='timeslide',
                    children= [
                        html.Iframe(src='https://theweatherpartner.xyz/projects/c102/Miscelanea/caudal.html', style={'min-height':'700px','min-width':'100%'})
                    ],
                    style={'outline-color':colors['bg'],
                           'outline-style':'solid',
                           'display':'inline-block',
                           'float':'left', 
                           'width':'98%',
                           'backgroundColor':colors['elem_bg'],
                           'padding':'1%',
                           'outline-width':'5px',
                           'font-family':font['family'],
                           'color':colors['letter'],
                           'text-align':'center'}),
            ],
        )
    ], 
)

@app.callback(
    [Output(component_id='temp-scatter_chart', component_property='figure'),
     Output(component_id='precip-scatter_chart', component_property='figure'),
     Output(component_id='precip-e1', component_property='children'),
     Output(component_id='precip-e2', component_property='children'),
     Output(component_id='precip-e3', component_property='children'),
     Output(component_id='precip-e4', component_property='children'),
     Output(component_id='precip-e5', component_property='children'),
     Output(component_id='precip-map', component_property='figure')
    ],
    [Input(component_id='lat-slider', component_property='value'),
     Input(component_id='lon-slider', component_property='value'),
     Input(component_id='temp-map', component_property='clickData')])

def callback_graph(vlat,vlon,clickData):
    py = vlat
    px = vlon
    tx = clickData['points'][0]['lon']
    ty = clickData['points'][0]['lat']
    dff = df[(df['Longitude']==tx)&(df['Latitude']==ty)]
    
    dfff = df[(df['Longitude']>=px[0])&(df['Latitude']>=py[0])&(df['Longitude']<=px[1])&(df['Latitude']<=py[1])]
    times = list(dict.fromkeys(list((dfff.Time))))
    precip = []
    for i in range(len(times)):
        precip.append([times[i],
                      dfff[dfff['Time']==times[i]].PrecipitacionAcumulada_e1.mean(),
                      dfff[dfff['Time']==times[i]].PrecipitacionAcumulada_e2.mean(),
                      dfff[dfff['Time']==times[i]].PrecipitacionAcumulada_e3.mean(),
                      dfff[dfff['Time']==times[i]].PrecipitacionAcumulada_e4.mean(),
                      dfff[dfff['Time']==times[i]].PrecipitacionAcumulada_e5.mean()])
    data = pd.DataFrame(precip, columns=['Time','e1','e2','e3','e4','e5'])
    
    tfig = {'data':[go.Scatter(x = dff.Time, y = dff.Temperatura_e1, mode = 'lines', name = 'ensemble 1'),
                   go.Scatter(x=dff.Time, y=dff.Temperatura_e2,mode='lines', name = 'ensemble 2'),
                   go.Scatter(x=dff.Time, y=dff.Temperatura_e3,mode='lines', name = 'ensemble 3'),
                   go.Scatter(x=dff.Time, y=dff.Temperatura_e4,mode='lines', name = 'ensemble 4'),
                   go.Scatter(x=dff.Time, y=dff.Temperatura_e5,mode='lines', name = 'ensemble 5')],
            'layout':go.Layout(title='Temperatura en (lon='+str(round(tx,2))+', lat='+str(round(ty,2))+')',
                                 xaxis={'title':'Tiempo', 'color':colors['letter']},
                                 yaxis={'title':'Precipitacion acumulada (l/m2)', 'range':[0,df.Temperatura_e1.max()],
                                        'color':colors['letter']},
                                 paper_bgcolor=colors['elem_bg'],
                                 plot_bgcolor=colors['elem_bg'],
                                 font={'color':colors['letter'], 'family':font['family']},
                                              )}
    pfig = {'data':[go.Scatter(x = data.Time, y = data.e1, mode='lines', name = 'ensemble 1'),
                    go.Scatter(x=data.Time, y=data.e2, mode='lines', name = 'ensemble 2'),
                    go.Scatter(x=data.Time, y=data.e3, mode='lines', name = 'ensemble 3'),
                    go.Scatter(x=data.Time, y=data.e4, mode='lines', name = 'ensemble 4'),
                    go.Scatter(x=data.Time, y=data.e5, mode='lines', name = 'ensemble 5')],
              'layout':go.Layout(title='Precipitacion acumulada',
                                 xaxis={'title':'Tiempo', 'color':colors['letter']},
                                 yaxis={'title':'Precipitacion acumulada (l/m2)', 'range':[0,df.PrecipitacionAcumulada_e1.max()],
                                        'color':colors['letter']},
                                 paper_bgcolor=colors['elem_bg'],
                                 plot_bgcolor=colors['elem_bg'],
                                 font={'color':colors['letter'], 'family':font['family']},
                                              )}
    pe1 = html.Div(id='precip-e1',
                   children=[html.Br(),html.Br(),html.Br(),
                             html.H4('Ensemble 1:'),
                             html.H2(str(round((data[data['Time']==times[35]].e1.mean()-data[data['Time']==times[23]].e1.mean()),3))),
                             html.H4('l/m2'),
                             html.Br()])
    pe2 = html.Div(id='precip-e2',
                   children=[html.Br(),html.Br(),html.Br(),
                             html.H4('Ensemble 2:'),
                             html.H2(str(round((data[data['Time']==times[35]].e2.mean()-data[data['Time']==times[23]].e2.mean()),3))),
                             html.H4('l/m2'),
                             html.Br()])
    pe3 = html.Div(id='precip-e3',
                   children=[html.Br(),
                             html.H4('Ensemble 3:'),
                             html.H2(str(round((data[data['Time']==times[35]].e3.mean()-data[data['Time']==times[23]].e3.mean()),3))),
                             html.H4('l/m2'),
                             html.Br()])
    pe4 = html.Div(id='precip-e4',
                   children=[html.Br(),
                             html.H4('Ensemble 4:'),
                             html.H2(str(round((data[data['Time']==times[35]].e4.mean()-data[data['Time']==times[23]].e4.mean()),3))),
                             html.H4('l/m2'),
                             html.Br()])
    pe5 = html.Div(id='precip-e5',
                   children=[html.Br(),
                             html.H4('Ensemble 5:'),
                             html.H2(str(round((data[data['Time']==times[35]].e5.mean()-data[data['Time']==times[23]].e5.mean()),3))),
                             html.H4('l/m2'),
                             html.Br()])
    
    pmap = {'data':[go.Scattermapbox(lat=dfff[dfff['Time']==list_time[0]].Latitude,
                                     lon=dfff[dfff['Time']==list_time[-1]].Longitude,
                                     hoverinfo=["lon", "lat"], opacity=0.8,
                                     mode = 'markers',
                                     marker=go.Marker(
                                         color =dfff[dfff['Time']==list_time[-1]].PrecipitacionAcumulada_e1,
                                         colorscale= 'PuBu',
                                         opacity=0.7,
                                         showscale=False,
                                         symbol = 'circle'))],
            'layout':go.Layout(mapbox=dict(accesstoken=mapbox_access_token,
                                           center=dict(lat=8.6995,lon=-80.25),
                                           zoom = 6),
                               paper_bgcolor=colors['elem_bg'],
                               plot_bgcolor=colors['elem_bg'])}
    return tfig, pfig, pe1, pe2, pe3, pe4, pe5, pmap

if __name__ == "__main__":
    
    # Display app start
    logger.error('*' * 80)
    logger.error('App initialisation')
    logger.error('*' * 80)

    # Starting flask server
    app.run_server(debug=True)
