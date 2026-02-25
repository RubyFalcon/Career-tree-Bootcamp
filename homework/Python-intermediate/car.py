class Car:
   def __init__(self,model: str, year: int, color: str,for_sale: bool):
      self.model = model
      self.year = year
      self.color = color
      self.for_sale = for_sale

   def drive(self):
      print(f"You drove the {self.color} {self.model}!")   
   def stop(self):
      print(f"You stopped the {self.color} {self.model}")

   def describe(self):
      print(f"{self.year} {self.color} {self.model}")