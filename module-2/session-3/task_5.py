
def title_view(titles,views):
    final = []
    for title,view in zip(titles,views):
        rounded_view = round(view,-3)
        final.append((title,rounded_view))
    return final

titles = ["ironman","The Incredible hulk","Thor"]
views = [1243,2101,2810]
print(title_view(titles,views))