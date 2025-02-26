from random import choice, randint

class QuickSort:
    """Implementing the Quick Sort algorithm in a Python class"""
    
    def __init__(self, list_: list[int]) -> None:
        self.__list = list_
        self.__pivot = int()
        self.__quicksort_list = []
    
    def __pivot_choice_method(self) -> int:
        pivot: int = choice(self.__list)
        self.__pivot = pivot
    
    def __partitioning_method(self) -> None:
        minor_list: list[int] = list()
        major_list: list[int] = list()
        pivot_list: list[int] = list()
        
        for number in self.__list:
            if number < self.__pivot:
                minor_list.append(number)
            elif number == self.__pivot:
                pivot_list.append(number)
            else:
                major_list.append(number)
        
        self.__pivot_list = pivot_list
        self.__minor_list = minor_list
        self.__major_list = major_list
    
    def __ordering_method(self) -> None:
        self.__minor_list.sort()
        self.__major_list.sort()
    
    def __append_method(self) -> None:
        final_list: list[int] = self.__minor_list + self.__pivot_list + self.__major_list
        self.__quicksort_list = final_list
    
    def result(self) -> str:
        self.__pivot_choice_method()
        self.__partitioning_method()
        self.__ordering_method()
        self.__append_method() 
    
    def __str__(self):
        return f'The original list is {self.__list}.\nThe randomly pivot is {self.__pivot}.\nThe quicksorted list is {self.__quicksort_list}'

if __name__ == '__main__':
    my_list = QuickSort([randint(1, 100) for i in range(10)])
    my_list.result()
    print(my_list)