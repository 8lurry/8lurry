# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from .demo import *
SITE = Site(
    globals(),
    remote_user_header='REMOTE_USER')
DEBUG = True
