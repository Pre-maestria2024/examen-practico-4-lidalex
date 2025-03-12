
def max_dollars(m, n, h, d):
    total_d = sum(d)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Salud inicial 0, sin alimentos consumidos

    for i in range(m):
        temp_dp = dp.copy()
        for s in range(n + 1):
            if dp[s] != float('inf'):
                new_s = min(s + h[i], n)
                temp_dp[new_s] = min(temp_dp[new_s], dp[s] + d[i])
        dp = temp_dp

    return total_d - dp[n] if dp[n] != float('inf') else 0

def main():
    m, n = map(int, input().split())  # 
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    resultado = max_dollars(m, n, H, D)
    print(resultado)

if __name__ == '__main__':
    main()
