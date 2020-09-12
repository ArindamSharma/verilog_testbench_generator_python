module HalfAdder (a,b,sum, ca);
input a,b;
// input c,d,e,f,g,h,i,j,k,l;
// input c1,d1,e1,f1,g1,h1,i1,j1,k1,l1;
output sum,ca;
	assign sum = a ^ b;
	assign ca  = a&b;
endmodule