
def multi_get_letter(str_input):

    if isinstance(str_input, unicode):
        unicode_str = str_input
    else:
        try:
            unicode_str = str_input.decode('utf8')
        except:
            try:
                unicode_str = str_input.decode('gbk')
            except:
                print 'unknown coding'
                return

    return_list = []
    for one_unicode in unicode_str:
        return_list.append(single_get_first(one_unicode))
        print return_list
    return return_list

def single_get_first(strs):
    pinyin = ''
    for str in strs:
        try:
            str = str.encode('gbk')
            ord(str)
            if str == ' ' or str == '_' or str == '/' or str == '-'  or str == '.'  or str == '\''  or str == '"':
                continue
            pinyin = pinyin + str
        except:
            try:
                asc = ord(str[0]) * 256 + ord(str[1]) - 65536
            except:
                return ''
            if asc >= -20319 and asc <= -20284:
                 pinyin = pinyin + 'a'
            if asc >= -20283 and asc <= -19776:
                 pinyin = pinyin + 'b'
            if asc >= -19775 and asc <= -19219:
                 pinyin = pinyin + 'c'
            if asc >= -19218 and asc <= -18711:
                 pinyin = pinyin + 'd'
            if asc >= -18710 and asc <= -18527:
                 pinyin = pinyin + 'e'
            if asc >= -18526 and asc <= -18240:
                 pinyin = pinyin + 'f'
            if asc >= -18239 and asc <= -17923:
                 pinyin = pinyin + 'g'
            if asc >= -17922 and asc <= -17418:
                 pinyin = pinyin + 'h'
            if asc >= -17417 and asc <= -16475:
                 pinyin = pinyin + 'j'
            if asc >= -16474 and asc <= -16213:
                 pinyin = pinyin + 'k'
            if asc >= -16212 and asc <= -15641:
                 pinyin = pinyin + 'l'
            if asc >= -15640 and asc <= -15166:
                 pinyin = pinyin + 'm'
            if asc >= -15165 and asc <= -14923:
                 pinyin = pinyin + 'n'
            if asc >= -14922 and asc <= -14915:
                 pinyin = pinyin + 'o'
            if asc >= -14914 and asc <= -14631:
                 pinyin = pinyin + 'p'
            if asc >= -14630 and asc <= -14150:
                 pinyin = pinyin + 'q'
            if asc >= -14149 and asc <= -14091:
                 pinyin = pinyin + 'r'
            if asc >= -14090 and asc <= -13119:
                 pinyin = pinyin + 's'
            if asc >= -13118 and asc <= -12839:
                 pinyin = pinyin + 't'
            if asc >= -12838 and asc <= -12557:
                 pinyin = pinyin + 'w'
            if asc >= -12556 and asc <= -11848:
                 pinyin = pinyin + 'x'
            if asc >= -11847 and asc <= -11056:
                 pinyin = pinyin + 'y'
            if asc >= -11055 and asc <= -10247:
                 pinyin = pinyin + 'z'
    return pinyin.upper()