def solution(phone_book):
    answer = True
    index = 1
    for standard in phone_book:
        for compare_num in range(index, len(phone_book)):
            if phone_book[compare_num].rfind(standard) == 0:
                return False
        index += 1
    return answer
