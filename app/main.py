def count_occurrences(phrase: str, letter: str) -> int:
    
    count = 0

    for p in phrase:
        if p.lower() == letter.lower():
            count += 1
    
    return count
