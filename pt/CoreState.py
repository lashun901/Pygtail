from pt.Bucket import BlitBucket, Color
from pygame import event, KEYDOWN, K_SPACE
from random import randint as ri

class State:
    def __init__(state,STATE) -> None:
        state.STATE = STATE
        state.delta_time = state.STATE.delta_time
        state.Blit_Bucket: BlitBucket = state.STATE.Blit_Bucket
        state.KILL = state.STATE.Kill

        state.IMAGES_LOADED: bool = False # Keeps track of whether or not images have been loaded into the Blit Bucket.

    def partial_event_loop(state, event):
        state.Blit_Bucket.partial_event_loop(event)