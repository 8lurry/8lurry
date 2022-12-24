# -*- coding: UTF-8 -*-
# Copyright 2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino_xl.lib.blogs import Plugin


class Plugin(Plugin):

    extends_models = ['Entry']
