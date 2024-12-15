# Baseband Channel
# d=simulate_channel(x,tx_power,switch_graph)  # API defintion 3.5.2

import numpy as np
import matplotlib.pyplot as plt

# Input parameters that are given
np.set_printoptions(suppress=True, precision=4)
distance = 36000000    # Height of GEO satellites above the surface of the earth in m
CarrierFreq = 20000000000   # Carrier frequency of 20 GHz
LightSpeed = 300000000  # Speed of light in m/s
Ga = 40    # Transmitter antenna gain in dBi
Gb = 40       # Receiver antenna gain in dBi
TN= 165       # Noise temperature in K
BW = 800000000    # Bandwidth in Hz
kB = 1.38e-23    # Boltzmann constant in W/Hz K


# Calculate Path Loss in dB
PathLoss = (20 * np.log10 ((4 * np.pi * distance * CarrierFreq )/LightSpeed)) - (Ga + Gb)
PathLoss_linear  =  10 ** (-PathLoss/10)

print(f'\033[32m\033[1mPath loss:\033[0m\033[0m {PathLoss} dB')
print(f'\033[32m\033[1mLinear path loss:\033[0m\033[0m {PathLoss_linear}')

# Calculate Noise Power
Noise_power = (kB * TN * BW)   # Noise power for bandwidth is Power spectral density * bandwidth. Power spectral density = (kB * TN )/2
print(f'\033[32m\033[1mNoise Power:\033[0m\033[0m {Noise_power}')

def transmitter_power():
    ''''
    A channel is constituted of transmitter amplifier, path loss, additive whote gaussian noise and receiver amplifier
    Transmitter amplifier - amplifies the transmitted signal
    Path Loss -
    Receiver amplifier - amplifies received signal. GRX =1

    Path loss =

    Aim is to achieve a desired SNR
    '''
# Calculate transmitter power for SNR = 20 dB at receiver
    trans_power = (Noise_power * (10**2) )/PathLoss_linear
    print(f'\033[32m\033[1mTransmitter Power:\033[0m\033[0m {trans_power} ')
    return 10.0
def simulate_channel(x,tx_power,switch_graph):
    np.set_printoptions(suppress=True, precision=6)
    amplified_x = x * tx_power
    print(f'\033[32m\033[1mAmplified input:\033[0m\033[0m {amplified_x}')
# Calculate attenuated signal by multiplying with path loss factor
    att_sig = amplified_x * np.sqrt (PathLoss_linear)
    print(f'\033[32m\033[1mAttenuated input after path losses:\033[0m\033[0m {att_sig}')
    # Complex_att_sig = att_sig[:,0] + 1j*att_sig[:,1]
    # print(f'Complex attenuated signal:{Complex_att_sig}')
    Noise_std_dev= np.sqrt(Noise_power/2)
    print(f'\033[32m\033[1mStandard deviation of noise:\033[0m\033[0m {Noise_std_dev}')
    Random_Noise = np.random.randn(len(x))
    print(f'\033[32m\033[1mRandom generated noise:\033[0m\033[0m {Random_Noise}')
    Noise_real= Noise_std_dev * np.random.randn(len(x))
    Noise_imag = Noise_std_dev * np.random.randn(len(x))
    WGN = np.column_stack(Noise_real + 1j * Noise_imag)
    print(f'\033[32m\033[1mWhite Gaussian Noise:\033[0m\033[0m {WGN}')
    y = att_sig + WGN
    SNR=10 * np.log10 (tx_power * PathLoss_linear / Noise_power)
    print (f'\033[32m\033[1mChannel Output:\033[0m\033[0m {y}')

    if switch_graph.upper()==('ON'):
        plt.figure(figsize=(6, 6))
        plt.scatter(np.real(y), np.imag(y), color='r')
        plt.title('Received Signal (with Noise)', fontweight='bold')
        plt.xlabel('In-phase', fontweight='bold')
        plt.ylabel('Quadrature-phase', fontweight ='bold')
        plt.grid(True)
        plt.show()

    else:
        pass

    return y,SNR

