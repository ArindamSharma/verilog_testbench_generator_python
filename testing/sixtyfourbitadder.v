`include "threetwobitadder.v"

module sixtyfourbitadder(A,B,cin,sum,carry);
	input [63:0]A,B;
	output [63:0]sum;
	input cin;
	output carry;
	wire w0;
	threetwobitadder f0(A[31:0],B[31:0],cin,sum[31:0],w0);
	threetwobitadder f1(A[63:32],B[63:32],w0,sum[63:32],carry);
endmodule