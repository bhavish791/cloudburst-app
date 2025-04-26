{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "dcf91b6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5bd8bc40",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"weatherHistory.csv\",usecols = [2,3,4,5,6,7,8,10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "0be853e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precip Type</th>\n",
       "      <th>Temperature (C)</th>\n",
       "      <th>Apparent Temperature (C)</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind Speed (km/h)</th>\n",
       "      <th>Wind Bearing (degrees)</th>\n",
       "      <th>Visibility (km)</th>\n",
       "      <th>Pressure (millibars)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>55794</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>2.777778</td>\n",
       "      <td>0.105556</td>\n",
       "      <td>0.89</td>\n",
       "      <td>9.6600</td>\n",
       "      <td>180</td>\n",
       "      <td>9.9820</td>\n",
       "      <td>1018.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24045</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>10.061111</td>\n",
       "      <td>10.061111</td>\n",
       "      <td>0.92</td>\n",
       "      <td>6.2146</td>\n",
       "      <td>33</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>1021.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29781</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>0.555556</td>\n",
       "      <td>-2.944444</td>\n",
       "      <td>0.82</td>\n",
       "      <td>11.2700</td>\n",
       "      <td>10</td>\n",
       "      <td>16.1000</td>\n",
       "      <td>1019.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45814</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>3.161111</td>\n",
       "      <td>1.583333</td>\n",
       "      <td>0.93</td>\n",
       "      <td>6.1180</td>\n",
       "      <td>142</td>\n",
       "      <td>3.5420</td>\n",
       "      <td>1030.17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>62542</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>18.772222</td>\n",
       "      <td>18.772222</td>\n",
       "      <td>0.97</td>\n",
       "      <td>3.2200</td>\n",
       "      <td>330</td>\n",
       "      <td>15.7297</td>\n",
       "      <td>1010.91</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Precip Type  Temperature (C)  Apparent Temperature (C)  Humidity  \\\n",
       "55794  CloudBurst         2.777778                  0.105556      0.89   \n",
       "24045  CloudBurst        10.061111                 10.061111      0.92   \n",
       "29781  CloudBurst         0.555556                 -2.944444      0.82   \n",
       "45814  CloudBurst         3.161111                  1.583333      0.93   \n",
       "62542  CloudBurst        18.772222                 18.772222      0.97   \n",
       "\n",
       "       Wind Speed (km/h)  Wind Bearing (degrees)  Visibility (km)  \\\n",
       "55794             9.6600                     180           9.9820   \n",
       "24045             6.2146                      33           8.0500   \n",
       "29781            11.2700                      10          16.1000   \n",
       "45814             6.1180                     142           3.5420   \n",
       "62542             3.2200                     330          15.7297   \n",
       "\n",
       "       Pressure (millibars)  \n",
       "55794               1018.60  \n",
       "24045               1021.87  \n",
       "29781               1019.90  \n",
       "45814               1030.17  \n",
       "62542               1010.91  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d5a75e6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precip Type</th>\n",
       "      <th>Temperature (C)</th>\n",
       "      <th>Apparent Temperature (C)</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind Speed (km/h)</th>\n",
       "      <th>Wind Bearing (degrees)</th>\n",
       "      <th>Visibility (km)</th>\n",
       "      <th>Pressure (millibars)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>9.472222</td>\n",
       "      <td>7.388889</td>\n",
       "      <td>0.89</td>\n",
       "      <td>14.1197</td>\n",
       "      <td>251</td>\n",
       "      <td>15.8263</td>\n",
       "      <td>1015.13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>9.355556</td>\n",
       "      <td>7.227778</td>\n",
       "      <td>0.86</td>\n",
       "      <td>14.2646</td>\n",
       "      <td>259</td>\n",
       "      <td>15.8263</td>\n",
       "      <td>1015.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>9.377778</td>\n",
       "      <td>9.377778</td>\n",
       "      <td>0.89</td>\n",
       "      <td>3.9284</td>\n",
       "      <td>204</td>\n",
       "      <td>14.9569</td>\n",
       "      <td>1015.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>8.288889</td>\n",
       "      <td>5.944444</td>\n",
       "      <td>0.83</td>\n",
       "      <td>14.1036</td>\n",
       "      <td>269</td>\n",
       "      <td>15.8263</td>\n",
       "      <td>1016.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>8.755556</td>\n",
       "      <td>6.977778</td>\n",
       "      <td>0.83</td>\n",
       "      <td>11.0446</td>\n",
       "      <td>259</td>\n",
       "      <td>15.8263</td>\n",
       "      <td>1016.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96448</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>26.016667</td>\n",
       "      <td>26.016667</td>\n",
       "      <td>0.43</td>\n",
       "      <td>10.9963</td>\n",
       "      <td>31</td>\n",
       "      <td>16.1000</td>\n",
       "      <td>1014.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96449</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>24.583333</td>\n",
       "      <td>24.583333</td>\n",
       "      <td>0.48</td>\n",
       "      <td>10.0947</td>\n",
       "      <td>20</td>\n",
       "      <td>15.5526</td>\n",
       "      <td>1015.16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96450</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>22.038889</td>\n",
       "      <td>22.038889</td>\n",
       "      <td>0.56</td>\n",
       "      <td>8.9838</td>\n",
       "      <td>30</td>\n",
       "      <td>16.1000</td>\n",
       "      <td>1015.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96451</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>21.522222</td>\n",
       "      <td>21.522222</td>\n",
       "      <td>0.60</td>\n",
       "      <td>10.5294</td>\n",
       "      <td>20</td>\n",
       "      <td>16.1000</td>\n",
       "      <td>1015.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96452</th>\n",
       "      <td>CloudBurst</td>\n",
       "      <td>20.438889</td>\n",
       "      <td>20.438889</td>\n",
       "      <td>0.61</td>\n",
       "      <td>5.8765</td>\n",
       "      <td>39</td>\n",
       "      <td>15.5204</td>\n",
       "      <td>1016.16</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>85224 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Precip Type  Temperature (C)  Apparent Temperature (C)  Humidity  \\\n",
       "0      CloudBurst         9.472222                  7.388889      0.89   \n",
       "1      CloudBurst         9.355556                  7.227778      0.86   \n",
       "2      CloudBurst         9.377778                  9.377778      0.89   \n",
       "3      CloudBurst         8.288889                  5.944444      0.83   \n",
       "4      CloudBurst         8.755556                  6.977778      0.83   \n",
       "...           ...              ...                       ...       ...   \n",
       "96448  CloudBurst        26.016667                 26.016667      0.43   \n",
       "96449  CloudBurst        24.583333                 24.583333      0.48   \n",
       "96450  CloudBurst        22.038889                 22.038889      0.56   \n",
       "96451  CloudBurst        21.522222                 21.522222      0.60   \n",
       "96452  CloudBurst        20.438889                 20.438889      0.61   \n",
       "\n",
       "       Wind Speed (km/h)  Wind Bearing (degrees)  Visibility (km)  \\\n",
       "0                14.1197                     251          15.8263   \n",
       "1                14.2646                     259          15.8263   \n",
       "2                 3.9284                     204          14.9569   \n",
       "3                14.1036                     269          15.8263   \n",
       "4                11.0446                     259          15.8263   \n",
       "...                  ...                     ...              ...   \n",
       "96448            10.9963                      31          16.1000   \n",
       "96449            10.0947                      20          15.5526   \n",
       "96450             8.9838                      30          16.1000   \n",
       "96451            10.5294                      20          16.1000   \n",
       "96452             5.8765                      39          15.5204   \n",
       "\n",
       "       Pressure (millibars)  \n",
       "0                   1015.13  \n",
       "1                   1015.63  \n",
       "2                   1015.94  \n",
       "3                   1016.41  \n",
       "4                   1016.51  \n",
       "...                     ...  \n",
       "96448               1014.36  \n",
       "96449               1015.16  \n",
       "96450               1015.66  \n",
       "96451               1015.95  \n",
       "96452               1016.16  \n",
       "\n",
       "[85224 rows x 8 columns]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df[\"Precip Type\"] ==\"CloudBurst\"] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4ea23f3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precip Type</th>\n",
       "      <th>Temperature (C)</th>\n",
       "      <th>Apparent Temperature (C)</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind Speed (km/h)</th>\n",
       "      <th>Wind Bearing (degrees)</th>\n",
       "      <th>Visibility (km)</th>\n",
       "      <th>Pressure (millibars)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1562</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.483333</td>\n",
       "      <td>-4.150000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>11.0929</td>\n",
       "      <td>219</td>\n",
       "      <td>0.4830</td>\n",
       "      <td>1031.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1563</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.483333</td>\n",
       "      <td>-4.061111</td>\n",
       "      <td>0.96</td>\n",
       "      <td>10.7387</td>\n",
       "      <td>200</td>\n",
       "      <td>0.3220</td>\n",
       "      <td>1031.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1564</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.922222</td>\n",
       "      <td>-3.477778</td>\n",
       "      <td>1.00</td>\n",
       "      <td>7.0679</td>\n",
       "      <td>206</td>\n",
       "      <td>0.1610</td>\n",
       "      <td>1031.23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1565</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-1.038889</td>\n",
       "      <td>-4.400000</td>\n",
       "      <td>1.00</td>\n",
       "      <td>9.4990</td>\n",
       "      <td>199</td>\n",
       "      <td>0.1610</td>\n",
       "      <td>1031.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1566</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-1.088889</td>\n",
       "      <td>-4.438889</td>\n",
       "      <td>1.00</td>\n",
       "      <td>9.4346</td>\n",
       "      <td>219</td>\n",
       "      <td>0.3220</td>\n",
       "      <td>1031.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93265</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.783333</td>\n",
       "      <td>-2.950000</td>\n",
       "      <td>0.99</td>\n",
       "      <td>6.1019</td>\n",
       "      <td>91</td>\n",
       "      <td>3.1073</td>\n",
       "      <td>1016.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93266</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-1.111111</td>\n",
       "      <td>-1.111111</td>\n",
       "      <td>0.93</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.1610</td>\n",
       "      <td>1016.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93267</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-1.044444</td>\n",
       "      <td>-1.044444</td>\n",
       "      <td>1.00</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.7728</td>\n",
       "      <td>1016.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93311</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.511111</td>\n",
       "      <td>-0.511111</td>\n",
       "      <td>1.00</td>\n",
       "      <td>3.5098</td>\n",
       "      <td>74</td>\n",
       "      <td>14.6832</td>\n",
       "      <td>1004.57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93506</th>\n",
       "      <td>No CloudBurst</td>\n",
       "      <td>-0.027778</td>\n",
       "      <td>-2.705556</td>\n",
       "      <td>0.99</td>\n",
       "      <td>7.8568</td>\n",
       "      <td>320</td>\n",
       "      <td>3.0107</td>\n",
       "      <td>1014.76</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10712 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Precip Type  Temperature (C)  Apparent Temperature (C)  Humidity  \\\n",
       "1562   No CloudBurst        -0.483333                 -4.150000      1.00   \n",
       "1563   No CloudBurst        -0.483333                 -4.061111      0.96   \n",
       "1564   No CloudBurst        -0.922222                 -3.477778      1.00   \n",
       "1565   No CloudBurst        -1.038889                 -4.400000      1.00   \n",
       "1566   No CloudBurst        -1.088889                 -4.438889      1.00   \n",
       "...              ...              ...                       ...       ...   \n",
       "93265  No CloudBurst        -0.783333                 -2.950000      0.99   \n",
       "93266  No CloudBurst        -1.111111                 -1.111111      0.93   \n",
       "93267  No CloudBurst        -1.044444                 -1.044444      1.00   \n",
       "93311  No CloudBurst        -0.511111                 -0.511111      1.00   \n",
       "93506  No CloudBurst        -0.027778                 -2.705556      0.99   \n",
       "\n",
       "       Wind Speed (km/h)  Wind Bearing (degrees)  Visibility (km)  \\\n",
       "1562             11.0929                     219           0.4830   \n",
       "1563             10.7387                     200           0.3220   \n",
       "1564              7.0679                     206           0.1610   \n",
       "1565              9.4990                     199           0.1610   \n",
       "1566              9.4346                     219           0.3220   \n",
       "...                  ...                     ...              ...   \n",
       "93265             6.1019                      91           3.1073   \n",
       "93266             0.0000                       0           0.1610   \n",
       "93267             0.0000                       0           0.7728   \n",
       "93311             3.5098                      74          14.6832   \n",
       "93506             7.8568                     320           3.0107   \n",
       "\n",
       "       Pressure (millibars)  \n",
       "1562                1031.56  \n",
       "1563                1031.47  \n",
       "1564                1031.23  \n",
       "1565                1031.41  \n",
       "1566                1031.98  \n",
       "...                     ...  \n",
       "93265               1016.30  \n",
       "93266               1016.41  \n",
       "93267               1016.60  \n",
       "93311               1004.57  \n",
       "93506               1014.76  \n",
       "\n",
       "[10712 rows x 8 columns]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df[\"Precip Type\"] ==\"No CloudBurst\"] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "238704c9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22104b13",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dea7195d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "4e7b50e9",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pressure (millibars)', ylabel='Density'>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x864 with 8 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig,axs = plt.subplots(4,2,figsize=(12,12))\n",
    "sns.kdeplot(x=df[\"Temperature (C)\"],ax =axs[0,0])\n",
    "sns.kdeplot(x=df[\"Apparent Temperature (C)\"],ax =axs[0,1])\n",
    "sns.kdeplot(x=df[\"Humidity\"],ax =axs[1,0])\n",
    "sns.kdeplot(x=df[\"Wind Speed (km/h)\"],ax =axs[1,1])\n",
    "sns.kdeplot(x=df[\"Wind Bearing (degrees)\"],ax =axs[2,0])\n",
    "sns.kdeplot(x=df[\"Visibility (km)\"],ax =axs[2,1])\n",
    "sns.kdeplot(x=df[\"Pressure (millibars)\"],ax =axs[3,1])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f113db2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Precip Type                 517\n",
       "Temperature (C)               0\n",
       "Apparent Temperature (C)      0\n",
       "Humidity                      0\n",
       "Wind Speed (km/h)             0\n",
       "Wind Bearing (degrees)        0\n",
       "Visibility (km)               0\n",
       "Pressure (millibars)          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Precip Type\"].value_counts()\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "dd6754d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Precip Type'].fillna('CloudBurst', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "0ece7612",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Precip Type                 0\n",
       "Temperature (C)             0\n",
       "Apparent Temperature (C)    0\n",
       "Humidity                    0\n",
       "Wind Speed (km/h)           0\n",
       "Wind Bearing (degrees)      0\n",
       "Visibility (km)             0\n",
       "Pressure (millibars)        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23ee6936",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de0939b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "3dd71821",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "le = LabelEncoder()\n",
    "df[\"Precip Type\"] = le.fit_transform(df[\"Precip Type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "2649fdd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    85741\n",
       "1    10712\n",
       "Name: Precip Type, dtype: int64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Precip Type\"].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "a761bba9",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df[[\"Temperature (C)\",\"Apparent Temperature (C)\",\"Humidity\",\"Wind Speed (km/h)\",\"Wind Bearing (degrees)\",\"Visibility (km)\",\"Pressure (millibars)\"]]\n",
    "y = df[[\"Precip Type\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "ced778cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "8ea460df",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "7e4fc0ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB\n",
    "from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "4c0c4299",
   "metadata": {},
   "outputs": [],
   "source": [
    "gnb = GaussianNB()\n",
    "mnb = MultinomialNB()\n",
    "bnb = BernoulliNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "f0ec001e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.940645897050438\n",
      "[[16035  1066]\n",
      " [   79  2111]]\n",
      "[0.99509743 0.66446333]\n",
      "[0.93766446 0.96392694]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Admin\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:1143: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "gnb.fit(x_train,y_train)\n",
    "y_pred = gnb.predict(x_test)\n",
    "print(accuracy_score(y_test,y_pred))\n",
    "print(confusion_matrix(y_test,y_pred))\n",
    "print(precision_score(y_test,y_pred,average = None))\n",
    "print(recall_score(y_test,y_pred,average= None))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "52ae9797",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n",
      "[[17101     0]\n",
      " [    0  2190]]\n",
      "[1. 1.]\n",
      "[1. 1.]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Admin\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:1143: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "bnb.fit(x_train,y_train)\n",
    "y_pred = bnb.predict(x_test)\n",
    "print(accuracy_score(y_test,y_pred))\n",
    "print(confusion_matrix(y_test,y_pred))\n",
    "print(precision_score(y_test,y_pred,average = None))\n",
    "print(recall_score(y_test,y_pred,average= None))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "9d0ba9cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Admin\\anaconda3\\lib\\site-packages\\sklearn\\base.py:439: UserWarning: X does not have valid feature names, but BernoulliNB was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([1])"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "h = [[-2.866667,-7.027778,0.93,11.1251,180,1.1109,1034.23]]\n",
    "bnb.predict(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "86e081b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle \n",
    "pickle.dump(bnb,open(\"cbmodel.pkl\",\"wb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e815959",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bd90dad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
