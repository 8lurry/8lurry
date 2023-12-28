# -*- coding: UTF-8 -*-
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, _


class UserKeys(dd.Model):
    class Meta:
        abstract = True

    signature = dd.CharField(
        max_length=500, verbose_name=_("Signature key"), blank=True, null=True
    )

    decrypt = dd.CharField(
        max_length=500, verbose_name=_("Decryption key"), blank=True, null=True
    )
