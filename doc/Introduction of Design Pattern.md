# What’s a design pattern?
Design Patterns are typical solutions to commonly occurring problems in software design. 
They are like already captured with the experience and already found out the pros and cons and suggested in which problem which Design pattern will be suitable. 

The pattern is not a specific piece of code, but a general concept for the solving the particular problem.

# Classification of patterns
There are total 23 patterns which has been categorised into 3 main groups of pattern by their intent, or purpose.

# 1) Creational Pattern : 
    It provide object creation mechanism that increases the flexibility and reuse of existing code,  (5)
#    a)	Factory 
    Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
#   b)	Abstract Factory : 
    Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
#    c)	Builder
    Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.
#    d)	Prototype
    Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum.
#    e)	Singleton
    Ensure a class has only one instance, and provide a global point of access to it.

# 2)	Structural patterns: 
    It explain how to assemble the objects and classes into larger structures, while keeping the structures flexible and efficient. (7)
#    a)	Adapter
    Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator.
#    b)	Bridge
    Decouple an abstraction from its implementation allowing the two to vary independently.
#    c)	Composite
    Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
#    d)	Decorator
    Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.
#    e)	Facade
    Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
#    f)	Flyweight
    Use sharing to support large numbers of similar objects efficiently.
#    g)	Proxy
    Provide a surrogate or placeholder for another object to control access to it.
# 3)	Behavioural Patterns: 
    It takes cate of effective communication and the assignment of the responsibility between objects. (11)
#    a)	Chain of Responsibility 
    Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
#    b)	Command
    Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations.
#    c)	Iterator
    Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
#    d)	Mediator
    Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to vary independently.
#    e)	Memento
    Without violating encapsulation, capture and externalize an object's internal state allowing the object to be restored to this state later.
#    k)  Null object
    Avoid null references by providing a default object.
#    g)	Observer
    Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.
#    h)	State
    Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
#    i)	Strategy
    Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
#    j)	Template
    Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
#    k)	Visitor
    Represent an operation to be performed on the elements of an object structure. Visitor lets a new operation be defined without changing the classes of the elements on which it operates.



