SDE exercise specification
2026-07-18

# Description



## class bm

Manage Brownian motions, which is the source of randomness in the system.

### Property

|name|type|default|description|
|:---|:---|:---|:---|
|eot|float|1|The end of time point|
|nos|int|10|Number of time steps|
|time|float(nos)|-|linspaced time from 0 to eot|
|nop|int|1|Number of paths|
|dps|np.ndarray(nop,nos)|-|difference of sample paths|
|ps|np.ndarray(nop,nos)|-|sample paths|

### Method

|name|return|arg|description|
|:---|:---|:---|:---|
|init|-|eot, nos, nop|set time, dps, ps arccordingly|

## func plot_ps

plot sample paths, mean and std path
show or save the graph
make sure to label the conditions in the graph

|name|type|default|description|
|:---|:---|:---|:---|
|return|list|-|\[mean, std\]
|ps|np.ndarray(nop,nos)|-|sample paths to be pllotted|
|time|float(nos)|-|time frindged to the sample paths|
|filename|str|None|if None show() else savefig()|

## func sdeint

Generate sample paths by Euler-Maruyama method

### return and arg

|name|type|default|description|
|:---|:---|:---|:---|
|return|np.ndarray(nop,nos)|-|generated sample paths|
|mu|func(x, t)|-|drift|
|si|func(x, t)|-|diffusion|
|y0|np.ndarray(nop)|zeros|initial value|
|sp|class bm|-|source of stochastic process like Brownian Motion|

## est

estimate drift and diffusion parameter in each division

### return and arg

|name|type|default|description|
|:---|:---|:---|:---|
|return|list|-| \[ mu\[nsd, ntd\], si\[nsd, ntd\] \]|
|ps|np.ndarray\[nop,nos\]|-|sample paths|
|time|float\[nos\]|-|time frindged to the sample paths|
|t_div|np.ndarray\[ntd\]|-|provide time division|
|s_div|np.ndarray\[nsd\]|-|provide space division|

# Memo
- how to prohibit reassignment of bm
- file division improvement
- all should process have class instance?
- sdeint is a method of source process?
- venv dependencies should be provised. it has some unused packages