- writing python w a focus on writing functional code
- exploring the walrus operator, lambda functions and pathlib
- not completing day-by-day necessarily.

[day1](https://adventofcode.com/2024/day/1):
- used Counter and list comprehensions; 15 mins each.

[day2](https://adventofcode.com/2024/day/2):
- coming back to this one lol; no reason.

[day3](https://adventofcode.com/2024/day/3):
- the regex matching had me head scratching for a little bit, but took about 30 mins each.

[day4](https://adventofcode.com/2024/day/4) (completed 8th Dec.):
- p1: took me a few gos, so took a bit of time experimenting w coordinates... initially missed a direction, so time spent debugging was cuz one of the diagonal directions wasn't being considered; 2-3 hours.
- p2: quickly figured this one out. overthought it a little, tried my best to encapsulate everything in functions to avoid repeating code where possible; 15-30 mins.

[day5](https://adventofcode.com/2024/day/5) (completed 10th Dec.):
- p1: fairly straightforward, initially misinterpreted the subset for a subsequence, but promptly adjusted for that mistake; 20 mins.
- p2: will admit took me longer that it'd like to admit... initial attempt involved working backwards and building contiguous subarrays and checking if the rules applied, clearly that didn't work for various reasons. had to use gpt for a few points of feedback on my code and initial attempt, scraped that and went down the elementwise comparison route; 3-4 hours.

[day6](https://adventofcode.com/2024/day/6):
- [p1](day6/p1.py): another familiar and simple one. involved moving in 4 dimensions, rotating clockwise between adjacent directions whenever a boundary was hit, count total number of Xs. spent a bit of time debugging, forgot to mark the starting pos 😛. code is a bit messy will need refactoring - didn't do things as efficiently as i wouldve liked; 30 mins.
- p2: found this one bit confusing. involved identifying potential cycles if a new obstacle was added. spent too much time investigating whether a non quadratic time was possible, ended up just accepting the brute force for the sake of my sanity lol; feeling tad bit defeated... - need to review ; 5-6 hours. 

day7
- p1: took a bit of time cuz of debugging. kept overriding the main pointer (k) by constantly reassigning it as `k = k // 2`; fixed by assigning k to a temp variable then manipulating that value; silly mistakes - review ; 2-3 hours.
- p2: confusing to say the least. going to come back to this one. will need to review.
