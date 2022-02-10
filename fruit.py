def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list_rev = fruit_list.reverse()
    print(f"original: {fruit_list_rev}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")
main()