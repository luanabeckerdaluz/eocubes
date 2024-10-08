"""
API - EO Data Cube.

Python Client Library for Earth Observation Data Cubes.
This abstraction uses STAC.py library provided by BDC Project.

=======================================
begin                : 2021-05-01
git sha              : $Format:%H$
copyright            : (C) 2020 by none
email                : none@inpe.br
=======================================

This program is free software.
You can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Get information from STAC Service saved on config file.

Methods:

    collections, describe
"""

import pystac_client

from eocube import config


def collections():
    """List all available collections from STAC."""
    parameters = dict(access_token=config.ACCESS_TOKEN)
    stac_client = pystac_client.Client.open(
            config.STAC_URL,
            parameters= parameters
        )
    for collection in stac_client.get_collections():
        print(collection)
    return stac_client

def describe(collection):
    """Describe a given collection from STAC service.

    Parameters

     - collection <string, required>: the name of collection of interest listed in STAC.collections.
    """
    parameters = dict(access_token=config.ACCESS_TOKEN)
    stac_client = pystac_client.Client.open(
            config.STAC_URL,
            parameters= parameters
        )
    return stac_client.collections[collection]
