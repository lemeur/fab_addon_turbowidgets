
function init_json_editor(fieldname, json_schema, starting_value, json_config) {
    configObj = JSON.parse(json_config);
    schemaObj = JSON.parse(json_schema);
    newConfigObj = {
       schema: schemaObj,
       theme: 'spectre',
       iconlib: 'fontawesome4',
       object_layout: 'normal',
       template: 'default',
       show_errors: 'interaction',
       required_by_default: 1,
       no_additional_properties: 1,
       display_required_only: 0,
       remove_empty_properties: 0,
       keep_oneof_values: 1,
       ajax: 0,
       show_opt_in: 0,
       disable_edit_json: 1,
       disable_collapse: 1,
       disable_properties: 1,
       disable_array_add: 1,
       disable_array_reorder: 1,
       disable_array_delete: 1,
       enable_array_copy: 0,
       array_controls_top: 0,
       disable_array_delete_all_rows: 0,
       disable_array_delete_last_row: 0,
       prompt_before_delete: 1,
       ...configObj
    }
    if (starting_value !== "{}") {
        startValObj = JSON.parse(starting_value)
        newConfigObj =  {...newConfigObj, startval: startValObj}
    }
    theme = newConfigObj.theme
    iconlib = newConfigObj.iconlib
    JSONEditor.defaults.theme = theme;
    JSONEditor.defaults.iconlib = iconlib;
    var editor = new JSONEditor(document.getElementById('jse_'+fieldname),newConfigObj);
    editor.on('change',function() {
        var errors = editor.validate();
        if(errors.length) {
          console.log('JsonEditor Validation Error');
        }
        else {
          document.getElementById(fieldname).value = JSON.stringify(editor.getValue());
        }
    });
}


