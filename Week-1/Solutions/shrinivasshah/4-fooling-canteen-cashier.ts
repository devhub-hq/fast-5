function canChooseFunnySnacks(N: number, X: number, prices: Array<number>): string {
    let odd = prices.filter(p => p % 2 === 1).length;
    let even = N - odd;

    for (let oddCount = 1; oddCount <= Math.min(X, odd); oddCount += 2) {
        let evenCount = X - oddCount;
        if (evenCount <= even) {
            return "YES";
        }
    }
    return "NO";
}

console.log(canChooseFunnySnacks(5, 3, [1, 2, 3, 4, 5]));
console.log(canChooseFunnySnacks(4, 2, [1, 2, 3, 4]));