`include "HalfAdder.v"
`include "fulladder.v"
module wallace(A,B,op);
    input [7:0] A,B;
    output [15:0] op;

    wire[7:0] p1;
    wire[8:1] p2;
    wire[9:2] p3;
    wire[10:3] p4;
    wire[11:4] p5;
    wire[12:5] p6;
    wire[13:6] p7;
    wire[14:7] p8;

    assign p1=B[0]?A:8'd0;
    assign p2=B[1]?A:8'd0;
    assign p3=B[2]?A:8'd0;
    assign p4=B[3]?A:8'd0;
    assign p5=B[4]?A:8'd0;
    assign p6=B[5]?A:8'd0;
    assign p7=B[6]?A:8'd0;
    assign p8=B[7]?A:8'd0;

    // initial
    // begin
    // $monitor($time, "%b %b %b %b %b %b %b %b",p1,p2,p3,p4,p5,p6,p7,p8);
    // end


    wire[9:0] S11;
    wire[9:2] C11;

    assign S11[0]=p1[0];
    HalfAdder HA1(p1[1],p2[1],S11[1],C11[2]);
    fulladder FA1(p1[2],p2[2],p3[2],S11[2],C11[3]);
    fulladder FA2(p1[3],p2[3],p3[3],S11[3],C11[4]);
    fulladder FA3(p1[4],p2[4],p3[4],S11[4],C11[5]);
    fulladder FA4(p1[5],p2[5],p3[5],S11[5],C11[6]);
    fulladder FA5(p1[6],p2[6],p3[6],S11[6],C11[7]);
    fulladder FA6(p1[7],p2[7],p3[7],S11[7],C11[8]);
    HalfAdder HA2(p2[8],p3[8],S11[8],C11[9]);
    assign S11[9]=p3[9];

    wire[12:3] S12;
    wire[12:5] C12;

    assign S12[3]=p4[3];
    HalfAdder HA3(p4[4],p5[4],S12[4],C12[5]);
    fulladder FA7(p4[5],p5[5],p6[5],S12[5],C12[6]);
    fulladder FA8(p4[6],p5[6],p6[6],S12[6],C12[7]);
    fulladder FA9(p4[7],p5[7],p6[7],S12[7],C12[8]);
    fulladder FA10(p4[8],p5[8],p6[8],S12[8],C12[9]);
    fulladder FA11(p4[9],p5[9],p6[9],S12[9],C12[10]);
    fulladder FA12(p4[10],p5[10],p6[10],S12[10],C12[11]);
    HalfAdder HA4(p5[11],p6[11],S12[11],C12[12]);
    assign S12[12]=p6[12];

    wire[10:0] S21;
    wire[12:3] C21;

    assign S21[0]=S11[0];
    assign S21[1]=S11[1];
    HalfAdder HA5(S11[2],C11[2],S21[2],C21[3]);
    fulladder FA13(S11[3],C11[3],S12[3],S21[3],C21[4]);
    fulladder FA14(S11[4],C11[4],S12[4],S21[4],C21[5]);
    fulladder FA15(S11[5],C11[5],S12[5],S21[5],C21[6]);
    fulladder FA16(S11[6],C11[6],S12[6],S21[6],C21[7]);
    fulladder FA17(S11[7],C11[7],S12[7],S21[7],C21[8]);
    fulladder FA18(S11[8],C11[8],S12[8],S21[8],C21[9]);
    fulladder FA19(S11[9],C11[9],S12[9],S21[9],C21[10]);
    assign S21[10]=S12[10];
    assign C21[11]=S12[11];
    assign C21[12]=S12[12];

    wire[14:5] S22;
    wire[14:7] C22;

    assign S22[5]=C12[5];
    HalfAdder HA6(C12[6],p7[6],S22[6],C22[7]);
    fulladder FA20(C12[7],p7[7],p8[7],S22[7],C22[8]);
    fulladder FA21(C12[8],p7[8],p8[8],S22[8],C22[9]);
    fulladder FA22(C12[9],p7[9],p8[9],S22[9],C22[10]);
    fulladder FA23(C12[10],p7[10],p8[10],S22[10],C22[11]);
    fulladder FA24(C12[11],p7[11],p8[11],S22[11],C22[12]);
    fulladder FA25(C12[12],p7[12],p8[12],S22[12],C22[13]);
    HalfAdder HA7(p7[13],p8[13],S22[13],C22[14]);
    assign S22[14]=p8[14];

    wire[13:0] S31;
    wire[14:4] C31;

    assign S31[0]=S21[0];
    assign S31[1]=S21[1];
    assign S31[2]=S21[2];
    HalfAdder HA8(S21[3],C21[3],S31[3],C31[4]);
    HalfAdder HA9(S21[4],C21[4],S31[4],C31[5]);
    fulladder FA26(S21[5],C21[5],S22[5],S31[5],C31[6]);
    fulladder FA27(S21[6],C21[6],S22[6],S31[6],C31[7]);
    fulladder FA28(S21[7],C21[7],S22[7],S31[7],C31[8]);
    fulladder FA29(S21[8],C21[8],S22[8],S31[8],C31[9]);
    fulladder FA30(S21[9],C21[9],S22[9],S31[9],C31[10]);
    fulladder FA31(S21[10],C21[10],S22[10],S31[10],C31[11]);
    HalfAdder HA10(C21[11],S22[11],S31[11],C31[12]);
    HalfAdder HA11(C21[12],S22[12],S31[12],C31[13]);
    assign S31[13]=S22[13];
    assign C31[14]=S22[14];

    wire[14:0] S41;
    wire[15:5] C41;

    assign S41[0]=S31[0];
    assign S41[1]=S31[1];
    assign S41[2]=S31[2];
    assign S41[3]=S31[3];
    HalfAdder HA12(S31[4],C31[4],S41[4],C41[5]);
    HalfAdder HA13(S31[5],C31[5],S41[5],C41[6]);
    HalfAdder HA14(S31[6],C31[6],S41[6],C41[7]);
    fulladder FA32(S31[7],C31[7],C22[7],S41[7],C41[8]);
    fulladder FA33(S31[8],C31[8],C22[8],S41[8],C41[9]);
    fulladder FA34(S31[9],C31[9],C22[9],S41[9],C41[10]);
    fulladder FA35(S31[10],C31[10],C22[10],S41[10],C41[11]);
    fulladder FA36(S31[11],C31[11],C22[11],S41[11],C41[12]);
    fulladder FA37(S31[12],C31[12],C22[12],S41[12],C41[13]);
    fulladder FA38(S31[13],C31[13],C22[13],S41[13],C41[14]);
    HalfAdder HA15(C31[14],C22[14],S41[14],C41[15]);

    wire[16:0] F;
    wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12;
    assign w1=1'b0;
    assign F[0]=S41[0];
    assign F[1]=S41[1];
    assign F[2]=S41[2];
    assign F[3]=S41[3];
    assign F[4]=S41[4];
    fulladder FA39(S41[5],C41[5],w1,F[5],w2);
    fulladder FA40(S41[6],C41[6],w2,F[6],w3);
    fulladder FA41(S41[7],C41[7],w3,F[7],w4);
    fulladder FA42(S41[8],C41[8],w4,F[8],w5);
    fulladder FA43(S41[9],C41[9],w5,F[9],w6);
    fulladder FA44(S41[10],C41[10],w6,F[10],w7);
    fulladder FA45(S41[11],C41[11],w7,F[11],w8);
    fulladder FA46(S41[12],C41[12],w8,F[12],w9);
    fulladder FA47(S41[13],C41[13],w9,F[13],w10);
    fulladder FA48(S41[14],C41[14],w10,F[14],w11);
    HalfAdder HA16(C41[15],w11,F[15],w12);
    assign F[16]=w12;

    assign op=F;

endmodule // 