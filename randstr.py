import random
import string
import click

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

@click.command()
@click.argument('length')
def main(length):
    try:
        length = int(length)
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        print(''.join(randlst))
    except:
        print('./randstr [length]')
    

if __name__ == '__main__':
    main()
