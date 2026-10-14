song_duration = [2.06,3.07,1.59,4.51,5.01]

new_arr = list(map(lambda n:int(n)*60+ round((n %1) *100),song_duration))
print(new_arr)