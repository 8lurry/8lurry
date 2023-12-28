# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""Desktop UI for this plugin.

"""

from lino.api import dd, _

from lino.modlib.users import ui as parent_module
from lino.modlib.users.ui import *
from lino.modlib.users.ui import Users


class UserDetail(parent_module.UserDetail):
    """Layout of User Detail in Whitewall."""

    main = "general contact"

    general = dd.Panel(
        """
    box1
    remarks:40 users.AuthoritiesGiven:20
    """,
        label=_("General"),
    )

    box1 = """
    username user_type:20
    language time_zone
    id created modified
    signature decrypt
    """

    contact = dd.Panel(
        """
    first_name last_name initials
    """,
        label=_("Contact"),
    )


Users.detail_layout = UserDetail()

Users.column_names = "first_name email"
