import numpy as np
import pandas as pd

#функция с вызовом numpy
def my_numpy():
    arr = np.array([1,2,3,4,5,8,11])
    print(arr)
    print(type(arr))
    
#функция с вызовом pandas
def my_pandas():
    a = [1,2,3,4,5,8,11]
    myvar = pd.Series(a)
    print(myvar)
    #print("")
    #print(myvar[1])
    
#Точка входа в программу
def main():
    my_numpy()
    print("")
    my_pandas()
    return 0

if __name__ == '__main__':
    main()

