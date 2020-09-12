`include "fulladder.v"

module fourbitadder(A,B,cin,sum,carry);
	input [3:0]A,B;
	// input [7:0]C,D,E;
	output [3:0]sum;
	// output F,G,H,J;
	input cin;
	output carry;
	wire w1,w2,w0;
	fulladder f0(A[0],B[0],cin,sum[0],w0);
	fulladder f1(A[1],B[1],w0,sum[1],w1);
	fulladder f2(A[2],B[2],w1,sum[2],w2);
	fulladder f3(A[3],B[3],w2,sum[3],carry);
endmodule