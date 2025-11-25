from pydantic import BaseModel


class Employee(BaseModel):
    id: int | None = None
    name: str
    age: int


class EmployeeDB:
    def __init__(self, populate_db: list[Employee] = list()) -> None:
        self.__db = list()
        self.__index = 0
        if populate_db:
            list(map(lambda e: self.create(employee=e), populate_db))

    # CREATE
    def create(self, employee: Employee) -> int:
        self.__index += 1
        self.__db.append(
            Employee(id=self.__index, name=employee.name, age=employee.age)
        )
        return self.__index

    # READ
    def read(self, id: int) -> Employee | None:
        return next(filter(lambda x: x.id == id, self.__db), None)
        # raise ValueError(f"employee with id {id} not found!")

    def get_all(self) -> list[Employee]:
        return self.__db

    # UPDATE
    def update(self, id: int, employee: Employee) -> Employee:
        for item in self.__db:
            if item.id == id:
                index = self.__db.index(item)
                employee.id = id
                self.__db[index] = employee
                return employee

        raise ValueError(f"employee with id {employee.id} not found!")

    # DELETE
    def delete(self, id: int) -> bool:
        for i, e in enumerate(iterable=self.__db, start=0):
            if e.id == id:
                del self.__db[i]
                return True

        return False


# For testing
if __name__ == "__main__":
    db = EmployeeDB(
        populate_db=[
            Employee(name="Alice", age=20),
            Employee(name="Bob", age=42),
            Employee(name="Charles", age=50),
        ]
    )
    print(db.get_all(), "\n")
    print(db.read(id=2), "\n")
    print(db.update(id=2, employee=Employee(name="Bobart", age=42)), "\n")
    print(db.delete(id=1), "\n")
    print(db.get_all())
