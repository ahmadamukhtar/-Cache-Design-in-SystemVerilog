`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/11/2024 12:27:02 AM
// Design Name: 
// Module Name: set_associative
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module set_associative(
    input clk_i, rst_i,
    input [15:0] address,
    output logic hit_o,
    output logic [31:0] data_o
    );
    
    
    
    logic [133:0] cache_way_0[128];
    logic [133:0] cache_way_1[128];
    logic [133:0] data;
    
    logic [4:0] tag; 
    logic [6:0] cache_index;
    logic [1:0] word_offset;
    logic [4:0] cache_tag_0;
    logic [4:0] cache_tag_1;
    logic cache_valid_0;
    logic cache_valid_1;
    
    
    
    assign cache_index = address[10:4];   // block index for cache blocks
    assign word_offset = address[3:2];    // word offset for the block    
    assign tag = address[15:11];  // tag bits (last 4 MSB bits)
    assign cache_tag_0 = cache_way_0[cache_index][132:128];
    assign cache_tag_1 = cache_way_1[cache_index][132:128];
    assign cache_valid_0 = cache_way_0[cache_index][133];
    assign cache_valid_1 = cache_way_1[cache_index][133];
    
    always_comb
    begin
    	if (!rst_i)
        begin
            data = 0;
            hit_o = 0;
        end
    	else if( (cache_valid_0 == 1'b1) && cache_tag_0 == tag )
    	begin
    		hit_o = 1'b1;
    		data = cache_way_0[cache_index];
    	end
		else if( (cache_valid_1 == 1'b1) && cache_tag_1 == tag )
    	begin
    		hit_o = 1'b1;
    		data = cache_way_1[cache_index];
    	end
    	else
    	begin
    		hit_o = 1'b0;
    		data = 32'd0;
    	end    
    end
     
    always_comb
    begin
    	if(hit_o)
    	begin
            case(word_offset)
            2'd3:  data_o = data[31:0];
            2'd2:  data_o = data[63:32];
            2'd1:  data_o = data[95:64];
            2'd0:  data_o = data[127:96];
            default: data_o = 32'd0;
            endcase 
    	end
    	else
    	begin
    		data_o  = 32'd0;
    	end    
    end
    
    initial begin
    	$readmemb("/home/cc/ahmad/cache-tester-main/set_associative/init_files/way0.bin",cache_way_0);
    	$readmemb("/home/cc/ahmad/cache-tester-main/set_associative/init_files/way1.bin",cache_way_1);
    end
    
    
    
    
    
    
    
    
    
endmodule
