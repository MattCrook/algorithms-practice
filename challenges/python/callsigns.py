# find bb
# in
# abbc 
# a**bb**c

# find cd
# in
# adcdef
# a**d**cd**e**f

# Super simple
# find target, other wise replace with asterisk
def solution(callsigns, target):
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

print(solution(["accbc"], "cc"))
"*cc***"
