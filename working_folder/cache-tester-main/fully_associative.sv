
`timescale 1ns / 1ps

module fully_associative(
    input clk_i,
    input rst_i,
    input [15:0] address,
    output logic hit_o,
    output logic [31:0] data_o
    );
    
    
    
    logic [140:0] cache[256];
    logic [140:0] data;
    logic [11:0] cache_tag;
    logic cache_valid_bit;
    
    logic [11:0] tag;
    logic [1:0] word_offset;
    
    assign tag = address[15:4];
    assign word_offset = address[3:2];
    
    
/*
    
    always_comb
    begin
    	for(int i = 0; i < 256; i = i + 1)
    	begin
    		cache_tag[i] = cache[i][139:128];
    		cache_valid_bit[i] = cache[i][140];
    		if((cache_tag[i] == tag) && (cache_valid_bit[i]))
    		begin
    			hit_o = 1'b1;
    			data = cache[i][127:0];
    		end
    		else
    		begin
    			hit_o = 1'b0;
    			data = 0;
    		end
    	end
    
    end
*/
 
    logic found;
	logic [140:0] temp_data;

	always_comb begin
    found = 1'b0; // Initialize found to false
    data = 0; // Default data
    
    for(int i = 0; i < 256; i = i + 1) begin
        cache_tag = cache[i][139:128];
        cache_valid_bit = cache[i][140];
        
        if((cache_tag == tag) && cache_valid_bit) begin
            found = 1'b1; // Set found to true
            temp_data = cache[i][127:0]; // Store the data
            break;
        end
    end
    
    hit_o = found; // Set hit_o to the found status
    data = found ? temp_data : 0; // Use temp_data if found
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
					data_o = 32'd0;
				end
				
			end   
 
    
    string way;
    
    initial begin
    	for(int i = 0; i < 256; i++)
    	begin
    		$sformat(way, "/home/cc/ahmad/cache-tester-main/full_associative/init_files/way%0d.bin", i);
    		$readmemb(way,cache,i,i);
    	end
    end
    
    
    
    
    
endmodule
