#!/usr/bin/env python
import click

@click.command()
def hello():
    print('Hellow world')
    
    if __name__ == '__main__':
        return 0
hello()