from tkinter import *
from tkinter import messagebox

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
    command = DoublePendulumCommand(root)
    command.execute()


def run_mass_spring_damper():
    command = MasSpringDamperCommand(root)
    command.execute()


def run_multiple_pendulum():
    command = MultiplePendulumCommand(root)
    command.execute()


def run_particle_sim():
    command = ParticleSimCommand(root)
    command.execute()


def run_pendulum():
    command = PendulumCommand(root)
    command.execute()


def run_projectile():
    command = ProjectileCommand(root)
    command.execute()


def run_solar():
    command = SolarCommand(root)
    command.execute()


def run_verlet_cloth_1():
    command = ClothMouse1Command(root)
    command.execute()


def run_verlet_cloth_2():
    command = ClothMouse2Command(root)
    command.execute()


def run_verlet_particle():
    command = VerletParticleCommand(root)
    command.execute()


def run_verlet_rigid_body():
    command = VerletRigidBodyCommand(root)
    command.execute()


########   Physics 2 Functions   #########

def run_arrow():
    command = ArrowsCommand(root)
    command.execute()


def run_balls_lines():
    command = BallsandLinesCommand(root)
    command.execute()


def run_box2d_verticle():
    command = Box2DCommand(root)
    command.execute()


def run_breakout():
    command = BreakoutCommand(root)
    command.execute()


def run_copy_pickle():
    command = CopyPickleCommand(root)
    command.execute()


def run_flipper():
    command = FlipperCommand(root)
    command.execute()


def run_deformable():
    command = DeformableCommand(root)
    command.execute()


def run_playground():
    command = PlaygroundCommand(root)
    command.execute()


def run_point_query():
    command = PointQueryCommand(root)
    command.execute()


def run_spiderweb():
    command = SpiderwebCommand(root)
    command.execute()


########   Math Functions   #########
def run_bayesian_regression():
    command = BayesianRegressionCommand(root)
    command.execute()


def run_brownian_motion():
    command = BrownianMotionCommand(root)
    command.execute()


def run_derivatives():
    command = DerivativesCommand(root)
    command.execute()


def run_eq_grapher():
    command = EqGrapherCommand(root)
    command.execute()


def run_exponential_decay():
    command = ExpDecayCommand(root)
    command.execute()


def run_fermats_spiral():
    command = FermatsSpiralCommand(root)
    command.execute()


def run_georgias_spiral():
    command = GeorgiasSpiralCommand(root)
    command.execute()


def run_histogram():
    command = HistogramComand(root)
    command.execute()


def run_newton_iteration():
    command = NewtonIterationCommand(root)
    command.execute()


def run_riemann_sum():
    command = RiemannSumCommand(root)
    command.execute()


########## Math 2 Functions #########

def run_3D_plot():
    command = Plot3DCommand(root)
    command.execute()


def run_area_chart():
    command = AreaChartCommand(root)
    command.execute()


def run_bar_chart():
    command = BarChartCommand(root)
    command.execute()


def run_donut_plot():
    command = DonutPlotCommand(root)
    command.execute()


def run_gapminder_animation():
    command = GapminderCommand(root)
    command.execute()


def run_monte_carlo():
    command = MonteCarloCommand(root)
    command.execute()


def run_multiple_lines_chart():
    command = MultipleLinesCommand(root)
    command.execute()


def run_scatter_plot():
    command = ScatterPlotCommand(root)
    command.execute()


def run_taylor_series():
    command = TaylorCommand(root)
    command.execute()


#######################################


########   Misc Functions   #########

def run_barnsley_fern():
    command = BarnsleyCommand(root)
    command.execute()


def run_bubble_sort():
    command = BubbleSortCommand(root)
    command.execute()


def run_fractal_tree():
    command = FractalTreeCommand(root)
    command.execute()


def run_honeycomb():
    command = HoneycombCommand(root)
    command.execute()


def run_mandelbrot():
    command = InteractiveMandelbrotCommand(root)
    command.execute()


def run_langtons_ant():
    command = LangtonAntCommand(root)
    command.execute()


def run_quasi_crystal():
    command = QuasiCrystalCommand(root)
    command.execute()


def run_rainbow_click():
    command = RainbowClickCommand(root)
    command.execute()


def run_rainbow_rain():
    from miscc import rainbowrain
    root.execfile('rainbowrain.py')


def run_rainbow_rain_circle():
    command = RainbowRainCommand(root)
    command.execute()


def run_random_fractals():
    command = RandomFractalCommand(root)
    command.execute()


def run_siers_triangles():
    command = SierPinskiCommand(root)
    command.execute()


#############################################################
def close_window():
    root.destroy()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        sys.exit()


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

    phyroot.protocol("WM_DELETE_WINDOW", on_closing)


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

    phyroot2.protocol("WM_DELETE_WINDOW", on_closing)


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
                command=lambda: [run_bayesian_regression()],
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

    mathroot.protocol("WM_DELETE_WINDOW", on_closing)


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

    mathroot2.protocol("WM_DELETE_WINDOW", on_closing)


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

    b4 = Button(misroot,
                bg="gray",
                fg="white",
                text="Fractal Tree",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_fractal_tree,
                width=30).grid()

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

    misroot.protocol("WM_DELETE_WINDOW", on_closing)


def recall_window():
    root.deiconify()


def destroyer():
    root.quit()
    root.destroy()


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

button6 = Button(app, text="Miscellaneous", bd=12, relief="raised", command=missmenu, width=15)
button6.configure(bg="#BDB76B", font="Calibri 9 bold")
button6.grid(padx=1, pady=2)

button7 = Button(app, text="Exit", bd=12, relief="raised", command=sys.exit, width=15)
button7.configure(bg="gray", fg="white", font="Calibri 9 bold")
button7.grid(padx=1, pady=2)

# start event
root.mainloop()
