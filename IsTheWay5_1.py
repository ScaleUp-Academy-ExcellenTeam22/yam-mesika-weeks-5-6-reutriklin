from os import listdir

def beginWithDeep(path):
    return [file for file in os.listdir(path) if file.startswith("deep")]
    

beginWithDeep("C:\excellents\yam-mesika-weeks-5-6-reutriklin\images")
