# fab_addon_turbowidgets
A collection of widgets for Flask-AppBuilder

Work in progress...

## JsonEditorWidget
A Widget to replace the default TextInput editor in a Flask-AppBuilder view (for a StringField).
You can pass it a schema and this will display a dynamic form to set the arrtibutes of the Json string.

install:
````
python setup.py install
````
copy the jinja_utils.py files to your app and import it from your app.
copy or adapt your base template in order to load CSS and JS from addons (see extra/app_base.html)
use this new template as your base template by changing the way your app is initialized in you main app/__init__.py
```
appbuilder = AppBuilder(app, db.session, base_template='app_base.html')
```
