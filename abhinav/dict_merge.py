def merge_dict():
    dict1 = {'a':1,'b':3,'c':5}
    dict2 = {'a':21, 'e':33, 'f':344}
    
    dict1.update(dict2)
    d={}
    d=dict1.copy()
    print(d)

if __name__ == "__main__":    
    merge_dict()        
