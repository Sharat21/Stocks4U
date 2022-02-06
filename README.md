# Stocks4U
A quick and easy way to access the stock market, and learn what investments to make

Created by Sharat Krishnan, Aditya Kumar, Jay Patel
___________________________________________________________________________________________
## Inspiration
As we come out of the coronavirus pandemic and our lives begin to return to normal, the economy is going to be bouncing back. We wanted to help small businesses and people take advantage of the rebounding economy and grow their stock portfolio. Many small businesses are not even on the stock market and they might want to go public during this time to raise their capital. We wanted to not only take advantage of the restoring economy but also help people and small businesses restore their financial wellbeing and make smart investments.

## What it does
Stocks4U is an innovative new application that allows the user to search any stock and a period of time and we return a graphical representation of the stock prices along with trendlines. The user is able to enter any period of time and any stock on various international indexes, from the New York Stock Exchange to the Toronto Stock Exchange. Then, we allow the user to choose from 6 different trend lines - Linear Fit, LOWESS (Locally Weighted Scatterplot Smoothing), Rolling Average, Polynomial, EWM (Exponentially Weighted Moving Average), and Expanding Mean. 

We also include the unique feature of extrapolation which allows the user to extend the trendline and see how it moves in the future. For example, after 40 days from the actual end date, we can extrapolate the 40 days to get a potential trend of where the stocks would go.

## How we built it
We are able to retrieve all the stock data from a Yahoo Finance library which returns the data in the form of a DataFrame object from the pandas library. We then manipulate this DataFrame object so that we are able to plot it as a scatterplot using the Plotly library. We then use the trendline features of the Plotly library to plot the trendline of the user's choice. For the extrapolation, we use the numpy library and its arrays to plot further points on the trendline which we then plot onto the graph.

## Challenges we ran into
We faced many learning curves in making this project as all the libraries and algorithms that we implement were new to us. We learned how to use several different libraries, from the Plotly to numpy. We also had to learn about many of statistical concepts in order to implement the trendlines. Implementing the extrapolation was an especially new and challenging concept for us. Time management was also another challenge, since we had to balance our work and project time since we had about 24 hours to work. 

A big challenge we faced was manipulating the stock data, which came as a DataFrame object, so that we could plot it as a scatter plot and also implement trendlines. The big problem with the data was that each data point(stock price) was associated with a date rather than a number. This was an issue because a trendline could not be generated with x axis in dates. After several hours of debugging, we were able to develop a work around this problem by creating a set of points of the trendline and graphing it separately.

## Accomplishments that we're proud of
We are also proud that we were able to overcome every obstacle and bug we encountered and come out on top by creating a full project. 

## What we learned
This was a great learning experience for us as we learned several aspects of statistical programming which will be extremely useful for future projects. We learned how to work with different libraries, read different documentations, and gain a lot of expertise in dealing with the Plotly library and graphing.

## What's next for T.I.D.E Tech: Stocks4U
The next steps for Stocks4U is to implement a whole user interface, to allow the user to have a more simple and immersive  experience when working with Stocks4U. The UI would just be a simple application which allows the users to choose their stock, the dates, the type of trend, and if they would like to extrapolate to a certain date or not. We would also like to turn this into a web application to make it more accessible  to people, so that way many small business owners can easily access Stocks4U and join in on the investments. We also hope to add a feature, where users can see hot trends or the trending stocks at that time to allow businesses to save time and just quickly invest in the trending stocks.

