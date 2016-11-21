#!/usr/bin/env python
"""
.. codeauthor:: Eric Hutton <huttone@colorado.edu>

.. sectionauthor:: Eric Hutton <huttone@colorado.edu>
"""
__version__ = '0.1'

from .flexure import Flexure
from .funcs import (get_flexure_parameter, subside_point_load,
                    subside_point_loads)

__all__ = ['Flexure', 'get_flexure_parameter', 'subside_point_load',
           'subside_point_loads']
