
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:13:38 2021

@author: mlc
"""
import pandas as pd
import geopandas as geopd
from owslib.wfs import WebFeatureService
# a instalação do pyproj no conda tem erro: fazer pip3 install --force-reinstall pyproj para instalar através do pip3
# também tive que instalar: conda install ruamel_yaml
import pyproj
from requests import Request


# test pyproj  # https://stackoverflow.com/questions/55390492/runtimeerror-bno-arguments-in-initialization-list
pyproj.Proj("+init=epsg:3857")

# URL for WFS backend
url = "http://si.icnf.pt/wfs/rnap" # areas protegidas
url = "http://si.icnf.pt/wfs/ifn_2015" # inventário

# See details about this particular WFS
# -------------------------------------

# Initialize
wfs = WebFeatureService(url=url)

# Service provider
print(wfs.identification.title)

# Get WFS version
print(wfs.version)

# Available methods
print([operation.name for operation in wfs.operations])

# Available data layers
print(list(wfs.contents))

# Print all metadata of all layers
for layer, meta in wfs.items():
    print(meta.__dict__)

# Get data from WFS
# -----------------

# Fetch the last available layer (as an example) --> 'vaestoruutu:vaki2017_5km'
layer = list(wfs.contents)[-1]

# Specify the parameters for fetching the data
params = dict(service='WFS', version="1.0.0", request='GetFeature', typeName=layer, outputFormat='json')

# Parse the URL with parameters
q = Request('GET', url, params=params).prepare().url

# Read data from URL
data = geopd.read_file(q)

data.columns


