import time

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def convert_to_unix_timestamp(decimal):
    timestamp = time.gmtime(decimal)
    formatted_time = time.strftime('%d-%m-%Y %I:%M:%S %p UTC', timestamp)
    return formatted_time

def main():
    # Take input from the user
    number = input("Enter a TikTok Video number string: ")
    
    # Convert decimal to binary
    binary = decimal_to_binary(int(number))
    
    # Select first 31 lines of the binary code
    truncated_binary = binary[:31]
    
    # Convert truncated binary back to decimal
    decimal = binary_to_decimal(truncated_binary)
    
    # Convert decimal to Unix timestamp
    timestamp = convert_to_unix_timestamp(decimal)
    
    print("Video String:", number)
    print("Decimal to Binary:", binary)
    print("Truncated Binary:", truncated_binary)
    print("                    D / M / Y")
    print("Video Upload Date:", timestamp)

if __name__ == '__main__':
    main()
