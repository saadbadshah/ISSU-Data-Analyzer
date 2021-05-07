import click
from JsonData import JsonData

@click.command()

@click.option('--u', default=False, help="Enter User UUID")
@click.option('--d', default=False, help="Enter Doc UUID")
@click.option('--t', default=False, help="Enter Task ID")
@click.option('--f', default=False, help="Enter File Name")

## To run: python cw2.py --d 130213181706-22ed1502eac642129c9cc9ebdd6e28b2 --t 2b --f data.txt

def main(u,d,t,f):
   test1 = JsonData(f)
   if t == '2a':
       test1.DisplayCountry(d)
   if t == '2b':
       test1.CountryContrinent(d)
   if t == '3a':
       test1.Browser3a()
   if t == '3b':
       test1.Browser3b()
   if t == '4':
       test1.Readerprofile()
   if t == '5d':
       test1.AlsoLikes5d(u)


 #  print (command)


if __name__ == '__main__':
       main()
