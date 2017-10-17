import math
import os
'''
প্রবলেমঃ
একটা প্রোগ্রাম লিখেন । যে প্রোগ্রামে ইনপুট "p132" 132 বা p এর পর যে কোন সংখ্যা দিলে প্রাইম কিনা বের করবে । আর "m12" বা m এর পর যে সংখ্যা থাকুক না কেন তার নামতা লেখবে 100 পর্যন্ত ।
..
দ্বিতীয় ধাপ । 100 পর্যন্ত নামতা লেখার পর c ড্রাইভে m12 নামের টৈক্সট ফাইলে নামতা সেভ করবে ।
....
input: p7
output: prime number
input: p8
output: not prime
input: m7
output: 7×1=7
7×2=14
.....100 পর্যন্ত । তারপর c ড্রাইভে m7.txt ফাইলে নামতা লিখে রাখবে ।
'''


def is_prime(n):
    '''Return 'Ture' if n is a prime number. Otherwise Return 'False'. '''
    if n == 1:
        return False
    if n == 2:
        return True
    max_div = math.floor(math.sqrt(n))
    for d in range(3, max_div + 1, 2):
        if n % d == 0:
            return False
    return True


def multiplexer_save(n, file_name):
    '''Multiply n on 1 to 100 times and save it to C:\Multiplexer\ Location.'''
    folder_path = r'C:\\Multiplexer\\'
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    with open(folder_path + file_name, 'w') as f:
        for mul in range(1, 101):
            f.write('{} * {} = {}\n'.format(n, mul, n * mul))
    print('Done!')
    print('Go to "C:\\Multiplexer\\" to see the output.')


def main():
    user_input = input('Input: ')
    if str(user_input).startswith('p'):
        try:
            number = int(user_input[1:])
            if is_prime(number):
                print('Output: Prime Number.')
            else:
                print('Output: Not Prime.')
        except Exception as e:
            print(e)

    elif str(user_input).startswith('m'):
        try:
            number = int(user_input[1:])
            file_name = str(user_input) + '.txt'
            multiplexer_save(number, file_name)
        except Exception as e:
            print(e)
    else:
        print('Enter a valid input.')

if __name__ == '__main__':
    main()
