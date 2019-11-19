import json
import logging

from flask_babel import lazy_gettext as _
from markupsafe import Markup
from wtforms import widgets
from wtforms.widgets import Input, html_params, HTMLString

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

class JsonEditorWidget(object):
    """
    JsonEditor
    """

    data_template = (
        '<input class="form-control hidden" %(text)s />'
        '<div class="input-group" id="jse_%(id)s">'
        "</div>"
        '<script>'
        " %(before_js)s"
        '</script>'
        '<script>'
            "init_json_editor('%(id)s', '%(json_schema)s', '%(starting_value)s', '%(json_config)s');"
        '</script>'
        '<script>'
        " %(after_js)s"
        '</script>'
    )

    def __init__(self, schema, before_js=None,after_js=None, jseditor_config=DEFAULT_JSEDITOR_CONFIG):
        super().__init__()
        self.schema = schema
        self.before_js = before_js
        self.after_js = after_js
        self.jseditor_config = jseditor_config

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)
        starting_value = ""
        if field.data:
            starting_value = '{}'.format(field.data)

        if not self.schema:
            field.json_schema = "{}"
        else:
            field.json_schema = json.dumps(self.schema)

        if not self.before_js:
            self.before_js = "// No Extra Javascript given"
        if not self.after_js:
            self.after_js = "// No Extra Javascript given"

        

        input_params = html_params(type="text", value=field.data, **kwargs)
        template_string = self.data_template % {"text": input_params,
                        "json_schema": field.json_schema,
                        "starting_value": starting_value,
                        "json_config": json.dumps(self.jseditor_config),
                        "id": field.id,
                        "before_js": self.before_js,
                        "after_js": self.after_js
                       }
        return HTMLString(template_string)
