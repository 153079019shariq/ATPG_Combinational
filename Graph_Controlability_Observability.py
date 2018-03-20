import networkx as nx 
G = nx.DiGraph()
G.add_node('R',type='input',cc0=1,cc1=0,co=0)
G.add_node('PP17',type='input',cc0=1,cc1=1,co=0)
G.add_node('PP18',type='input',cc0=1,cc1=1,co=0)

G.add_node('1',type='gate',gatetype='not',cc0=0,cc1=0,co=0)
G.add_node('2',type='gate',gatetype='not',cc0=0,cc1=0,co=0)
G.add_node('3',type='gate',gatetype='and',cc0=0,cc1=0,co=0)
G.add_node('4',type='gate',gatetype='nor',cc0=0,cc1=0,co=0)
G.add_node('5',type='gate',gatetype='and',cc0=0,cc1=0,co=0)
G.add_node('6',type='gate',gatetype='or',cc0=0,cc1=0,co=0)


G.add_node('fanout1',type='fanout',cc0=0,cc1=0,co=0)
G.add_node('fanout2',type='fanout',cc0=0,cc1=0,co=0)
G.add_node('fanout3',type='fanout',cc0=0,cc1=0,co=0)
G.add_node('fanout4',type='fanout',cc0=0,cc1=0,co=0)

G.add_node('Z',type='output',cc0=0,cc1=0,co=0)
G.add_node('PPO7',type='output',cc0=0,cc1=0,co=0)
G.add_node('PPO8',type='output',cc0=0,cc1=0,co=0)

G.add_edges_from([('R', 'fanout1'),('fanout1','4'),('fanout1','1'),('1','3'),('PP18','2'),('2','3'),('3','fanout2'),('fanout2','4'),('fanout2','5'),('fanout2','PPO8'),
		('PP17','fanout3'),('fanout3','4'),('fanout3','5'),('4','6'),('5','fanout4'),('fanout4','Z'),('fanout4','6'),('6','PPO7')], value_non_fault='x',value_faulty='x', fault='')
#G.add_edge('G3','fanout1', value_non_fault='x',value_faulty='x',fault='sa1')

#~ 
#~ plt.savefig("check_Graph.png")
#~ plt.ion()
#~ plt.show()
