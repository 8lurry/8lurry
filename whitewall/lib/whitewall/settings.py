# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.projects.std.settings import *
from whitewall import SETUP_INFO

class Site(Site):

    verbose_name = "Whitewall"
    title = "Whitewall"
    description = SETUP_INFO['description']
    version = SETUP_INFO['version']
    url = SETUP_INFO['url']

    use_topbar_navigation = True
    demo_fixtures = ['std', 'demo', 'demo2']
    user_types_module = 'whitewall.lib.whitewall.user_types'
    migration_class = 'whitewall.lib.whitewall.migrate.Migrator'
    custom_layouts_module = 'whitewall.lib.whitewall.layouts'

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`.

        """
        yield super(Site, self).get_installed_apps()
        yield 'whitewall.lib.users'
        yield 'whitewall.lib.whitewall'
        yield 'lino_xl.lib.blogs'

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('system', 'use_dashboard_layouts', True)
        yield ('users', 'allow_online_registration', True)

    def setup_quicklinks(self, ut, tb):
        super(Site, self).setup_quicklinks(ut, tb)
