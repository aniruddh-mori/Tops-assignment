

def format_follower_count(num):
    if (num>=1000000):
        return "{:.1f}M".format(num/1000000)
    elif (num>=1000):
        return f"{num/1000}K"
    else:
        return num
print(format_follower_count(912000))
