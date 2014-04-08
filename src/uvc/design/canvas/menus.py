# -*- coding: utf-8 -*-

from os import path

from dolmen.menu import Menu
from dolmen.menu.interfaces import IMenu
from dolmen.template import TALTemplate
from grokcore.component import name, context, title
from zope.interface import implementer, Interface
from zope.security.management import getInteraction


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


def get_template(filename):
    return TALTemplate(path.join(path.dirname(__file__), 'templates', filename))


@implementer(IGlobalMenu)
class GlobalMenu(Menu):
    name('globalmenu')
    title(u"GlobalMenu")

    template = get_template('globalmenu.cpt')
    menu_class = u'nav nav-pills pull-right'
    css = "global_menu"


@implementer(IContextualActionsMenu)
class ContextualActionsMenu(Menu):
    name('contextualactionsmenu')
    title(u"Actions")

    template = get_template('objectmenu.cpt')
    menu_class = u'nav nav-pills pull-right'
    css = "actions_menu"


class AddMenu(Menu):
    name('uvcsite-addmenu')
    context(Interface)
    title(u'Hinzufügen')

    template = get_template('addmenutemplate.cpt')

    menu_class = u'nav nav-pills pull-right'
    css = "addmenu"


@implementer(IPersonalMenu)
class PersonalMenu(Menu):
    name('personal')
    title('Personal menu')
    context(Interface)
    template = get_template('personal.cpt')

    menu_class = u'nav nav-tabs'
    css = "navigation"


@implementer(IPersonalPreferences)
class PersonalPreferences(Menu):
    name('personalpreferences')
    title('Personal Preferences')

    template = get_template('personal.cpt')
    menu_class = "nav navbar-nav pull-right"


@implementer(IDocumentActions)
class DocumentActionsMenu(Menu):
    name('documentactions')
    title('Document Actions')
    menu_class = "pull-right"
    template = get_template('personal.cpt')


@implementer(IFooterMenu)
class FooterMenu(Menu):
    name('footermenu')
    title('Footer Menu')
    template = get_template('personal.cpt')
    menu_class = "nav nav-tabs pull-right"


class UserMenu(Menu):
    name('useractions')
    title('User actions')
    context(Interface)
    template = get_template('useractions.cpt')

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
    template = get_template('navigationmenutemplate.cpt')

    menu_class = u'nav nav-tabs'
    css = "navigation"
