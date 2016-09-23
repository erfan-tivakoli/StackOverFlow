__author__ = 'Rfun'
import os

def main():
    for file_name in os.listdir('./Sample_datas'):
        with open('Sample_datas/'+file_name) as f:
            print('opened')


if __name__ == '__main__':
    main()