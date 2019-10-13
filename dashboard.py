import pandas as pd
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash
data=pd.read_csv('gapminder.csv')

print(data.head())

app=dash.Dash()
server=app.server


app.layout=html.Div([
    html.H1(children="MY DASHBOARD",style={'color':'red','text-align':'center'}),
    html.Div(children=[
        dcc.Graph(id='scatter-plot',
                  figure={'data':[go.Scatter(x=data['pop'],
                                             y=data['gdpPercap'],
                                             mode='markers')],
                          'layout':go.Layout(title='Scatter-plot')})
    ],
             style={'border':'1px black solid','float':'left','width':'49%'}),
    html.Div(children=[
        dcc.Graph(id='box-plot',
                  figure={'data':[go.Box(x=data['gdpPercap'])],
                          'layout':go.Layout(title='Box-plot')})
    ],
             style={'border':'1px black solid','float':'left','width':'49%'}),
    html.Div(style={'border':'1px black solid','float':'left','width':'98%'})
])



if __name__=="__main__":
    app.run_server()