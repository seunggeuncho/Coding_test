def solution(phone_book):
    answer = True
    index = 1
    phone_book.sort(key=len)
    phone_book.sort()
    for index in range(len(phone_book)):
        if index + 1 == len(phone_book):
            break
        if phone_book[index + 1].rfind(phone_book[index]) == 0:
            return False
    return answer
