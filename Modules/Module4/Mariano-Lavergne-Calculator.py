print("Area of a trapezoid Calculator")
print("""
        / ----A-----\\
       / |           \\
      /  H            \\
     /   |             \\
    /    |              \\
   /-----------B---------\\
       """)

A = int(input("How long is tha A base?:"))
H = int(input("What is the height of the trapezoid?:"))
B = int(input("How long is the B base?:"))
print("The Area of the square is:", (A+ B)/2 * H)

print()
def AreaOfTrapezoid(A, B, H):
     print(f"Area of the trapezoid is {int(A+ B)/2 * H}")
print("Base A is 5 cm")
print("Base B is 5 cm")
print("Height (H) is 5 cm")
AreaOfTrapezoid(5, 5, 5)



