.. doctest docs/specs/roles.rst
.. _whitewall.specs.roles:

========================
User roles in Whitewall
========================

>>> import lino
>>> lino.startup('whitewall.projects.whitewall1.settings.doctests')
>>> from lino.api.doctest import *

Menus
-----

Site manager
------------------

Rolf is a :term:`site manager`, he has a complete menu.

>>> show_menu('robin')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Local Exchange : offers, demands
- Configure :
  - System : Users, Site Parameters
- Explorer :
  - System : Authorities, User types, User roles
- Site : About, User sessions
