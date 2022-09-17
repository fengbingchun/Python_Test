import argparse
import sys

# Blog: https://blog.csdn.net/fengbingchun/article/details/126909875

print("sys.argv:", sys.argv)

parser = argparse.ArgumentParser(description="test argparse's use", add_help=True)

var = 4
if var == 1:
    parser.add_argument("integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator") # positional argument
    parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max, help="sum the integers(default: find the max)") # optional argument

    args = parser.parse_args()
    print(args.accumulate(args.integers)) # print either the sum or the max of the command-line integers
elif var == 2: # nargs
    parser.add_argument('--foo', nargs='?', const='c', default='d')
    args = parser.parse_args()
    print(args.foo) # print 'c' or 'd' or command-line input
elif var == 3: # choices
    parser.add_argument('addr', type=str, choices=['csdn', 'github'])
    args = parser.parse_args()
    print("addr:", args.addr)
elif var == 4: # metavar
    parser.add_argument('--foo')
    parser.add_argument('--bar', metavar='XXX')
    args = parser.parse_args()
elif var == 5: # required
    parser.add_argument("--addr", type=str, help="github address", required=True)
    args = parser.parse_args()
    print("addr:", args.addr)

print("test finish")