## Non adjacent quantum states

In quantum mechanics, electrons in an atom occupy orbitals (energy levels).

A key rule is the Pauli Exclusion Principle: two electrons cannot occupy the same quantum state simultaneously.

Practically, this means electrons must “skip over” certain configurations to stay stable.

Now imagine you are given an array of energy values for orbitals.

If you place an electron in orbital i, you cannot place another electron in orbital i-1 or i+1 (they are adjacent, violating stability).

**Your goal:** maximize the total energy of the atom while respecting this quantum rule.

Example:
```
Input:
arr = {5, 5, 10, 100, 10, 5}
arr = {3, 2, 7, 10}
arr = {3, 2, 5, 10, 7}

```
```
Output:
110
13
15
```
