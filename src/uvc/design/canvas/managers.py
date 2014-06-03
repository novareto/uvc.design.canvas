# -*- coding: utf-8 -*-

from cromlech.browser import IViewSlot


class IPageTop(IViewSlot):
    """Marker For the area that sits at the top of the page.
    """


class ITabs(IViewSlot):
    """Marker for the action tabs.
    """


class IAboveContent(IViewSlot):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(IViewSlot):
    """Marker For the area that sits under the page body.
    """


class IHeaders(IViewSlot):
    """Marker For Headers
    """


class IToolbar(IViewSlot):
    """Marker for Toolbar
    """


class IFooter(IViewSlot):
    """
    """


class IExtraInfo(IViewSlot):
    """
    """
