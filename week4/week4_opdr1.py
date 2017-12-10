class SeperateChainHashtable(object):
    """docstring for SeperateChainHashtable

    Attributes:
        table (list): List of sets were all values are in the table are stored.
    """

    def __init__(self, size):
        """Create hashtable based on "separate chaining hashing".

        Args:
            size (integer): Initial size of the the table.
        """
        self.table = [set() for x in range(size)]

    def search(self, e):
        """Check if item in table.

        Args:
            e (number): Number that will be checked.

        Returns:
            Boolean: True when item in table, False when item not in table.
        """
        return e in self.table[hash(e) % len(self.table)]

    def insert(self, e):
        """Add item to the table. Automatically rehashes table when load factor larger then 0.75.

        Args:
            e (number): Number that will be added tot the table.
        """
        elementsintable = 1
        for numberset in self.table:
            for number in numberset:
                elementsintable += 1
        if (elementsintable / len(self.table) > 0.75):
            self.rehash(len(self.table) * 2)
        self.table[hash(e) % len(self.table)].add(e)

    def delete(self, e):
        """Remove item from table, throw exception when item not in table.

        Args:
            e number: Number that will be removed from the table

        Raises:
            IndexError: E not in table
        """
        if self.search(e):
            self.table[hash(e) % len(self.table)].remove(e)
        else:
            raise IndexError("Unknown value")

    def rehash(self, new_len):
        """Reposition all element in a new table of length new_len.

        Args:
            new_len (int): Length of the new table.
        """
        print("!!!!!!!!!Rehash")
        oldtable = self.table
        self.table = [set() for x in range(new_len)]
        for numberset in oldtable:
            for number in numberset:
                self.insert(number)

        print("Rehash-table-print")
        print(self.table)

if __name__ == "__main__":
    import random
    hashtable = SeperateChainHashtable(10)

    randomnumbers = [random.random() for n in range(0, 200)]
    for number in randomnumbers:
        hashtable.insert(number)

    for number in range(len(randomnumbers)):
        if number %2 == 0:
            hashtable.delete(randomnumbers[number])

    print(hashtable.table)
