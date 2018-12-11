#! /usr/bin/python3.6

from .catiaapplication import CATIAApplication
from .document import Document
from .general_functions import create_measurable
from .measurable import CATIAMeasurable
from .part import Part
from .product import Product
from .reference import create_reference
from .workbenches import create_spa_workbench


__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to access the CATIA Measurable object.'
__name__ = "pycatia"
__version__ = "0.0.2"
__url__ = "https://github.com/evereux/pycatia"

name = __name__
