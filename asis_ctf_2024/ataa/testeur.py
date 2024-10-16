import sys
from math import gcd

red = '\033[31m'
green = '\033[32m'
reset = '\033[0m'
blue = '\033[34m'
yellow = '\033[93m'

nbit = 128
u = 170141183460469231731687303715884105727
v = 170141183460469231731687303715884105757
w = 170141183460469231731687303715884105779
x = 170141183460469231731687303715884105799
y = 170141183460469231731687303715884105851
z = 170141183460469231731687303715884105871
k = 170141183460469231731687303715884105889 # can be equal to one of before


def main():
    p = sys.argv[1]

    print(f"{blue}p = {p}\n{reset}")

    try:
        if u.bit_length() == v.bit_length() == w.bit_length() == x.bit_length() == \
           y.bit_length() == z.bit_length() == nbit and k.bit_length() >= nbit:
            print(f"{green}u, v, w, x, y, z bit_length() == 128 et k.bit_length() >=128\n{reset}")
    except:
        print(f"{red}u, v, w, x, y, z bit_length() != 128 ou k.bit_length() < 128\n{reset}")
        return

    if len(set([u, v, w, x, y, z])) == 6:
        print(f"{green}pas de duplicate dans les 6 premiers\n{reset}")
    else:
        print(f"{red}c'est non pour les duplicates\n{reset}")
        return

    # all(map(...))

    # if gcd(u, v, w, x, y, z, k, p) == 1:
    gcd_r = gcd(u, v, w, x, y, z, k)
    if gcd_r == 1:
        print(f"{green}plus grand diviseur commun est bien 1\n{reset}")
    else:
        print(f"{red}plus grand diviseur commun {gcd_r}\n{reset}")
        return

    # puissance

    print(f"{blue}test ok prêt à envoyer dans le prompt de nc")
    print("Les valeurs à mettre:\n\n")
    print(f"{yellow}{u}, {v}, {w}, {x}, {y}, {z}, {k}{reset}")

if __name__ == '__main__':
    main()