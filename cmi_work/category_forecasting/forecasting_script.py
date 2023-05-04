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


(
                y_fcst,
                p_value_ols,
                r_squared_ols,
                rmse_ols,
                mape_ols,
            ) = simple_linear_regression_forecast(df_act, df_fcst, index_var, price_var)