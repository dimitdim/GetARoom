"""
Data analysis routines
"""
import numpy as np
import pylab as mpl

def load_csv(filename):
    """
    Loads a CSV into an array.
    """
    data=np.genfromtxt(filename,delimiter=",",autostrip=True, dtype=float)
    return [data[:,0],data[:,3]]


def parse_time(time):
    """
    Converts the time vector to be all in seconds.
    """
    out=np.zeros(len(time))
    for t in range(len(time)):
        time_now=time[t].rsplit('_')
        h=int(time_now[0])
        m=int(time_now[1])
        s=int(time_now[2])
        out[t]=s+60*m+3600*h
    return out

def parse_vals(vals):
    """
    Smooths missing values.
    """
    for v in range(len(vals)):
        if vals[v]==-1:
            vals[v]=vals[v-1]
    return vals
        
    
    
def analyze_light(data):
    """
    Looks at light sensor data and guesses if the light is either on or off.
    Returns an equal length data set that maps each value to true or false.
    Process:
    Determine state at T=0 (lights on?  Lights off?)
    Numerically differentiate dataset while tracking state.  Store min/max values.
    Determine a threshold as slightly less than the slope of the line going from min to max in one time step, but more than
    the light value change by sunrise alone.
    If the numerical derivative value is over a certain threshold, flag a state change.
    Return a dataset that lists the state as a function of time.
    This routine should optimally be self calibrating.
    """
    light_state=np.zeros(len(data))
    grad1=abs(np.gradient(data)) #Careful on units, this is not taken with respect to another variable.
    max_deriv=np.amax(grad1)
    max_val=np.amax(data)
    threshold=max_deriv/2
    
    state=data[0]>0.5*max_val
    
    for k in range(len(grad1)-1):
        light_state[k]=100*int(state)
        if grad1[k]>threshold:
            state= (abs(data[k]-max_val)<data[k])
    #print(grad1)
    #grad1=np.convolve(np.array([1,-1,1,-1,1,-1,1,-1,1,-1]),grad1)
    return [grad1,light_state]
        
if __name__=='__main__':
    a=load_csv('140417060703.csv')
    g=analyze_light(parse_vals(a[1]))
    mpl.plot(a[0],a[1],label='Raw Data')
    mpl.plot(a[0],g[0],label='1st derivative')
    mpl.plot(a[0],g[1],label='Light State')
    mpl.legend(loc='upper right')
    mpl.show()
