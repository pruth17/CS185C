import json

observation_symbols = ['mov','push','add','call','cmp','jmp', 'imul',
                     'xor','pop','jz','jnz','lea','sub','test',
                     'retn','or','and','inc','nop','dec','shr',
                     'movzx','jb','sbb','adc','shl','leave',
                     'jnb','jbe','discarded']

# THIS FILE IS FOR PRODUCING THE OBSERVATION MATRIX
B = {}
ob_d = open("opcode_rates.csv","r")
data = ob_d.readlines()
ob_d.close()

for i in range(1,len(data)):
  x = data[i].split(",")
  state = x[0]
  print(state)
  B[state] = {}
  
  
for c in range(1,len(x)):
    print(observation_symbols[c-1])
    B[state][observation_symbols[c-1]]=round((float(x[c].strip()[0:-1]) / 100),3)

with open('observation_matrix', 'w') as outfile:
    json.dump(B, outfile)