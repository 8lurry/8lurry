# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""This is the main module of Whitewall.

.. autosummary::
   :toctree:

   lib
   projects


"""

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO.get('version')

doc_trees = ['docs']
