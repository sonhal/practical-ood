# Designing Classes with a Single Responsibility

The foundation of an object-oriented system is the message. Bu the most visivle is the class.
This chapter will start by concentration on what belongs in a class. What are your classes, how many should there be, 
behaviour should they implement? And maybe most importantly how much of themself should they expose?


First insist that it should be simple! The goal is to model the application using classes. Such that it does what it is 
supposed to do right now and is also easy to change later.

Anyone can arrange code to work right now. Creating a easy to change application is a different matter. The quality of 
easy changebility reveals the craft of the programmer.

The techniques for doing this are lucky easy!

2.1 DECIDING WHAT BELONGS IN A CLASS
You know what code you need to write, but not where to put it.

2.1.1 Grouping Methods into Classes

In class based OO langues like Ruby, Java methods are defined in classes. The classes created will affect how you think 
about the application forever. They define a virtual world, on that constraints the imagination for everyone downstream.
If the application successeds, many of the earlier descings will need to bechanged later. When that day comes, your or 
any other developers ability to successfully make those changes is determined by the applications design.

Design is more the art of preserving changebility than it is the act of achiving perfection.

2.1.2 Organizing Code to Allow for Easy Changes

We define east to change as:

 - changes have no unexpected side effects
 - small changes in requirments require correspondingly small changes in code
 - exisiting code is easy to reuse
 - the easiest way to make a change is to add code that itself is easy to change
 
 Code should therefore be:
 
 - Transparent
    
    The consequences of change should be obcious in the code that is changing and in distant code that relies on it.
 
 - Reasonable
 
    The cost of any change should be proportional to the benefits the change achieves
 
 - Usable
 
    Existing code should be usable in new and unexpected contexts
    
 - Exemplary
 
    The code itself should encourage those who change it to perpetuate these qualities
    
 
Code that is Transparent, Reasonable, Usable, and Exemplary (TRUE) not only meets today’s needs but can also be changed 
to meet the needs of the future. The first step in creating code that is TRUE is to ensure that each class has a 
single, well-defined responsibility.
 
2.2 CREATING CLASSES THAT HAVE A SINGLE RESPONSIBILITY
A class should do the smallest possible useful thing; that is, it should have a single responsibility.

When creating the first classes, look for class candidates that have both data and behaviour


 
