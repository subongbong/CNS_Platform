import threading
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class gfunction(threading.Thread):
    def __init__(self, UDP):
        threading.Thread.__init__(self)
        self.UDP_data = UDP

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(2, 1, 1)

        self.ani = FuncAnimation(self.fig, self.animate, interval=1000)

    def animate(self, i):
        self.ax1.clear()
        self.ax1.plot(self.UDP_data.list_mem['CNS_time']['Val'], self.UDP_data.list_mem['QPROLD']['Val'],
                      label='Result', linewidth=1)

    def run(self):
        print(self.name, 'gfunction start')

