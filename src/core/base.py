import sys
import glfw
from core.openGLUtils import OpenGLUtils
from datetime import datetime

class Base:
    
    def __init__(self, window_title="GLFW Window", screen_size=(800, 600)):
        if not glfw.init():
            raise RuntimeError("Failed to initialize GLFW...")
        
        self._Window = glfw.create_window(
            screen_size[0], screen_size[1],
            window_title,
            None, None
        )
        
        if not self._Window:
            glfw.terminate()
            raise RuntimeError("Failed to initialize GLFW window...")

        # set current context as window
        glfw.make_context_current(self._Window)
        
        # print system info
        OpenGLUtils.printSystemInfo()
        glfw.set_key_callback(self._Window, self.keyboardEvents)
        
        self._TimeStamp = datetime.now()

    def update(self):
        pass

    def keyboardEvents(self, window, key, scancode, action, mods):
            print('KB:', key, chr(key), end=' ')
            if action == glfw.PRESS:
                print('press')
            elif action == glfw.REPEAT:
                print('repeat')
            elif action == glfw.RELEASE:
                print('release')
            if key == glfw.KEY_A:
                print('This is A.')
            elif key == glfw.KEY_UP:
                print('This is Up.')
            elif key == glfw.KEY_ENTER:
                print('This is Enter.')
    
    def shutdown(self):
        glfw.terminate()
        sys.exit()

    def run(self):
        while not glfw.window_should_close(self._Window):

            # render
            self.update()
            glfw.swap_buffers(self._Window)
            
            # poll for events
            glfw.poll_events()
            
        self.shutdown()
        
    def deltaTime(self):
        now = datetime.now()
        delta = now - self._TimeStamp
        self._TimeStamp = now
        return delta.total_seconds()