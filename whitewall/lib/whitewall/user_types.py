# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)


"""Defines the standard user roles for Whitewall."""


from lino.core.roles import SiteAdmin, SiteUser, SiteStaff
from lino.modlib.office.roles import OfficeUser, OfficeOperator, OfficeStaff
from lino_xl.lib.blogs.roles import BlogsReader
from lino_xl.lib.contacts.roles import SimpleContactsUser, ContactsUser, ContactsStaff
from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import gettext_lazy as _


class AnonUser(BlogsReader):
    pass


class AuthenticatedUser(AnonUser, SiteUser, OfficeUser, SimpleContactsUser):
    pass


class Moderator(AuthenticatedUser, SiteStaff, OfficeOperator, ContactsUser):
    pass


class SuperUser(Moderator, SiteAdmin, OfficeStaff, ContactsStaff):
    pass


UserTypes.clear()
add = UserTypes.add_item
add(
    "000",
    _("Anonymous"),
    AnonUser,
    "anonymous",
    readonly=True,
    authenticated=False,
)
add("100", _("User"), AuthenticatedUser, "user")
add("500", _("Moderator"), Moderator, "moderator")
add("900", _("Administrator"), SuperUser, "admin")
