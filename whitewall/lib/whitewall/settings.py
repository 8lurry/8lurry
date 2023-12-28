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
    custom_layouts_module = "whitewall.lib.whitewall.layouts"
    theme_name = "whitewall"

    def get_welcome_messages(self, ar):
        for m in super().get_welcome_messages(ar):
            yield m

        yield f"""<p>GNUPG PUBLIC KEY:</p>
<div id="gpg-container" style="background: #eeffcc; max-width: 80ch; color: black; border: 1px solid green; border-radius: 3px; font-family: monospace;">
<span onclick="document.execCommand('copy')" style="cursor: pointer; position: inherit; float: right; border: 1px dashed blue; border-radius: 3px;">COPY</span>
<div id="gpg">
<p style="padding: 3px;">-----BEGIN PUBLIC KEY-----</p>
<p style="overflow-wrap: anywhere; padding: 3px;">
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAym5Y10NteJfS2kVO9CQ6\
2OFJo9s0OlM3yxM0UxQpH6omq3XZrSqFkDs6b1gftTVxDEnIT7pt0fPfnTEv1LKX\
q9FCV46xpYixhNbxzhWVarlhaZ6lL56FHyZaccrdGKevzRJxMpEpuqCbIC682i8W\
QeDiPiHiqx514bgUMUyupoVNfYDw6ts2DBfvN3dGxUCIadmCxA7AMljphlhnq9tw\
sVtTVzk2XkI+jmCYxCIncGAVg7FETRkGQIuRZ+n6f1SVKMPYAzGRYAVqU3aeQ7W7\
bB6FAXReT9fP3ep5xGnK2qqs6JiY/Fo4+3RoWZ+xfDv+Kp3WzIUQGLEwEmYzbu/P\
hQIDAQAB</p>
<p style="padding: 3px;">-----END PUBLIC KEY-----</p></div></div>"""

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`."""
        yield super(Site, self).get_installed_apps()
        yield "whitewall.lib.users"
        yield "whitewall.lib.whitewall"
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
        yield "system", "use_dashboard_layouts", True
        # yield "users", "allow_online_registration", True
        # yield "users", "third_party_authentication", True
        yield "linod", "use_channels", True

    def setup_quicklinks(self, ut, tb):
        super(Site, self).setup_quicklinks(ut, tb)


# activate_social_auth_testing(globals(), google=True)
