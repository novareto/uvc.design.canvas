# -*- coding: utf-8 -*-

from os import path

from ul.browser import Menu
from dolmen.template import TALTemplate
from grokcore.component import name, context, title, adapter, implementer
from zope.interface import Interface, implements
from zope.security.management import getInteraction
from cromlech.browser import ITemplate
from uvc.entities.browser.menus import *


def get_template(filename):
    return TALTemplate(path.join(path.dirname(__file__), 'templates', filename))


class ContextualActionsMenu(Menu):
    name('contextualactionsmenu')
    title(u"Actions")
    context(Interface)
    implements(IContextualActionsMenu)
    menu_class = u'nav nav-pills pull-right'


class GlobalMenu(Menu):
    name('globalmenu')
    title(u"GlobalMenu")
    context(Interface)
    implements(IGlobalMenu)

    menu_class = u'nav nav-pills pull-right'
    css = "global_menu"


class AddMenu(Menu):
    name('uvcsite-addmenu')
    context(Interface)
    title(u'Hinzufügen')
    implements(IAddMenu)

    menu_class = u'nav nav-pills pull-right'
    css = "addmenu"


class PersonalMenu(Menu):
    name('personal')
    title('Personal menu')
    context(Interface)
    implements(IPersonalMenu)

    menu_class = u'nav nav-tabs'
    css = "navigation"


class PersonalPreferences(Menu):
    name('personalpreferences')
    title('Personal Preferences')
    context(Interface)
    implements(IPersonalPreferences)

    template = get_template('personal.cpt')
    menu_class = "nav navbar-nav pull-right"


class DocumentActionsMenu(Menu):
    name('documentactions')
    title('Document Actions')
    context(Interface)
    implements(IDocumentActions)
    

class FooterMenu(Menu):
    name('footermenu')
    title('Footer Menu')
    context(Interface)
    implements(IFooterMenu)


class UserMenu(Menu):
    name('useractions')
    title('User actions')
    context(Interface)
    implements(IUserMenu)

    menu_class = u'nav nav-tabs'
    css = "navigation"

    def standalone(self):
        return self.request.application_url + "/meine_daten"

    @property
    def username(self):
        policy = getInteraction()
        if len(policy.participations) == 1:
            principal = policy.participations[0].principal
            return principal.description or principal.id
        return None


class NavigationMenu(Menu):
    name('navigation')
    title('Navigation')
    context(Interface)
    implements(INavigationMenu)
    menu_class = u'nav nav-tabs'
    css = "navigation"


class Quicklinks(Menu):
    name('quicklinks')
    title('Quicklinks')
    context(Interface)
    implements(INavigationMenu)
    menu_class = u'nav nav-tabs'
    css = "quicklinks"


@adapter(IGlobalMenu, Interface)
@implementer(ITemplate)
def global_template(context, request):
    return get_template('globalmenu.cpt')


@adapter(INavigationMenu, Interface)
@implementer(ITemplate)
def nav_template(context, request):
    return get_template('navigationmenutemplate.cpt')


@adapter(IUserMenu, Interface)
@implementer(ITemplate)
def user_template(context, request):
    return get_template('useractions.cpt')


@adapter(IPersonalMenu, Interface)
@implementer(ITemplate)
def personal_template(context, request):
    return get_template('personal.cpt')


@adapter(IAddMenu, Interface)
@implementer(ITemplate)
def add_template(context, request):
    return get_template('addmenutemplate.cpt')

    
@adapter(IContextualActionsMenu, Interface)
@implementer(ITemplate)
def object_template(context, request):
    return get_template('objectmenu.cpt')
