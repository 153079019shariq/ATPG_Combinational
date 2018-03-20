module c17(output1,output2,G1,G2,G3,G4,G5) ;
input G1,G2,G3,G4,G5 ;
output output1,output2 ;
wire G8,G9,G12,G15,G16,G17,fanout1,fanout2,fanout3 ;
assign fanout1 = G3 ;
assign fanout2 = G9 ;
assign fanout3 = G12 ;
assign output1 = G16 ;
assign output2 = G17 ;
nand NAND2_0 (G8,G1,fanout1) ;
nand NAND2_1 (G9,fanout1,G4) ;
nand NAND2_2 (G12,G2,fanout2) ;
nand NAND2_3 (G15,fanout2,G5) ;
nand NAND2_4 (G16,G8,fanout3) ;
nand NAND2_5 (G17,fanout3,G15) ;
endmodule
