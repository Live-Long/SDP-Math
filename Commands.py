from tkinter import *

class Command:
    def execute(self, root): pass


##### PHYSICS COMMANDS ######

class DoublePendulumCommand(Command):
    def execute(self, root):
        from phy import DoublePendulum
        root.execfile('DoublePendulum.py')


class MasSpringDamperCommand(Command):
    def execute(self, root):
        from phy import mass_spring_damper
        root.execfile('mass_spring_damper.py')


class MultiplePendulumCommand(Command):
    def execute(self, root):
        from phy import multiple_pendulum
        root.execfile('multiple_pendulum.py')


class ParticleSimCommand(Command):
    def execute(self, root):
        from phy import particle_simulation
        root.execfile('particle_simulation.py')


class PendulumCommand(Command):
    def execute(self, root):
        from phy import Pendulum
        root.execfile('Pendulum.py')


class ProjectileCommand(Command):
    def execute(self, root):
        from phy import projectile_full
        root.execfile('projectile_full.py')


class SolarCommand(Command):
    def execute(self, root):
        from phy import solar1
        root.execfile('solar1.py')


class ClothMouse1Command(Command):
    def execute(self, root):
        from phy import verlet_cloth_system_mouse
        root.execfile('verlet_cloth_system_mouse.py')


class ClothMouse2Command(Command):
    def execute(self, root):
        from phy import verlet_cloth_system_mouse2
        root.execfile('verlet_cloth_system_mouse2.py')


class VerletParticleCommand(Command):
    def execute(self, root):
        from phy import verlet_particle
        root.execfile('verlet_particle.py')


class VerletRigidBodyCommand(Command):
    def execute(self, root):
        from phy import verlet_rigid_body_mouse
        root.execfile('verlet_rigid_body_mouse.py')


##### PHYSICS 2 COMMANDS #####

class ArrowsCommand(Command):
    def execute(self, root):
        from phy2 import arrows
        root.execfile('arrows.py')


class BallsandLinesCommand(Command):
    def execute(self, root):
        from phy2 import balls_and_lines
        root.execfile('balls_and_lines.py')


class Box2DCommand(Command):
    def execute(self, root):
        from phy2 import box2d_vertical_stack
        root.execfile('box2d_vertical_stack.py')


class BreakoutCommand(Command):
    def execute(self, root):
        from phy2 import breakout
        root.execfile('breakout.py')


class CopyPickleCommand(Command):
    def execute(self, root):
        from phy2 import copy_and_pickle
        root.execfile('copy_and_pickle.py')


class DeformableCommand(Command):
    def execute(self, root):
        from phy2 import deformable
        root.execfile('deformable.py')


class FlipperCommand(Command):
    def execute(self, root):
        from phy2 import flipper
        root.execfile('flipper.py')


class PlaygroundCommand(Command):
    def execute(self, root):
        from phy2 import playground
        root.execfile('playground.py')


class PointQueryCommand(Command):
    def execute(self, root):
        from phy2 import point_query
        root.execfile('point_query.py')


class SpiderwebCommand(Command):
    def execute(self, root):
        from phy2 import spiderweb
        root.execfile('spiderweb.py')


##### MATH COMMANDS #####
class BayesianRegressionCommand(Command):

    def execute(self, root):
        from math_done import bayesian_regression
        root.execfile('bayesian_regression.py')


class BrownianMotionCommand(Command):
    def execute(self, root):
        from math_done import brownian_motion
        root.execfile('brownian_motion.py')


class DerivativesCommand(Command):
    def execute(self, root):
        from math_done import derivative
        root.execfile('derivative.py')


class EqGrapherCommand(Command):
    def execute(self, root):
        from math_done import Eq_grapher
        root.execfile('Eq_grapher.py')


class ExpDecayCommand(Command):
    def execute(self, root):
        from math_done import exponential_decay
        root.execfile('exponential_decay.py')


class FermatsSpiralCommand(Command):
    def execute(self, root):
        from math_done import Fermat_spiral
        root.execfile('Fermat_spiral.py')


class GeorgiasSpiralCommand(Command):
    def execute(self, root):
        from math_done import GeorgiasSpiral
        root.execfile('GeorgiasSpiral.py')


class HistogramComand(Command):
    def execute(self, root):
        from math_done import histogram
        root.execfile('histogram.py')


class NewtonIterationCommand(Command):
    def execute(self, root):
        from math_done import newton_iteration
        root.execfile('newton_iteration.py')


class RiemannSumCommand(Command):
    def execute(self, root):
        from math_done import RiemannSum
        root.execfile('RiemannSum.py')


##### MATH 2 COMMANDS #####

class Plot3DCommand(Command):
    def execute(self, root):
        from math2 import animation_3D_plot
        root.execfile('animation_3D_plot.py')


class AreaChartCommand(Command):
    def execute(self, root):
        from math2 import chart_input
        try:
            print("Give Inputs")
            root.execfile('chart_input.py')
        except Exception:
            return


class BarChartCommand(Command):
    def execute(self, root):
        from math2 import chart_input_adapter
        try:
            print("Give Inputs")
            root.execfile('chart_input_adapter.py')
        except Exception:
            return


class DonutPlotCommand(Command):
    def execute(self, root):
        from math2 import donut_plot
        root.execfile('donut_plot.py')


class GapminderCommand(Command):
    def execute(self, root):
        from math2 import gapminder_animation
        root.execfile('gapminder_animation.py')


class MonteCarloCommand(Command):
    def execute(self, root):
        from math2 import monte_carlo_integration
        root.execfile('monte_carlo_integration.py')


class ScatterPlotCommand(Command):
    def execute(self, root):
        from math2 import scatter_plot
        root.execfile('scatter_plot.py')


class TaylorCommand(Command):
    def execute(self, root):
        from math2 import taylor_series
        root.execfile('taylor_series.py')


class MultipleLinesCommand(Command):
    def execute(self, root):
        from math2 import multiple_lines_chart
        root.execfile('multiple_lines_chart.py')


###### MISCELLANEOUS COMMANDS #######

class BarnsleyCommand(Command):
    def execute(self, root):
        from miscc import BarnsleyFern
        root.execfile('BarnsleyFern.py')


class BubbleSortCommand(Command):
    def execute(self, root):
        from miscc import bubble_sort_UI
        root.execfile('bubble_sort_UI.py')


class FractalTreeCommand(Command):
    def execute(self, root):
        from miscc import FractalTree
        root.execfile('FractalTree.py')


class HoneycombCommand(Command):
    def execute(self, root):
        from miscc import honeycomb
        root.execfile('honeycomb.py')


class InteractiveMandelbrotCommand(Command):
    def execute(self, root):
        from miscc import InteractiveMandelbrot
        root.execfile('InteractiveMandelbrot.py')


class LangtonAntCommand(Command):
    def execute(self, root):
        from miscc import LangtonsAnt
        root.execfile('LangtonsAnt.py')


class QuasiCrystalCommand(Command):
    def execute(self, root):
        from miscc import quasicrystal
        root.execfile('quasicrystal.py')


class RainbowClickCommand(Command):
    def execute(self, root):
        from miscc import RainbowClick
        root.execfile('RainbowClick.py')


class RainbowRainCommand(Command):
    def execute(self, root):
        from miscc import rainbowrain
        root.execfile('rainbowrain.py')


class RandomFractalCommand(Command):
    def execute(self, root):
        from miscc import RandomFractalSpiral
        root.execfile('RandomFractalSpiral.py')


class SierPinskiCommand(Command):
    def execute(self, root):
        from miscc import Sierpinski
        root.execfile('Sierpinski.py')
