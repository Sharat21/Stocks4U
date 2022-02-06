import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
import pandas as pd
import yfinance as yf

user_name = str(input("Please Enter Stock Ticker Symbol: "))
start_date = str(input("Please Enter start date: "))
end_date = str(input("Please Enter end date: "))
trend_type = str(input("Enter Trend Line Options "
                       "Linear Fit, LOWESS (Locally WEighted Scatterplot Smoothing), "
                       " Rolling Average, EWM (Exponentially Weighted Moving Average), "
                       "Polynomial or Expanding Mean : "))


tik = yf.Ticker(user_name.upper())
data = tik.history(interval="1d", start=start_date, end=end_date)
pd.options.plotting.backend = "plotly"
df = data
a = df.Close
count = 0
lst2 = []
lst = []
lst3 = []


for i in range(len(a)):
    count += 1
    lst.append(a[i])
    lst2.append(i)

if trend_type.title() == 'Rolling Average':
    trend_type = 'rolling'
elif trend_type.upper() == 'LOWESS':
    trend_type = 'lowess'
elif trend_type.upper() == 'EWM':
    trend_type = 'ewm'
elif trend_type.title() == 'Linear Fit':
    trend_type = 'ols'
elif trend_type.title() == 'Expanding Mean':
    trend_type = 'expanding'

df = df.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    df[i] = df[i].astype('float64')
df.insert(0, "index", lst2)
for i in df['Date']:
    dt_object1 = datetime.strptime(str(i), "%Y-%m-%d %H:%M:%S")
    lst3.append(dt_object1)

fig = go.Figure()

if trend_type.title() == 'Polynomial':
    exp = str(input('Would you like to extrapolate (y/n)? '))

    z = np.polyfit(lst2, lst, 3)
    f = np.poly1d(z)
    y_new = f(lst2)
    if exp.lower() == 'y':
        dt = str(input('Please a date (YYYY-MM-DD) you would like to extrapolate to: '))
        date = datetime.strptime(f'{dt} 00:00:00', "%Y-%m-%d %H:%M:%S")
        end_d = datetime.strptime(f'{end_date} 00:00:00', "%Y-%m-%d %H:%M:%S")
        difference = date - end_d
        temp = str(difference).split(' ')

        count += int(temp[0])
        print(temp[0])
        other_x = np.array(count)

        other_y = f(other_x)
        y_new = np.append(y_new, other_y)
        fig = go.Figure()
        a = lst3.copy()
        a.append(date)
        fig.add_trace(
            go.Scatter(x=a, y=y_new,
                       name=str('Trend '),
                       line=dict(width=4, dash='dash')))
    else:
        fig.add_trace(
            go.Scatter(x=df['Date'], y=y_new,
                       name=str('Trend '),
                       line=dict(width=4, dash='dash')))


else:
    if trend_type == 'ewm':
        help_fig = px.scatter(df, x=lst2, y=df['Close'],
                              trendline=trend_type, trendline_options=dict(halflife=2))
    else:
        help_fig = px.scatter(df, x=lst2, y=df['Close'],
                              trendline=trend_type)

    x_trend = help_fig["data"][1]['x']
    y_trend = help_fig["data"][1]['y']

    fig.add_trace(
        go.Scatter(x=df['Date'], y=y_trend,
                   name=str('Trend '),
                   line=dict(width=4, dash='dash')))

fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Close'],
               name=str('Actual Data '),
               line=dict(width=4)))
fig.update_layout(
    title=f"The Stock Market For {user_name.upper()}",
    xaxis_title="Date",
    yaxis_title="Stock Price",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ))

fig.show()
