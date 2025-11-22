class Circle:

    def __init__(self,radus):
        self.radus = radus

    def area(self):
        return 3.14*(self.radus**2)
    
    def perimeter(self):
        return 2* 3.14 * self.radus
    
c1 = Circle(10)


print(c1.area())

from datetime import date

class Person:

    def __init__(self,name,country,birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self):
        current_year = date.today().year
        return current_year - self.birth_year
    

p = Person('sardor','uzbekistan',2003)

print(p.get_age())


class Calculator:

    def __init__(self,a ,b):
        self.a = a
        self.b = b


    def qushish(self):
        return self.a + self.b
    
    def ayirish(self):
        return self.a - self.b
    
    def kupay(self):
        return self.a * self.b
    
    def bul (self):
        return self.a / self.b

cal = Calculator(2,5)

print(f'{cal.a} va {cal.b} natija: {cal.ayirish()}')
        


class Shape:
    def area(self):
        return 'hech narsa yuq'
    
    def perimetr(self):
        return 'hech narsa yuq'


class Circle(Shape):

    def __init__(self,radus):
        self.radus = radus
    

    def area(self):
        return 3.14 * self.radus**2
    
    def perimetr(self):
        return 2* 3.14 * self.radus
    

class Triangle(Shape):

    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetr(self):
        return self.a + self.b + self.c
    

class Square(Shape):

    def __init__(self, side):
        self.side = side


    def area(self):
        return self.side**2
    
    def perimetr(self):
        return 4* self.side


c = Circle(10) 
t = Triangle(2,3,4)
s = Square(6)
    
    
print(c.perimetr())
        
print(t.perimetr())

print(s.perimetr())


# Har bir tugun (node) uchun klass
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # chap bola
        self.right = None  # o'ng bola


# BST (Binary Search Tree) klassi
class BinarySearchTree:
    def __init__(self):
        self.root = None   # boshlanishda daraxt bo'sh

    # Element qo'shish
    def insert(self, value):
        if self.root is None:            # agar daraxt bo‘sh bo‘lsa
            self.root = Node(value)      # root qilib qo‘yamiz
        else:
            self._insert(value, self.root)

    # Yordamchi rekursiv funksiyasi
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    # Qidirish funksiyasi
    def search(self, value):
        return self._search(value, self.root)

    # Yordamchi rekursiv funksiyasi
    def _search(self, value, current_node):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)


# -------------------- TEST --------------------

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

print("10 bor mi?", bst.search(10))
print("7 bor mi?", bst.search(7))
print("100 bor mi?", bst.search(100))


class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        if not  self.items:
            return 'bunaqasi yuq'
        return self.items.pop()

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())



# Har bir tugun (node)
class Node:
    def __init__(self, data):
        self.data = data      # tugundagi qiymat
        self.next = None      # keyingi tugunga ishora


# Linked List klassi
class LinkedList:
    def __init__(self):
        self.head = None      # boshlanishda ro'yxat bo'sh

    # Ro'yxatni ko'rsatish
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Oxiriga tugun qo'shish
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:         # agar list bo'sh bo'lsa
            self.head = new_node      # bosh tugun qilib qo'yamiz
        else:
            current = self.head
            while current.next is not None:   # oxirgi tugunni topamiz
                current = current.next
            current.next = new_node           # oxiriga qo'shamiz

    # Tugunni o'chirish (qiymat bo'yicha)
    def delete(self, data):
        # Ro'yxat bo'sh bo'lsa
        if self.head is None:
            return

        # Agar bosh tugun o'chirilsa
        if self.head.data == data:
            self.head = self.head.next
            return

        # O'rta tugunlarni tekshirish
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # tugunni o'chirish
                return
            current = current.next


# ------------------ TEST ------------------

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()   # 10 -> 20 -> 30 -> None

ll.delete(20)

ll.display()   # 10 -> 30 -> None


class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self,name,price):
        self.items[name] = price

    def remov_item(self,name):
        if name  in self.items:
            del self.items[name]
        else:
            print(f"{name} savatda yo'q!")

    def total(self):
        return sum(self.items.values())
    
cart = ShoppingCart()

cart.add_item('olma',1000)
cart.add_item('banan',2000)
cart.add_item('behi',3000)

cart.remov_item('olma')

cart.total()


class Stack:
    def __init__(self):
        self.items = []   # stack elementlari shu yerda saqlanadi

    # Element qo'shish (push)
    def push(self, item):
        self.items.append(item)

    # Elementni olish (pop)
    def pop(self):
        if not self.items:
            return "Stack bo'sh!"
        return self.items.pop()

    # Stackni ko'rsatish
    def display(self):
        if not self.items:
            print("Stack bo'sh!")
        else:
            print("Stack elementlari:", self.items)


# ----------- TEST -----------
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()        # [10, 20, 30]

print("Olingan:", stack.pop())  # 30
stack.display()                 # [10, 20]


class Queue:
    def __init__(self):
        self.items = []   # navbat elementlari shu yerda saqlanadi

    # Navbatga element qo'shish (enqueue)
    def enqueue(self, item):
        self.items.append(item)

    # Navbatdan element olish (dequeue)
    def dequeue(self):
        if not self.items:
            return "Queue bo'sh!"
        return self.items.pop(0)  # birinchi qo'yilgan birinchi chiqadi

    # Navbatni ko'rish
    def display(self):
        if not self.items:
            print("Queue bo'sh!")
        else:
            print("Queue:", self.items)


# ----------- TEST -----------
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()          # Queue: [10, 20, 30]

print("Olingan:", q.dequeue())  # 10
q.display()                     # Queue: [20, 30]


class Bank:
    def __init__(self):
        self.accounts = {}    # {"Ali": 100000, "Vali": 50000}

    # Mijoz qo'shish
    def add_customer(self, name, balance=0):
        if name in self.accounts:
            print("Bu mijoz allaqachon bor!")
        else:
            self.accounts[name] = balance

    # Hisobga pul qo'shish
    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
        else:
            print("Bunday mijoz topilmadi!")

    # Hisobdan pul yechish
    def withdraw(self, name, amount):
        if name not in self.accounts:
            print("Bunday mijoz topilmadi!")
            return
        
        if self.accounts[name] < amount:
            print("Hisobda pul yetarli emas!")
        else:
            self.accounts[name] -= amount

    # Mijoz balansini ko'rish
    def get_balance(self, name):
        if name in self.accounts:
            return self.accounts[name]
        return "Bunday mijoz yo'q!"

    # Barcha mijozlarni ko'rsatish
    def display_customers(self):
        print("---- BANK MIJOZLARI ----")
        for name, balance in self.accounts.items():
            print(f"{name}: {balance} so'm")


# ------------ TEST ------------
bank = Bank()

bank.add_customer("Sardor", 100000)
bank.add_customer("Ali", 50000)

bank.deposit("Sardor", 20000)
bank.withdraw("Ali", 30000)

print("Sardor balansi:", bank.get_balance("Sardor"))
print("Ali balansi:", bank.get_balance("Ali"))

bank.display_customers()
