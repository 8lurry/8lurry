# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""Defines and instantiates a demo version of a Whitewall Site."""

import datetime

from ..settings import *


class Site(Site):

    # is_demo_site = True
    # the_demo_date = datetime.date(2015, 5, 23)

    languages = "en bn"

    default_ui = 'lino_react.react'

SITE = Site(globals())

DEBUG = True
