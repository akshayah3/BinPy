
# coding: utf-8

# Example for N Bit Binary Down Counter.

# In[1]:

# imports
from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import NBitDownCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope


# In[2]:

# Initialize a toggle connectr for inpput in TFlipFlop

toggle = Connector(1)

# Initializing the Clock
# A clock of 10 hertz frequency

clock = Clock(1, 10)
clock.start()

clk_conn = clock.A


# In[3]:

# Initialize enable

enable = Connector(1)


# In[4]:

# Setting No of Bits to 4

# Initializing Down Counter with 4 bits and clock_conn

b = NBitDownCounter(4, clk_conn)


# In[5]:

# Initiating the oscilloscope

# starting the oscillioscope

# setting the scale

o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))

o.start()

o.setScale(0.035)  # Set scale by trial and error.

# Set the width of the oscilloscope
o.setWidth(100)

o.unhold()


# In[6]:

# Initial State

print (b.state())


# In[7]:

# Triggering the counter sequentially 2^4 + 2 times

for i in range(1, 2 ** 4 + 2):
    b.trigger()
    print (b.state())

o.display()


# In[8]:

# Calling the instance will trigger

b()

print(b.state())


# In[9]:

# Setting the Counter

b.setCounter()

print(b.state())


# In[10]:

# Resetting the Counter

b.resetCounter()

print(b.state())


# In[11]:

# Disabling the Counter

b.disable()
b.trigger()

print(b.state())


# In[12]:

# Enabling the Counter

b.enable()
b.trigger()

print(b.state())


# In[13]:

# Kill the clock and the oscilloscope thread after use

o.kill()

clock.kill()
