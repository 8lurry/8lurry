# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)


"""
Whitewall extension of :mod:`lino.modlib.users`.

.. autosummary::
   :toctree:

    models
    desktop
    fixtures.demo
    fixtures.demo2

"""

from lino.modlib import users


class Plugin(users.Plugin):
    extends_models = ["User"]
