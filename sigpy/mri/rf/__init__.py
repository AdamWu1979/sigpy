"""This MRI submodule contains functions and classes for MRI pulse design.

It currently provides tools for SLR pulse design and RF pulse simulation.
Tools for designing pTx, adiabatic, and other types of rf pulses,
as well as gradient and trajectory designers will be added soon.

Explore RF design tutorials at `sigpy-rf-tutorials`_.

See in-progress features at `sigpy-rf`_.

.. _sigpy-rf-tutorials: https://github.com/jonbmartin/sigpy-rf-tutorials
.. _sigpy-rf: https://github.com/jonbmartin/sigpy-rf

"""
from sigpy.mri import linop

from sigpy.mri.rf import adiabatic, b1sel, io, linop, multiband, optcont, ptx,\
    shim, sim, slr, trajgrad, util
from sigpy.mri.rf.adiabatic import *  # noqa
from sigpy.mri.rf.b1sel import *  # noqa
from sigpy.mri.rf.io import *  # noqa
from sigpy.mri.rf.linop import *  # noqa
from sigpy.mri.rf.multiband import *  # noqa
from sigpy.mri.rf.optcont import *  # noqa
from sigpy.mri.rf.ptx import *  # noqa
from sigpy.mri.rf.shim import *  # noqa
from sigpy.mri.rf.sim import *  # noqa
from sigpy.mri.rf.slr import *  # noqa
from sigpy.mri.rf.trajgrad import *  # noqa
from sigpy.mri.rf.util import *  # noqa

__all__ = ['linop']
__all__.extend(adiabatic.__all__)
__all__.extend(b1sel.__all__)
__all__.extend(io.__all__)
__all__.extend(multiband.__all__)
__all__.extend(optcont.__all__)
__all__.extend(ptx.__all__)
__all__.extend(sim.__all__)
__all__.extend(shim.__all__)
__all__.extend(slr.__all__)
__all__.extend(trajgrad.__all__)
__all__.extend(util.__all__)
