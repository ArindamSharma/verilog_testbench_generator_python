module fulladder (a,b,cin,sum,carry);
input a,b; 
input cin;
output sum, carry;
	assign sum =(a ^ b ^cin );
	assign carry = (a & b)|(cin & a)|(b & cin);

endmodule