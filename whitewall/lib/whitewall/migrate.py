# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""Default data migrator for Whitewall.


"""

from lino.utils import dpy


class Migrator(dpy.Migrator):
    """The standard migrator for Whitewall.

    This is used because
    :class:`whitewall.projects.whitewall.settings.Site` has
    :attr:`migration_class <lino.core.site.Site.migration_class>` set
    to ``"whitewall.lib.whitewall.migrate.Migrator"``.

    """

    def migrate_from_0_0_1(self, globals_dict):
        # do something here
        return "0.0.2"
