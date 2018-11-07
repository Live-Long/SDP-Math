"""This example lets you dynamically create static walls and dynamic balls

"""
__docformat__ = "reStructuredText"

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d

X, Y = 0, 1
### Physics collision types
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

assigned_color = "blue"

def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y + 600


def mouse_coll_func(arbiter, space, data):
    """Simple callback that increases the radius of circles touching the mouse"""
    s1, s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)

    return False


def draw_collision(arbiter, data):
    for c in arbiter.contact_point_set.points:
        r = max(3, abs(c.distance * 5))
        r = int(r)
        p = tuple(map(int, c.point_a))
        pygame.draw.circle(data["surface"], THECOLORS["red"], p, r, 0)

isElastic = False


class ball_class(object):

    color = "blue"
    def __init__(self, p):
        self.body = pymunk.Body(10, 100)
        self.body.position = p
        self.shape = pymunk.Circle(self.body, 10, (0, 0))
        self.shape.elasticity = 0.85 if isElastic else 0.0
        self.shape.friction = 0.5
        self.shape.collision_type = COLLTYPE_BALL


    def reduce_elasticity(self):
        if self.shape.elasticity >= 0.01:
            self.shape.elasticity = self.shape.elasticity - 0.000001


def main():

    def toggle_ball_color():
        if ball_class.color == "blue":
            ball_class.color = "green"
        else:
            ball_class.color = "blue"

    global isElastic
    pygame.init()
    pygame.display.set_caption("Balls and Lines")
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    ## Balls
    balls = []
    ball_objects = []
    ### Mouse
    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
    mouse_shape.collision_type = COLLTYPE_MOUSE
    space.add(mouse_shape)

    ch = space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL)
    ch.data["surface"] = screen
    ch.pre_solve = mouse_coll_func
    ch.post_solve = draw_collision

    ### Static line
    line_point1 = None
    static_lines = []
    run_physics = True


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == KEYDOWN and event.key == K_p:
                pygame.image.save(screen, "balls_and_lines.png")
            elif event.type == KEYDOWN and event.key == K_e:
                isElastic = not isElastic
            elif event.type == KEYDOWN and event.key == K_c:
                toggle_ball_color()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                p = event.pos[X], flipy(event.pos[Y])
                ball_obj = ball_class(p)
                space.add(ball_obj.body, ball_obj.shape)
                balls.append(ball_obj.shape)
                ball_objects.append(ball_obj)

            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                if line_point1 is None:
                    line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                if line_point1 is not None:
                    line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
                    body = pymunk.Body(body_type=pymunk.Body.STATIC)
                    shape = pymunk.Segment(body, line_point1, line_point2, 0.0)
                    shape.friction = 0.99
                    space.add(shape)
                    static_lines.append(shape)
                    line_point1 = None

            elif event.type == KEYDOWN and event.key == K_SPACE:
                run_physics = not run_physics

        p = pygame.mouse.get_pos()
        mouse_pos = Vec2d(p[X], flipy(p[Y]))
        mouse_body.position = mouse_pos

        if pygame.key.get_mods() & KMOD_SHIFT and pygame.mouse.get_pressed()[0]:
            body = pymunk.Body(10, 10)
            body.position = mouse_pos
            shape = pymunk.Circle(body, 10, (0, 0))

            shape.collision_type = COLLTYPE_BALL
            space.add(body, shape)
            balls.append(shape)

        ### Update physics
        if run_physics:
            dt = 1.0 / 60.0
            for x in range(1):
                space.step(dt)

        ### Draw stuff
        screen.fill(THECOLORS["white"])

        # Display some text
        font = pygame.font.SysFont("Helvetica", 16)
        text = """LMB: Create ball
LMB + Shift: Create many balls
RMB: Drag to create wall, release to finish
B: Toggle Elasticity
Space: Pause physics simulation"""
        y = 5
        for line in text.splitlines():
            text = font.render(line, 1, THECOLORS["black"])
            screen.blit(text, (5, y))
            y += 15

        for bl in ball_objects:
            bl.reduce_elasticity()

        for ball in balls:
            r = ball.radius
            v = ball.body.position
            rot = ball.body.rotation_vector
            p = int(v.x), int(flipy(v.y))
            p2 = Vec2d(rot.x, -rot.y) * r * 0.9
            pygame.draw.circle(screen, THECOLORS[ball_class.color], p, int(r), 2)
            pygame.draw.line(screen, THECOLORS["red"], p, p + p2)

        if line_point1 is not None:
            p1 = line_point1.x, flipy(line_point1.y)
            p2 = mouse_pos.x, flipy(mouse_pos.y)
            pygame.draw.lines(screen, THECOLORS["black"], False, [p1, p2])

        for line in static_lines:
            body = line.body
            line.elasticity = 0.95
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = pv1.x, flipy(pv1.y)
            p2 = pv2.x, flipy(pv2.y)
            pygame.draw.lines(screen, THECOLORS["black"], False, [p1, p2])

        ### Flip screen
        pygame.display.flip()
        clock.tick(50)
        # pygame.display.set_caption("fps: " + str(clock.get_fps()))


def run():
    doprof = 0
    if not doprof:
        try:
            main()
        except Exception:
            pass
    else:
        import cProfile, pstats

        prof = cProfile.run("main()", "profile.prof")
        stats = pstats.Stats("profile.prof")
        stats.strip_dirs()
        stats.sort_stats('cumulative', 'time', 'calls')
        stats.print_stats(30)


run()

