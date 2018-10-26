import geometry

data = input("Enter Radius of " + 
" a circle:")
radius = float(data)

print ("Area of a circle: {:.2f}"
.format(geometry.area_circle(radius)))