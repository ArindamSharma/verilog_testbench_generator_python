`include "fourbitadder.v"

module eightbitadder(A,B,cin,sum,carry);
	input [7:0]A,B;
	output [7:0]sum;
	input cin;
	output carry;
	wire w0;
	fourbitadder f0(A[3:0],B[3:0],cin,sum[3:0],w0);
	fourbitadder f1(A[7:4],B[7:4],w0,sum[7:4],carry);
endmodule