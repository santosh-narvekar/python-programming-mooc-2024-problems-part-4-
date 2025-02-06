# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(integer,string):
    if(string == ""):
        string = "*"
    
    print(string[0] * integer)

def shape(width,triangle_fill,height,rectangle_fill):
    cur_triangle_row = 1
    while cur_triangle_row <= width:
        line(cur_triangle_row,triangle_fill) 
        cur_triangle_row += 1
    
    cur_rectangle_row = 1
    while cur_rectangle_row <= height:
        line(width,rectangle_fill) 
        cur_rectangle_row += 1
        
    
if __name__ == "__main__":
    shape(3, ".", 0, ",")