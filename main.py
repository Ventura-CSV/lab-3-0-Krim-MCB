def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))
    if number % 2 == 1:
        result=1
    else:
        result=0
    """
    Make your code here
    """

    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
