# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""Database models for this plugin.

"""

from lino.api import dd
from lino.modlib.users.models import *
from .mixins import UserKeys


class User(User, UserKeys):

    class Meta(User.Meta):
        app_label = 'users'
        abstract = dd.is_abstract_model(__name__, "User")
