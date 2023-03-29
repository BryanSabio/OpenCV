from operations_cv import take_photo
from ui_interface import invok_ui

if '__main__' == __name__:
    def callback(name): return take_photo(name)
    invok_ui(callback)
