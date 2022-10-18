#!/usr/bin/env python3
import argparse
import readchar
import random
import time
from collections import namedtuple
import numpy as np
import pprint

def main():
    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('-utm', '--use_time_mode', type=int, required=False, help='max number of secs for time mode or maximum number of inputs for number of inputs mode')
    parser.add_argument('-mv', '--max_value', type=int, required=False,help='max number of seconds for time mode or max number of inputs for number of inputs mode')

    args = vars(parser.parse_args())

    Input=namedtuple('Input',['requested_k', 'received_k' ,'duration'])#define the namedTuple
    inputs=[]#define the list to collect the namedTuple

    print('press x to start: ')
    key = readchar.readkey()
    if key == 'x':# press x to start
        start=time.time()#start count the total time
        start_date=str(time.ctime())
        count=0
        wrong=0
        avg_duration=0
        avg_hit=0
        avg_miss=0
        while(True):
            t=random.randrange(97,122)# generate random number between ascii number of small character
            print('tape: '+ chr(t))
            partial_time_start=time.time()#start count the time for single round
            key = readchar.readkey()
            partial_time_end=time.time()
            partial_second=partial_time_end-partial_time_start#compute time for press the key
            avg_duration += partial_second
            if key == ' ':# when pressed space exit
                break

            data=Input(chr(t),key,partial_second)#create tuple
            inputs.append(data)#append tuple in the list

            count += 1

            if key != chr(t):#wrong key
                print(key+' wrong, time of response: '+str(partial_second))
                wrong += 1
                avg_miss = avg_miss + partial_second
            else:#right key
                avg_hit = avg_hit + partial_second
                print(key+' correct, time of response: '+str(partial_second))

            if args['use_time_mode'] != None:#if arg of time is set
                time_elapsed=time.time()
                second=(time_elapsed-start)
                if second >= float(args['use_time_mode']):
                    print('time: '+str(second)+' seconds')
                    break

            if args['max_value'] != None:#if arg of number is set
                if count >= args['max_value']:
                    print('typing: '+str(count))
                    break

        end=time.time()#take the final time
        duration_second=end-start#total duratioon
        avg_duration = avg_duration/count
        avg_hit = avg_hit/count
        avg_miss = avg_miss / count
        my_dict={'accuracy': (count-wrong)/count, 
                'inputs': inputs ,
                'number_of_hits': count-wrong ,
                'number_of_types': count ,
                'test_duration': duration_second ,
                'test_end': str(time.ctime()) ,
                'test_start': start_date ,
                'type_average_duration': avg_duration ,
                'type_hit_average_duration': avg_hit ,
                'type_miss_average_duration': avg_miss}
        pprint.pprint(my_dict)

if __name__ == "__main__":
    main()