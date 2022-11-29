class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
	
    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))
	
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
	
    def get_picture(self):
        string = ""
        for i in range(self.height):
            string = string + '*'*self.width + "\n"
        if len(string)>50: return "Too big for picture."
        return string

    def get_amount_inside(self, obj=None):
        self_height = self.height
        self_width = self.width
        obj_height = obj.height
        obj_width = obj.width
        
        if obj == None: return 0
        if self_height < obj_height or self_width < obj_width: return 0

        count = 0

        while self_height >= obj_height:
            if self_width%obj_width == 0:
                count += round(self_width/obj_width)
            else:
                count += round(self_width/obj_width)-1
            self_height -= obj_height
        return count

class Square(Rectangle):
	def __init__(self, side):
		self.width = side
		self.height = side

	def __str__(self):
		return f"Square(side={self.width})"

	def set_side(self, side):
		self.width = side
		self.height = side