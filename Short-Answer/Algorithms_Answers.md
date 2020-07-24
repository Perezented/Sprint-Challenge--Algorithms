#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) what is n?
Error for true answer.
O((nlog(n))^3)

b) O(n)

c) log(n)

## Exercise II

Building can be 10 stories tall and an unknown floor is the break point of this rubber sounding egg.
Take the egg each floor and drop it from the middle most floor(around 5). if it breaks, go down to the mid point of the already existing midpoint(around floor 3). if it doesnt, find the midpoint the top half(around floor 7). Repeat test and keep finding the midpoint for each section of the building
(Binary Search)

<!--
make eggTest(floor)
    egg is on floor 1
    drop egg on floor 1,
        if it breaks, that's your floor.
        else:
            if it does not break,
            add a floor and run function with new floor number
 -->
