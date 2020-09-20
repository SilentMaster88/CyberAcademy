import subprocess as sp
import multiprocessing as mp


def main():
    '''
    for i in range(100000, 999999):

        if i % 10000 == 0:
            print(i)
        test = crack_cycle(str(i))
        if test == 1:
            break
    '''

    seq = ('{:06d}'.format(i) for i in range(1000000))
    pool = mp.Pool()
    for res in pool.imap_unordered(crack_cycle, seq):
        if res == 1:
            break


def crack_cycle(password):
    print(password)
    p = sp.Popen(['/home/jack/PycharmProjects/bruteforce1/crackme.sh', password], stdout=sp.PIPE)
    out, err = p.communicate()

    if out.decode('UTF-8').strip() != "Access Denied.":
        print("La password è: ", password)
        return 1

if __name__ == '__main__':
    main()
