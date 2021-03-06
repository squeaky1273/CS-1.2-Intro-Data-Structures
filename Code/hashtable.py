#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Running time: O(n); The algorithm goes through all the buckets and everything in them to create a list.
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Running time: O(n); The algorithm goes through all the buckets and everything in them to create a list.
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = [] #Note: Create an empty list
        for bucket in self.buckets: #Note: For all the buckets, add all the key and values to the list
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(n); 
        Worst Running time: O(n);
        The algorithm goes through the buckets to show the items to each bucket.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(n); 
        Worst Running time: O(n);
        The algorithm goes through all of the buckets and counts all the items in each bucket.
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0 #Note: Count starts out as 0
        for bucket in self.buckets: #Note: for each item in the bucket, add 1 to the count
            for key, value in bucket.items():
                count += 1
        return count #Note: Return the count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(1); 
        Worst Running time: O(L);
        The algorithm finds the key of the linkedlist and the index of the bucket.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.buckets[index].is_empty() == False: #Note: There are items in the buckets
            return bucket.find(lambda item: item[0] == key) is not None #Note: Return the given item.
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(1); 
        Worst  Running time: O(L);
        The algorithm finds the key of the linkedlist and the index of the bucket.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.contains(key):
            return bucket.find(lambda item: item[0] == key)[1] #Note: Return the value
        else:
            raise KeyError('Key not found: {}'.format(key)) #Note: Else return error

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(1);
        Worst Running time: O(L);
        The algorithm finds the key of the linkedlist and the index of the bucket. It also performs without transversal.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.contains(key):
            self.buckets[index].delete(bucket.find(lambda item: item[0] == key)) #Note: Update the value
        self.buckets[index].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Best Running time: O(1); 
        Worst Running time: O(L);
        The algorithm finds the key of the linkedlist and the index of the bucket.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.contains(key): #Note: If there is an item, then delete it
            self.buckets[index].delete(bucket.find(lambda item: item[0] == key)) #Note: Delete the entry
        else:
            raise KeyError('Key not found: {}'.format(key)) #Note: Else return error

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
