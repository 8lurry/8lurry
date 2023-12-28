# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""Database models for this plugin.

"""

from lino.api import dd
from lino.modlib.users import models as parent_module
from lino.modlib.users.models import *
from .mixins import UserKeys


class User(parent_module.User, UserKeys):
    class Meta(parent_module.User.Meta):
        abstract = dd.is_abstract_model(__name__, "User")
