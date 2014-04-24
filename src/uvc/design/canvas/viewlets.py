# -*- coding: utf-8 -*-

try:
    import uvclight as grok
except ImportError:
    import grok

from .managers import IAboveContent, IPageTop, IHeaders
from .menus import IPersonalMenu, IContextualActionsMenu
from .menus import NavigationMenu, PersonalMenu, AddMenu, ContextualActionsMenu
from zope.interface import Interface
 

class ObjectActionMenuViewlet(grok.Viewlet):
    grok.name('contextualactions')
    grok.title('Actions')
    grok.viewletmanager(IAboveContent)
    grok.order(119)

    def render(self):
        menu = ContextualActionsMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class AddMenuViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IAboveContent)
    grok.order(120)

    def render(self):
        menu = AddMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class PersonalMenuViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IPageTop)
    grok.order(100)
    
    def render(self):
        menu = PersonalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class NavigationMenuViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IAboveContent)
    grok.order(100)

    def render(self):
        menu = NavigationMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class GlobalMenuViewlet(grok.Viewlet):
    grok.baseclass()
    grok.name('globalmenu')
    grok.context(Interface)
    grok.viewletmanager(IPageTop)
    grok.order(11)
    
    template = None