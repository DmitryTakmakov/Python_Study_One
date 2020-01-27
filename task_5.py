rating = [4, 9, 14, 19, 24]
user_rating = int(input('Please enter a rating position:\n'))
rating.append(user_rating)
rating.sort(reverse=True)
print(rating)
