from abc import abstractmethod, ABC  # Abstract Base Class
from copy import deepcopy
from typing import List
import string


class Person:
    def __init__(self, name: string, address: string) -> None:
        self._name = name
        self._address = address

    @property
    def name(self) -> string:
        return self._name

    @property
    def address(self) -> string:
        return self._address

    @name.setter
    def name(self, value: string) -> None:
        self._name = value

    @address.setter
    def address(self, value: string) -> None:
        self._address = value

    def __dict__(self) -> dict:
        return {
            'name': self._name,
            'address': self._address
        }

    def __copy__(self) -> __init__:
        return Person(deepcopy(self._name),
                      deepcopy(self._address))

    def __eq__(self, other) -> bool:
        return (self._name == other.name and
                self._address == other.address)

    def __hash__(self) -> int:
        prime = 31
        res = 1
        res *= prime + hash(self._name)
        res *= prime + hash(self._address)
        if res < 0: res = - res
        return res

    def __str__(self) -> string:
        return f'Person[name={self._name}, address={self._address}]'


class Student(Person):
    nCourses: int = 0
    courses: List = []
    grades: List = []

    def __init__(self, name: string, address: string) -> None:
        super().__init__(name, address)

    def addCourseGrade(self, course: string, grade: string) -> None:
        self.courses.append(course)
        self.grades.append(grade)
        self.nCourses += 1

    def getAverageGrade(self) -> float:
        return sum(self.grades) / self.nCourses

    def __dict__(self) -> dict:
        return {
            'name': super().name,
            'address': super().address
        }

    def __copy__(self) -> __init__:
        return Student(deepcopy(super().name),
                       deepcopy(super().address),
                       deepcopy(self.nCourses),
                       deepcopy(self.courses))

    def __eq__(self, other: Person) -> bool:
        return super().__eq__(other)

    def __hash__(self) -> int:
        prime = 31
        res = super().__hash__()
        res *= prime + self.nCourses
        res *= prime + hash(tuple(self.courses))
        if res < 0: res = - res
        return res

    def __str__(self) -> string:
        return f'Student[name={super().name}, address={super().address}, courses={self.courses}]'


class Teacher(Person):
    def __init__(self, name: string, address: string) -> None:
        super().__init__(name, address)
        self.courses = []
        self.n_courses = 0

    @property
    def courses(self) -> List:
        return self._courses  # R

    @property
    def n_courses(self) -> int:
        return self._n_courses

    def addCourse(self, course: string) -> None:
        self.courses.append(course)

    def removeCourse(self, course: string) -> None:
        self.courses.remove(course)

    @abstractmethod
    def getSalary(self) -> float:
        pass

    def __dict__(self) -> dict:
        return {
            'name': super().name,
            'address': super().address,
            'courses': self.courses
        }

    def __copy__(self) -> __init__:
        return Teacher(deepcopy(super().name),
                       deepcopy(super().address),
                       deepcopy(self.courses),
                       deepcopy(self.n_courses))

    def __eq__(self, other: object):
        return super().__eq__(other)

    def __hash__(self):
        prime = 31
        res = super().__hash__()
        res *= prime + self.n_courses
        res *= prime + hash(tuple(self.courses))
        if res < 0: res = - res
        return res

    def __str__(self):
        return f'Teacher[name={super().name}, address={super().address}, courses={self.courses}]'

    @n_courses.setter
    def n_courses(self, value):
        self._n_courses = value

    @courses.setter
    def courses(self, value):
        self._courses = value


class HourlyTeacher(Teacher, ABC):
    def __init__(self, name: string, address: string, hours_worked: int, hourly_rate: float):
        super().__init__(name, address)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self) -> int:
        return self._hours_worked  # Retorne o atributo interno, não self.hours_worked

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    @hours_worked.setter
    def hours_worked(self, value):
        self._hours_worked = value

    @hourly_rate.setter
    def hourly_rate(self, value):
        self._hourly_rate = value

    def calculateWeeklyPay(self) -> float:
        return self.hours_worked * self.hourly_rate

    def __dict__(self) -> dict:
        return {
            'name': super().name,
            'address': super().address,
            'courses': self.courses,
            'hours_worked': self.hours_worked,
            'hourly_rate': self.hourly_rate
        }

    def __copy__(self):
        new_teacher = HourlyTeacher(self.name, self.address, self.hours_worked, self.hourly_rate)
        new_teacher._courses = deepcopy(self._courses)  # Copiar cursos se necessário
        return new_teacher

    def __eq__(self, other) -> bool:
        return super().__eq__(other)

    def __hash__(self) -> int:
        prime = 31
        res = super().__hash__()
        res *= prime + self.hours_worked
        res *= prime + self.hourly_rate
        if res < 0: res = - res
        return res


class SalaryTeacher(Teacher, ABC):
    def __init__(self, name: string, address: string, salary: float):
        super().__init__(name, address)
        self.salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        self._salary = value

    def getSalary(self) -> float:
        return self.salary

    def __dict__(self) -> dict:
        return {
            'name': super().name,
            'address': super().address,
            'courses': self.courses,
            'salary': self.salary
        }

    def __copy__(self):
        new_teacher = SalaryTeacher(self.name, self.address, self.salary)
        new_teacher._courses = deepcopy(self._courses)  # Copiar cursos se necessário
        return new_teacher

    def __eq__(self, other) -> bool:
        return super().__eq__(other)

    def __hash__(self) -> int:
        prime = 31
        res = super().__hash__()
        res *= prime + self.salary
        if res < 0: res = - res
        return res


def test_person():
    vinicius = Person('Vinicius', 'Rua 1')
    print(vinicius)

    hash_code = vinicius.__hash__()
    print(hash_code)


def test_student():
    vinicius = Student('Vinicius', 'Rua 1')
    vinicius.addCourseGrade('Math', 10)
    vinicius.addCourseGrade('History', 9)
    vinicius.addCourseGrade('Geography', 8)
    print(vinicius)

    hash_code = vinicius.__hash__()
    print(hash_code)


def test_hourly_teacher():
    vinicius = HourlyTeacher('Vinicius', 'Rua 1', 40, 10)
    vinicius.addCourse('Math')
    vinicius.addCourse('History')
    vinicius.addCourse('Geography')
    print(vinicius)

    hash_code = vinicius.__hash__()
    print(hash_code)


def test_salary_teacher():
    vinicius = SalaryTeacher('Vinicius', 'Rua 1', 1000)
    vinicius.addCourse('Math')
    vinicius.addCourse('History')
    vinicius.addCourse('Geography')
    print(vinicius)

    hash_code = vinicius.__hash__()
    print(hash_code)


def main():
    test_person()
    test_student()
    test_hourly_teacher()
    test_salary_teacher()


if __name__ == '__main__':
    main()
