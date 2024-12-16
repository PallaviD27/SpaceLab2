# Modulation
# d = map2symbols(c, switch_mod, switch_graph) , API definition 3.4.2
import numpy as np
import matplotlib.pyplot as plt


'''Start'''

def map2symbols(CodeWord,switch_mod,switch_graph):
    '''
    Implements Modulation on the encoded bit sequence to either 16-QAM or 16-PSK.
    Parameters:
        CodeWord (np.ndarray): Encoded sequence after (7,4) Hamming encoding application,length is multiple of 7
        Switch_mod: For selection of the modulating scheme - '0' for 16 QAM and '1' for 16 PSK
        Switch_graph (string): ON/on/OFF/of - Displays the graphical representation of output when ON/on
    Returns:
        Output_Vector (np.ndarray): Array with the In-phase and Quad-phase components
        according to the Modulating Scheme selected
    '''
# Initialise output vector as a list
    Output_Vec =[]

# Switch mode 0 implies 16 QAM
    if switch_mod==0:

# Print Constellation for 16 QAM

# Define Gray-coded mapping for levels -3, -1, +1, +3
        gray_mapping = {
            -3: '00',
            -1: '01',
            +1: '11',
            +3: '10'
        }

# Define 16-QAM constellation points (I, Q) pairs
        I_levels = [-3, -1, +1, +3]
        Q_levels = [-3, -1, +1, +3]

# Generate all combinations of I and Q
        constellation_points = [(I, Q) for I in I_levels for Q in Q_levels]

# Generate Gray codes for all points
        gray_codes = [
            f'{gray_mapping[I]}{gray_mapping[Q]}' for I, Q in constellation_points
        ]

# Separate I and Q for plotting
        I_values = [point[0] for point in constellation_points]
        Q_values = [point[1] for point in constellation_points]

# Plot the constellation diagram
        plt.figure(figsize=(8, 8))
        plt.scatter(I_values, Q_values, color='blue', label='16-QAM points')
        plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
        plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.title('16-QAM Constellation Diagram with Gray Mapping', fontweight='bold')
        plt.xlabel('In-phase (I)*sqrt(10)', fontweight='bold')
        plt.ylabel('Quadrature-phase (Q)* sqrt(10)', fontweight='bold')

# Annotate points with Gray codes
        for i, point in enumerate(constellation_points):
            plt.text(
                point[0] + 0.2,
                point[1] + 0.2,
                gray_codes[i],
                fontsize=10,
                color="red",
                ha="center"
            )

        plt.xlim(-4, 4)
        plt.ylim(-4, 4)
        plt.legend()


        Code_length = int(len(CodeWord))

 # Dictionary definition for 16-QAM Modulation
        QAM_Mapping = {'0000':(-3/np.sqrt(10),-3/np.sqrt(10)),
                       '0001': (-3/np.sqrt(10),-1/np.sqrt(10)),
                       '0100': (-1/np.sqrt(10),-3/np.sqrt(10)),
                       '0101': (-1/np.sqrt(10),-1/np.sqrt(10)),
                       '1100': (1/np.sqrt(10),-3/np.sqrt(10)),
                       '1000': (3/np.sqrt(10), -3/np.sqrt(10)),
                       '1001': (3/np.sqrt(10), -1/np.sqrt(10)),
                       '1101': (1/np.sqrt(10), -1/np.sqrt(10)),
                       '1111': (1/np.sqrt(10), 1/np.sqrt(10)),
                       '1011': (3/np.sqrt(10), 1/np.sqrt(10)),
                       '1010': (3/np.sqrt(10), 3/np.sqrt(10)),
                       '1110': (1/np.sqrt(10), 3/np.sqrt(10)),
                       '0110': (-1/np.sqrt(10), 3/np.sqrt(10)),
                       '0111': (-1/np.sqrt(10), 1/np.sqrt(10)),
                       '0011': (-3/np.sqrt(10), 1/np.sqrt(10)),
                       '0010': (-3/np.sqrt(10), 3/np.sqrt(10)),
                       }
# Display the in-phase and quadrature phase values corresponding to a set of 4 bits
        for p in range(Code_length // 4):
            ModSetp = CodeWord[p * 4:(p + 1) * 4] # Split the encoded bit stream into sets of 4
            print(f'\033[32m\033[1mModulating Set {p}:\033[0m\033[0m {ModSetp}') # Print for verification
            ModSetp_binary = ''.join(map(str, ModSetp)) # Convert the strings to binary
            if ModSetp_binary in QAM_Mapping:
                I, Q = QAM_Mapping[ModSetp_binary]
                print(f"\033[32m\033[1mMatch found for Modulating Set {ModSetp_binary}:\033[0m\033[0m I = {I}, Q = {Q}")
                Output_Vec.append((I,Q))
                Output_Vector = np.array(Output_Vec)

            else:
                print(f"No match found for Modulating Set {ModSetp_binary}")


# Display the 16 QAM Constellation
        plt.show()

        print(f"\033[32m\033[1mOutput Vector:\033[0m\033[0m\n{Output_Vector}")

# Switch mode variable = 1 implies 16-PSK
    elif switch_mod==1:

# Print Constellation diagram for 16-PSK
        PSK=16   # Define number of Constellation Points
        np.set_printoptions(suppress=True, precision=4)  # Print option to suppress the scientific notation for sin and cosine
        phase = np.linspace(0,2*np.pi, PSK,endpoint=False) # Evenly spaced phase points
        phase_degrees=np.degrees(phase) # Convert radian phase values to degrees (just for verification)
        print(f"\033[32m\033[1mPhase values(in degrees):\033[0m\033[0m \n{phase_degrees}")
        I1=np.cos(phase)   # In-phase(x-axis/real) component
        print(f"\033[32m\033[1mIn-phase values:\033[0m\033[0m\n {I1}")
        Q1=np.sin(phase)   # Quadrature-phase (y-axis/imaginary) component
        print(f"\033[32m\033[1mQuadrature-phase values:\033[0m\033[0m \n {Q1}")

# Plot the constellation

# Dictionary definition for 16-PSK Modulation
        PSK_Mapping = {'0000':(I1[0],Q1[0]),
                       '0001': (I1[15],Q1[15]),
                       '0100': (I1[9],Q1[9]),
                       '0101': (I1[10],Q1[10]),
                       '1100': (I1[8],Q1[8]),
                       '1000': (I1[1],Q1[1]),
                       '1001': (I1[2],Q1[2]),
                       '1101': (I1[7],Q1[7]),
                       '1111': (I1[6],Q1[6]),
                       '1011': (I1[3],Q1[3]),
                       '1010': (I1[4],Q1[4]),
                       '1110': (I1[5],Q1[5]),
                       '0110': (I1[12],Q1[12]),
                       '0111': (I1[11],Q1[11]),
                       '0011': (I1[14],Q1[14]),
                       '0010': (I1[13],Q1[13]),
                       }

        Code_length = int(len(CodeWord))
        plt.figure(figsize=(6,6))

        for label,(x,y) in PSK_Mapping.items():
            plt.scatter(x, y, color='blue')
            plt.text(x*1.05, y*1.05, label,ha='center',va='center',fontsize=10, color='red')
        plt.axhline(0,color='black',linewidth=0.5)
        plt.axvline(0, color ='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xlabel('In-phase (I)',fontweight='bold')
        plt.ylabel('Quadrature-phase (Q)',fontweight='bold')
        plt.title('16-PSK Constellation Diagram with Gray Mapping',fontweight='bold')

# Display the In-phase and Quad-phase values for each of the 4 bits in the Coded sequence
        for p1 in range(Code_length // 4):
            np.set_printoptions(suppress=True, precision=4)
            ModSetp1 = CodeWord[p1 * 4:(p1 + 1) * 4]
            print(f'\033[32m\033[1mModulating Set {p1}:\033[0m\033[0m {ModSetp1}')
            ModSetp1_binary = ''.join(map(str, ModSetp1))
            if ModSetp1_binary in PSK_Mapping:
                I2, Q2 = PSK_Mapping[ModSetp1_binary]
                np.set_printoptions(suppress=True, precision=4)
                print(f"\033[32m\033[1mMatch found for Modulating Set {ModSetp1_binary}:\033[0m\033[0m I = {I2}, Q = {Q2}")
                Output_Vec.append((I2, Q2))
# Get Output vector as array
                Output_Vector=np.array(Output_Vec)
            else:
                print(f"No match found for Modulating Set {ModSetp1_binary}")

        # plt.show()
        # plt.close()
        print(f"\033[32m\033[1mOutput Vector:\033[0m\033[0m\n{Output_Vector}")

    else:
        print("Not a valid switch_mod input")

# Plot the In-phase and Quad-phase values if switch_graph is ON
    if switch_graph.upper()=="ON":
        real_parts=[I3 for I3,Q3 in Output_Vector]
        imaginary_parts=[Q3 for I3,Q3 in Output_Vector]
        Fig2=plt.figure(figsize=(6,6))
        plt.xlim(-1.5,1.5)
        plt.ylim(-1.5,1.5)
        plt.scatter(real_parts,imaginary_parts)
        for w, (g, h) in enumerate(zip(real_parts, imaginary_parts)):
            label = f"({g:.2f}, {h:.2f})"  # Label the point with its (g, h) values
            plt.text(g, h, label, ha='center', va='center', fontsize=10)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.xlabel('In-phase (I)', fontweight='bold')
        plt.ylabel('Quadrature-phase (Q)', fontweight='bold')
        plt.title('Modulated Symbols', fontweight='bold')

        # plt.show()

    elif switch_graph.upper()=="OFF":
         pass


    return Output_Vector

