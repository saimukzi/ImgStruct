import importlib

klass_dict = {}

def render_element(element_data, main):
    global klass_dict
    element_klass = element_data['class']
    if element_klass not in klass_dict:
        klass_dict[element_klass] = importlib.import_module(f'img_struct.element.{element_klass}')
    return klass_dict[element_klass].render_element(element_data, main)
