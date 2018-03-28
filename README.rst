========================================================
Nety - Currently under heavy work, don't use it for now!
========================================================

.. image:: https://img.shields.io/travis/YtenSoftware/Nety/master.svg?style=flat-square
   :target: https://travis-ci.org/YtenSoftware/Nety
   :alt: Travis CI Status

.. image:: https://img.shields.io/pypi/v/Nety.svg?style=flat-square
   :target: https://pypi.python.org/pypi/Nety/
   :alt: Version

.. image:: https://img.shields.io/github/tag/YtenSoftware/Nety.svg?style=flat-square   
   :target: https://github.com/YtenSoftware/Nety
   :alt: GitHub Version

.. image:: http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square
   :target: https://www.gnu.org/copyleft/gpl.html
   :alt: License

.. image:: https://img.shields.io/github/issues/YtenSoftware/Nety.svg?style=flat-square
   :target: https://github.com/YtenSoftware/Nety/issues
   :alt: Issues

.. image:: https://img.shields.io/github/stars/YtenSoftware/Nety.svg?style=flat-square
   :target: https://github.com/YtenSoftware/Nety/stargazers
   :alt: Stars

.. image:: https://img.shields.io/badge/Yten-Software-blue.svg?style=flat-square
   :alt: YtenSoftware

.. contents:: Table of Contents

.. _introduction:

Introduction: What is Nety?
=====================================

Nety is a Python_ library, which parses through Cisco IOS-style
(and other vendor) configurations.  It can:

- Audit existing router / switch / firewall / wlc configurations
- Retrieve portions of the configuration
- Modify existing configurations
- Build new configurations

The library examines an IOS-style config and breaks it into a set of linked
parent / child relationships.  You can perform complex queries about these 
relationships.

.. image:: https://raw.githubusercontent.com/YtenSoftware/Nety/master/sphinx-doc/_static/nety_parent_child.png
   :target: https://raw.githubusercontent.com/YtenSoftware/Nety/master/sphinx-doc/_static/nety_parent_child.png
   :alt: Nety Parent / Child relationships


What if we don't use Cisco?
===========================

Don't let that stop you.

As of Nety 1.2.4, you can parse `brace-delimited configurations`_ 
into a Cisco IOS style (see `Github Issue #17`_), which means that 
Nety understands these configurations:

- Juniper Networks Junos, and Screenos
- F5 Networks configurations

Nety also handles anything that has a Cisco IOS style of configuration, which includes:

- Cisco IOS, Cisco Nexus, Cisco IOS-XR, Cisco IOS-XE, Aironet OS, Cisco ASA, Cisco CatOS
- Arista EOS
- Brocade
- HP Switches
- Force 10 Switches
- Dell PowerConnect Switches
- Extreme Networks
- Enterasys


Docs
====

- You can find the HTML Docs `online <https://netwrk.ch/nety/>`_
- There is also a `Nety Tutorial <http://pennington.net/tutorial/Nety/ccp_tutorial.html>`_

.. _Pre-Requisites:

Pre-requisites
==============

Nety_ requires Python versions 3.2+ (We no longer support Python 2.x); the OS should not
matter. If you want to run it under a Python virtualenv_, it's been heavily 
tested in that environment as well.

.. _Installation:

Installation and Downloads
==========================

The best way to get Nety is with setuptools_ or pip_.  If you 
already have setuptools_, you can install as usual:

::

      # Substitute whatever Nety version you like...
      easy_install -U nety==1.3.0

Alternatively you can install into Python2.x with pip_:

::

      pip install --upgrade Nety

Use ``pip3`` for Python3.x...

::

      pip3 install --upgrade Nety

Otherwise `download it from PyPi <https://pypi.python.org/pypi/Nety>`_, extract it and run the ``setup.py`` script:

::

      python setup.py install

If you're interested in the source, you can always pull from the `github repo`_:


- From github_:
  ::

      git clone https://github.com/YtenSoftware/Nety.git


.. _FAQ:

FAQ
===

#) *QUESTION*: I want to use Nety_ with Python3; is that safe?  *ANSWER*: As long as you're using Python 3.3 or higher, it's safe. I test every release against Python 3.2+; however, Python 3.2 is currently exposed to a small bug for some configurations (see `Github Issue #14`_).

#) *QUESTION*: Some of the code in the documentation looks different than what I'm used to seeing.  Did you change something?  *ANSWER*: Yes, starting around Nety_ v0.9.10 I introducted more methods directly on ``IOSConfigLine()`` objects; going forward, these methods are the preferred way to use Nety_.  Please start using the new methods shown in the example, since they're faster, and you type much less code this way.

#) *QUESTION*: Nety_ saved me a lot of time, I want to give money.  Do you have a donation link?  *ANSWER*:  I love getting emails like this; helping people get their jobs done is why I wrote the module.  However, I'm not accepting donations.

#) *QUESTION*: Is there a way to use this module with perl?  *ANSWER*: Yes, I do this myself. Install the python package as you normally would and import it into perl with ``Inline.pm`` and ``Inline::Python`` from CPAN.

#) *QUESTION*: When I use ``find_children("interface GigabitEthernet3/2")``, I'm getting all interfaces beginning with 3/2, including 3/21, 3/22, 3/23 and 3/24. How can I limit my results?  *ANSWER*: There are two ways... the simplest is to use the 'exactmatch' option...  ``find_children("interface GigabitEthernet3/2", exactmatch=True)``. Another way is to utilize regex expansion that is native to many methods... ``find_children("interface GigabitEthernet3/2$")``

.. _`Other-Resources`:

Other Resources
===============

- `Dive into Python3`_ is a good way to learn Python
- `Team CYMRU`_ has a `Secure IOS Template`_, which is especially useful for external-facing routers / switches
- `Cisco's Guide to hardening IOS devices`_

.. _`Bug-Tracker-and-Support`:

Bug Tracker and Support
=======================

- Please report any suggestions, bug reports, or annoyances with Nety_ through the `github bug tracker`_.
- If you're having problems with general python issues, consider searching for a solution on `Stack Overflow`_.  If you can't find a solution for your problem or need more help, you can `ask a question`_.
- If you're having problems with your Cisco devices, you can open a case with `Cisco TAC`_; if you prefer crowd-sourcing, you can ask on the Stack Exchange `Network Engineering`_ site.

.. _Unit-Tests:

Unit-Tests
==========

`Travis CI project <https://travis-ci.org>`_ tests Nety on Python versions 2.6 through 3.4, as well as a `pypy JIT`_ executable.

Click the image below for details; the current build status is:

.. image:: https://img.shields.io/travis/YtenSoftware/Nety/master.svg?style=flat-square
   :target: https://travis-ci.org/YtenSoftware/Nety
   :alt: Travis CI Status

.. _`License and Copyright`:

License and Copyright
=====================

Nety_ is licensed GPLv3_; 
2016.


.. _Author:

Author and Thanks
=================

Nety_ was developed by Yten Software

Special thanks to mpenning for his great CiscoConfParse_, Nety is a successor of it!


.. _Nety: https://pypi.python.org/pypi/Nety

.. _Python: http://python.org/

.. _CiscoConfParse: https://github.com/mpenning/nety

.. _`pypy JIT`: http://pypy.org/

.. _`Github Issue #13`: https://github.com/mpenning/CiscoConfParse/issues/13

.. _`Github Issue #14`: https://github.com/mpenning/CiscoConfParse/issues/14

.. _`Github Issue #17`: https://github.com/mpenning/CiscoConfParse/issues/17

.. _`brace-delimited configurations`: https://github.com/YtenSoftware/Nety/blob/master/configs/sample_01.junos

.. _setuptools: https://pypi.python.org/pypi/setuptools

.. _pip: https://pypi.python.org/pypi/pip

.. _virtualenv: https://pypi.python.org/pypi/virtualenv

.. _`github repo`: https://github.com/YtenSoftware/Nety

.. _github: https://github.com/YtenSoftware/Nety

.. _mercurial: http://mercurial.selenic.com/

.. _`github bug tracker`: https://github.com/YtenSoftware/Nety/issues

.. _`regular expressions`: http://docs.python.org/2/howto/regex.html

.. _`docs`: http://www.pennington.net/py/Nety/

.. _`ipaddr`: https://code.google.com/p/ipaddr-py/

.. _`GPLv3`: http://www.gnu.org/licenses/gpl-3.0.html

.. _`ASF License 2.0`: http://www.apache.org/licenses/LICENSE-2.0

.. _`Dive into Python3`: http://www.diveintopython3.net/

.. _`Network Engineering`: http://networkengineering.stackexchange.com/

.. _`Stack Overflow`: http://stackoverflow.com/

.. _`ask a question`: http://stackoverflow.com/questions/ask

.. _`Secure IOS Template`: https://www.cymru.com/Documents/secure-ios-template.html

.. _`Team CYMRU`: http://www.team-cymru.org/

.. _`Cisco TAC`: http://cisco.com/go/support

.. _`Juniper networks`: http://www.juniper.net/

.. _`Cisco's Guide to hardening IOS devices`: http://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html

