import logging
from flask_appbuilder.basemanager import BaseManager
from flask_babel import lazy_gettext as _
from flask import Blueprint, url_for


log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views
   
"""


class TurboWidgetsManager(BaseManager):


    def __init__(self, appbuilder):
        """
             Use the constructor to setup any config keys specific for your app. 
        """
        super(TurboWidgetsManager, self).__init__(appbuilder)
        #self.appbuilder.get_app.config.setdefault('MYADDON_KEY', 'SOME VALUE')
        self.static_bp = Blueprint('fab_addon_turbowidgets', __name__,
                                   url_prefix='/static_addon_turbowidgets',
                                   template_folder='templates',
                                   static_folder='static/fab_addon_turbowidgets',
                                   static_url_path='/fab_addon_turbowidgets')
        self.addon_js = [('fab_addon_turbowidgets.static', 'js/jsoneditor.js'),
                         ('fab_addon_turbowidgets.static', 'js/main.js')]
        self.addon_css = [('fab_addon_turbowidgets.static', 'css/jsoneditor.min.css')]
        log.info("Initializing TurboWidgetsManager")

    def register_views(self):
        """
            This method is called by AppBuilder when initializing, use it to add you views
        """
        pass

    def pre_process(self):
        log.info("Adding static blueprint for fab_addon_turbowidgets.")
        self.appbuilder.get_app.register_blueprint(self.static_bp)
        #log.debug("App Routes after turbowidgets Blueprint registering=",[str(p) for p in self.appbuilder.get_app.url_map.iter_rules()])

    def post_process(self):
        pass

