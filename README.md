# Hong-Kong-Temperature-Prediction-
In this project, we employed a seasonal ARIMA model to forecast the temperature in Hong Kong.
The temperature data is downloaded from Hong Kong Observatory. The link is http://www.hko.gov.hk/cis/monthlyElement_uc.htm. 
We used the historical data from 1885 Jan to 2017 Dec and forecast temperature of different months of 2018.

By Ljung-Box test, we achieved the best model when the parameters of this seasonal ARIMA is (1,0,0)*(0,1,1,12). 
The p-value of Ljung-Box test is 0.47
