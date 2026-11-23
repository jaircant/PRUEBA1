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
