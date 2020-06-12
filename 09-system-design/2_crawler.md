# Crawler

## Question

I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages. I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a set, `visited`, where I'm storing URLs I've already `visited`. Now the crawler only visits a URL if it hasn't already been visited.

How can I trim down the amount of space taken up by `visited`?

## Answer

Use a trie, which uses O(s^n) space, rather than O(n \* s^n) space as before, where s is the size of the allowed character set.

Replace common prefixes/suffixes with characters not allowed in URLs.
