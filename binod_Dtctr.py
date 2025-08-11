import os        

file = os.listdir()

def cb(file):
    for item in file:
        # if(item.endswith("txt")):
        if item.endswith('txt'):
            with open(item) as f:
                f1 = f.read()
            if "binod" in f1.lower():
                print(f"binod mil gaya bhai , {item} ke andar")
            else:
                print(f"{item} ke andar nahi mila sala")
            
cb(file)




