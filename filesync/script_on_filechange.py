#!/usr/bin/python 

import argparse
import os
import fabric
from fsevents import Observer
from fsevents import Stream
import signal
import sys 

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)

def callback(subpath, operation, remote):
    print "rsync %s %s" % (subpath, remote)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    parser = argparse.ArgumentParser(description='Sync files to a remote server of scp.')
    parser.add_argument('path', type=str, metavar=('local', 'remote'), nargs=2,
                        help='path for the monitor')

    args = parser.parse_args()
    print args.path
    observer = Observer()
    stream = Stream(lambda x, y: callback(x,y, args.path[1]), args.path[0])
    observer.schedule(stream)
    try:
      observer.start()
      while True:      # instead of this infinite loop, you can do
         pass          # whatever processing you wanted
    except KeyboardInterrupt:
      observer.stop()




if __name__ == "__main__":
    main()
