class Rectangle():
  def __init__(self, width, height):
      self.width = width
      self.height = height


  def __str__(self):
      return f"Rectangle(width={self.width}, height={self.height})"


  def set_width(self, new_width):
      self.width = new_width


  def set_height(self, new_height):
      self.height = new_height


  def get_area(self):
      area = self.width * self.height
      return area


  def get_perimeter(self):
      perimeter = (2 * self.width) + (2 * self.height)
      return perimeter


  def get_diagonal(self):
      diagonal = ((self.width**2 + self.height**2) **.5)
      return diagonal


  def get_picture(self):
      if self.width > 50 or self.height > 50:
          return "Too big for picture."
      else:
          width = (self.width * "*") + "\n"
          picture = self.height * width
          return picture


  def get_amount_inside(self, shape):
      w_int_qty = self.width // shape.width #=> comparing the polygons width
      h_int_qty = self.height // shape.height #=> comparing the polygons height
      #number of times the shape fits in the rectangle:
      qty_pol_inside = w_int_qty * h_int_qty
      return qty_pol_inside

class Square(Rectangle):
  def __init__(self, side):
      self.side = side
      width = self.side
      height = self.side
      super().__init__(width, height)


  def __str__(self):
      return f"Square(side={self.side})"


  def set_side(self, new_side):
      self.side = new_side
      self.width = new_side
      self.height = new_side


  def set_width (self, new_width):
      self.set_side(new_width)


  def set_height(self, new_height):
      self.set_side(new_height)
    