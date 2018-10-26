import geometry

inputs = input("Enter the side lengths of a tringle :" )
#radius = float(data)
(a,b,c)= (float(x) for  x in inputs.split(","))
P = geometry.triangle_perimeter(a,b,c)
A = geometry.triangle_heronsarea(a,b,c)

print ("Perimeter:{:.2f}".format(P))
print ("Area:{:.2f}".format(A))

