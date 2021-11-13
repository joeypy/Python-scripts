def is_prime(number):
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            return False
    return True
    
def run():
    number = int(input("Escriba el número: "))
    if is_prime(number):
        print(f"El número '{number}' es primo")
    else:
        print(f"El número '{number}' NO es primo")
   

if __name__ == '__main__':
    run()     
        