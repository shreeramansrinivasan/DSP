import numpy as np 
import matplotlib.pyplot as plt
import math
import pdb
#NCO - Numerically controlled oscillator 
#Parameters of interest 
# Frequency word - Decides the update rate of the phase accumulator 
# Phase accumulator - Updates the current phase based on the frequency word , B + F bits , 
# B is the address length of the lookup table , F is the fractional bitwidth 
# 
# Lookup table - Typically contains a sinusoid 1 cycle in length , can be addressed by B bits 
#Dac bitwidth is also typically the same as B bits 
class lookup_table:
    def __init__(self,size):
        self.table = [math.sin(2*math.pi*i/size) for i in range(0,size)]
class NCO:
    def __init__(self,lookup_table_size: int ,phase_accumulator_int_bitwidth: int , phase_accumulator_frac_bitwidth: int ,frequency_word_val: int ) -> [None]:
        self.sine_table = lookup_table(lookup_table_size)
        self.frequency_word = frequency_word_val
        self.phase_accumulator_int_bitwidth = phase_accumulator_int_bitwidth
        self.phase_accumulator_frac_bitwidth = phase_accumulator_frac_bitwidth
        self.accum_val = 0
        self.output = 0
    def run_phase_accum(self) -> [None]:
        self.accum_val+=self.frequency_word
        if self.accum_val >= 2**(self.phase_accumulator_frac_bitwidth + self.phase_accumulator_int_bitwidth):
            self.accum_val = self.accum_val%(2**(self.phase_accumulator_frac_bitwidth + self.phase_accumulator_int_bitwidth))
    def lookup_output(self):
        return self.sine_table.table[self.accum_val >> self.phase_accumulator_frac_bitwidth]
    def GenerateOut(self,num_samples: int) -> list:
        self.output = [0 for i in range(0,num_samples)]
        for index in range(0,num_samples):
            self.run_phase_accum()
            self.output[index] = self.lookup_output()







#tests 
frequency_word = 2**20 - 2**14 + 3 # Start with frequency word 1/32  
integer_bitwidth = 16
fractional_bitwidth = 5 # 16.5 phase accumulator bitwidth 
phase_accumulator_bitwidth = integer_bitwidth + fractional_bitwidth
sampling_rate_dac = 1e6 # sampling rate of the dac 
expected_frequency = (frequency_word/(2**(phase_accumulator_bitwidth))) * sampling_rate_dac
num_samples = int(2e6)
lookup_table_size = 2**(integer_bitwidth)
nco_instance = NCO(lookup_table_size,integer_bitwidth,fractional_bitwidth,frequency_word)
nco_instance.GenerateOut(num_samples)
plt.plot(nco_instance.output[0:(65536*2)])
plt.show()
sine_wave_fft = np.fft.fft(nco_instance.output)
sine_wave_fft_abs = np.abs(sine_wave_fft)
breakpoint()
max_frequency_index = np.argmax(sine_wave_fft_abs[0:(num_samples//2)])
plt.plot(20*np.log10(sine_wave_fft_abs))
plt.show()
plt.plot(nco_instance.sine_table.table)
plt.show()
print(len(sine_wave_fft_abs))
print('expected_frequency',expected_frequency)
print('max_frequency_index',max_frequency_index)
print(max_frequency_index*(sampling_rate_dac)/len(sine_wave_fft_abs))
is_within_a_bin_of_right_frequency = bool( abs(max_frequency_index*(sampling_rate_dac)/len(sine_wave_fft_abs)  - expected_frequency) < (sampling_rate_dac/(2**(phase_accumulator_bitwidth))))
print('is_within_a_bin_of_right_frequency' , is_within_a_bin_of_right_frequency)