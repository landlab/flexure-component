import sys
import argparse

import numpy as np

from landlab import RasterModelGrid, load_params
from flexure import Flexure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('loads', type=argparse.FileType('r'),
                        help='loading file')
    parser.add_argument('--params', type=argparse.FileType('r'),
                        help='parameter file')

    args = parser.parse_args()

    loads = np.loadtxt(args.loads)
    params = load_params(args.params)
    spacing = params.pop('spacing', [1., 1.])

    grid = RasterModelGrid(loads.shape, spacing=spacing)
    grid.at_node['lithosphere__overlying_pressure_increment'] = loads

    flexure = Flexure(grid, **params)
    flexure.update()

    dz = grid.at_node['lithosphere_surface__elevation_increment']

    np.savetxt(sys.stdout, dz.reshape(grid.shape))
