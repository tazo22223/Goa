# ცვლადის შექმნა, რომელიც შეიცავს ინტეჯერს
number = 10

try:
    # TypeError-ის პროვოცირება
    result = number + "სტრინგი"
except TypeError as e:
    print("TypeError გამოვლინდა:", e)
