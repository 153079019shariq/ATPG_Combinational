
import copy
def AND_gate(a,b):
	return {
			'00':'0',
			'01':'0',
			'0x':'0',
			'10':'0',
			'11':'1',
			'1x':'x',
			'x0':'0',
			'x1':'x',
			'xx':'x'
			}[a+b]
			
	
def OR_gate(a,b):
	return {
			'00':'0',
			'01':'1',
			'0x':'x',
			'10':'1',
			'11':'1',
			'1x':'1',
			'x0':'x',
			'x1':'1',
			'xx':'x'
			}[a+b]		
			

def NAND_gate(a,b):
	return {
			'00':'1',
			'01':'1',
			'0x':'1',
			'10':'1',
			'11':'0',
			'1x':'x',
			'x0':'1',
			'x1':'x',
			'xx':'x'
			}[a+b]
			
def NOR_gate(a,b):
	return {
			'00':'1',
			'01':'0',
			'0x':'x',
			'10':'0',
			'11':'0',
			'1x':'0',
			'x0':'x',
			'x1':'0',
			'xx':'x'
			}[a+b]
			
			
def XOR_gate(a,b):
	return {
			'00':'0',
			'01':'1',
			'0x':'x',
			'10':'1',
			'11':'0',
			'1x':'x',
			'x0':'x',
			'x1':'x',
			'xx':'x'
			}[a+b]	
				

def XNOR_gate(a,b):
	return {
			'00':'1',
			'01':'0',
			'0x':'x',
			'10':'0',
			'11':'1',
			'1x':'x',
			'x0':'x',
			'x1':'x',
			'xx':'x'
			}[a+b]
			
			
def NOT_gate(a):
	return {
			'0':'1',
			'1':'0',
			'x':'x'
			}[a]	

def BUFFER_gate(a):
	return {
			'0':'0',
			'1':'1',
			'x':'x'
			}[a]	
			
def stuck_at_0(a):
	return AND_gate(a,'0')

def stuck_at_1(a):
	return OR_gate(a,'1')
	
	
def AND_Control(list_predecessorCC0,list_predecessorCC1):
	return (min(list_predecessorCC0)+1),(sum(list_predecessorCC1)+1)

def OR_Control(list_predecessorCC0,list_predecessorCC1):
	return (sum(list_predecessorCC0)+1),(min(list_predecessorCC1)+1)


def NAND_Control(list_predecessorCC0,list_predecessorCC1):
	return (sum(list_predecessorCC1)+1),(min(list_predecessorCC0)+1)

def NOR_Control(list_predecessorCC0,list_predecessorCC1):
	return (min(list_predecessorCC1)+1),(sum(list_predecessorCC0)+1)
	
def NOT_Control(list_predecessorCC0,list_predecessorCC1):
	return (list_predecessorCC1[0]+1),(list_predecessorCC0[0]+1)
	
def XOR_Control(list_predecessorCC0,list_predecessorCC1):
	return (min(sum(list_predecessorCC0),sum(list_predecessorCC1))+1,
			min((list_predecessorCC0[0]+list_predecessorCC1[1]),(list_predecessorCC0[1]+list_predecessorCC1[0]))+1)
	
def XNOR_Control(list_predecessorCC0,list_predecessorCC1):
	return (min((list_predecessorCC0[0]+list_predecessorCC1[1]),(list_predecessorCC0[1]+list_predecessorCC1[0]))+1,
			min(sum(list_predecessorCC0),sum(list_predecessorCC1))+1)


	
def AND_NAND_Obser(list_predecessorCC0,edgeCO):
	Observability_list=[]
	for i in list_predecessorCC0:
		list_temp =copy.deepcopy(list_predecessorCC0)
		list_temp.remove(i)
		sum1=sum(list_temp) + edgeCO +1
		Observability_list.append(sum1)
	return Observability_list
	

def OR_NOR_Obser(list_predecessorCC1,edgeCO):
	Observability_list=[]
	for i in list_predecessorCC1:
		list_temp =copy.deepcopy(list_predecessorCC1)
		list_temp.remove(i)
		sum1=sum(list_temp) + edgeCO +1
		Observability_list.append(sum1)
	return Observability_list


def XOR_XNOR_Obser(list_predecessorCC1,list_predecessorCC0,edgeCO):
	Observability_list=[]
	for i in range(len(list_predecessorCC1)):
		list_temp1 =copy.deepcopy(list_predecessorCC1)
		list_temp2 =copy.deepcopy(list_predecessorCC0)
		del list_temp1[i]
		del list_temp2[i]
		sum1=min(sum(list_temp1),sum(list_temp2)) + edgeCO +1
		Observability_list.append(sum1)
	return Observability_list

def NOT_Obser(edgeCO):
	list_temp=[]
	list_temp.append(edgeCO +1)
	return list_temp

list_predecessorCC0	=[1,2]	
list_predecessorCC1 =[3,4]

print XOR_Control([1,1],[1,1])
#print AND_Control(list_predecessorCC0,list_predecessorCC1)
#print AND_NAND_Obser([1,2,3],1)
#print OR_NOR_Obser([1,10,20],5)
#print NOT_Obser(10)
#output =stuck_at_1('0')
#print output
#print type(output)
