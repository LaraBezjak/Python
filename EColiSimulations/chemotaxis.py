#Rather, research has shown that it follows a normal distribution with mean of 68° (1.19 radians) and standard deviation of 36° (0.63 radians)


import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import colors
from matplotlib import patches
import colorspace

SEED = 128  #Any random seed
np.random.seed(SEED)

#Constants for E.coli tumbling
tumble_time_mu = 0.1

#E.coli movement constants
speed = 20         #um/s, speed of E.coli movement
sec_per_step = 0.5 #Able to respond every 0.5 second
response_time = 0.5 #Able to respond every 0.5 second

#Model constants
start = [0, 0]  #All cells start at [0, 0]
ligand_center = [1500, 1500] #Position of highest concentration
center_exponent, start_exponent = 8, 2
origin_to_center = 0 #Distance from start to center, intialized here, will be actually calculated later
saturation_conc = 10 ** 8 #From BNG model

# Calculates Euclidean distance between point a and b
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Exponential gradient, the exponent follows a linear relationship with distance to center
def calc_concentration(pos):
    dist = euclidean_distance(pos, ligand_center)
    exponent = (1 - dist / origin_to_center) * (center_exponent - start_exponent) + start_exponent
    
    return 10 ** exponent

# Calculate the wait time for next tumbling event
def run_duration(curr_conc, past_conc, position, run_time_expected):
        
    curr_conc = min(curr_conc, saturation_conc) #Can't detect higher concentration if receptors saturates
    past_conc = min(past_conc, saturation_conc)
    change = (curr_conc - past_conc) / past_conc #proportion change in concentration, float
    run_time_expected_adj_conc = run_time_expected * (1 + 10 * change) #adjust based on concentration change, float
    
    if run_time_expected_adj_conc < 0.000001:
        run_time_expected_adj_conc = 0.000001 #positive wait times
    elif run_time_expected_adj_conc > 4 * run_time_expected:
        run_time_expected_adj_conc = 4 * run_time_expected     #the decrease to tumbling frequency is only to a certain extent
    #Sample the duration of current run from exponential distribution, mean=run_time_expected_adj_conc
    curr_run_time = np.random.exponential(run_time_expected_adj_conc)
    
    return curr_run_time

# Horizontal and Vertical movement of tumbling
def tumble_move():
    #Sample the new direction unformly from 0 to 2pi, record as a float
    new_dir = np.random.uniform(low = 0.0, high = 2 * math.pi)
        
    projection_h = math.cos(new_dir) #displacement projected on Horizontal direction for next run, float
    projection_v = math.sin(new_dir) #displacement projected on Vertical direction for next run, float
    
    #Length of the tumbling sampled from exponential distribution with mean=0.1, float
    tumble_time = np.random.exponential(tumble_time_mu)
    
    return projection_h, projection_v, tumble_time

# This function performs simulation
# Input: number of cells to simulate (int), how many seconds (int), the expected run time before tumble (float)
# Return: the simulated trajectories paths: array of shape (num_cells, duration+1, 2)
def simulate_chemotaxis(num_cells, duration, run_time_expected):
    
    #Takes the shape (num_cells, duration+1, 2)
    #any point [x,y] on the simulated trajectories can be accessed via paths[cell, time]
    paths = np.zeros((num_cells, duration + 1, 2))

    for rep in range(num_cells):
        # Initialize simulation
        t = 0 #record the time elapse
        curr_position = np.array(start) #start at [0, 0]
        past_conc = calc_concentration(start) #Initialize concentration
        projection_h, projection_v, tumble_time = tumble_move() #Initialize direction randomly

        while t < duration:
            curr_conc = calc_concentration(curr_position)

            curr_run_time = run_duration(curr_conc, past_conc, curr_position, run_time_expected) #get run duration, float

            # if run time (r) is within the step (s), run for r second and then tumble
            if curr_run_time < response_time: 
                #displacement on either direction is calculated as the projection * speed * time
                #update current position by summing old position and displacement
                curr_position = curr_position + np.array([projection_h, projection_v]) * speed * curr_run_time
                projection_h, projection_v, tumble_time = tumble_move() #tumble
                t += (curr_run_time + tumble_time) #increment time

            # if r > s, run for r; then it will be in the next iteration
            else:
                #displacement on either direction is calculated as the projection * speed * time
                #update current position by summing old position and displacement
                curr_position = curr_position + np.array([projection_h, projection_v]) * speed * response_time
                t += response_time #no tumble here

            #record position approximate for integer number of second
            curr_sec = int(t)
            if curr_sec <= duration:
                #fill values from last time point to current time point
                paths[rep, curr_sec] = curr_position.copy()
                past_conc = curr_conc
    
    return paths

###             2 Visualizing trajectories
#Run simulation for 3 cells with different background tumbling frequencies, Plot paths

duration = 800   #seconds, duration of the simulation
num_cells = 3
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant
run_time_expected_all = [0.2, 1.0, 5.0]
paths = np.zeros((len(run_time_expected_all), num_cells, duration + 1, 2))
                
for i in range(len(run_time_expected_all)):
    run_time_expected = run_time_expected_all[i]
    paths[i] = simulate_chemotaxis(num_cells, duration, run_time_expected)

conc_matrix = np.zeros((3500, 3500))
for i in range(3500):
    for j in range(3500):
        conc_matrix[i][j] = math.log(calc_concentration([i - 500, j - 500]))

mycolor = [[256, 256, 256], [256, 255, 254], [256, 253, 250], [256, 250, 240], [255, 236, 209], [255, 218, 185], [251, 196, 171], [248, 173, 157], [244, 151, 142], [240, 128, 128]] #from coolors：）
for i in mycolor:
    for j in range(len(i)):
        i[j] *= (1/256)
cmap_color = colors.LinearSegmentedColormap.from_list('my_list', mycolor)


for freq_i in range(len(run_time_expected_all)):
    fig, ax = plt.subplots(1, figsize = (8, 8))
    ax.imshow(conc_matrix.T, cmap=cmap_color, interpolation='nearest', extent = [-500, 3000, -500, 3000], origin = 'lower')

    #Plot simulation results
    time_frac = 1.0 / duration
    #Time progress: dark -> colorful
    for t in range(duration):
        ax.plot(paths[freq_i,0,t,0], paths[freq_i,0,t,1], 'o', markersize = 1, color = (0.2 * time_frac * t, 0.85 * time_frac * t, 0.8 * time_frac * t))
        ax.plot(paths[freq_i,1,t,0], paths[freq_i,1,t,1], 'o', markersize = 1, color = (0.85 * time_frac * t, 0.2 * time_frac * t, 0.9 * time_frac * t))
        ax.plot(paths[freq_i,2,t,0], paths[freq_i,2,t,1], 'o', markersize = 1, color = (0.4 * time_frac * t, 0.85 * time_frac * t, 0.1 * time_frac * t))
    ax.plot(start[0], start[1], 'ko', markersize = 8)
    ax.plot(1500, 1500, 'bX', markersize = 8)
    for i in range(num_cells):
        ax.plot(paths[freq_i,i,-1,0], paths[freq_i,i,-1,1], 'ro', markersize = 8)

    ax.set_title("Background tumbling freq:\n tumble every {} s".format(run_time_expected_all[freq_i]), x = 0.5, y = 0.9, fontsize = 12)
    ax.set_xlim(-500, 3000)
    ax.set_ylim(-500, 3000)
    ax.set_xlabel("poisiton in μm")
    ax.set_ylabel("poisiton in μm")
    
plt.show()


###more 
#Run simulation for 3 cells with different background tumbling frequencies, Plot paths

duration = 800   #seconds, duration of the simulation
num_cells = 3
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant
run_time_expected_all = [0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]


paths = np.zeros((len(run_time_expected_all), num_cells, duration + 1, 2))
                
for i in range(len(run_time_expected_all)):
    run_time_expected = run_time_expected_all[i]
    paths[i] = simulate_chemotaxis(num_cells, duration, run_time_expected)


num_fig_row = round(len(run_time_expected_all) / 2.0)
fig, ax = plt.subplots(num_fig_row, 2, figsize = (16, 24))

#First set color map
mycolor = [[256, 256, 256], [256, 255, 254], [256, 253, 250], [256, 250, 240], [255, 236, 209], [255, 218, 185], [251, 196, 171], [248, 173, 157], [244, 151, 142], [240, 128, 128]] #from coolors：）
for i in mycolor:
    for j in range(len(i)):
        i[j] *= (1/256)
cmap_color = colors.LinearSegmentedColormap.from_list('my_list', mycolor)

for freq_i in range(len(run_time_expected_all)):
    index1, index2 = freq_i // 2, freq_i % 2
    xlen = max(paths[freq_i,:,:,0].flatten()) - min(paths[freq_i,:,:,0].flatten())
    ylen = max(paths[freq_i,:,:,1].flatten()) - min(paths[freq_i,:,:,1].flatten())
    sqrlen = int(round(max(xlen, ylen), 0))
    xlim_l, xlim_h = min(paths[freq_i,:,:,0].flatten()), min(paths[freq_i,:,:,0].flatten()) + sqrlen
    ylim_l, ylim_h = min(paths[freq_i,:,:,1].flatten()), min(paths[freq_i,:,:,1].flatten()) + sqrlen


    #Simulate the gradient distribution, plot as a heatmap
    conc_matrix = np.zeros((sqrlen, sqrlen))
    for i in range(sqrlen):
        for j in range(sqrlen):
            conc_matrix[i][j] = calc_concentration([i + xlim_l, j + ylim_l])
    conc_matrix = np.log(conc_matrix)
    ax[index1][index2].imshow(conc_matrix.T, cmap=cmap_color, interpolation='nearest', extent = [xlim_l, xlim_h, ylim_l, ylim_h], origin = 'lower')

    #Plot simulation results
    time_frac = 1.0 / duration
    #Time progress: dark -> colorful
    for t in range(duration):
        ax[index1][index2].plot(paths[freq_i,0,t,0], paths[freq_i,0,t,1], 'o', markersize = 1, color = (0.2 * time_frac * t, 0.85 * time_frac * t, 0.8 * time_frac * t))
        ax[index1][index2].plot(paths[freq_i,1,t,0], paths[freq_i,1,t,1], 'o', markersize = 1, color = (0.85 * time_frac * t, 0.2 * time_frac * t, 0.9 * time_frac * t))
        ax[index1][index2].plot(paths[freq_i,2,t,0], paths[freq_i,2,t,1], 'o', markersize = 1, color = (0.4 * time_frac * t, 0.85 * time_frac * t, 0.1 * time_frac * t))
    ax[index1][index2].plot(start[0], start[1], 'ko', markersize = 8)
    for i in range(num_cells):
        ax[index1][index2].plot(paths[freq_i,i,-1,0], paths[freq_i,i,-1,1], 'ro', markersize = 8)

    #Indicate the saturation areas
    circle1 = plt.Circle((ligand_center[0], ligand_center[0]), radius_saturation, fill = False, ec = "black", ls = '--')
    ax[index1][index2].set_title("Background: avg tumble every {} s".format(run_time_expected_all[freq_i]), x = 0.5, y = 0.9)
    ax[index1][index2].add_artist(circle1)
    ax[index1][index2].set_xlim(xlim_l, xlim_h)
    ax[index1][index2].set_ylim(ylim_l, ylim_h)
    ax[index1][index2].set_xlabel("poisiton in um")
    ax[index1][index2].set_ylabel("poisiton in um")

if len(time_exp) % 2 != 0:
    fig.delaxes(ax[num_fig_row - 1, 1]) #delete the last figure if odd number of subplots
fig.tight_layout()

plt.show()

###      3 Comparing performances
#Run simulation for 500 cells with different background tumbling frequencies, Plot average distance to highest concentration point
duration = 1500   #seconds, duration of the simulation
#num_cells = 500
num_cells = 300
run_time_expected_all = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant

all_distance = np.zeros((len(time_exp), num_cells, duration)) #Initialize to store results

paths = np.zeros((len(run_time_expected_all), num_cells, duration + 1, 2))
                
for i in range(len(run_time_expected_all)):
    run_time_expected = run_time_expected_all[i]
    paths[i] = simulate_chemotaxis(num_cells, duration, run_time_expected)

for freq_i in range(len(run_time_expected_all)):
    for c in range(num_cells):
        for t in range(duration):
            pos = paths[freq_i, c, t]
            dist = euclidean_distance(ligand_center, pos)
            all_distance[freq_i, c, t] = dist

all_dist_avg = np.mean(all_distance, axis = 1)
all_dist_std = np.std(all_distance, axis = 1)
print(all_dist_avg[0][-10:])

#Below are all for plotting purposes
#Define the colors to use
colors1 = colorspace.qualitative_hcl(h=[0, 300.], c = 60, l = 70, pallete = "dynamic")(len(time_exp))

xs = np.arange(0, duration)

fig, ax = plt.subplots(1, figsize = (10, 8))

for freq_i in range(len(time_exp)):
    mu, sig = all_dist_avg[freq_i], all_dist_std[freq_i]
    ax.plot(xs, mu, lw=2, label="tumble every {} second".format(run_time_expected_all[freq_i]), color=colors1[freq_i])
    ax.fill_between(xs, mu + sig, mu - sig, color = colors1[freq_i], alpha=0.1)

ax.set_title("Average distance to highest concentration")
ax.set_xlabel('time (s)')
ax.set_ylabel('distance to center (µm)')
ax.legend(loc='lower left', ncol = 1)

ax.grid()




