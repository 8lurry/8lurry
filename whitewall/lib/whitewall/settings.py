# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021-2022 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.projects.std.settings import *
from lino.projects.std.settings import Site as StdSite
from lino.core.auth.utils import activate_social_auth_testing
from whitewall import SETUP_INFO


class Site(StdSite):
    verbose_name = "Whitewall"
    title = "Whitewall"
    description = SETUP_INFO["description"]
    version = SETUP_INFO["version"]
    url = SETUP_INFO["url"]
    web_front_ends = [
        (None, "lino.modlib.publisher"),
        ('admin', "lino_react.react")]


    demo_fixtures = []
    user_types_module = "whitewall.lib.whitewall.user_types"
    migration_class = "whitewall.lib.whitewall.migrate.Migrator"
    theme_name = "whitewall"

    def get_installed_plugins(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`."""
        yield super().get_installed_plugins()
        yield "whitewall.lib.users"
        yield "whitewall.lib.whitewall"
        yield "lino_xl.lib.countries"
        yield "whitewall.lib.blogs"
        yield "lino.modlib.linod"
        yield "lino.modlib.memo"
        yield "lino.modlib.uploads"
        yield "lino.modlib.publisher"
        yield "lino_xl.lib.contacts"
        yield "lino_xl.lib.cal"
        yield "lino_xl.lib.calview"
        yield "lino_xl.lib.google"
        yield "lino.modlib.comments"

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield 'publisher', 'locations', (
            ('b', 'blogs.LatestEntries'),
            ('p', 'publisher.Pages'),
            ('r', 'uploads.Uploads'),
            ('s', 'sources.Sources'),
            ('t', 'topics.Topics'),
            ('u', 'users.Users')
        )


    def setup_quicklinks(self, ut, tb):
        super(Site, self).setup_quicklinks(ut, tb)


# activate_social_auth_testing(globals(), google=True)
