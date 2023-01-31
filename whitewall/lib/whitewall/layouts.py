# -*- coding: UTF-8 -*-
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.modlib.system.choicelists import DashboardLayouts
from lino.api import _

DashboardLayouts.clear()
add = DashboardLayouts.add_item
add("default", _("Default dashboard"), """
welcome_messages
blogs.PublicEntries
""")
