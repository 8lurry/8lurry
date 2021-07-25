# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""General demo data for Whitewall.

"""

from lino.api import rt


def findbyname(model, name):
    """
    Utility function.
    """
    return model.objects.get(name=name)


# def objects():
#     """This will be called by the :ref:`dpy` deserializer during
#     :manage:`prep` and must yield a list of object instances to
#     be saved.
#
#     """
#     User = rt.models.users.User
#     UserTypes = rt.models.users.UserTypes
#
#     yield User(username='8lurry', user_type=UserTypes.admin, language="en")
