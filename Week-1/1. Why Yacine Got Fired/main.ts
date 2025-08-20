
function findMissingNumber(n: number, arr: Array<number>): number {
    const expectedSum = (n * (n + 1)) / 2;
    const actualSum = arr.reduce((acc, val) => acc + val, 0);
    return expectedSum - actualSum;
}

console.log(findMissingNumber(5, [1, 2, 5, 3])); // 4
console.log(findMissingNumber(5, [2, 3, 4, 5])); // 1
console.log(findMissingNumber(5, [1, 2, 3, 4])); // 5
