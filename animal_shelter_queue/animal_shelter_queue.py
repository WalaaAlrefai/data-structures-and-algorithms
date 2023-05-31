from stack_and_queue.stack_and_queue import Queue, Node

class AnimalShelter():
    def __init__(self,type:str=None, name:str=None) -> str:
        self.type = type
        self.name = name
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self,animal:str) -> str:
        if animal.type == "cat":
            self.cats.enqueue(animal)
        elif animal.type == "dog":
            self.dogs.enqueue(animal)
        else:
            return "null"
        
    def dequue(self, pref:str) ->str :
        if pref == "cat":
            return self.cats.dequeue()
        elif pref =="dog":
            return self.dogs.dequeue()
        else:
            return "null"


if __name__ == "__main__":
    a1 = AnimalShelter()
    print(a1)