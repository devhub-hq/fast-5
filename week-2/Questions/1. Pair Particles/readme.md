## Pair Particles
In the universe, particles are usually created in pairs — an electron with a positron, a quark with an antiquark.

Astronomers are studying data from a cosmic detector. Normally, every particle ID appears exactly twice (once for the particle, once for its twin).

But due to a quantum glitch, one particle was recorded without a partner.

**Your task:**
 Given a list of particle IDs, where every ID appears twice except one, find that lone particle.


**Constraints:**

- Solve it in `O(n)` time (the detector streams massive data).
- Use only `O(1)` space (memory is limited aboard the spacecraft).

Test case :
```
Input : particles = [101, 7, 42, 101, 42]
Output: 7
```

<details>
<summary>Hint for optimisation
</summary>

When a particle meets its twin, they annihilate, leaving nothing behind.
</details>
