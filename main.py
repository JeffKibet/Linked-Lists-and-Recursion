from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    employees = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    for emp_id in [101, 102, 103, 104]:
        employees.insert_at_end(emp_id)
    employees.insert_at_front(100)
    
    # TODO: 3) Display the list to verify insertion
    print("Employee IDs:")
    employees.display()
    

    # TODO: 4) Call recursive_sum and print the result
    print(f"Sum of IDs: {employees.recursive_sum()}")
    

    # TODO: 5) Call recursive_search with a target and print result
    for target in (103, 999):
        found = employees.recursive_search(target)
        print(f"ID {target} {'found' if found else 'not found'}")
    

    # TODO: 6) Call recursive_reverse, then display the reversed list
    employees.recursive_reverse()
    print("Reversed:")
    employees.display()
    


# 