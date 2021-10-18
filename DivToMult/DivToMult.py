import os;

def dtm(valueToMultiply, result):
    x = result / valueToMultiply;
    print("(",x,")");

while True:
    v = float(input("Value to multiply: "));
    r = float(input("Result: "));
    print("");
    dtm(v,r)
    input(("\nPress ENTER..."))
    os.system("cls" if os.name == "nt" else "clear")
