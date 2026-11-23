module tt_nm_multiplexor (
    input  wire       ENABLE,
    input  wire       SELECTOR,
    input  wire [3:0] ENT_A,
    input  wire [3:0] ENT_B,
    output reg  [3:0] SALIDA
);

    always @(*) begin
        case ({ENABLE, SELECTOR})
            2'b10:   SALIDA = ENT_A;
            2'b11:   SALIDA = ENT_B;
            default: SALIDA = 4'b0000;
        endcase
    end

endmodule
module tt_um_multiplexor (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire [3:0] salida;

    tt_nm_multiplexor mux (
        .ENABLE   (ui_in[7]),
        .SELECTOR (ui_in[6]),
        .ENT_A    ({uio_in[0], ui_in[2:0]}),
        .ENT_B    ({uio_in[1], ui_in[5:3]}),
        .SALIDA   (salida)
    );

    assign uo_out  = {4'b0000, salida};
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
