# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.projects.std.settings import *
from whitewall import SETUP_INFO

class Site(Site):

    verbose_name = "Whitewall"
    description = SETUP_INFO['description']
    version = SETUP_INFO['version']
    url = SETUP_INFO['url']

    demo_fixtures = ['std', 'demo', 'demo2']
    user_types_module = 'whitewall.lib.whitewall.user_types'
    migration_class = 'whitewall.lib.whitewall.migrate.Migrator'

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`.

        """
        yield super(Site, self).get_installed_apps()
        yield 'whitewall.lib.users'
        yield 'whitewall.lib.whitewall'
        # yield 'lino.modlib.export_excel'
        # yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.weasyprint'
        # yield 'lino_xl.lib.appypod'

    def setup_quicklinks(self, ut, tb):
        super(Site, self).setup_quicklinks(ut, tb)
