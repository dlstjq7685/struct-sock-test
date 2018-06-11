import threading

class myth(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.objects = objects
        return

    def run(self):
        print('thread')
        return

def main():
    ths = myth()

    print('buck you')

    ths.start()

    ths.join()

if __name__=='__main__':
    main()