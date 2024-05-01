                Checking Password:
correct_password = "password123"
attempts = 3
while attempts > 0:
    password = input("Enter Password: ")
    if password == correct_password:
        print("Correct Password")
        break 
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
else:
    print("Locked")

               
                Name Loop:
num_times = int(input("Enter a number: "))
name = input("Enter your name: ")
for _ in range(num_times):
    print(name)
              
              
               Multiplications:
  while True:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        break
    else:
        print("Not a positive integer.")

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

                
                Prime Numbers:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter an integer: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


                FizzBuzz
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

