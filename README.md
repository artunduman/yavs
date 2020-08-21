# YAVS (Yet Another Visualizer for Sorting)
In the early phases of a CS education, almost every student learns about sorting. 
There are many visualizers for students to internalize these procedures. 
They are quite nice and for some cases specific, but not flexible. 
Wouldn't it be great if you could define your own algorithm and a framework would make necessary calls to show you what that would look like?


This framework allows its users to write their custom sorting logic with an extremely simple API.
It allows you to make simple changes to an existing sorting algorithm and run your visualization in no time! 

## Plug 'n' Play

## Write Your Own

## Installation

    pip install sorting-visualizer

## Limitations

The most obvious limitation of this framework is that sorting algorithm should be "in place". 
However, note that this definition of in place doesn't strictly mean it should take O(1) space.
Rather this means that the algorithm should make all the changes on the array itself. 
It can still take O(logn) space, because of the call stacks.
