import os
import sys
import logging
import time
from datetime import datetime as dt
import random
from random import randint

import yaml
import joblib
import pickle
from itertools import chain, combinations, product
import ast
import math
from math import sqrt

import numpy as np
import pandas as pd
from scipy import stats

import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.x13 import x13_arima_analysis
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.exponential_smoothing.ets import ETSModel
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import cross_validate
from statsmodels.tsa.forecasting.stl import STLForecast
from statsmodels.tsa.forecasting.theta import ThetaModel

from sklearn.preprocessing import FunctionTransformer

# ======================================================================
#Define Liner regresionon function 

def simple_linear_regression_forecast(df_act, df_fcst, x_var, y_var):
    """
    Performs simple linear regression using statsmodels on a given dataframe,
    splits it into train and test sets, and returns the p-value and R-squared
    value for the training set and the RMSE value for the test set.

    fitted model is used to forecast the output for a dataframe having independent variable

    Parameters:
    -----------
    df_act : pandas.DataFrame
        The input dataframe containing the independent and dependent variables.

    df_fcst : pandas.DataFrame
        The  dataframe containing the independent variable and used to forecast the output.


    x_var: name of independent varaiable
    y_var: name of dependent varaiable

    Returns:
    --------
    forecasted output, p-value, R-squared, and RMSE values, respectively.
    """
    # Split the dataframe into train and test sets
    df_train = df_act[:-12]
    df_test = df_act[-12:]

    # define independent and dependent sets
    y_train = df_train[y_var]
    x_train = df_train[x_var]
    x_train = sm.add_constant(x_train)

    y_test = df_test[y_var]
    x_test = df_test[x_var]
    x_test = sm.add_constant(x_test)

    # Fit the linear regression model on the train set
    model_ols = sm.OLS(y_train, x_train).fit()

    # Get regression summary
    summary_ols = model_ols.summary()

    # Extract p-value for independent variable from summary
    p_value_ols = summary_ols.tables[1].data[2][4]

    # Calculate R-squared for train set
    r_squared_ols = model_ols.rsquared

    # Calculate RMSE for test set
    y_test_pred = model_ols.predict(x_test)
    rmse_ols = np.sqrt(mean_squared_error(y_test, y_test_pred))

    # Calculate the MAPE for the test set
    mape_ols = np.mean(np.abs((y_test - y_test_pred) / y_test)) * 100

    # forecast
    y_fcst = model_ols.predict(x_fcst)

   

    return y_fcst, p_value_ols r_squared_ols rmse_ols, mape_ols


(
                y_fcst,
                p_value_ols,
                r_squared_ols,
                rmse_ols,
                mape_ols,
            ) = simple_linear_regression_forecast(df_act, df_fcst, index_var, price_var)