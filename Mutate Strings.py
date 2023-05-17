first_message = input()
second_message = input()
prev_word = ''
final_message = ''
for i in range(0, len(second_message)+1):
    final_message += second_message[:i] + first_message[i:]
    if final_message != first_message and final_message != prev_word:
        print(final_message)
        prev_word = final_message
        final_message = ''
    else:
        final_message = ''
        continue
