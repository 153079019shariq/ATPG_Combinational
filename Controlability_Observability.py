from Graph_Controlability_Observability import G
import Gates
import networkx as nx
from collections import OrderedDict


def print_G_node(node):
	#for node  in G.nodes(data=True):
		#print node
		#print node[0],node[1]['cc0'],node[1]['cc1'],node[1]['co']
		print node,G.nodes[node]['co']

def controlabilty(node):
	global G
	list_predecessorCC0 =[]
	list_predecessorCC1 =[]
	if(G.nodes[node]['type']!='input'):
		for predecessor in  G.predecessors(node):
				 list_predecessorCC0.append(G.nodes[predecessor]['cc0'])
				 list_predecessorCC1.append(G.nodes[predecessor]['cc1'])
			
		#print "list_predecessor",list_predecessorCC0
		#print "list_predecessor",list_predecessorCC1
		if(G.nodes[node]['type']=='gate'):
				if(G.nodes[node]['gatetype']=='and'):
					G.nodes[node]['cc0'],G.nodes[node]['cc1']= Gates.AND_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='or'):
					G.nodes[node]['cc0'],G.nodes[node]['cc1']= Gates.OR_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='nand'):
					G.nodes[node]['cc0'],G.nodes[node]['cc1']= Gates.NAND_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='nor'):
					G.nodes[node]['cc0'],G.nodes[node]['cc1']= Gates.NOR_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='not'):
					G.nodes[node]['cc0'],G.nodes[node]['cc1']= Gates.NOT_Control(list_predecessorCC0,list_predecessorCC1)
		
		elif(G.nodes[node]['type']=='fanout'):
				G.nodes[node]['cc0'],G.nodes[node]['cc1']= list_predecessorCC0[0],list_predecessorCC1[0]
		
		elif(G.nodes[node]['type']=='output'):
				G.nodes[node]['cc0'],G.nodes[node]['cc1']= list_predecessorCC0[0],list_predecessorCC1[0]

def observabiltiy(node):
		global G
		#Predeccesor are the input of the gate and node is the gate itself.	
		if(G.nodes[node]['type']=='gate'):		
				print "%%%%%%%%%%%%%%%%%%%%%%%%%%Gate Observability%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
				print "node in gate",node
				list_predecessorCC0 =[]
				list_predecessorCC1 =[]
				for predecessor in  G.predecessors(node):
						 list_predecessorCC0.append(G.nodes[predecessor]['cc0'])
						 list_predecessorCC1.append(G.nodes[predecessor]['cc1'])
				nodeCO		=G.nodes[node]['co']
				list_predecessorCO =[]
				print 	"list_predecessorCC0",list_predecessorCC0
				print   "list_predecessorCC1",list_predecessorCC1
				print   "nodeCO",nodeCO
				if(G.nodes[node]['gatetype']=='and' or G.nodes[node]['gatetype']=='nand'):
					print list_predecessorCC0
					print nodeCO
					list_predecessorCO = Gates.AND_NAND_Obser(list_predecessorCC1,nodeCO)
					#print "list_predecessorCO",list_predecessorCO
				elif(G.nodes[node]['gatetype']=='or' or G.nodes[node]['gatetype']=='nor'):
					list_predecessorCO = Gates.AND_NAND_Obser(list_predecessorCC0,nodeCO)
					print "list_predecessorCO",list_predecessorCO
				elif(G.nodes[node]['gatetype']=='not'):
					list_predecessorCO = Gates.NOT_Obser(nodeCO)
				count =0	
				for predecessor in  G.predecessors(node):
					print "predessecor",predecessor
					G.nodes[predecessor]['co'] = list_predecessorCO[count]
					print "G.nodes[predecessor]['co']",G.nodes[predecessor]['co']
					count +=1
					print_G_node(predecessor)
		#Node is fanout itself and branches of it are successor.		
		elif(G.nodes[node]['type']=='fanout'):
				print "$$$$$$$$$$$$$$$$$$$$$$$Fanout Observability$$$$$$$$$$$$$$$$$$$$$$$$"
				print "node in fanout",node
				list_successor =[]
				for successor in G.successors(node):
					list_successor.append(G.nodes[successor]['co'])
				G.nodes[node]['co']  =min(list_successor)
				print_G_node(node)
		
		elif(G.nodes[node]['type']=='output'):
				for predecessor in  G.predecessors(node):
					print "predecessor",predecessor
					G.nodes[predecessor]['co'] = G.nodes[node]['co']
					print "G.nodes[predecessor]['co']",G.nodes[predecessor]['co']
					print_G_node(predecessor)	
					
lis =['R','PP17','PP18','fanout1','1','2','3','fanout2','fanout3','4','5','fanout4','6','PPO7','PPO8','Z']	
#1st controlabiliy should be calculated then observability.The controlability is calculated from PI to PO.And the observability is calculated from PO to PI.
for node in lis:	
		controlabilty(node)
lis1 =['R','PP17','PP18','fanout1','1','2','3','fanout2','fanout3','4','5','fanout4','6','PPO7','PPO8','Z']	
for node in reversed(lis):	
		#print "node",node
		observabiltiy(node)
#print_G_node()
