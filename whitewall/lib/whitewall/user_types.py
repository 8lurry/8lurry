# -*- coding: UTF-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)


"""Defines the standard user roles for Whitewall."""


from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import gettext_lazy as _

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"),        UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("User"),             SiteUser,  'user')
add('500', _("Moderator"),        SiteStaff, 'moderator')
add('900', _("Administrator"),    SiteAdmin, 'admin')
