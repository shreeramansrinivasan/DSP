During my work with some function generators, I stumbled onto Numerically controlled oscillators - NCOs.
The idea is pretty neat and is explored more in these two beautiful blogposts - https://john-gentile.com/kb/dsp/NCO_DDS.html
and https://blog.thelonepole.com/2011/7/numerically-controlled-oscillators
I remember hearing about them during undergrad and then dint turn up under my purview until I recently had to fiddle a arb generator for arbitrary waveform synthesis. 
A short overview is that NCOs are used to generate arbitrary sinusoidal frequencies  (with some constraints) based on a lookup table. 
One can think of the lookup table as containing a single cycle sinusoid. The lookup table is typically indexed using a phase word , which is computed every clock cycle from a frequency word. 
For every clock: 
    Phase_word = Phase_word + frequency_word 
This phase_word, post some truncation and saturation, indexes the lookup table. The output of the lookup table is the output value of that particular clock. 
The block diagram looks like this :

