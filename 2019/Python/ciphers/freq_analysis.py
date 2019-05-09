#ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ .,!'
#LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,! '
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letter_count(mesesage):
    letter_count = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
        'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
        'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
        'W': 0, 'X': 0, 'Y': 0, 'Z': 0, '.': 0, ',': 0, '!': 0, ' ': 0,
        '?': 0
    }
    for letter in mesesage.upper():
        if letter not in letter_count:
            letter_count[letter] = 0
        if letter in LETTERS:
            letter_count[letter] += 1
    return letter_count


def get_item_at_index_zero(items):
    return items[0]


def get_frequency_order(message):
    letter_to_frequency = get_letter_count(message)
    frequency_to_letter = {}
    for letter in LETTERS:
        if letter_to_frequency[letter] not in frequency_to_letter:
            frequency_to_letter[letter_to_frequency[letter]] = [letter]
        else:
            frequency_to_letter[letter_to_frequency[letter]].append(letter)

    for freq in frequency_to_letter:
        frequency_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        frequency_to_letter[freq] = ''.join(frequency_to_letter[freq])
    freq_pairs = list(frequency_to_letter.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    freq_order = []
    for freq_pair in freq_pairs:
        freq_order.append(freq_pair[1])

    return ''.join(freq_order)


def english_frequency_match_score(message):
    freq_order = get_frequency_order(message)
    match_score = 0
    for common_letter in ETAOIN[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1
    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in freq_order[-6]:
            match_score += 1
    return match_score


def decrypt_caeser_cipher(msg, key):
    out = ''
    for symbol in msg:
        symbol = symbol.upper()
        if symbol not in LETTERS or symbol == '':
            continue
        symbol_index = LETTERS.find(symbol)
        translated_index = symbol_index - key
        if translated_index < 0:
            translated_index += len(LETTERS)
        out += LETTERS[translated_index]
    return out


def statsically_best_fit_caesar_cipher(msg):
    highest_tests = 0
    best_fit = None
    fit_key = None

    for key in range(len(LETTERS)):
        test = decrypt_caeser_cipher(msg, key)
        test_result = english_frequency_match_score(test)
        print(key, test_result, test)
        if test_result > highest_tests:
            highest_tests = test_result
            best_fit = test
            fit_key = key

    return f"{best_fit}"


def statistical_dictionary_attack(message, words):
    freq_order = get_frequency_order(message)
    print(freq_order)
    print(ETAOIN)
    msg_head = freq_order[:6]
    msg_tail = freq_order[-6:]
    etaoin_head = ETAOIN[:6]
    etaoin_tail = ETAOIN[-6:]
    print(etaoin_head)
    print(msg_head)
    print(etaoin_tail)
    print(msg_tail)
    print(message)
    print(secret.upper().replace(" ", ""))
    msg = list(message)
    for i in range(len(freq_order)):
        for j in range(len(msg)):
            if msg[j] == freq_order[i]:
                msg[j] = ETAOIN[i]
    return ''.join(msg)

secret = "Cryptanalysis of the Enigma ciphering system enabled the western Allies in World War II to read substantial amounts of Morse-coded radio communications of the Axis powers that had been enciphered using Enigma machines. This yielded military intelligence which, along with that from other decrypted Axis radio and teleprinter transmissions, was given the codename Ultra. This was considered by western Supreme Allied Commander Dwight D. Eisenhower to have been 'decisive' to the Allied victory."
message = "DSZQUBOBMZTJTPGUIFFOJHNBDJQIFSJOHTZTUFNFOBCMFEUIFXFTUFSOBMMJFTJOXPSMEXBSJJUPSFBETVCTUBOUJBMBNPVOUTPGNPSTFDPEFESBEJPDPNNVOJDBUJPOTPGUIFBYJTQPXFSTUIBUIBECFFOFODJQIFSFEVTJOHFOJHNBNBDIJOFTUIJTZJFMEFENJMJUBSZJOUFMMJHFODFXIJDIBMPOHXJUIUIBUGSPNPUIFSEFDSZQUFEBYJTSBEJPBOEUFMFQSJOUFSUSBOTNJTTJPOTXBTHJWFOUIFDPEFOBNFVMUSBUIJTXBTDPOTJEFSFECZXFTUFSOTVQSFNFBMMJFEDPNNBOEFSEXJHIUEFJTFOIPXFSUPIBWFCFFOEFDJTJWFUPUIFBMMJFEWJDUPSZ"
# print("Statistical fit caeser cipher: ")
# best_fit = statsically_best_fit_caesar_cipher(message)
# print(best_fit)
print("Statistical dictionary attack: ")
with open('dictionary.txt') as fp:
    words = fp.readlines()
print(statistical_dictionary_attack(message, words))
