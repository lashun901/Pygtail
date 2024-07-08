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
                pass

state_manager.Add_State("Base App", MainMenu(STATE=state_manager))
state_manager.Change_State("Base App")
state_manager.Run()

### Test Area End ###

quit()
super_quit()