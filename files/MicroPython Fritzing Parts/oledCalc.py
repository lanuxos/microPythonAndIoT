# OLED Calculator
char = []
while True:
    text = input('\nInput your display text [max length 16 characters]:\n')
    if len(text) <= 16:
        text = text
        if len(text) == 16:
            result = 0
            print(f'\nTo centering <<{text}>> on 128x64 OLED, first letter start at: {result}')
            # return result
        else:
            start = (16 - len(text)) * 8
            mod = start % 2
            if mod == 0:
                result = start // 2
                print(f'\nTo centering <<{text}>> on 128x64 OLED, first letter start at: {result}')
                # return result
            else:
                result = (start // 2) + (mod / 2)
                print(f'\nTo centering <<{text}>> on 128x64 OLED, first letter start at: {result}')
                # return result
    else:
        text = text[:16]
        result = 0
        print(f'\nTo centering <<{text}>> on 128x64 OLED, first letter start at: {result}')
        # return result
