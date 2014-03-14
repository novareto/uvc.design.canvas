# -*- coding: utf-8 -*-

try:
    from cromlech.browser import IViewSlot as Interface
except ImportError:
    from zope.interface import Interface


class IPageTop(Interface):
    """Marker For the area that sits at the top of the page.
    """


class ITabs(Interface):
    """Marker for the action tabs.
    """


class IAboveContent(Interface):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(Interface):
    """Marker For the area that sits under the page body.
    """


class IHeaders(Interface):
    """Marker For Headers
    """


class IToolbar(Interface):
    """Marker for Toolbar
    """


class IFooter(Interface):
    """
    """


class IExtraInfo(Interface):
    """
    """
