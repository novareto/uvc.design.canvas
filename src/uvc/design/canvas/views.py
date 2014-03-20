# -*- coding: utf-8 -*-

try:
    from cromlech.browser import IView as Interface
except ImportError:
    from zope.interface import Interface


class IHomepage(Interface):
    pass
