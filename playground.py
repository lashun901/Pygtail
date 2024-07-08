from sys import exit as super_quit
from pt.StateManager import StateManager, Surface, Color, State, KEYDOWN, K_SPACE
from random import randint as ri


dim = (640, 360)

### Test Area ###
state_manager = StateManager(dim=dim)

class MainMenu(State):
    def __init__(state, STATE) -> None:
        super().__init__(STATE)

        state.Blit_Bucket.add("Color Square",
                              Surface((65,65)),
                              Surface((65,65)).get_rect(center=(dim[0]//2, dim[1]//2)),
                              Color(255,255,255))
    
    def partial_event_loop(state, event):
        super().partial_event_loop(event=event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                state.Blit_Bucket.alter_color("Color Square", color=Color(ri(0,255),ri(0,255),ri(0,255)))
                state.Blit_Bucket.alter_location("Color Square", location=(ri(0,600),ri(0,320)))
                new_side_length = ri(15,75)
                state.Blit_Bucket.alter_surface("Color Square", surface=Surface((new_side_length, new_side_length)))

state_manager.Add_State("Base App", MainMenu(STATE=state_manager))
state_manager.Change_State("Base App")
state_manager.Run()

### Test Area End ###

quit()
super_quit()