#Print out 'e' using indexing
s='hello'
print(s[1])
#Reverse the string 'hello' by slicing
print(s[::-1])
#Print out "o" in the string 'hello' using indexing in 2 diffrent methods
print(s[4])
print(s[-1:])
#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,"hello"]]
list3[2][2]="goodbye"
print(list3)
#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])