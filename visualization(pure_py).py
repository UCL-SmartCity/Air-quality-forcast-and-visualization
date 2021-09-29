# -*- encoding:utf-8 -*-

import pandas as pd
import plotly.express as px


def viz(FilePath_monitoring):
    dataMap = pd.read_csv(FilePath_monitoring).iloc[:, 1:]
    # Apply token from the official website: https://www.mapbox.com/studio
    token = 'pk.eyJ1IjoibGFiaW5nanVuIiwiYSI6ImNrc3JuaW1xMzBvdncyb2xtZWk3Ym93ajgifQ.LjSxb0FvmRsSS9_cxoy8mw'

    fig = px.scatter_mapbox(dataMap,
                            lon='longitude',
                            lat='latitude',
                            color="sitecode",  # use different colors for each site
                            hover_data=['CO',
                                        'NO2',
                                        'SO2',
                                        'O3',
                                        'PM10',
                                        'PM25'],
                            size_max=16,
                            color_continuous_scale=px.colors.carto.Temps
                            )

    fig.update_layout(mapbox={'accesstoken': token,
                              "center": {'lon': -0.11, 'lat': 51.5},  # assigned map center
                              'zoom': 9.48,
                              'style': 'light',
                              },
                      margin={'l': 0, 'r': 0, 't': 0, 'b': 0})
    fig.show()


FilePath_monitoring = 'data/monitoring.csv'
viz(FilePath_monitoring)
