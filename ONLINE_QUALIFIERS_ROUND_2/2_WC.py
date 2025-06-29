def find_whispers(log, key):
    positions = []
    log_len = len(log)
    key_len = len(key)

    for start in range(log_len - key_len + 1):
        valid = True
        for k in range(key_len):
            ch_log = log[start + k]
            ch_key = key[k]
            if ch_key != '?' and ch_key.lower() != ch_log.lower():
                valid = False
                break
        if valid:
            positions.append(start)

    print(len(positions))
    if positions:
        print(' '.join(str(pos) for pos in positions))
    else:
        print()

chatlog_input = input().strip()
pattern_input = input().strip()

find_whispers(chatlog_input, pattern_input)
