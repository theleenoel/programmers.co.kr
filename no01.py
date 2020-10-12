def solution(n, lost, reserve):
    answer = 0
     
    for i in lost:              
        if i-1 in reserve:      
            reserve.remove(i-1) 
            answer+=1          
        elif i+1 in reserve:    
            reserve.remove(i+1) 
            answer+=1           
            
    return n-len(lost)