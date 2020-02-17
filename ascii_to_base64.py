#Happy
#72 97 112 112 121
#010010 000110 000101 110000 011100 000111 100100 000000
#18 6 5 48 28 7 36 0
#S G F w c H k =

def get_pad_size(msg):
    cnt = len(msg)*8 -1
    mok = int(cnt / 24)
    padsize =int((mok+1)*24)

    space_cnt = (padsize - cnt) // 8

    return (padsize, space_cnt)

def get_bitpattern(string):

    res = ''

    for msg in string:

        top_bit = 128
        idx = 0
        text_num = ord(msg)

        while True:
            mok = text_num // top_bit
            text_num = text_num - (top_bit*mok)
            top_bit //= 2

            res += str(mok)

            if top_bit <= 1:
                res += str(text_num)
                break
            idx += 1

    pad_size, null_cnt = get_pad_size(string)
    fixed_bitarray = res.ljust(pad_size,'0')

    if null_cnt != 0:
        fixed_bitarray = fixed_bitarray[:-null_cnt*6]+("x"*6*null_cnt)

    return fixed_bitarray

def split_bitpattern(bitstring):
    return [bitstring[i*6:(i+1)*6] for i in range(int(len(bitstring)/6))]

def base64(msg):

    b64_table = {
        0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',
        11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',
        21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',
        31:'f',32:'g',33:'h',34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',
        41:'p',42:'q',43:'r',44:'s',45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',
        51:'z',52:'0',53:'1',54:'2',55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',
        61:'9',62:'+',63:'/'
    }
    #rerv_b64_table = dict((v, k) for k, v in b64_table.items())

    replaced_str = ''

    split_list = split_bitpattern(get_bitpattern(msg))

    for string in split_list:
        b64_idx = 0
        bit_num = 32

        if string == "xxxxxx":
            replaced_str += "="

        else:
            for ch in string:
                b64_idx += int(ch)*bit_num
                bit_num //= 2

            replaced_str += b64_table[b64_idx]

    return replaced_str

if __name__ == "__main__":

    msg = input("Base64-Encoding >> ")

    r_msg = base64(msg)

    print(r_msg)