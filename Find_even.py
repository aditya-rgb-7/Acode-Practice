def find_even(numbers):
  result=[]
  for n in numbers:
      if n%2==0:
        
        result.append(n)
        
  return result

N = [1,2,3,4,5,6,7,8,9,10]
print(find_even(N))