def decode_message(s, shifts):
    message = list(s)  # Convert string to list of characters
    
    for shift in shifts:
        start, end, direction = shift
        
        for i in range(start, end + 1):
            if direction == 1:
                message[i] = chr((ord(message[i]) - ord('a') + 1) % 26 + ord('a'))
            else:
                message[i] = chr((ord(message[i]) - ord('a') + 25) % 26 + ord('a'))
    
    return ''.join(message)  # Convert list of characters back to string

if __name__ == "__main__":
    s = "hello"
    shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
    
    decoded_message = decode_message(s, shifts)
    print("Decoded message:", decoded_message)
