def matching(regex, char):
    if len(regex) == 0 and len(char) == 0:
        return True
    elif len(regex) == 0:
        return True
    elif len(char) == 0:
        return False
    elif regex == '.':
        return True
    else:
        return regex == char


def equal_length_matching(regex, char):
    if len(regex) in (0, 1) or len(char) in (0, 1):
        return matching(regex, char)
    for r, c in zip(range(len(regex)), range(len(char))):
        if matching(regex[r], char[c]):
            if regex[r] == regex[-1]:
                return True
            elif regex[r] != regex[-1] and char[c] == char[-1]:
                return False
        else:
            return False


def not_equal_length_matching(regex, char):
    r, c, n = 0, 0, 0
    if len(regex) == 0 or len(char) == 0:
        return matching(regex, char)
    else:
        while n < min(len(regex), len(char)):
            if matching(regex[r], char[c]):
                if regex[r] == regex[-1]:
                    return True
                elif regex[r] != regex[-1] and char[c] == char[-1]:
                    return False
                r += 1
                c += 1
                n += 1
            else:
                if char[c] == char[-1]:
                    return False
                c += 1


def begin_matching(regex, char):
    if len(regex) == 0:
        return True
    else:
        if len(char) == 0:
            return False
        else:
            if not matching(regex[0], char[0]):
                if regex.find(regex[0]) == len(regex) - 1:
                    return False
                else:
                    if regex[0] == '\\':
                        if regex[1] == char[0]:
                            return begin_matching(regex[2:], char[1:])
                        else:
                            return False
                    else:
                        if regex[1] in '?*':
                            if regex[1] != regex[-1]:
                                return begin_matching(regex[2:], char[0:])
                        else:
                            return False
            else:
                if regex.find(regex[0]) == len(regex) - 1:
                    return True
                else:
                    if regex[0] == '\\':
                        if regex[1] == char[0]:
                            return begin_matching(regex[2:], char[1:])
                        else:
                            return False
                    else:
                        if regex[1] == '?':
                            return begin_matching(regex[2:], char[1:])
                        elif regex[1] == '*':
                            if char[0] == char[-1]:
                                return True
                            else:
                                return begin_matching(regex, char[1:])
                        elif regex[1] == '+':
                            if char[0] == char[-1]:
                                return True
                            else:
                                if char[0] != char[1]:
                                    return begin_matching(regex[2:], char[1:])
                                else:
                                    return begin_matching(regex, char[1:])
                        else:
                            return begin_matching(regex[1:], char[1:])


def end_matching(regex, char):
    if regex == '' and len(char) != 0:
        return False
    elif len(regex) == 0 or len(char) == 0:
        return matching(regex, char)
    elif regex == '.':
        return True
    else:
        if matching(regex[0], char[0]):
            if regex[0] == regex[-1]:
                return end_matching(regex[1:], char[1:])
            else:
                if regex[1] == '?':
                    pass
                elif regex[1] == '*':
                    pass
                elif regex[1] == '+':
                    if char[0] != char[1]:
                        return end_matching(regex[2:], char[1:])
                    else:
                        return end_matching(regex, char[1:])
                else:
                    return end_matching(regex[1:], char[1:])
        else:
            if regex[0] == '\\':
                if regex[1] == char[0]:
                    return end_matching(regex[2:], char[1:])
                else:
                    return end_matching(regex, char[1:])
            elif regex[0] == '+':
                pass
            elif regex[0] == '?':
                pass
            elif regex[0] == '\\':
                pass
            else:
                return end_matching(regex, char[1:])


def recur_matching(regex, char):
    if len(regex) == 0 or len(char) == 0:
        return matching(regex, char)
    if begin_matching(regex, char):
        return begin_matching(regex, char)
    else:
        return recur_matching(regex, char[1:])


def match(regex, char):
    if regex.startswith('^') and regex.endswith('$'):
        regex = regex.strip('^$')
        return begin_matching(regex, char) and end_matching(regex, char)
    elif regex.startswith('^'):
        regex = regex.strip('^')
        return begin_matching(regex, char)
    elif regex.endswith('$'):
        regex = regex.strip('$')
        return end_matching(regex, char)
    else:
        return recur_matching(regex, char)
