# -*- coding: utf-8 -*-

from dolmen.menu.interfaces import IMenu


class IGlobalMenu(IMenu):
    """Marker for GlobalMenu
    """


class IPersonalPreferences(IMenu):
    """Marker for PersonalPreferences
    """


class IFooterMenu(IMenu):
    """Marker for Footer
    """


class IDocumentActions(IMenu):
    """Marker for DocumentActions
    """


class IExtraViews(IMenu):
    """Marker for additional Views for Folders
       Objects etc...
    """


class IPersonalMenu(IMenu):
    """Marker for PersonalMenu
    """


class IContextualActionsMenu(IMenu):
    """Marker for PersonalMenu
    """


class ISubMenu(IMenu):
    pass
