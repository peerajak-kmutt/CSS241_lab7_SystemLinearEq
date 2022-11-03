# Nested List Comprehension

## 1. Create a matrix whose Lower Traingle and diagonal elements are 1, and the rest are 0.</br >

For Example</br >

```python
n=3
onesk = np.ones((n,n))
print(onesk)
```
```ruby
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
```

```python
print('We want this matrix\n')
print(np.array([[1.,0.,0.],[1.,1.,0.],[1.,1.,1.]]))
```
```ruby
We want this matrix

[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]
 ```
```python
zero_xyindx = [(0,1),(0,2),(1,2)]
xyindx = tuple(zip(*zero_xyindx))
print(xyindx)
print('Notice ((all x),(all y))')
```
```ruby
((0, 0, 1), (1, 2, 2))
Notice ((all x),(all y))
```
```python
onesk[xyindx] = 0
print(onesk)
```
```ruby
[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]
```


## 2. List of primes number less than N
Below shows the code that return list of all prime numbers, which are less than N</br >
```python
N=100
primes = []
for num in range(1,N):
    list_of_divisables = []
    for d in range(2,num):
        if num%d == 0: #divisable by some number
            list_of_divisables.append(d)
    if not list_of_divisables:
        primes.append(num)
        
print(primes)
```
Your job is to write this into Nested list comprehension with only one line of code.

## 3. Dict of primes whose key is the index of prime number.
We want odd keys only. Eg. primes from Prob2 is the list of primes.
```python
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```
We create dict of primes this way
```python
dict_of_primes = dict(zip(range(len(primes)),primes))
print(dict_of_primes)
```
```ruby
{0: 1, 1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17, 8: 19, 9: 23, 10: 29, 11: 31, 12: 37, 13: 41, 14: 43, 15: 47}
```
We want only those odd-value-keys.
```ruby
{1: 2, 3: 5, 5: 11, 7: 17, 9: 23, 11: 31, 13: 41, 15: 47}
```
Answer should be only 2 lines of code
```python
  primes = #Your code here Ans from Problem2
  odd_dict_of_primes =  #Your Code Here  
  ```
