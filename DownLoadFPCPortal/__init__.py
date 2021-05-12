import logging
from arcgis.gis import GIS
from arcgis.features import GeoAccessor, GeoSeriesAccessor, FeatureLayer

import sys, os

import pandas as pd
import datetime as dt
from arcgis.features import FeatureLayerCollection

import json
import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    test = os.environ["tester"]#Password retrieved from key vault integrated in the function
    gis = GIS("https://portal.arcgis.com", "UserName", test)
    item=gis.content.get('Feature ID')
    p=item.name
    l=item.layers[0]
    d=pd.Timestamp("today").strftime("%Y%m%d") 

    kl=l.query().sdf.head(3)
    df=kl.to_csv(index=False)

    a = {'activity': f"{p}_{d}"}

    

    outputblob.set(df)

    return json.dumps(a)

    