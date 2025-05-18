`timescale 1ns / 1ps
module direct_mapped(
    input clk_i,
    input rst_i,
    input [15:0] address,
    output logic hit_o,
    output logic [31:0] data_o
    );
    
    //localparam [7:0] blocks = 256;   // total no of blocks in the cache 
    //localparam [3:0] words_per_block = 4;   // total number of words per block
    
    
    // cache declaration
    logic [132:0] cache[256];
//    logic [16:0] address[4096];
//    logic [11:0] pa_pointer;
  //  logic [3:0] cache_tags[blocks]; // tag for each block
  //  logic cache_valid_bit[blocks];   // valid bit for each block  
    logic [3:0] tag; 
    logic [7:0] cache_index;
    logic [1:0] word_offset;   
    //logic [7:0] hit_count = 0;
    //logic [7:0] miss_count = 0; 
    logic [3:0] cache_tag;
   // logic [132:0] index_block;
    logic cache_valid_bit; 
    assign tag = address[15:12];  // tag bits (last 4 MSB bits)
    assign cache_index = address[11:4];   // block index for cache blocks
    assign word_offset = address[3:2];    // word offset for the block
    assign cache_tag = cache[cache_index][131:128];
   // assign index_block = cache[cache_index];
    assign cache_valid_bit = cache[cache_index][132];
    
    always_comb
    begin
        if (!rst_i)
        begin
            data_o = 0;
            hit_o = 0;
        end
        else if( cache_tag == tag && cache_valid_bit == 1'b1)
        begin
            hit_o = 1'b1;
            //hit_count = hit_count + 1;
            case(word_offset)
            2'd3:  data_o = cache[cache_index][31:0];
            2'd2:  data_o = cache[cache_index][63:32];
            2'd1:  data_o = cache[cache_index][95:64];
            2'd0:  data_o = cache[cache_index][127:96];
            default: data_o = 32'd0;
            endcase
        end
        else
        begin
            data_o = 32'h00000000;
            hit_o = 1'b0;
            //miss_count = miss_count + 1;
        end   
    end
    initial 
    begin
        $readmemb("/home/cc/ahmad/cache-tester-main/way0.bin",cache);
    end
endmodule
