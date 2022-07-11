def find_area(f):
  a=f[0]*(f[3]-f[5])
  b=f[2]*(f[5]-f[1])
  c=f[4]*(f[1]-f[3])
  return(abs(a+b+c))

def my_main():
    areas = {} 
    n = int(input())
    for _ in range(n):
      l=list(map(float,input().split()))
      areas[find_area(l)] = l

    for _ in range(0,n):
        for area,ver in areas.items():
            print(f"Area of rectangle with vertices ({ver[0]},{ver[1]}),({ver[2]},{ver[3]}),({ver[4]},{ver[5]}) is {area}")

if __name__ == '__main__':
    my_main()