def manual_range(start, end, step):
    # ვქმნით დიაპაზონს
    range_list = list(range(start, end, step))
    #ვბეჭდავთ მხოლოდ ლუწ რიცხვებს
    for num in range_list:
        f num % 2 == 0:
        print(num)
