# -*- coding: UTF-8 -*-
# Copyright 2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, _
from lino_xl.lib.blogs import models as parent_module
from lino_xl.lib.blogs.models import *


class Entry(parent_module.Entry):
    class Meta(parent_module.Entry.Meta):
        abstract = dd.is_abstract_model(__name__, "Entry")
        verbose_name = _("Appunti")

    # fields = ['date', 'topic', 'title', 'content', 'author', 'album']


class HomeEntries(parent_module.LatestEntries):
    pass
