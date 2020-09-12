`include "sixteenbitadder.v"

module threetwobitadder(A,B,cin,sum,carry);
	input [31:0]A,B;
	output [31:0]sum;
	input cin;
	output carry;
	wire w0;
	sixteenbitadder f0(A[15:0],B[15:0],cin,sum[15:0],w0);
	sixteenbitadder f1(A[31:16],B[31:16],w0,sum[31:16],carry);
endmodule