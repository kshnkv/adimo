class Cat:
    def setChar(self, w, c):
        self.weight = w
        self.color = c
        
cat1=Cat()
cat1.setChar("15", "Black")

cat2=Cat()
cat2.setChar("11", "White")

print (cat1.weight, cat1.color)
print (cat2.weight, cat2.color)
