## Even pair

In an ancient observatory, two astronomers are charting pairs of stars (X, Y).

The first star, X, can only have brightness values from 1 to A.

The second star, Y, can only have brightness values from 1 to B.

The astronomers are only interested in cosmic pairs where the combined brightness (X + Y) shines evenly across the universe in other words, where X + Y is even.

**Your task:** Count how many such star pairs exist.

**constraints** : space `0(1)` , time `0(1)`

Example:
```
Input:
1 1
2 3
4 6
8 9
```

```
Output:
1
3
12
36
```

Exaplaination :
```
X=2 , Y=3

1      1   (Even)
1      2   (Odd)
1      3   (Even)
2      2   (Even)
2      3   (Odd)

Output : 3
```
