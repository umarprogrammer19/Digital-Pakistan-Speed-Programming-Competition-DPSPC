def minimize_project_time(n, m, a, tm, ta, m0, a0, dm, da):
    dp_main = [0] * n
    dp_alt = [0] * n

    dp_main[0] = m0 + m[0]
    dp_alt[0] = a0 + a[0]

    for i in range(1, n):
        dp_main[i] = min(
            dp_main[i - 1] + m[i],
            dp_alt[i - 1] + ta[i] + m[i], 
        )

        dp_alt[i] = min(
            dp_alt[i - 1] + a[i],
            dp_main[i - 1] + tm[i] + a[i],
        )

    result = min(dp_main[n - 1] + dm, dp_alt[n - 1] + da)
    return result
n = int(input())
m = list(map(int, input().split()))
a = list(map(int, input().split()))
tm = list(map(int, input().split()))
ta = list(map(int, input().split()))
m0, a0, dm, da = map(int, input().split())
print(minimize_project_time(n, m, a, tm, ta, m0, a0, dm, da))
