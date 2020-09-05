class Node:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key=None, value=None):
        if value is None: # validate both key and value entered
            self.head = None
        else:
            self.head = Node(key, value)

    def __str__(self):
        return_string = '['
        if self.head is None:
            return return_string + 'None]'
        current = self.head
        while current.next is not None:
            return_string += f'({current.key}: {current.value}), '
            current = current.next
        return return_string + f'({current.key}: {current.value})' + ']'

    #returns the new head
    def add_to_head(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            node = Node(key, value)
            node.next = self.head
            self.head = node
        return self.head

    def find_by_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    # returns value
    def find_by_key(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def insert(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return current
            current = current.next
        # if key is not present in list, add to head
        self.add_to_head(key, value)

    def delete(self, key):
        current = self.head
        if current.key == key: #the head is to be deleted
            value = current.value
            self.head = current.next
            return value
        while current.next is not None:
            if current.next.key == key:
                #this is what we need to delete
                value = current.next.value
                current.next = current.next.next
                return value
            current = current.next
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = []
        self.load = 0
        # _ for unused variable
        for _ in range(self.capacity):
            self.buckets.append(HashTableEntry(None, None))
        

    def __str__(self):
        return_str = '['
        for i in range(self.capacity - 1):
            return_str += f'{self.buckets[i]}, '
        return return_str + f'{self.buckets[self.capacity - 1]}]'


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # make a variable equal to 5381
        hashed_result = 5381
        ## iterate over the bytes of our key
        key_bytes = key.encode()
        ## for each byte,
        for byte in key_bytes:
        ### shift the variable and add it and add the bye
            hashed_result = ((hashed_result << 5) + hashed_result) + byte

        return hashed_result



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the buckets capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ### 1. Hash the key
        ### 2. Take the hash and mod it with len of array
        hashed_key = self.hash_index(key)
        ### 3. Check if there's a value at that index
            ### 3a. Go to index, put in that value
        self.buckets[hashed_key] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hashed_key = self.hash_index(key) 
        if hashed_key:
            hashed_key = None
        else:
            print("Key not Found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hashed_key = self.hash_index(key)
        value = self.buckets[hashed_key]
        # if self.buckets[hashed_key] != None:
        #     return self.buckets[hashed_key]
        # else:
        #     return None
        return value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # instantiate a new HashTable
        resized_HT = HashTable(new_capacity)
        # add values from old HT to new reized HT
        for hashtable in self.buckets:
            # traverse thru linked list (hashtable)
            current = hashtable.head
            while current != None:
                # add each value to new HT
                resized_HT.put(current.key, current.value)
                current = current.next
            # switch hashtables
            self.capacity = resized_HT.capacity
            self.buckets = resized_HT.buckets
            self.load = resized_HT.load


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
