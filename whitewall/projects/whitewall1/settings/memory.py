# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from .demo import *
from .demo import DATABASES

SITE = Site(globals())
DATABASES["default"]["NAME"] = ":memory:"
