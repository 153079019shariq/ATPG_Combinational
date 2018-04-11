from Graph_Controlability_Observability import G
import Gates
import networkx as nx
from collections import OrderedDict
import operator
		
def print_Graph_edges_Contollabilty():
	global G	
	for item in G.edges(data=True):
			print item[0],item[1], item[2]['cc0'],item[2]['cc1'],item[2]['co']
					

def controlabilty(node):
	global G
	list_predecessorCC0 =[]
	list_predecessorCC1 =[]
	
	if(G.nodes[node]['type']=='gate' or G.nodes[node]['type']=='fanout' or  G.nodes[node]['type']=='FF'):
		
		for predecessor in  list(G.in_edges(nbunch=node, data=False)):
			list_predecessorCC0.append(G.edges[predecessor]['cc0'])					#Multiple inedge
			list_predecessorCC1.append(G.edges[predecessor]['cc1'])
		
		if(G.nodes[node]['type']=='gate'):
				
				i= list(G.out_edges(nbunch=node, data=False))[0]					#One outedge as output of Gate is one
				if(G.nodes[node]['gatetype']=='and'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.AND_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='or'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.OR_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='nand'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.NAND_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='nor'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.NOR_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='xor'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.XOR_Control(list_predecessorCC0,list_predecessorCC1)									
				elif(G.nodes[node]['gatetype']=='xnor'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.XNOR_Control(list_predecessorCC0,list_predecessorCC1)
				elif(G.nodes[node]['gatetype']=='not'):
					G.edges[i]['cc0'],G.edges[i]['cc1']= Gates.NOT_Control(list_predecessorCC0,list_predecessorCC1)
				#print "G.edges[i]['cc0'],G.edges[i]['cc1']",G.edges[i]['cc0'],G.edges[i]['cc1']
		
		elif(G.nodes[node]['type']=='fanout'):
				for i in  list(G.out_edges(nbunch=node, data=False)):
					G.edges[i]['cc0'],G.edges[i]['cc1']= list_predecessorCC0[0],list_predecessorCC1[0] #Multiple outedge
				#print "G.edges[i]['cc0'],G.edges[i]['cc1']",G.edges[i]['cc0'],G.edges[i]['cc1']
				
		elif(G.nodes[node]['type']=='FF'):
				for i in  list(G.out_edges(nbunch=node, data=False)):
					G.edges[i]['cc0'],G.edges[i]['cc1']= list_predecessorCC0[0]+1,list_predecessorCC1[0]+1	#One outedge
				#print "G.edges[i]['cc0'],G.edges[i]['cc1']",G.edges[i]['cc0'],G.edges[i]['cc1']
					
		#print_Graph_edges()
		




#-----------------------------------------------Levelization of the Graph-------------------------------------------------------------------------



def assign(lis,dic):
	flag=0
	for k in lis:
			  	if(k in dic.keys()):
					continue
				else:
					flag=1
					break
	return flag

def maxi(lis,dic):
	maxim=0
	for i in lis:
		if(maxim <dic[i]):
			maxim =dic[i]
	return maxim





def Level (Graph):
	global dic_level
	dic_level={}
	#print Graph.nodes(data=True)
	for item in Graph.nodes():
		
		
		if(Graph.nodes[item]['type']=='input' ):
			dic_level[item]=1
	#print "Length of Graph",len(Graph)
	while (len(dic_level)<len(Graph)):	
		for item in Graph.nodes():
			if(Graph.nodes[item]['type']=='fanout' or Graph.nodes[item]['type']=='FF'):
				list_inedge =list(Graph.in_edges(nbunch=item, data=False))
				if(list_inedge[0][0] in dic_level.keys()):	
					dic_level[item]=dic_level[list_inedge[0][0]]+1
			elif(Graph.nodes[item]['type']=='output'):
				list_inedge =list(Graph.in_edges(nbunch=item, data=False))
				if(list_inedge[0][0] in dic_level.keys()):	
					dic_level[item]=dic_level[list_inedge[0][0]]
				
			elif(Graph.nodes[item]['type']=='gate'):
				list_inedge =list(Graph.in_edges(nbunch=item, data=False))	
				lis=[]
				lis =[i[0] for i in list_inedge]
				if(assign(lis,dic_level) ==0):
					dic_level[item] =maxi(lis,dic_level)+1
				else:
					continue
				#dic_level[item]=maxi
	return dic_level
#---------------------------------------------------------------------------------------------------------------------------------------	

bfs= Level (G)
print bfs
sorted_x = sorted(bfs.items(), key=operator.itemgetter(1))

list1=[]
def lis(sorted_x):
	global list1
	
	for i in sorted_x:
		list1.append(i[0])
	
		
lis(sorted_x)
#--------------------------------------------------------------------------------------------------------------------------------------------

def Contollability_circuit():
	for node in list1:	
		controlabilty(node)


print_Graph_edges_Contollabilty()

