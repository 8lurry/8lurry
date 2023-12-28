# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021-2022 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""Defines and instantiates a demo version of a Whitewall Site."""

from pathlib import Path
import datetime
from whitewall.lib.whitewall.settings import *


class Site(Site):
    is_demo_site = True
    the_demo_date = datetime.date(2015, 5, 23)

    languages = "en bn"

    demo_fixtures = ["std", "demo", "demo2"]

    # default_ui = 'lino.modlib.extjs'
    default_ui = "lino_react.react"

    def get_plugin_configs(self):
        yield super().get_plugin_configs()
        yield "google", "client_secret_file", Path.home() / "lino" / "whitewall_client_secret.json"


SITE = Site(globals())
DEBUG = True
USE_TZ = True
TIME_ZONE = "UTC"
