import networkx as nx 
G = nx.DiGraph()
G.add_node('A',type='input')
G.add_node('B',type='input')


G.add_node('1',type='gate',gatetype='nand')
G.add_node('2',type='gate',gatetype='nand')
G.add_node('3',type='gate',gatetype='nand')
G.add_node('4',type='gate',gatetype='nand')
G.add_node('5',type='gate',gatetype='nand')
G.add_node('6',type='gate',gatetype='nand')
G.add_node('7',type='gate',gatetype='nand')
G.add_node('8',type='gate',gatetype='nand')
G.add_node('9',type='gate',gatetype='nand')


G.add_node('fanout1',type='fanout')
G.add_node('fanout2',type='fanout')
G.add_node('fanout3',type='fanout')
G.add_node('fanout4',type='fanout')
G.add_node('fanout5',type='fanout')


G.add_node('X',type='output')
G.add_node('Y',type='output')
G.add_node('Z',type='output')

G.add_edges_from([('A', 'fanout1'),('G9', 'fanout2'),('G12', 'fanout3'),('G16', 'output1'),('G17', 'output2'),
('fanout1', 'G8'),('G4', 'G9'),('fanout2', 'G12'),('G5', 'G15'),('fanout3', 'G16'),('G15', 'G17'),('G1', 'G8'),('fanout1', 'G9'),
('G2', 'G12'),('fanout2', 'G15'),('G8', 'G16'),('fanout3', 'G17')], value_non_fault='x',value_faulty='x', fault='')
G.add_edge('G3','fanout1', value_non_fault='x',value_faulty='x',fault='sa1')
