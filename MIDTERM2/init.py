import os

parent_dir = "malicia/"

Q = [] 
V = []
N = 0 

initial_state={}

total  = 0
for root, dirs, files in os.walk(parent_dir, topdown = False):
  family=root.split(parent_dir)[1]
  if(family != "" and len(files) != 0):
    total += len(files)
    N += 1
    Q.append(root.split(parent_dir)[1])
    
for root, dirs, files in os.walk(parent_dir, topdown = False):
  family = root.split(parent_dir)[1]
  if(family != "" and len(files) != 0):
    percentage=(len(files) / total)
    initial_state[root.split(parent_dir)[1]] = percentage

values={}
values["Q"]=Q
values["N"]=N
values["V"]=V

observation_symbols=['mov','push','add','call','cmp','jmp', 'imul',
                     'xor','pop','jz','jnz','lea','sub','test',
                     'retn','or','and','inc','nop','dec','shr',
                     'movzx','jb','sbb','adc','shl','leave',
                     'jnb','jbe','discarded']
values["M"]=len(observation_symbols)

letter='A'
for x in range(len(observation_symbols)):
  if x<10:
    values["V"].append(str(x))
  else:
    values["V"].append(letter)
    letter=chr(ord(letter)+1)
