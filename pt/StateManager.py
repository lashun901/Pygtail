from pygame import *
from time import time as t
from pt.Bucket import BlitBucket
from pt.CoreState import State

class StateManager:
    def __init__(state, dim: tuple) -> None:
        init()

        state.dim: tuple = dim
        state.canvas: Surface = display.set_mode(state.dim)

        state.is_popped = False

        state.delta_time: float = t()
        state.frame_length: float = t() - state.delta_time

        state.current_state: State = None
        state.STATES = {}

        state.Blit_Bucket = BlitBucket(canvas=state.canvas)

    def Add_State(state, new_state_name, new_state: State):
        if isinstance(new_state, State):
            state.STATES[new_state_name] = new_state
        else:
            return TypeError
    
    def Set_State(state, new_state: State):
        if isinstance(new_state, State):
            state.current_state = new_state
        else:
            return TypeError
    
    def Delete_State(state, state_name):
        try: 
            del state.STATES[state_name]
        except KeyError:
            print("*_* STATE NOT DELETED, BECAUSE STATE WAS NOT FOUND. INVALID KEY! *_*")
        
    def Change_State(state, state_name):
        try:
            state.current_state = state.STATES[state_name]
        except KeyError:
            print("*_* STATE NOT DELETED, BECAUSE STATE WAS NOT FOUND. INVALID KEY! *_*")
    
    def Kill(state):
        state.is_popped = True
    
    def Revive(state):
        state.is_popped = False
    
    def event_loop(state):
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE: state.Kill()
            
            state.current_state.partial_event_loop(e)

    def Run(state):
        while state.is_popped == False:
            state.event_loop()
            state.Blit_Bucket.update()