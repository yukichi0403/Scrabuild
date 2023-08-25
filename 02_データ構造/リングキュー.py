#リングキュー
class RingQueue:
    def __init__(self,size:int):
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.no = 0

    def enqueue(self,a:int):
        if self.no < self.size :
            self.queue[self.tail] = a
            self.tail += 1
            self.no += 1
            if self.tail == self.size:
                self.tail = 0
        else:
            print('queue is full')
    
    def dequeue(self):
        if self.no > 0:
            tmp = self.queue[self.head]
            self.head += 1
            self.no -= 1
            print(tmp)
            #全て埋まったら0にする＝最初に戻る
            if self.head == self.size:
                self.head = 0
        else:
            print('queue is empty')