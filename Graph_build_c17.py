import sys
faulty_edge_list =[sys.argv[1],sys.argv[2],sys.argv[3]]
#faulty_edge_list =['fanout3','G17','sa0']
input_list =[]
output_list=[]
wire_list =[]
nodes_list =[]
edges_list =[]

fanout1_list =[]
output_of_gates =[]
input1_of_gates =[]
input2_of_gates =[]

dic_gate_types ={}

with open ('c17.v','r') as f:
	lines = f.read().splitlines()
	for i in lines:
		list1= i.split()
		if(list1[0]=='wire'):
			wire_list=list1[1].split(',')
		if(list1[0]=='input'):
			input_list=list1[1].split(',')
		if(list1[0]=='output'):
			output_list=list1[1].split(',')
		if(list1[0]=='assign'):
			edges_list.append((list1[3],list1[1]))
			if(list1[1] in wire_list):
				fanout1_list.append(list1[1])
		
		if(list1[0]=='nand' or list1[0]=='nor' or list1[0]=='or' or list1[0]=='and' or list1[0]=='not'):
			list2 = list1[2].split(',')
			output_of_gates.append(list2[0].lstrip('('))
			input1_of_gates.append(list2[1])
			input2_of_gates.append(list2[2].rstrip(')'))
			dic_gate_types[list2[0].lstrip('(')]=list1[0]
		
		

print "dic_gate_types",dic_gate_types
print type(dic_gate_types[output_of_gates[0]])
nodes_list =	input_list	+	output_of_gates + fanout1_list +	output_list 


for i in range(len(output_of_gates)):
	edges_list.append((input2_of_gates[i],output_of_gates[i]))

for i in range(len(output_of_gates)):
	edges_list.append((input1_of_gates[i],output_of_gates[i]))

		

print "input_list",input_list
print "fanout1_list",fanout1_list
print "output_of_gates",output_of_gates
print "output_list",output_list

print "wire_list",wire_list

print "**************************************"

print "nodes_list",nodes_list
print "edges_list",edges_list 

#*****************************Constructing a graph*************************************************************************
output = """import networkx as nx 
G = nx.DiGraph()""" + "\n"

add_node =""
add_edges_from= "G.add_edges_from(["
add_faulty_edges_check="G.add_edge('fanout3','G17', value_non_fault='x',value_faulty='x',fault='sa1')"
add_faulty_edges	="G.add_edge" +"(" + "\'"+ faulty_edge_list[0] + "\'" + "," + "\'"+ faulty_edge_list[1] + "\'" + ", value_non_fault='x',value_faulty='x',fault=" +"\'"+ faulty_edge_list[2] +"\'"+ ")"

print "add_f",add_faulty_edges

for  i in nodes_list:
	if(i in input_list):
		add_node  += "G.add_node" +"(" + "\'"+ i + "\'"+ "," + "type" + "=" + "\'"+ "input" + "\'" + ")" + "\n"
	if(i in fanout1_list):
		add_node  += "G.add_node" +"(" + "\'"+ i + "\'"+ "," + "type" + "=" + "\'" + "fanout" + "\'" + ")" + "\n"
	if(i in output_of_gates):
		add_node  += "G.add_node" +"(" + "\'"+ i + "\'"+ "," + "type" + "=" + "\'" + "gate" + "\'" + ","+"gatetype" + "=" + "\'" + dic_gate_types[i] + "\'" + ")" + "\n"
	if(i in output_list):
		add_node  += "G.add_node" +"(" + "\'"+ i + "\'"+ "," + "type" + "=" + "\'" + "output" + "\'" + ")" + "\n"
	
print add_node 

for i in range(len(edges_list)):
	if(i==len(edges_list)-1):
		add_edges_from += str(edges_list[i])
	else:
		add_edges_from += str(edges_list[i])+","
	
	
add_edges_from	+= "], value_non_fault='x',value_faulty='x', fault='')" 
#print add_edges_from

output += add_node + add_edges_from  + "\n" + add_faulty_edges

#print output 
f = open("Graph_build.py", 'w')
f.write(output)
f.close()



