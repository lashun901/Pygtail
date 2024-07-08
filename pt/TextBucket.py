from pygame import Surface, Rect, Color, font

class TextBox:
    def __init__(tb, text: str, location: tuple) -> None:
        tb.text = text
        tb.location = location
        tb.active = True

class TextBucket:
    def __init__(tb, canvas: Surface) -> None:
        tb.canvas = canvas
        tb.text_boxes = {}

    def _create_text_box(tb, text: str, location: tuple):
        return TextBox(text, location)

    def add(tb, id: str, text: str, location: tuple):
        try:
            tb.text_boxes[id] = tb._create_text_box(text, location)
        except:
            print("Something Went Wrong. Could Not Add Text Box.\n")
    
    def dump(tb, id: str):
        try:
            del tb.bucket[id]
        except:
            print("Something went wrong. Could Not Delete Te.")