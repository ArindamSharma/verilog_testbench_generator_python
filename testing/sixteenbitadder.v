`include "eightbitadder.v"

module sixteenbitadder(A,B,cin,sum,carry);
	input [15:0]A,B;
	output [15:0]sum;
	input cin;
	output carry;
	wire w0;
	eightbitadder f0(A[7:0],B[7:0],cin,sum[7:0],w0);
	eightbitadder f1(A[15:8],B[15:8],w0,sum[15:8],carry);
endmodule