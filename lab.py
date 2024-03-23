class BMI:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return (self.weight == other.weight) and (self.height == other.height)
        return False
