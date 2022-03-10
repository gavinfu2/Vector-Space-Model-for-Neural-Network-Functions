import numpy as np

def inner_product(a,b):
        print("Vectors : ")
        print("a = ", a)
        print("\nb = ", b)

        print("\nInner profuct of vectors =")
        print(np.inner(a, b))
        print("-----------------------")

def norm(a):
    norm = np.linalg.norm(a)
    print(norm)
    print("-----------------------")

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    print("-----------------------")

# Test
a=np.array([1,2,4])
b=np.array([6,1,9])
inner_product(a,b)
print("norm o [1,2,4]: ")
norm(a)
print("norm o [6,1,9]: ")
norm(b)
print("angle of A")
print(angle_between(a,b))

x=np.array([1,1,3,1,2])
y=np.array([9,8,5,2,1])
inner_product(x,y)
print("norm of [1,1,3,1,2]: ")
norm(x)
print("norm of [9,8,5,2,1]: ")
norm(y)
print("angle of B")
print(angle_between(x,y))