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
|time|float(nos+1)|-|linspaced time from 0 to eot|
|nop|int|1|Number of paths|
|dps|np.ndarray(nop,nos+1)|-|difference of sample paths|
|ps|np.ndarray(nop,nos+1)|-|sample paths|

### Method

|name|return|arg|description|
|:---|:---|:---|:---|
|init|-|eot, nos, nop|set time, dps, ps accordingly|

## func plot_ps

plot sample paths, mean and std path
show or save the graph
make sure to label the conditions in the graph

|name|type|default|description|
|:---|:---|:---|:---|
|return|list|-|\[mean, std\]
|ps|np.ndarray(nop,nos+1)|-|sample paths to be pllotted|
|time|float(nos+1)|-|time frindged to the sample paths|
|filename|str|None|if None show() else savefig()|

## func sdeint

Generate sample paths by Euler-Maruyama method

### return and arg

|name|type|default|description|
|:---|:---|:---|:---|
|return|np.ndarray(nop,nos+1)|-|generated sample paths|
|sp|class bm|-|source of stochastic process like Brownian Motion|
|mu|func(x, t)|-|drift|
|si|func(x, t)|-|diffusion|
|y0|np.ndarray(nop)|zeros|initial value is as of yet set since nop is not allowed to access|

## func est

estimate drift and diffusion parameter in each division

### return and arg

|name|type|default|description|
|:---|:---|:---|:---|
|return|list|-| \[ mu\[nsd, ntd\], si\[nsd, ntd\] \]|
|ps|np.ndarray\[nop,nos+1\]|-|sample paths|
|time|float\[nos+1\]|-|time associated with the sample paths|
|t_div|np.ndarray\[ntd+1\]|-|provide time division, must be a subset of time and shares start and end point|
|s_div|np.ndarray\[nsd+1\]|-|provide space division. the start and end points are -inf and inf|


## plot_det_mu and plot_det_si

|name|type|default|description|
|:---|:---|:---|:---|
|mu|||
|t_div|||

## plot_auto_mu and plot_auto_si

|name|type|default|description|
|:---|:---|:---|:---|
|si|||
|s_div|||

## plot_est

|name|type|default|description|
|:---|:---|:---|:---|
|si|||
|mu|||
|t_div|||
|s_div|||

# Memo
- how to prohibit reassignment of bm
- file division improvement
- all should process have class instance?
- sdeint is a method of source process?
- venv dependencies should be provised. it has some unused packages