import json
import logging

from flask_babel import lazy_gettext as _
from markupsafe import Markup
#from wtforms import widgets
from wtforms.widgets import html_params, HTMLString
from wtforms import SelectField
from wtforms.compat import izip, text_type

log = logging.getLogger(__name__)

DEFAULT_JSEDITOR_CONFIG = {
       'theme': 'spectre',
       'iconlib': 'fontawesome4',
       'object_layout': 'normal',
       'template': 'default',
       'show_errors': 'interaction',
       'required_by_default': 1,
       'no_additional_properties': 1,
       'display_required_only': 0,
       'remove_empty_properties': 0,
       'keep_oneof_values': 1,
       'ajax': 0,
       'show_opt_in': 0,
       'disable_edit_json': 1,
       'disable_collapse': 1,
       'disable_properties': 1,
       'disable_array_add': 1,
       'disable_array_reorder': 1,
       'disable_array_delete': 1,
       'enable_array_copy': 0,
       'array_controls_top': 0,
       'disable_array_delete_all_rows': 0,
       'disable_array_delete_last_row': 0,
       'prompt_before_delete': 1,
}

class DynamicSelectField(SelectField):
    """
    DynamicSelect
    """

    def __init__(
        self,
        label=None,
        validators=None,
        coerce=text_type,
        choices_func=None,
        validate_choice=True,
        **kwargs
    ):
        super(DynamicSelectField, self).__init__(label=label, validators=validators, coerce=coerce, **kwargs)
        self.choices_func = choices_func
        self.validate_choice= validate_choice

    def iter_choices(self):
        self.__set_choices__()
        for value, label in self.choices:
            yield (value, label, self.coerce(value) == self.data)
        
    def __set_choices__(self):
        if not callable(self.choices_func):
            choices = []
        else:
            choices = self.choices_func()
        self.choices = choices

    def pre_validate(self, form):
        self.__set_choices__()
        if self.validate_choice:
            for v, _ in self.choices:
                if self.data == v:
                    break
            else:
                raise ValueError(self.gettext("Not a valid choice"))



class JsonEditorWidget(object):
    """
    JsonEditor
    """

    data_template = (
        '<input class="form-control hidden" %(text)s />'
        '<div %(jse_params)s  id="jse_%(id)s">'
        "</div>"
        '<script>'
        " %(before_js)s"
        '</script>'
        '<script>'
            "editor_%(id)s = init_json_editor('%(id)s', '%(json_schema)s', '%(starting_value)s', '%(json_config)s');"
            "if (typeof listOfJsonEditors === 'undefined') { listOfJsonEditors = new Object()};"
            "listOfJsonEditors['%(id)s'] = editor_%(id)s;"
        '</script>'
        '<script>'
        " %(after_js)s"
        '</script>'
    )

    def __init__(self, json_schema, before_js=None,after_js=None, extra_classes=None, jseditor_config=DEFAULT_JSEDITOR_CONFIG, master_id=None):
        super().__init__()
        self.json_schema = json_schema
        self.before_js = before_js
        self.after_js = after_js
        self.jseditor_config = jseditor_config
        self.extra_classes = extra_classes
        self.master_id = master_id

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)
        starting_value = ""
        if field.data:
            starting_value = '{}'.format(field.data)
        else:
            starting_value = "{}"

        if not callable(self.json_schema):
            schema = self.json_schema
        else:
            schema = self.json_schema()

        input_classes = 'input-group'
        if self.extra_classes:
            input_classes = input_classes + ' ' + self.extra_classes

        if not schema:
            field.json_schema = "{}"
        else:
            field.json_schema = json.dumps(schema)

        before_js = "// No Extra Javascript given"
        if not callable(self.before_js) and self.before_js:
            before_js = self.before_js
        if callable(self.before_js):
            before_js = self.before_js()

        after_js = "// No Extra Javascript given"
        if not callable(self.after_js) and after_js:
            after_js = self.after_js
        if callable(self.after_js):
            after_js = self.after_js()


        input_params = html_params(type="text", value=field.data, **kwargs)
        jse_dict = {
            'id': "jse_{}".format(field.id),
            'class': input_classes
        }
        if self.master_id:
            jse_dict['master_id'] = self.master_id
        jse_params = html_params(**jse_dict)
        template_string = self.data_template % {
                        "text": input_params,
                        "jse_params": jse_params,
                        "id": field.id,
                        "json_schema": field.json_schema,
                        "starting_value": starting_value,
                        "json_config": json.dumps(self.jseditor_config),
                        "before_js": before_js,
                        "after_js": after_js
                       }
        return HTMLString(template_string)
