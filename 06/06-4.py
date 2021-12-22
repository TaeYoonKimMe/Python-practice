def impactWord(word):
    letter = ""
    total = ""
    count = 0
    for i in range(len(word)):
        if letter != word[i]:
            letter = word[i]
            if count:
                total = total + str(count)
            total = total + word[i]
            count = 1
            if i == len(word)-1:
                total = total + str(count)
        else:
            count += 1

    print(total)

impactWord("aaabbccccccaaaab")

