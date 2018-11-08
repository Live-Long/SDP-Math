
class Command:
    def execute(self,root): pass


##### PHYSICS COMMANDS ######

class DoublePendulumCommand(Command):
    def execute(self,root):
        from phy import DoublePendulum
        root.execfile('DoublePendulum.py')


class MasSpringDamperCommand(Command):
    def execute(self,root):
        from phy import mass_spring_damper
        root.execfile('mass_spring_damper.py')


class MultiplePendulumCommand(Command):
    def execute(self,root):
        from phy import multiple_pendulum
        root.execfile('multiple_pendulum.py')

class ParticleSimCommand(Command):
    def execute(self,root):
        from phy import particle_simulation
        root.execfile('particle_simulation.py')


class PendulumCommand(Command):
    def execute(self,root):
        from phy import Pendulum
        root.execfile('Pendulum.py')


class ProjectileCommand(Command):
    def execute(self,root):
        from phy import projectile_full
        root.execfile('projectile_full.py')

class SolarCommand(Command):
    def execute(self,root):
        from phy import solar1
        root.execfile('solar1.py')



class ClothMouse1Command(Command):
    def execute(self,root):
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





###### MISCELLANEOUS COMMANDS #######

class BarnsleyCommand(Command):
    def execute(self, root):
        from miscc import BarnsleyFern
        root.execfile('BarnsleyFern.py')


class BubbleSortCommand(Command):
    def execute(self, root):
        from miscc import bubble_sort_UI
        root.execfile('bubble_sort_UI.py')

class DragonCurveCommand(Command):
    def execute(self, root):
        from miscc import DragonCurve
        root.execfile('DragonCurve.py')


class FractalTreeCommand(Command):
    def execute(self, root):
        from miscc import FractalTree
        root.execfile('FractalTree.py')


class HilbertCommand(Command):
    def execute(self, root):
        from miscc import Hilbert
        root.execfile('Hilbert.py')

class HoneycombCommand(Command):
    def execute(self, root):
        from miscc import honeycomb
        root.execfile('honeycomb.py')

class InteractiveMandelbrotCommand(Command):
    def execute(self, root):
        from miscc import InteractiveMandelbrot
        root.execfile('InteractiveMandelbrot.py')


class LangtonLoopCommand(Command):
    def execute(self, root):
        from miscc import langtonloop
        root.execfile('langtonloop.py')


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
    def execute(self,root):
        from miscc import RandomFractalSpiral
        root.execfile('RandomFractalSpiral.py')

class SierPinskiCommand(Command):
    def execute(self,root):
        from miscc import Sierpinski
        root.execfile('Sierpinski.py')
