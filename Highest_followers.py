#Logic function to return highest followers in the Github
followers = {'Sally': 3, 'Ken': 5, 'Michael': 2}
highest = max(followers.values())
n = [k for k, v in followers.items() if v == highest]
str1 = ', '.join(n)
print(str1, 'got the highest followers')