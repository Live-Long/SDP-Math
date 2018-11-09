class Command:
    def execute(self): pass


##### PHYSICS COMMANDS ######

class DoublePendulumCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import DoublePendulum
        self.root.execfile('DoublePendulum.py')


class MasSpringDamperCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import mass_spring_damper
        self.root.execfile('mass_spring_damper.py')


class MultiplePendulumCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import multiple_pendulum
        self.root.execfile('multiple_pendulum.py')


class ParticleSimCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import particle_simulation
        self.root.execfile('particle_simulation.py')


class PendulumCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import Pendulum
        self.root.execfile('Pendulum.py')


class ProjectileCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import projectile_full
        self.root.execfile('projectile_full.py')


class SolarCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import solar1
        self.root.execfile('solar1.py')


class ClothMouse1Command(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import verlet_cloth_system_mouse
        self.root.execfile('verlet_cloth_system_mouse.py')


class ClothMouse2Command(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import verlet_cloth_system_mouse2
        self.root.execfile('verlet_cloth_system_mouse2.py')


class VerletParticleCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import verlet_particle
        self.root.execfile('verlet_particle.py')


class VerletRigidBodyCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy import verlet_rigid_body_mouse
        self.root.execfile('verlet_rigid_body_mouse.py')


##### PHYSICS 2 COMMANDS #####

class ArrowsCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import arrows
        self.root.execfile('arrows.py')


class BallsandLinesCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import balls_and_lines
        self.root.execfile('balls_and_lines.py')


class Box2DCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import box2d_vertical_stack
        self.root.execfile('box2d_vertical_stack.py')


class BreakoutCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import breakout
        self.root.execfile('breakout.py')


class CopyPickleCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import copy_and_pickle
        self.root.execfile('copy_and_pickle.py')


class DeformableCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import deformable
        self.root.execfile('deformable.py')


class FlipperCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import flipper
        self.root.execfile('flipper.py')


class PlaygroundCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import playground
        self.root.execfile('playground.py')


class PointQueryCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import point_query
        self.root.execfile('point_query.py')


class SpiderwebCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from phy2 import spiderweb
        self.root.execfile('spiderweb.py')


##### MATH COMMANDS #####
class BayesianRegressionCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import bayesian_regression
        # self.root.execfile('bayesian_regression.py')


class BrownianMotionCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import brownian_motion
        self.root.execfile('brownian_motion.py')


class DerivativesCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import derivative
        # self.root.execfile('derivative.py')


class EqGrapherCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import Eq_grapher
        # self.root.execfile('Eq_grapher.py')


class ExpDecayCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import exponential_decay
        self.root.execfile('exponential_decay.py')


class FermatsSpiralCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import Fermat_spiral
        self.root.execfile('Fermat_spiral.py')


class GeorgiasSpiralCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import GeorgiasSpiral
        self.root.execfile('GeorgiasSpiral.py')


class HistogramComand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import histogram
        self.root.execfile('histogram.py')


class NewtonIterationCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import newton_iteration
        self.root.execfile('newton_iteration.py')


class RiemannSumCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math_done import RiemannSum
        self.root.execfile('RiemannSum.py')


##### MATH 2 COMMANDS #####

class Plot3DCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import animation_3D_plot
        self.root.execfile('animation_3D_plot.py')


class AreaChartCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import chart_input
        self.root.execfile('chart_input.py')


class BarChartCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import chart_input_adapter
        self.root.execfile('chart_input_adapter.py')


class DonutPlotCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import donut_plot
        self.root.execfile('donut_plot.py')


class GapminderCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import gapminder_animation
        self.root.execfile('gapminder_animation.py')


class MonteCarloCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import monte_carlo_integration
        self.root.execfile('monte_carlo_integration.py')


class ScatterPlotCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import scatter_plot
        self.root.execfile('scatter_plot.py')


class TaylorCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import taylor_series
        self.root.execfile('taylor_series.py')


class MultipleLinesCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from math2 import multiple_lines_chart
        self.root.execfile('multiple_lines_chart.py')


###### MISCELLANEOUS COMMANDS #######

class BarnsleyCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import BarnsleyFern
        self.root.execfile('BarnsleyFern.py')


class BubbleSortCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import bubble_sort_UI
        self.root.execfile('bubble_sort_UI.py')


'''
class DragonCurveCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import DragonCurve
        self.root.execfile('DragonCurve.py')
'''


class FractalTreeCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import FractalTree
        self.root.execfile('FractalTree.py')


'''
class HilbertCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import Hilbert
        self.root.execfile('Hilbert.py')
'''


class HoneycombCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import honeycomb
        self.root.execfile('honeycomb.py')


class InteractiveMandelbrotCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import InteractiveMandelbrot
        self.root.execfile('InteractiveMandelbrot.py')


'''
class LangtonLoopCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import langtonloop
        self.root.execfile('langtonloop.py')
'''


class LangtonAntCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import LangtonsAnt
        self.root.execfile('LangtonsAnt.py')


class QuasiCrystalCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import quasicrystal
        self.root.execfile('quasicrystal.py')


class RainbowClickCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import RainbowClick
        self.root.execfile('RainbowClick.py')


class RainbowRainCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import rainbowrain
        self.root.execfile('rainbowrain.py')


class RandomFractalCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import RandomFractalSpiral
        self.root.execfile('RandomFractalSpiral.py')


class SierPinskiCommand(Command):
    root = None

    def __init__(self, root):
        self.root = root

    def execute(self):
        from miscc import Sierpinski
        self.root.execfile('Sierpinski.py')
