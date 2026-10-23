
call_duration = (12, 5, 0, 20, 7, 3, 15)
list_call = list(call_duration)
for i in list_call:
    if i <5:
        list_call.remove(i)
final_tup = ("Updated Tuple : ",tuple(list_call))
print(final_tup)
