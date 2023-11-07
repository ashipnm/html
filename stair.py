def CountWays_DP(n) :
    ways = [ 0, 1, 2 ] 
    for i in range(3, n + 1) :
        ways.append(ways[i-1] + ways[i-2])
    return ways[n]

def CountWays_Rec (n) :
    if (n == 0 or n == 1 or n == 2) :
        return n
    return ( CountWays_Rec(n-1) + CountWays_Rec(n-2) )

def main() :

    steps = int(input("Enter steps : "))
    print("[DP] Ways of reaching the top : " + str(CountWays_DP(steps)))
    print("[Recursion] Ways of reaching the top : " + str(CountWays_Rec(steps)))

if __name__ == "__main__" :
    main()
