# Two egg problem

## Question

A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.

If an egg is dropped from above that floor, it will break. If it is dropped from that floor or below, it will be completely undamaged and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.

## Answer

We will drop the first egg on certain intervals until it breaks, and search the previous interval iteratively starting from the bottom. We want the number of levels per interval to decrease by one so the total number of searches in the worst case will be the same. In other words,

n + (n-1) + (n-2) + ... + 2 + 1 >= 100
n(n+1) / 2 >= 100
n = 14

We will drop the first egg on floors 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, until it breaks, and use the second egg to search.
