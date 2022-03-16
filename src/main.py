"""
author: L
date: 2022/3/16 14:23
"""

from load_data import Data
from parse import args

if __name__ == "__main__":
    print(args)
    data_generator = Data(path=args.data_path + args.dataset, batch_size=args.batch_size, maxlen=args.maxlen)
    # train(data_generator, args)
