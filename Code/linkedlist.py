#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Running time: O()n; It takes time to complete the algorithm as the list increases. 
        """
        # TODO: Loop through all nodes and count one for each

        length = 0 #Note: Start at 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            length +=1 #Note: Add to the length
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Running time: O()1; The algorithm only checks the taila dn replace it.
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item) #Note: Create new node
        if self.tail is not None: #Note: If there is no tail
            self.tail.next = new_node 
        else:
            self.head = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        """Running time: O(1); The algorithm only checks the head and replaces it.
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        new_node = Node(item) #Note: Create new node
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else: 
            new_node.next = self.head #Note: Pick the next item
            self.head = new_node #Note: The item becomes the head

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        """Best case running time: O(1); This runs if the item is the self.head.
        """
        """Worst case running time: O(n); The algorithm runs a number of (n) loops.
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        
        current_node = self.head #Note: The current node is the head
        while current_node is not None:
            if quality(current_node.data) == True:
                return current_node.data
            else:
                current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        """Best case running time: O(1); This runs if the item is the self.head.
        """
        """Worst case running time: O(n); The algorithm runs a number of (n) loops.
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        if self.head is None: #Note: If there isn't a head
            raise ValueError('Item not found: {}'.format(item)) #Note: There is an error

        elif self.head is not None: #Note: If there is a head
            prev_node = None
            current_node = self.head
            new_node = self.head.next
            
            if current_node.data is not item: #Note: If the data is not the item
                while current_node.data is not item and current_node.next is not None:
                    prev_node = current_node
                    current_node = current_node.next
                    new_node = current_node.next
                
                if current_node.data is not item and current_node is self.tail: #Note: If the data is not the item AND the node is the tail,
                    raise ValueError('Item not found: {}'.format(item)) #Return an error
                
                elif new_node is None: #Note: If there is no new node
                    prev_node.next = None
                    self.tail = prev_node
                    if prev_node is self.head:
                        self.tail = self.head
                
                else: prev_node.next = new_node #Note: The next node in the new node
            
            elif new_node is None: #Note: If there is no new node
                self.head = None #Note: There is no head
                self.tail = None #Note: There is no tail
            
            else:
                self.head = new_node


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
