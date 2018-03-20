import networkx as nx 
G = nx.DiGraph()
G.add_node('A',type='input',cc0=1,cc1=0,co=0)
G.add_node('B',type='input')
G.add_node('C',type='input')

G.add_node('1',type='gate',gatetype='and')
G.add_node('2',type='gate',gatetype='nand')
G.add_node('3',type='gate',gatetype='or')
G.add_node('4',type='gate',gatetype='xor')
G.add_node('5',type='gate',gatetype='and')
G.add_node('6',type='gate',gatetype='xor')


G.add_node('fanout1',type='fanout')
G.add_node('fanout2',type='fanout')
G.add_node('fanout3',type='fanout')


G.add_node('Z',type='output')
G.add_node('Y',type='output')

G.add_edges_from([('A','1'),('B','fanout1'),('fanout1','1'),('fanout1','2'),('fanout1','4'),('fanout1','6'),('C','fanout2'),('fanout2','2'),
		('fanout2','4'),('1','3'),('2','3'),('3','fanout3'),('fanout3','5'),('fanout3','Y'),('4','5'),('5','6'),('6','Z')], value_non_fault='x',value_faulty='x', fault='',cc0=0,cc1=0,co=0)
G.add_edge('A', '1', value_non_fault='x',value_faulty='x',fault='sa1',cc0=1,cc1=1,co=0)
G.add_edge('B','fanout1', value_non_fault='x',value_faulty='x',fault='sa1',cc0=1,cc1=1,co=0)
G.add_edge('C','fanout2', value_non_fault='x',value_faulty='x',fault='sa1',cc0=1,cc1=1,co=0)

G.add_edge('fanout3','5', value_non_fault='x',value_faulty='x',fault='sa1',cc0=1,cc1=1,co=0)

#~ plt.savefig("check_Graph.png")
#~ plt.ion()
#~ plt.show()
