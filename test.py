# ========================================================
# Use two stacks to implement a queue


class Queue(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self, element):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
q = Queue()
q.enqueue(1)
q.enqueue(5)
print(q)
q.dequeue(1)

# ========================================================
# Newton's Method: let f(x) = 0, and there exists f'(x), solve for x

# ========================================================
# Binary search
'''
1. 转移方程
  a. left < mid < right
  b. left = mid < right
  c. left = mid = right
2. 确定while loop边界条件
  a. left < right
  b. left <= right
  c. left + 1 < right
3. 确定结果 what to return?
'''

# eg1. search for a targeted value in a sorted array, and return its
# index. If not in the array, return -1.


def binarysearch(array, target):
    left = 0
    right = len(array) - 1
    mid = left + (right - left) // 2
    while left < right:
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# eg2. search for a insert position. The given array is sorted and values
# are non - repeat. array = [1, 2, 3, 5, 6, 7], insert value = 4.


def binaryinsert(array, insert_value):
    left = 0
    right = len(array) - 1
    mid = left + (right - left) // 2
    while left < right:  # when right == left, break
        if insert_value == array[mid]:
            return mid
        elif insert_value < array[mid]:
            right = mid
        else:
            left = mid + 1
    if array[left] > insert_value:
        return left
    else:
        return left + 1

        # ========================================================
        # C++ Basic Questions
'''
1. Polymorphism
Base class A and child class B
Due to inherentance property, B should have same 'foo' function
Assuming there a 'foo' function in A, and it's a virtual function
Then we can redefine the behavior of 'foo' in B.

C is another child class.
Use a pointer new B
通过一个公用的class, define一个A class的pointer，指向不同的child class的object，这样他们的实现是不同class的implementation
A * pa1 = new B()  # A class 的 pointer等于B class的一个object
A * pa2 = new C()
then pa1 and pa2 can call 'foo' function
这样可以save some code，不用一个一个define b = B.foo(), c = C.foo()....

2. Virtual function
Base class has a function 'foo', and we want the child class to have different implementations, then this 'foo' function needs to be defined as a virtual function so that the child classes can define their own implementations.

3. Reference vs. Pointer
Pointer is a variable per se, only the content of it is a memory address.
Reference is an alias, while its impletementation is unknown.

4. Function overwrite vs function overload
Function overwrite: child class overwrites a function in the base class
Functions overload: can have same name, but must have different arguments.
Function signiture: a function identifier. Mingle of function name, arguments and other info.

5. Inheritance:
'''
