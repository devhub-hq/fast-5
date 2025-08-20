
function findDuplicate (str: string) {
    let result = "";
    if (!str) return "";
    const arr = str.split("");
    const seen = new Set<string>();
    arr.forEach((item) => {
        if (seen.has(item)) {
            result = item;
        } else {
            seen.add(item);
        }
    });
    return result;
}

console.log(findDuplicate("abca"));
console.log(findDuplicate("abcde"));