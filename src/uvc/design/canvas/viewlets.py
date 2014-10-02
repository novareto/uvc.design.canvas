# -*- coding: utf-8 -*-

from .managers import IAboveContent, IPageTop
from .menus import NavigationMenu, PersonalMenu, AddMenu, ContextualActionsMenu
from grokcore.component import baseclass, name, title, context, order
from dolmen.viewlet import Viewlet, slot as viewletmanager
from uvc.content.interfaces import IContent
from zope.interface import Interface


class ObjectActionMenuViewlet(Viewlet):
    name('contextualactions')
    title('Actions')
    viewletmanager(IAboveContent)
    context(IContent)
    order(119)

    def render(self):
        menu = ContextualActionsMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class AddMenuViewlet(Viewlet):
    context(Interface)
    viewletmanager(IAboveContent)
    order(120)

    def render(self):
        menu = AddMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class PersonalMenuViewlet(Viewlet):
    context(Interface)
    viewletmanager(IPageTop)
    order(100)

    def render(self):
        menu = PersonalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class NavigationMenuViewlet(Viewlet):
    context(Interface)
    viewletmanager(IAboveContent)
    order(100)

    def render(self):
        menu = NavigationMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class GlobalMenuViewlet(Viewlet):
    baseclass()
    name('globalmenu')
    context(Interface)
    viewletmanager(IPageTop)
    order(11)

    template = None


__all__ = [
    'ObjectActionMenuViewlet',
    'AddMenuViewlet',
    'PersonalMenuViewlet',
    'NavigationMenuViewlet',
    'GlobalMenuViewlet',
    ]
