import hashlib


def sub_search(s: str):
    assert len(s) > 0, 'Строка не может быть пустой'
    hash_subs = []
    len_s = len(s)
    for l in range(1, len_s + 1):
        for j in range(0, len_s):
            subs = s[j:j + l]
            print(subs)
            h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
            if h_subs not in hash_subs and len(subs) != len_s :
                hash_subs.append(h_subs)
    print(f'Список хэшей подстрок в этой строке \n{hash_subs}')
    return f'В этой строке {len(hash_subs)} подстрок'


s = input('Введите строку: ')
print(sub_search(s))