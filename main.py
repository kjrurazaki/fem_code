from dbm.dumb import error
import fem_1d
from matplotlib import pyplot as plt

def start():
    xcoord, uh, ureal, err = fem_1d.run_1D()
    
    # Plotting the numerical and real solutions
    plt.plot(xcoord, uh, 'or')
    plt.plot(xcoord, ureal(xcoord), 'b')
    plt.show()
    
    print(f'Error of numerical solution:{err}')

if __name__ == "__main__":
    start()