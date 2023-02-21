from OpenGL.GL import *
import glfw

delta = 0.1
angle = 0.0
posx = 0.0
posy = 0.0
size = 0.0


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "хуй", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, transfer_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    while not glfw.window_should_close(window):
        display(window)

    glfw.destroy_window(window)
    glfw.terminate()


def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()

    glRotatef(angle, 0, 0, 1)

    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 1, 0.5)

    glVertex2f(0.5 + size, 0.5 + size)
    glVertex2f(1 + size, 0 + size)
    glVertex2f(-1 + size, 0 + size)

    glEnd()

    glPopMatrix()
    angle += 0.1
    glfw.swap_buffers(window)
    glfw.poll_events()


def transfer_callback(window, key, scancode, action, mods):
    global posx
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            posx += 0.1
        if key == 263:
            posx -= 0.1


def scroll_callback(window, xoffset, yoffset):
    global size
    if (xoffset > 0):
        size -= yoffset / 10
    else:
        size += yoffset / 10


if __name__ == "__main__":
    main()
