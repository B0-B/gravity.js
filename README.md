# gravity.js
A playground web engine for gravity/physics simulations and rendering.


# Optimization

## Square Root Method
The benchmark is performed by monitoring the exponentially smoothed average of the iteration time until it stablizes around a value, the highest occurense per period was denoted. The denotation error lies within $1ms$.  

|Particles|Math.sqrt (ms)| **.5 (ms) | Math.Pow (ms) |
|---|---|---|---|
|1000|388|280|276|
|2000|1200|785|810|
|4000|2600|2600|2550|