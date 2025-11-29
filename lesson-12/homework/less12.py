1)

"""
prime_threaded.py

Threaded prime number checker.
Usage example at bottom of file (if __name__ == "__main__").
"""

import threading
import math
from typing import List

def is_prime(n: int) -> bool:
    """Tez va ishonchli primalik testi."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True

def worker(start: int, end: int, out_list: List[int], lock: threading.Lock):
    """Worker thread: start..end (inclusive) diapazondagi sonlarni tekshiradi."""
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    # natijani thread-safe tarzda umumiy ro'yxatga qo'shamiz
    with lock:
        out_list.extend(local_primes)

def threaded_primes(range_start: int, range_end: int, n_threads: int = 4) -> List[int]:
    """Berilgan diapazondagi barcha tub sonlarni topadi (parallel ishlaydi)."""
    if range_end < range_start:
        return []

    # diapazonni bo'lamiz
    total = range_end - range_start + 1
    chunk = max(1, total // n_threads)
    threads = []
    result = []
    lock = threading.Lock()

    s = range_start
    for i in range(n_threads):
        e = s + chunk - 1
        # oxirgi thread qolganlarni oladi
        if i == n_threads - 1:
            e = range_end
        if s > range_end:
            break
        t = threading.Thread(target=worker, args=(s, e, result, lock))
        t.start()
        threads.append(t)
        s = e + 1

    for t in threads:
        t.join()

    result.sort()
    return result

# Misol uchun ishlatish
if __name__ == "__main__":
    # Masalan 1 dan 200 orasidagi tub sonlarni 6 thread bilan topamiz:
    primes = threaded_primes(1, 200, n_threads=6)
    print("Primes:", primes)


#2

"""
threaded_wordcount.py

Threaded word count for a large text file.
Each thread processes a slice of lines and returns a Counter.
"""

import threading
from collections import Counter
from typing import List
import re

WORD_RE = re.compile(r"\w+", flags=re.UNICODE)

def tokenize(text: str) -> List[str]:
    """Matnni tokenlarga ajratadi (kichik harflarga o'zgartirib)."""
    return [w.lower() for w in WORD_RE.findall(text)]

def worker(lines: List[str], out_counters: List[Counter], lock: threading.Lock):
    """Thread worker: berilgan qatorlar ustida ishlaydi va Counter qo'shadi."""
    c = Counter()
    for line in lines:
        words = tokenize(line)
        c.update(words)
    with lock:
        out_counters.append(c)

def threaded_word_count(file_path: str, n_threads: int = 4) -> Counter:
    """Faylni o'qib, so'zlar hisobini parallel hisoblaydi."""
    # Hammasini xotiraga olamiz (agar fayl juda katta bo'lsa, foizli bo'lib o'qish ham yozsa bo'ladi)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    if total_lines == 0:
        return Counter()

    # Bo'lib beramiz
    chunk_size = max(1, total_lines // n_threads)
    threads = []
    counters = []
    lock = threading.Lock()

    start = 0
    for i in range(n_threads):
        end = start + chunk_size
        if i == n_threads - 1:
            end = total_lines
        if start >= total_lines:
            break
        t = threading.Thread(target=worker, args=(lines[start:end], counters, lock))
        t.start()
        threads.append(t)
        start = end

    for t in threads:
        t.join()

    # barcha Counterlarni birlashtirish
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    return total_counter

# Misol uchun ishlatish
if __name__ == "__main__":
    # Test uchun kichik sample fayl yaratamiz
    sample_text = """Hello world
This is a test. Hello again!
World of Python: threading, parallelism.
Test the worker threads. hello HELLO"""
    test_path = "sample_text.txt"
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(sample_text)

    counts = threaded_word_count(test_path, n_threads=3)
    print("Top words:")
    for word, cnt in counts.most_common(10):
        print(word, cnt)
