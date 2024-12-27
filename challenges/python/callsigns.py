################################################
# Find given target, other wise replace with asterisk.
#
# - find bb in abbc, and covert it to a**bb**c.
#
# - find cd in adcdef and convert it to a**d**cd**e**f

###################################################

callsign_01 = "abbc"
callsign_02 = "adcdef"



class Solution(object):
  def solution_01(self, callsigns, target):
      new_callsigns = []
      for callsign in callsigns:
          for i in range(len(callsign)):
              print(callsign[i: i+len(target)])
              if callsign[i: i+len(target)] == target:
                  #new_callsigns.append(i)
                  new_callsigns.append(callsign[i: i+len(target)])
              else:
                  new_callsigns.append("*")
      return ''.join(new_callsigns)




#   def solution_02(self, callsign, target):
    #   solution = []
    #   if target not in callsign:
    #       return "Callsign not found"
    #   # callsign_letters = [ch for ch in callsign]
    #   # can also use the list() function
    #   letters = list(callsign)
    #   l = len(letters)
    #   for i in range(l):
    #     current = letters[i]
    #     left =  letters[i - 1]
    #     right = letters[i + 1]
    #     start = i + 1
    #     stop = l - 1
    #     while start <= stop:
    #       if current + left != target:
    #           solution.extend(["*", current])
    #           start = start + 1
    #       else:
    #           solution.extend(target)
    #       if current + right != target:
    #         solution.extend([i, "*"])
    #         stop = stop - 1
    #       else:
    #           solution.extend([target])
    #   return solution
      
      
      
    #   callsign_letters = [ch for ch in callsign]
    #   # can also use the list() function
    #   # l = list(callsign)
    #   input_length = len(callsign_letters)
    #   for i in range(input_length):
    #       left = i + 1
    #       right = input_length - 1
    #       while left < right:
    #           mid = (left + right) // 2
    #           if callsign_letters[i] + callsign_letters[left] == target:
    #               return
    #           if callsign_letters[i] + callsign_letters[right] == target:
    #               return
    #           callsign_letters[i] = "*"


solution = Solution()
print(solution.solution_01(callsign_01, "bb")) # "*bb**"
print(solution.solution_01(callsign_02, "cd")) # **cd***
print("--------------")
print(solution.solution_02(callsign_01, "bb"))
print(solution.solution_02(callsign_01, "cc"))
