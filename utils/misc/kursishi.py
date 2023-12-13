import math



def trapetsiya(a, b, n, integral):
    x=0
    try:
        exec(integral)
    except Exception as e:
        print(e)
        return {"status": False, "data": "Tenglamada imloviy xatolik mavjud!"}
            
    def fx(x: float):
        return eval(integral)
    
    delta_x = (b-a)/n
    h = delta_x
    
    x_list = [x0+h for x0 in range(n+1)]
    y_list = [fx(x=x) for x in x_list]
    
    result = delta_x*((y_list[0]+y_list[-1])/2+sum([y_list[i] for i in range(1, len(y_list)-1)]))
    return {"status": True, "data": result} 




def rectangle(a, b, n, integral):
    x = 0
    h = (b-a)/n

    try:
        exec(integral)
    except Exception as e:
        print(e)
        return {"status": False, "data": "Tenglamada imloviy xatolik mavjud!"}
    
    def fx(x: float):
        return eval(integral)
    
    x_list = [a+h*i for i in range(n+1)]
    y_list = [fx(x) for x in x_list]
    
    result = h*sum([y_list[i] for i in range(1, n)])
    
    return {"status": True, "data": result}


