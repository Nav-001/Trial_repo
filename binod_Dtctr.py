import os        

file = os.listdir()

def cb(file):
    for item in file:
        # if(item.endswith("txt")):
        if item.endswith('txt'):
            with open(item) as f:
                f1 = f.read()
            if "binod" in f1.lower():
                print(f" We had found the binod , {item} ke andar")
            else:
                print(f"we didn't find binod in {item} ")
            
cb(file)





