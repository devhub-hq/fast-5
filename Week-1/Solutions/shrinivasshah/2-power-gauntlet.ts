
function canPowerup (n: number): boolean {
    while (n > 1) {
        if (n % 2 !== 0) return false
        n = n / 2;
    }
    return true;
}

(console.log(canPowerup(8))); // true
(console.log(canPowerup(7))); // false
