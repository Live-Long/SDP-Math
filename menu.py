from tkinter import *

from PIL import Image, ImageTk

# window call and size

root = Tk()
root.title("Academedia ver. Alpha 1.1")
root.geometry("600x700")

# BG
C = Canvas(root, bg="blue", height=1, width=1)
filename = PhotoImage(file="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()


def RBGAImage(path):
    return Image.open(path).convert("RGBA")


# Logo
logoRBGA = RBGAImage("logo.png")
logo = ImageTk.PhotoImage(logoRBGA)
logolabel = Label(image=logo)
logolabel.configure(bg="black")
logolabel.grid(padx=70, pady=90)

# Title
app = Frame(root)
app.grid()


# Button Events
#############################################################

#   Physics Functions #
from Commands import *


def run_double_pendulum():
    command = DoublePendulumCommand()
    command.execute(root)


def run_mass_spring_damper():
    command = MasSpringDamperCommand()
    command.execute(root)


def run_multiple_pendulum():
    command = MultiplePendulumCommand()
    command.execute(root)


def run_particle_sim():
    command = ParticleSimCommand()
    command.execute(root)

def run_pendulum():
    command = PendulumCommand()
    command.execute(root)


def run_projectile():
    command = ProjectileCommand()
    command.execute(root)

def run_solar():
    command = SolarCommand()
    command.execute(root)


def run_verlet_cloth_1():
    command = ClothMouse1Command()
    command.execute(root)


def run_verlet_cloth_2():
    command = ClothMouse2Command()
    command.execute(root)


def run_verlet_particle():
    command = VerletParticleCommand()
    command.execute(root)


def run_verlet_rigid_body():
    command = VerletRigidBodyCommand()
    command.execute(root)

########   Physics 2 Functions   #########

def run_arrow():
    command = ArrowsCommand()
    command.execute(root)

def run_balls_lines():
    command = BallsandLinesCommand()
    command.execute(root)

def run_box2d_verticle():
    command = Box2DCommand()
    command.execute(root)

def run_breakout():
    command = BreakoutCommand()
    command.execute(root)

def run_copy_pickle():
    command = CopyPickleCommand()
    command.execute(root)

def run_flipper():
    command = FlipperCommand()
    command.execute(root)

def run_deformable():
    command = DeformableCommand()
    command.execute(root)

def run_newtons_cradle():
    from phy2 import newtons_cradle
    root.execfile('newtons_cradle.py')

def run_playground():
    command = PlaygroundCommand()
    command.execute(root)

def run_point_query():
    command = PointQueryCommand()
    command.execute(root)

def run_spiderweb():
    command = SpiderwebCommand()
    command.execute(root)



########   Math Functions   #########
def run_bayesian_regression():
    command = BayesianRegressionCommand()
    command.execute(root)


def run_brownian_motion():
    command = BrownianMotionCommand()
    command.execute(root)


def run_derivatives():
    command = DerivativesCommand()
    command.execute(root)


def run_eq_grapher():
    command = EqGrapherCommand()
    command.execute(root)


def run_exponential_decay():
    command = ExpDecayCommand()
    command.execute(root)


def run_fermats_spiral():
    command = FermatsSpiralCommand()
    command.execute(root)


def run_georgias_spiral():
    command = GeorgiasSpiralCommand()
    command.execute(root)


def run_histogram():
    command = HistogramComand()
    command.execute(root)


def run_newton_iteration():
    command = NewtonIterationCommand()
    command.execute(root)


def run_riemann_sum():
    command = RiemannSumCommand()
    command.execute(root)


########## Math 2 Functions #########

def run_3D_plot():
    command = Plot3DCommand()
    command.execute(root)


def run_area_chart():
    command = AreaChartCommand()
    command.execute(root)


def run_bar_chart():
    command = BarChartCommand()
    command.execute(root)


def run_donut_plot():
    command = DonutPlotCommand()
    command.execute(root)


def run_gapminder_animation():
    command = GapminderCommand()
    command.execute(root)


def run_monte_carlo():
    command = MonteCarloCommand()
    command.execute(root)


def run_multiple_lines_chart():
    command = MultipleLinesCommand()
    command.execute(root)


def run_scatter_plot():
    command = ScatterPlotCommand()
    command.execute(root)


def run_taylor_series():
    command = TaylorCommand()
    command.execute(root)


#######################################


########   Chemistry Functions ##########

def run_bond_antibond():
    from chem import bond_antibond
    root.execfile('bond_antibond.py')

#########################################


########   Misc Functions   #########

def run_barnsley_fern():
    command = BarnsleyCommand()
    command.execute(root)

def run_bubble_sort():
    command = BubbleSortCommand()
    command.execute(root)


def run_dragon_curve():
    command = DragonCurveCommand()
    command.execute(root)

def run_fractal_tree():
    command = FractalTreeCommand()
    command.execute(root)

def run_hilbert():
    command = HilbertCommand()
    command.execute(root)


def run_honeycomb():
    command = HoneycombCommand()
    command.execute(root)


def run_mandelbrot():
    command = InteractiveMandelbrotCommand()
    command.execute(root)

def run_langtons_loop():
    command = LangtonLoopCommand()
    command.execute(root)

def run_langtons_ant():
    command = LangtonAntCommand()
    command.execute(root)


def run_quasi_crystal():
    command = QuasiCrystalCommand()
    command.execute(root)


def run_rainbow_click():
    command = RainbowClickCommand()
    command.execute(root)


def run_rainbow_rain():
    from miscc import rainbowrain
    root.execfile('rainbowrain.py')


def run_rainbow_rain_circle():
    command = RainbowRainCommand()
    command.execute(root)

def run_random_fractals():
    command = RandomFractalCommand()
    command.execute(root)

def run_siers_triangles():
    command = SierPinskiCommand()
    command.execute(root)


#############################################################
def close_window():
    root.destroy()


def physicsmenu():
    root.withdraw()
    phyroot = Tk()
    phyroot.title("Academedia - Physics Menu")
    phyroot.geometry("600x700")

    Label(phyroot, text="Physics Menu", font="Eurostile 20 bold", padx=200, pady=20).grid()

    b1 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Double Pendulum",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_double_pendulum,
                width=30).grid()

    b2 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Mass Spring Damper",
                bd=12,
                relief="raised",
                command=run_mass_spring_damper,
                font="Calibri 9 bold",
                width=30).grid()

    b3 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Multiple Pendulum",
                bd=12,
                command=run_multiple_pendulum,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b4 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Particle Simulation",
                bd=12,
                command=run_particle_sim,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b5 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Pendulum",
                bd=12,
                command=run_pendulum,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b6 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Projectile",
                bd=12,
                command=run_projectile,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b7 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Solar",
                bd=12,
                command=run_solar,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b8 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Cloth System 1",
                bd=12,
                command=run_verlet_cloth_1,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b9 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Cloth System 2",
                bd=12,
                command=run_verlet_cloth_2,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b10 = Button(phyroot,
                 bg="gray",
                 fg="white",
                 text="Verlet Particle",
                 bd=12,
                 command=run_verlet_particle,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()

    b11 = Button(phyroot,
                 bg="gray",
                 fg="white",
                 text="Verlet Rigid Body Mouse",
                 bd=12,
                 command=run_verlet_rigid_body,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()

    exitb = Button(phyroot,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   command=lambda: [phyroot.destroy(), recall_window()]).grid()


###############################################

def physicsmenu2():
    root.withdraw()
    phyroot2 = Tk()
    phyroot2.title("Academedia - Physics Menu 2")
    phyroot2.geometry("600x700")

    Label(phyroot2, text="Physics Menu", font="Eurostile 20 bold", padx=200, pady=20).grid()

    b1 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Arrows",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_arrow,
                width=30).grid()

    b2 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Balls and Lines",
                bd=12,
                relief="raised",
                command=run_balls_lines,
                font="Calibri 9 bold",
                width=30).grid()

    b3 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Box 2D Vertical Stack",
                bd=12,
                command=run_box2d_verticle,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b4 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Breakout",
                bd=12,
                command=run_breakout,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b5 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Copy & Pickle",
                bd=12,
                command=run_copy_pickle,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b6 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Deformable",
                bd=12,
                command=run_deformable,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b7 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Flipper",
                bd=12,
                command=run_flipper,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    '''
    b8 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Newton's Cradle",
                bd=12,
                command=run_newtons_cradle,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    '''

    b9 = Button(phyroot2,
                bg="gray",
                fg="white",
                text="Playground",
                bd=12,
                command=run_playground,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b10 = Button(phyroot2,
                 bg="gray",
                 fg="white",
                 text="Point Query",
                 bd=12,
                 command=run_point_query,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()

    b11 = Button(phyroot2,
                 bg="gray",
                 fg="white",
                 text="Spiderweb",
                 bd=12,
                 command=run_spiderweb,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()

    exitb = Button(phyroot2,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   command=lambda: [phyroot2.destroy(), recall_window()]).grid()


####################################


####################################

def mathsmenu():
    root.withdraw()
    mathroot = Tk()
    mathroot.title("Academedia - Mathematics Menu")
    mathroot.geometry("600x700")

    Label(mathroot, text="Mathematics Menu", font="Eurostile 20 bold", padx=155, pady=20).grid()

    b1 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Bayesian Regression",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_bayesian_regression,
                width=30).grid()

    b2 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Brownian Motion",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_brownian_motion,
                width=30).grid()

    b3 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Derivatives",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_derivatives,
                width=30).grid()

    b4 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Equation Grapher",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_eq_grapher,
                width=30).grid()

    b5 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Exponential Decay",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_exponential_decay,
                width=30).grid()

    b6 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Fermat's Spiral",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_fermats_spiral,
                width=30).grid()

    b7 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Georgia's Spiral",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_georgias_spiral,
                width=30).grid()

    b8 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Histogram",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_histogram,
                width=30).grid()


    b10 = Button(mathroot,
                 bg="gray",
                 fg="white",
                 text="Newton Iteration",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_newton_iteration,
                 width=30).grid()

    b11 = Button(mathroot,
                 bg="gray",
                 fg="white",
                 text="Riemann Sum",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_riemann_sum,
                 width=30).grid()

    '''

    b12 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Taylor Series",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_taylor_series,
                width=30).grid()
    '''

    exitb = Button(mathroot,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   height=1,
                   command=lambda: [mathroot.destroy(), recall_window()]).grid()
########################################

def mathsmenu2():
    root.withdraw()
    mathroot2 = Tk()
    mathroot2.title("Academedia - Mathematics Menu 2")
    mathroot2.geometry("600x700")

    Label(mathroot2, text="Mathematics Menu 2", font="Eurostile 20 bold", padx=155, pady=20).grid()

    b0 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="3D Plot",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_3D_plot,
                width=30).grid()

    b1 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Area Chart",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_area_chart,
                width=30).grid()

    b2 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Bar Chart",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_bar_chart,
                width=30).grid()

    b3 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Donut Chart",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_donut_plot,
                width=30).grid()

    b4 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Gapminder Animation",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_gapminder_animation,
                width=30).grid()

    b5 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Monte Carlo Integration",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_monte_carlo,
                width=30).grid()

    b6 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Multiple Lines Chart",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_multiple_lines_chart,
                width=30).grid()

    b7 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Scatter Plot",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_scatter_plot,
                width=30).grid()

    b8 = Button(mathroot2,
                bg="gray",
                fg="white",
                text="Taylor Series",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_taylor_series,
                width=30).grid()


    exitb = Button(mathroot2,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   height=1,
                   command=lambda: [mathroot2.destroy(), recall_window()]).grid()


####################################

def chemistrysmenu():
    root.withdraw()
    chemroot = Tk()
    chemroot.title("Academedia - Chemistry Menu")
    chemroot.geometry("600x700")

    Label(chemroot, text="Chemistry menu will be \nimplemented in the future.\n Sorry for the inconvenience.",
          font="Eurostile 20 bold", padx=97, pady=20).grid()


    b1 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 1",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b2 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 2",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b3 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b4 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b5 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b6 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b7 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    exitb = Button(chemroot,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   command=lambda: [chemroot.destroy(), recall_window()]).grid()
    '''
    b11 = Button(chemroot,
                 bg="gray",
                 fg="white",
                 text="Task 3",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()
    b12 = Button(chemroot,
                 bg="gray",
                 fg="white",
                 text="Task 3",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 width=30).grid()

    #####  Scroll bar  ##########

    frame = Frame(chemroot)
    scroll = Scrollbar(frame)
    text = Text(frame, yscrollcommand=scroll.set)
    button = Button(chemroot)
    # Config
    text.insert(END, '\n'.join("ass"))
    scroll.config(command=text.yview)
    button.config(text=('Close'), command=chemroot.destroy)
    button.focus_set()
    # Packing
    text.grid(side='left', fill='both', expand=1)
    scroll.grid(side='right', fill='y')
    frame.grid(fill='both', expand=1)
    button.grid(ipadx=30)
    '''
    ###############################


####################################

def missmenu():
    root.withdraw()
    misroot = Tk()
    misroot.title("Academedia - Miscellaneous Menu")
    misroot.geometry("600x700")

    Label(misroot, text="Miscellaneous Menu", font="Eurostile 20 bold", padx=150, pady=20).grid()

    b1 = Button(misroot,
                bg="gray",
                fg="white",
                text="Barnsley Fern",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_barnsley_fern,
                width=30).grid()

    b2 = Button(misroot,
                bg="gray",
                fg="white",
                text="Bubble Sort",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_bubble_sort,
                width=30).grid()

    b3 = Button(misroot,
                bg="gray",
                fg="white",
                text="Dragon Curve",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_dragon_curve,
                width=30).grid()

    b4 = Button(misroot,
                bg="gray",
                fg="white",
                text="Fractal Tree",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_fractal_tree,
                width=30).grid()
    '''
    b5 = Button(misroot,
                bg="gray",
                fg="white",
                text="Hilbert",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_hilbert,
                width=30).grid()
    '''
    b6 = Button(misroot,
                bg="gray",
                fg="white",
                text="Honeycomb",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_honeycomb,
                width=30).grid()

    b7 = Button(misroot,
                bg="gray",
                fg="white",
                text="Interactive Mandelbrot",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_mandelbrot,
                width=30).grid()

    b8 = Button(misroot,
                bg="gray",
                fg="white",
                text="Langton's Loop",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_langtons_loop,
                width=30).grid()

    b9 = Button(misroot,
                bg="gray",
                fg="white",
                text="Langton's Ant",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_langtons_ant,
                width=30).grid()

    b10 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Quasi Crystal",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_quasi_crystal,
                 width=30).grid()

    b10 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Click",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_click,
                 width=30).grid()

    b11 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Rain",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_rain,
                 width=30).grid()

    '''
    b12 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Rain Circles",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_rain_circle,
                 width=30).grid()
                
    '''
    b13 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Random Fractal Spiral",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_random_fractals,
                 width=30).grid()    
    

    b14 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Sierpinski's Triangles",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_siers_triangles,
                 width=30).grid()

    exitb = Button(misroot,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   command=lambda: [misroot.destroy(), recall_window()]).grid()


def recall_window():
    root.deiconify()


#############################################################


# buttons
button1 = Button(app, text="Physics", bd=12, relief="raised", command=physicsmenu, width=15)
button1.configure(bg="#00008B", fg="white", font="Calibri 9 bold")
button1.grid(padx=1, pady=2)

button1 = Button(app, text="Physics 2", bd=12, relief="raised", command=physicsmenu2, width=15)
button1.configure(bg="#00008B", fg="white", font="Calibri 9 bold")
button1.grid(padx=1, pady=2)


button3 = Button(app, text="Mathematics", bd=12, relief="raised", command=mathsmenu, width=15)
button3.configure(bg="#8B0000", fg="white", font="Calibri 9 bold")
button3.grid(padx=1, pady=2)

button4 = Button(app, text="Mathematics 2", bd=12, relief="raised", command=mathsmenu2, width=15)
button4.configure(bg="#8B0000", fg="white", font="Calibri 9 bold")
button4.grid(padx=1, pady=2)

'''
button5 = Button(app, text="Chemistry", bd=12, relief="raised", command=chemistrysmenu, width=15)
button5.configure(bg="#006400", fg="white", font="Calibri 9 bold")
button5.grid(padx=1, pady=2)
'''

button6 = Button(app, text="Miscellaneous", bd=12, relief="raised", command=missmenu, width=15)
button6.configure(bg="#BDB76B", font="Calibri 9 bold")
button6.grid(padx=1, pady=2)

button7 = Button(app, text="Exit", bd=12, relief="raised", command=sys.exit, width=15)
button7.configure(bg="gray", fg="white", font="Calibri 9 bold")
button7.grid(padx=1, pady=2)

# start event
root.mainloop()
