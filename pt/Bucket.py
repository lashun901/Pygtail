from pygame import Surface, Rect, Color
from pygame.display import flip
from pt.TextBucket import TextBucket

class Image:
    def __init__(img, surface: Surface, location: Rect, color: Color = None):
        img.surface = surface
        img.location = location
        img.color = color
        img.active = True
        img.show = True

class BlitBucket:
    def __init__(bb, canvas: Surface, bg_color: Color = Color(0,0,0,255)):
        bb.canvas: Surface = canvas
        bb.bucket: dict = {}
        bb.bg_color = bg_color

        # Text Bucket Instantiation
        bb.Text_Bucket = TextBucket(bb.canvas)
    
    def _create_image(img, surface: Surface, location: Rect, color: Color = None):
        return Image(surface, location, color)

    def add(bb, id: str, surface: Surface, location: Rect, color: Color = None):
        try:
            bb.bucket[id] = bb._create_image(surface, location, color)
        except:
            print("Something Went Wrong. Could not add Surface.\n")
    
    def dump(bb, id: str):
        try:
            del bb.bucket[id]
        except:
            print("Something went wrong. Could Not Delete.")
    
    def alter_color(bb, id: str, color: Color):
        try:
            bb.bucket[id].color = color
        except:
            print("Something went wrong. Could Not Change Color.")
    
    def alter_location(bb, id: str, location: tuple | Rect):
        try:
            bb.bucket[id].location = location
        except:
            print("Something went wrong. Could Not Change Location.")
    
    def alter_surface(bb, id: str, surface: Surface):
        try:
            bb.bucket[id].surface = surface
        except:
            print("Something went wrong. Could Not Change Location.")
    
    def get_location(tb, id: str):
        try:
            return tb.bucket[id].location
        except Exception as E:
            print(E)
    
    def update(bb):
        bb.canvas.fill(bb.bg_color)
        for index, key in enumerate(bb.bucket):
            image = bb.bucket[key]
            if image.show:
                if image.color:
                    image.surface.fill(image.color)
                bb.canvas.blit(image.surface, image.location)
        
        bb.Text_Bucket.update()
    
    def partial_event_loop(bb, event):
        bb.Text_Bucket.partial_event_loop(event)
        
        flip()