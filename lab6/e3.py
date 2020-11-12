def find(string, match):
    match_count = 0

    for letter in string:
        if letter == match[match_count]:
            match_count += 1
        else:
            if letter == match[0]:
                match_count = 1
            else:
                match_count = 0

        if match_count == len(match):
            return True

    return False
    