from . import appbuilder, app

@app.context_processor
def jinja_addon_resources():
    #return dict(myexample='This is an example')
    addons_css = []
    addons_js = []
    mgrs = appbuilder.addon_managers
    for mgr in mgrs:
        mg = mgrs[mgr]
        if hasattr(mg, 'addon_css'):
            addons_css = addons_css + mg.addon_css
        if hasattr(mg, 'addon_js'):
            addons_js = addons_js + mg.addon_js
    return {'addons_js':addons_js, 'addons_css': addons_css}
