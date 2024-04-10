def telephone_number(numbers):
    cleaned_numbers = []
    for number in numbers:
        cleaned_number = (
            number.replace('-', '')
                  .replace('+', '')
                  .replace(' ', '')
                  .replace('(', '')
                  .replace(')', '')
        )
        if (cleaned_number.startswith('7') or cleaned_number.startswith('8')) \
           and len(cleaned_number) == 11:
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10:
            cleaned_number = '495' + cleaned_number
        cleaned_numbers.append(cleaned_number)
    results = []
    for number in cleaned_numbers[1:]:
        if number == cleaned_numbers[0]:
            results.append('YES')
        else:
            results.append('NO')
    return results


numbers = [input() for _ in range(4)]
for result in telephone_number(numbers):
    print(result)
