from collections import defaultdict
import sys


def compute_signature(s):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord("a")] += 1
    return tuple(freq)


def main():
    input = sys.stdin.readline
    N = int(input())
    prefix_map = defaultdict(int)

    for _ in range(N):
        s = input().strip()
        freq = [0] * 26
        seen = set()
        for ch in s:
            freq[ord(ch) - ord("a")] += 1
            sig = tuple(freq)
            if sig not in seen:
                prefix_map[sig] += 1
                seen.add(sig)

    Q = int(input())
    for _ in range(Q):
        query = input().strip()
        sig = compute_signature(query)
        print(prefix_map.get(sig, -1))


if __name__ == "__main__":
    main()
