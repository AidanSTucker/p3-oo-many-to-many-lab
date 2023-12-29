class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        related_contracts = self.contracts()
        return [contract.author for contract in related_contracts]


class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        related_contracts = self.contracts()
        return [contract.book for contract in related_contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        related_contracts = self.contracts()
        total = sum(contract.royalties for contract in related_contracts)
        return total


class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object")
        self.author = author
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        self.book = book
        if not isinstance(date, str):
            raise Exception("Invalid date type")
        self.date = date
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties type")
        self.royalties = royalties
        self.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = [contract for contract in cls.members if contract.date == date]
        sorted_contracts = sorted(contracts_on_date, key=lambda x: x.date)  # Sort by date
        return sorted_contracts

