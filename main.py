import os, sys, get_args

args = get_args.get()
if args.type == '1':
    print(sys.version)
elif args.type == '2':
    os.mkdir(args.name)
elif args.type == '3':
    print(os.listdir(os.pardir))
