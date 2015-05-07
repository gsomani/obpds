#
#   Copyright (c) 2015, Scott J Maddox
#
#   This file is part of Open Band Parameters Device Simulator (OBPDS).
#
#   OBPDS is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OBPDS is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with OBPDS.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import logging; logging.basicConfig()

# Make sure we import the local obpds version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from obpds import *

# Layers
p = Layer(0.5*um, Material(GaAs,  1e18/cm3))
n = Layer(1*um, Material(GaAs, -1e16/cm3))

# Device
d = TwoTerminalDevice(layers=[p, n],
                      Fp='left',
                      Fn='right')

# Simulate and show the band profile at 0.5 V reverse bias under the zero
# current approximation.
d.show_zero_current(V=-2)

# Print the capacitance at -0.5 V.
print 'C(V=-0.5) = {} F/cm**2'.format(d.get_capacitance(V=-0.5))

# Show the C-V data from -2 to 0.2 V
d.show_cv(-2, 0.2)

# Show the C-V data and then save it to 'cv.txt'
# d.save_cv('cv.txt', -2, 0.2, show=True)