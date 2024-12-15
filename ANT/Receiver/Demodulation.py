import numpy as np
import matplotlib.pyplot as plt

"""Parameters:
        d_hat:Vector of filtered received symbols
        switch_mod:switch between 16-QAM and 16-PSK
        switch_graph: switch graphical output on or off

      Output parameters:
        c_hat: vector of demodulated symbols"""

def detect_symbols(d_hat,switch_mod,switch_graph):
    symbols=np.array(['0000','1000','1001','1011','1010','1110','1111','1101','1100',
                      '0100','0101','0111','0110','0010','0011','0001'])
    c_hat=[]
    print(len(d_hat))
    print(d_hat)

      # 16QAM
    if (switch_mod==0):
        c_hat=[]
        # code_r='00'
        # code_i='00'
        # Check the real part and assign the code
        for d in d_hat:
            if np.real(d)<-2:
                code_r='00'
            elif -2<=np.real(d)<0:
                code_r='01'
            elif 0<=np.real(d)<=2:
                code_r='11'
            elif np.real(d)>2:
                code_r='10'
            else:
                code_r='Unknown'

        #Check it for imaginary pary
            if np.imag(d)<-2:
                code_i='00'
            elif -2<=np.imag(d)<0:
                code_i='01'
            elif 0<=np.imag(d)<=2:
                code_i='11'
            elif np.imag(d)>2:
                code_i='10'
            else:
                code_i='Unknown'

            combined_code=code_r+code_i
            # print('combined_code')
            c_hat.append(combined_code)



    #16PSK

    elif (switch_mod==1):
        angles = np.angle(d_hat)
        for angle in angles:
            angle = np.mod(angle, 2 * np.pi)  # Normalize angle to [0, 2π]
            if np.isclose(angle, 0, atol=1e-2):
                psk_code = '0000'
            elif np.isclose(angle, np.pi / 8, atol=1e-2):
                psk_code = '1000'
            elif np.isclose(angle, 2 * np.pi / 8, atol=1e-2):
                psk_code = '1001'
            elif np.isclose(angle, 3 * np.pi / 8, atol=1e-2):
                psk_code = '1011'
            elif np.isclose(angle, 4 * np.pi / 8, atol=1e-2):
                psk_code = '1010'
            elif np.isclose(angle, 5 * np.pi / 8, atol=1e-2):
                psk_code = '1110'
            elif np.isclose(angle, 6 * np.pi / 8, atol=1e-2):
                psk_code = '1111'
            elif np.isclose(angle, 7 * np.pi / 8, atol=1e-2):
                psk_code = '1101'
            elif np.isclose(angle, 8 * np.pi / 8, atol=1e-2):
                psk_code = '1100'
            elif np.isclose(angle, 9 * np.pi / 8, atol=1e-2):
                psk_code = '0100'
            elif np.isclose(angle, 10 * np.pi / 8, atol=1e-2):
                psk_code = '0101'
            elif np.isclose(angle, 11 * np.pi / 8, atol=1e-2):
                psk_code = '0111'
            elif np.isclose(angle, 12 * np.pi / 8, atol=1e-2):
                psk_code = '0110'
            elif np.isclose(angle, 13 * np.pi / 8, atol=1e-2):
                psk_code = '0010'
            elif np.isclose(angle, 14 * np.pi / 8, atol=1e-2):
                psk_code = '0011'
            elif np.isclose(angle, 15 * np.pi / 8, atol=1e-2):
                psk_code = '0001'
            else:
                psk_code = 'Unknown'

            c_hat.append(psk_code)
        else:
            pass

    return c_hat



























