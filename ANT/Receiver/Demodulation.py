import numpy as np
import matplotlib.pyplot as plt

"""Parameters:
        d_hat:Vector of filtered received symbols
        switch_mod:switch between 16-QAM and 16-PSK
        switch_graph: switch graphical output on or off

      Output parameters:
        c_hat: vector of demodulated symbols"""

def detect_symbols(d_hat,switch_mod,switch_graph):
    c_hat=[]
    symbols=np.array(['0000','1000','1001','1011','1010','1110','1111','1101','1100',
                      '0100','0101','0111','0110','0010','0011','0001'])
    psk_code = []
    if (switch_mod == 1):
        for p in d_hat:
            angle = np.angle(p)
            if 31*np.pi/16 <angle<=np.pi / 16:
                psk_code.append('0000')
            elif np.pi / 16 < angle <= 3 * np.pi / 16:
                psk_code.append('1000')
            elif 3 * np.pi / 16 < angle <= 5 * np.pi / 16:
                psk_code.append('1001')
            elif 5 * np.pi / 16 < angle <= 7 * np.pi / 16:
                psk_code.append('1011')
            elif 7 * np.pi / 16 < angle <= 9 * np.pi / 16:
                psk_code.append('1010')
            elif 9 * np.pi / 16 < angle <= 11 * np.pi / 16:
                psk_code.append('1110')
            elif 11 * np.pi / 16 < angle <= 13 * np.pi / 16:
                psk_code.append('1111')
            elif 13 * np.pi / 16 < angle <= 15 * np.pi / 16:
                psk_code.append('1101')
            elif 15 * np.pi / 16 < angle <= 17 * np.pi / 16:
                psk_code.append('1100')
            elif 17 * np.pi / 16 < angle <= 19 * np.pi / 16:
                psk_code.append('0100')
            elif 19 * np.pi / 16 < angle <= 21 * np.pi / 16:
                psk_code.append('0101')
            elif 21 * np.pi / 16 < angle <= 23 * np.pi / 16:
                psk_code.append('0111')
            elif 23 * np.pi / 16 < angle <= 25 * np.pi / 16:
                psk_code.append('0110')
            elif 25 * np.pi / 16 < angle <= 27 * np.pi / 16:
                psk_code.append('0010')
            elif 27 * np.pi / 16 < angle <= 29 * np.pi / 16:
                psk_code.append('0011')
            elif 29 * np.pi / 16 < angle <= 31 * np.pi / 16:
                psk_code.append('0001')
            print('psk_code', psk_code)

            c_hat.append(psk_code)
        if switch_graph == 1:
            x = np.real(p)
            y = np.imag(p)
            plt.figure(figsize=(8, 8))
            plt.scatter(x, y, color='blue')
            plt.title("16-PSK demodulation")
            plt.xlabel("In-phase Component")
            plt.ylabel("Quadrature Component")
            plt.show()

      # 16QAM
    if (switch_mod==0):
        code_r = []
        code_i = []
        # Decision thresholds
        real_threshold=[-3/np.sqrt(10),-1/np.sqrt(10),1/np.sqrt(10),3/np.sqrt(10)]
        imag_threshold=[-3/np.sqrt(10),-1/np.sqrt(10),1/np.sqrt(10),3/np.sqrt(10)]
        # Check the real part and assign the code
        for p in d_hat:

            if np.real(p)<=real_threshold[0]:
                code_r.append('00')
            elif np.real(p)<=real_threshold[1]:
                code_r.append('01')
            elif np.real(p)<=real_threshold[2]:
                code_r.append('11')
            else:
                code_r.append('10')

            print("real part(p):",np.real(p))


        #Check it for imaginary pary
            if np.imag(p)<=imag_threshold[0]:
                code_i.append('00')
            elif np.imag(p)<=imag_threshold[1]:
                code_i.append('01')
            elif np.imag(p)<=imag_threshold[2]:
                code_i.append('11')
            else:
                code_i.append('10')

            print("Imag part(p):", np.imag(p))


            combined_code=[]
            for i,r in zip(code_i,code_r):
                combined_code.append(i+r)
            print("combined_code",combined_code)
            for i,r in zip(code_r,code_i):
                combined_code.append(i+r)
            print("combined_code",combined_code)
            c_hat.append(combined_code)




    if switch_graph.upper()=='on':
        plt.figure(figsize=(8, 8))
        plt.scatter(code_r, code_i, color='blue')
        plt.title("16-QAM demodulation")
        plt.xlabel("In-phase Component")
        plt.ylabel("Quadrature Component")
        plt.grid(True)
        plt.legend()
        plt.show()

        return c_hat


























