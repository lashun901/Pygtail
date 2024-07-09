from pygame import Surface, Rect, Color, font
from pygame.font import Font
from string import printable

available_inputs = list(printable)

class TextBox:
    def __init__(tb, text: str, font: Font, location: tuple | Rect, text_color: Color = Color(0, 0, 0)) -> None:
        tb.text = text
        tb.font = font
        tb.location = location
        tb.surface = tb.font.render(tb.text, True, text_color)
        tb.active = True
        tb.show = True
    
    def set_location(tb, location: tuple | Rect) -> tuple | Rect:
        if isinstance(location, (tuple, Rect)):
            tb.location = location
        else: print("Invalid location given.")
    
    def get_surface_width(tb) -> int:
        return tb.surface.get_width()

    def get_surface_height(tb) -> int:
        return tb.surface.get_height()

class InputBox:
    def __init__(ib, rect_location: Rect, font_obj: Font) -> None:
        ib.active = False
        ib.location = rect_location
        ib.font = font_obj
        ib.text = ""
        ib.surface = ib.font.render(ib.text, True, Color(255, 255, 255))
    
    def render(ib):
        ib.surface = ib.font.render(ib.text, True, Color(255, 255, 255))
    
    def partial_event_loop(ib, e):
        pass # Left Here
    
"""
1.) Code functionality for adding an input box.
2.) Functionality for updating text inside input box.
NOTESS:
    I need to connect the PEL function in ALL Input boxes to the app's main event loop.
    (Maybe through iterating and checking if the text box is active(?))
"""

class TextBucket:
    def __init__(tb, canvas: Surface) -> None:
        tb.canvas = canvas
        tb.fonts = {"Consolas": font.SysFont("Consolas", 18)}
        tb.text_boxes = {}

    def _create_text_box(tb, text: str, location: tuple):
        return TextBox(text, tb.fonts["Consolas"], location)

    def _create_input_box(tb, rect_location: Rect):
        return InputBox(rect_location)
    
    def add_font(tb, font_name: str, point_size: int):
        tb.fonts[font_name] = font.SysFont(font_name, point_size)

    def add(tb, id: str, text: str, location: tuple):
        try:
            tb.text_boxes[id] = tb._create_text_box(text, location)
        except Exception as E:
            print(E)
    
    def dump(tb, id: str):
        try:
            del tb.text_boxes[id]
        except:
            print("Something went wrong. Could Not Delete Text Box.")
    
    def alter_location(tb, id: str, location: tuple | Rect):
        try:
            tb.text_boxes[id].set_location(location)
        except:
            print("Something went wrong. Could Not Alter Text Box Location.")

    def update(tb):
        for index, key in enumerate(tb.text_boxes):
            text_box = tb.text_boxes[key]
            if text_box.show:
                tb.canvas.blit(text_box.surface, text_box.location)
    
    def partial_event_loop(tb, event):
        pass # Left here