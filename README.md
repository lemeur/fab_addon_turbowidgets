# fab_addon_turbowidgets
A collection of widgets for Flask-AppBuilder


### Installation
* Install the addon
````
python setup.py install
````
* copy the jinja_utils.py files to your app and import it from your app. This will register two new Jinja variables (`addons_js`and `addons_css`) which are read from FAB_ADDONS attributes
* copy or adapt your base template in order to load CSS and JS from addons (see extra/app_base.html)
```
{% extends 'appbuilder/baselayout.html' %}

{% block head_css %}
    {{ super() }}

    {% for c in addons_css %}
        <link rel="stylesheet" href="{{url_for(c[0],filename=c[1])}}">
    {% endfor %}

{% endblock %}

{% block head_js %}
    {{ super() }}
    {% for j in addons_js %}
        <script src="{{url_for(j[0],filename=j[1])}}"></script>
    {% endfor %}
{% endblock %}
```
* use this new template as your base template by changing the way your app is initialized in you main app/__init__.py
```
appbuilder = AppBuilder(app, db.session, base_template='app_base.html')
```

## JsonEditorWidget
JsonEditorWidget is a FAB addon widget to replace the default TextInput editor in a Flask-AppBuilder view (for a StringField).

The model remains unchanged (here the address string field will contain a Json entry):
```
class Contact(Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    address =  Column(String(564))
    personal_phone = Column(String(20))
    personal_cellphone = Column(String(20))

    def __repr__(self):
        return self.name

```

The we preapre a schema describing the structure of the Json field so that JsonEditor will create a form for us:
```
    jseditor_schema =  {
        "type": "object",
        "title": " ",
        "required": ["cp","country"],
        "properties": {
            "country": {
                "type": "string",
                "propertyOrder": 1
            },
            "zipcode": {
                "type": "string",
                "propertyOrder": 2
            },
            "number": {
                "type": "integer",
                "propertyOrder": 3
            },
            "street": {
                "type": "string",
                "propertyOrder": 4
            }
        }
    }
```

Then in your view, you can use the widget like this:
```
from fab_addon_turbowidgets.widgets import JsonEditorWidget

...

    edit_form_extra_fields = {
        "address": StringField(
            "AddressJSON",
            widget=JsonEditorWidget(jseditor_schema, before_js, after_js),
        ),
    }
    add_form_extra_fields = edit_form_extra_fields
```
