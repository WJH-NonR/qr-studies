data = [69, 70, 135, 71, 71, 7, 51, 162, 242, 246, 71, 38, 151, 102, 82, 230, 118, 246, 246, 118, 198, 82, 230, 54, 246, 210, 246, 71, 38, 151, 102, 82, 246, 102, 246, 198, 70, 87, 39, 50, 243, 16, 0, 0, 0, 0, 0, 22, 213, 35, 135, 116, 215, 84, 55, 100, 224, 0, 0, 0, 0, 0, 0, 0, 0, 20, 162, 215, 151, 54, 228, 102, 21, 35, 247, 87, 55, 3, 215, 54, 134, 23, 38, 150, 230, 112, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 31, 195, 0, 0, 0, 0, 0, 0, 0, 0, 88, 187, 92, 127, 0, 0, 0, 0, 0, 0, 204, 145, 219, 41, 0, 0]

b41s = [1<<4 | i for i in range(1<<4)]
b47s = [i<<5 | 0b10110 for i in range(1<<3)]
b56s = [0b111<<5 | i for i in range(1<<5)]
b65s = [i<<5 | 0b10100 for i in range(1<<3)]
b110s = [0b110<<5 | i for i in range(1<<5)]
b117s = [i << 5 | 0b01101 for i in range(1<<3)]
b127s = [i << 5 | 0b00110 for i in range(1<<3)]
pos = [42,43,44,45,46,57,58,59,60,61,62,63,64,111,112,113,114,115,116,122,123,124,125,126,132,133]

from Crypto.Util.number import long_to_bytes, bytes_to_long
from string import ascii_letters, digits
c = (digits+ascii_letters+'-_').encode()

from itertools import product
def work(b56):
    import creedsolo
    rs = creedsolo.RSCodec(26)
    with open(f'qr/{b56-224}.txt', 'w') as f:
        data[56] = b56
        cnt = 0
        for b41, b47, b65, b110, b117, b127 in product(b41s, b47s, b65s, b110s, b117s, b127s):
            data[41] = b41
            data[47] = b47
            data[65] = b65
            data[110] = b110
            data[117] = b117
            data[127] = b127
            dec, _, _ = rs.decode(data, erase_pos=pos)
            shift = long_to_bytes(bytes_to_long(dec)<<4)
            if all(i in c for i in shift[41:67]):
                print(shift[2:86])
                print(shift[2:86], file=f, flush=True)
            cnt += 1
            if (b56 == 224 and cnt % 10000 == 0):
                print(f'{b56-224:>2}:{cnt/2**21*100}%')

from multiprocessing import Pool
with Pool(32) as p:
    p.map(work, b56s)