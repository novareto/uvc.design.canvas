# -*- coding: utf-8 -*-

from grokcore.component import baseclass, context
from dolmen.viewlet import Viewlet
from zope.interface import Interface


class MenuViewlet(Viewlet):
    baseclass()
    context(Interface)
    
    template = None
    menu = None

    def namespace(self):
        return {
            'context': self.context,
            'request': self.request,
            'view': self.view,
            'manager': self.manager,
            'viewlet': self,
            'menu': self.menu,
            'entries': self.menu.entries,
            }

    def render(self):
        if self.template is not None:
            return super(MenuViewlet, self).render()
        elif self.menu is not None:
            menu = self.menu(self.context, self.request, self.view)
            menu.update()
            return menu.render()
        else:
            raise NotImplementedError('Please, specify a menu class')


__all__ = [
    'MenuViewlet',
    ]
