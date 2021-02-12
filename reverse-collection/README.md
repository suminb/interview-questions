Functionally Reverse Collection
===============================

Given an interface `Collection` that provides the following functionalities,
write a function to reverse a collection.

```java
interface Collection<T> {
    boolean isEmpty();
    T first();
    T last();
    Collection<T> dropFirst();
    Collection<T> dropLast();
    Collection<T> append(T);
    Collection<T> empty();
}
```

Time limit: 10min
