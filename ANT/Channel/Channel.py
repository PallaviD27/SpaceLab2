# Baseband Channel
# d=simulate_channel(x,tx_power,switch_graph)  # API defintion 3.5.2

import numpy as np
import matplotlib.pyplot as plt

# Input parameters given in the task
np.set_printoptions(suppress=True, precision=8)
distance = 36000000    # Height of GEO satellites above the surface of the earth in m
CarrierFreq = 20000000000   # Carrier frequency of 20 GHz
LightSpeed = 300000000  # Speed of light in m/s
Ga = 40    # Transmitter antenna gain in dBi
Gb = 40       # Receiver antenna gain in dBi
TN= 165       # Noise temperature in K
BW = 800000000    # Bandwidth in Hz
kB = 1.38e-23    # Boltzmann constant in W/Hz K


# Calculate Path Loss in dB and in W
PathLoss_dB = (20 * np.log10 ((4 * np.pi * distance * CarrierFreq )/LightSpeed)) - (Ga + Gb)
PathLoss_linear  =  10 ** (PathLoss_dB/10)
print(f'\033[32m\033[1mPath loss:\033[0m\033[0m {PathLoss_dB} dB')
print(f'\033[32m\033[1mLinear path loss:\033[0m\033[0m {PathLoss_linear} W')

# Calculate Noise Power in W and dB
Noise_power = (kB * TN * BW)   # Noise power for bandwidth is Power spectral density * bandwidth. Power spectral density = (kB * TN )/2
Noise_power_dB = (10 * np.log10(Noise_power))
print(f'\033[32m\033[1mNoise Power:\033[0m\033[0m {Noise_power_dB} dB')

def transmitter_power():
    ''''
    Generates transmitter power (in W) based on transmitter power (in dB) calculated using different SNR values,
    path loss and noise power.
    Returns:
        trans_power_linear (np.array): linear transmitter powers for different SNR values
    '''

# Calculate transmitter power for SNR belonging to [-5dB,30dB] at receiver
    SNR_dB=np.arange(-5,35,5)
    print(f'SNR values: {SNR_dB}')
    trans_power_dB = SNR_dB + PathLoss_dB + Noise_power_dB
    trans_power_linear = 10 ** (trans_power_dB/10)
    print(f'\033[32m\033[1mTransmitter Power:\033[0m\033[0m {trans_power_dB} dB ')
    print(f'\033[32m\033[1m Linear Transmitter Power:\033[0m\033[0m {trans_power_linear} ')
    return trans_power_linear
def simulate_channel(x,tx_power,switch_graph):
    '''
    Simulates channel i.e. introduces path loss and Additive White Gaussian Noise
    Parameters:
        x (np.array) : Filtered signal after transmitter filter
        tx_power: Linear Transmitter power
        switch_graph: ON/on to generate the scatter diagram of channel output at different SNRs and OFF/off otherwise

    Returns:
        y (np.array): Output of channel after adding white gaussian noise to amplified filtered signal
        SNR: SNR used for calculating the transmitter powers
    '''
# Generate White Gaussian Noise
    Noise_std_dev = np.sqrt(Noise_power / 2)
    print(f'\033[32m\033[1mStandard deviation of noise:\033[0m\033[0m {Noise_std_dev}')
    Noise_real = np.random.normal(loc=0, scale=Noise_std_dev, size=len(x)) / np.sqrt(2)
    Noise_imag = np.random.normal(loc=0, scale=Noise_std_dev, size=len(x)) / np.sqrt(2)
    WGN = np.column_stack(Noise_real + 1j * Noise_imag)
    print(f'\033[32m\033[1mWhite Gaussian Noise:\033[0m\033[0m {WGN}')

# Plot channel output for different SNRs
    np.set_printoptions(suppress=True, precision=6)
    SNR_dB = np.arange(-5, 35, 5)
    trans_power_linear=transmitter_power()
    for power, snr in zip(trans_power_linear, SNR_dB):

# Generate Channel output by adding White Gaussian Noise to amplified signal
        amplified_x_at_Powerpower = x * np.sqrt(power) # Signal amplification is proportional to square root of power
        print(f'\033[32m\033[1mAmplified input at transmitter power = {power} W:\033[0m\033[0m {amplified_x_at_Powerpower}')
        y = amplified_x_at_Powerpower + WGN
        print (f'\033[32m\033[1mChannel Output at Power = {power } W:\033[0m\033[0m {y}')
        if switch_graph.upper()=='ON':
            plt.figure(figsize=(6, 6))
            plt.scatter(np.real(y), np.imag(y), color='r',label=f'SNR = {snr} dB\nTx Power = {power:.2e} W', alpha=0.7)
            plt.title('Channel Output (with Noise)', fontweight='bold')
            plt.xlabel('In-phase', fontweight='bold')
            plt.ylabel('Quadrature-phase', fontweight ='bold')
            plt.grid(True)
            plt.legend()

        else:
            pass

    return y,SNR_dB

