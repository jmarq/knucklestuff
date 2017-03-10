def scramble(s):
    """ returns a 2-tuple of strings resulting from the crossed fingers of a knuckle tattoo """
    return (s[0]+s[4]+s[1]+s[5]+s[2]+s[6]+s[3]+s[7],
            s[4]+s[0]+s[5]+s[1]+s[6]+s[2]+s[7]+s[3]
            )
