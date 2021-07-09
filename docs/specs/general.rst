.. _whitewall.specs.general:

==============================
General overview of Whitewall
==============================

The goal of Whitewall is

.. contents::
  :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('whitewall.projects.whitewall1.settings.doctests')
>>> from lino.api.doctest import *


Show the list of members:

>>> rt.show(rt.models.users.AllUsers)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
============ ===================== ========== =========================== =====================
 First name   e-mail address        place      offered_products            wanted_products
------------ --------------------- ---------- --------------------------- ---------------------
 Anne         anne@example.com      Tallinn    *Buckwheat*
 Argo         argo@example.com      Haapsalu   *Electricity repair work*
 Fred         fred@example.com      Tallinn    *Bread*, *Buckwheat*
 Henri        henri@example.com     Tallinn    *Electricity repair work*   *Buckwheat*, *Eggs*
 Jaanika      jaanika@example.com   Tallinn
 Katrin       katrin@example.com    Vigala
 Mari         mari@example.com      Tartu                                  *Eggs*
 Peter        peter@example.com     Vigala
 Robin        demo@example.com
 Rolf         demo@example.com
 Romain       demo@example.com
============ ===================== ========== =========================== =====================
<BLANKLINE>

The `Products` table shows all products in alphabetical order:

>>> rt.show(rt.models.lets.Products)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ========================= ================== ================== ================= =================
 ID   Designation               Designation (de)   Designation (fr)   Offered by        Wanted by
---- ------------------------- ------------------ ------------------ ----------------- -----------------
 1    Bread                                                           *Fred*
 2    Buckwheat                                                       *Anne*, *Fred*    *Henri*
 5    Building repair work
 3    Eggs                                                                              *Henri*, *Mari*
 6    Electricity repair work                                         *Argo*, *Henri*
 4    Sanitary repair work
==== ========================= ================== ================== ================= =================
<BLANKLINE>


The `Offers` table show all offers.

>>> rt.show(rt.models.lets.Offers)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== ======= ========================= =============
 ID   User    product                   valid until
---- ------- ------------------------- -------------
 1    Fred    Bread
 2    Fred    Buckwheat
 3    Anne    Buckwheat
 4    Henri   Electricity repair work
 5    Argo    Electricity repair work
==== ======= ========================= =============
<BLANKLINE>


The *ActiveProducts* table is an example of how to handle customized
complex filter conditions.  It is a subclass of `Products`, but adds
filter conditions so that only "active" products are shown, i.e. for
which there is at least one offer or one demand.  It also specifies
`column_names` to show the two virtual fields `offered_by` and
`wanted_by`.

>>> rt.show(rt.models.lets.ActiveProducts)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
========================= ================== ================== ================= =================
 Designation               Designation (de)   Designation (fr)   Offered by        Wanted by
------------------------- ------------------ ------------------ ----------------- -----------------
 Bread                                                           *Fred*
 Buckwheat                                                       *Anne*, *Fred*    *Henri*
 Eggs                                                                              *Henri*, *Mari*
 Electricity repair work                                         *Argo*, *Henri*
========================= ================== ================== ================= =================
<BLANKLINE>
