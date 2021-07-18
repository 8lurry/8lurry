# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""The :xfile:`models.py` module for this plugin.

"""

from lino.api import dd, _

class Appunti(dd.Model):

    class Meta:
        verbose_name = _("Note")

    fields = ['date', 'topic', 'title', 'content', 'author', 'album']
