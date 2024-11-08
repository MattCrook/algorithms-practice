#--------------------------------------------------------#
# Write a function that takes in a number in Fahrenheit and converts it to Celsius.
#--------------------------------------------------------#
import math



class FahrenheitToCelsius(object):
    def convert_f_to_c(self, x):
        c = math.floor((x - 32) * (5/9))
        solution = {
          "fahrenheit": x,
          "celsius": c,
        }

        return solution

    def convert_c_to_f(self, x):
      f = math.floor(x * 9/5) + 32
      solution = {
          "celsius": x,
          "fahrenheit": f,
        }

      return solution



sol_1 = FahrenheitToCelsius()
print("F to C: ", sol_1.convert_f_to_c(65))
print("C to F: ", sol_1.convert_c_to_f(18))
print("--------------------------")




def fahrenheit_to_celsius(x):
  c = math.floor((x - 32) * (5/9))

  sol = {
    "fahrenheit": x,
    "celsius": c,
  }

  return sol


print(fahrenheit_to_celsius(65))
print("--------------------------")
