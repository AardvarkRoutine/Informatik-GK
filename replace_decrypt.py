def frequency_analysis(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    total_chars = len(text)
    for char in freq_dict:
        freq_dict[char] = freq_dict[char] / total_chars

    print(dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)))
    return dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))

def replace_decrypt(text, freq_analysis):
    char_freq = {
    'e': 0.174,
    'n': 0.097,
    'i': 0.075,
    'r': 0.075,
    's': 0.072,
    'a': 0.065,
    't': 0.061,
    'd': 0.050,
    'h': 0.047,
    'u': 0.043,
    'l': 0.034,
    'c': 0.030,
    'g': 0.030,
    'm': 0.030,
    'o': 0.030,
    'b': 0.018,
    'w': 0.018,
    'f': 0.016,
    'k': 0.012,
    'z': 0.011,
    'v': 0.010,
    'p': 0.009,
    'j': 0.002,
    'y': 0.002,
    'x': 0.001,
    'q': 0.001
    }

    char_freq_text = freq_analysis(text)
    char_freq_text_keys = list(char_freq_text.keys())
    char_freq_keys = list(char_freq.keys())
    mapping = {}
    for i in range(len(char_freq_text_keys)):
        mapping[char_freq_text_keys[i]] = char_freq_keys[i]

def decrypt(text, mapping):
    decrypted_text = ''
    for char in text:
        if char in mapping:
            decrypted_text += mapping[char]
        else:
            decrypted_text += char
    return decrypted_text

def main():
    text = input('Enter the text to decrypt: ')
    print(decrypt(text, replace_decrypt(text, frequency_analysis)))

if __name__ == '__main__':
    main()
