
## `calculate_average(numbers: list[float]) → float`

Compute the arithmetic mean of a list of numbers.

**Parameters**

* `numbers` – A list (or tuple) of numeric values.

**Returns**

* The average (sum of all elements divided by count).
* Returns `0` if the list is empty (avoids division-by-zero).

**Example**

```python
>>> calculate_average([5, 10, 15, 20])
12.5
>>> calculate_average([])
0
```

---

## `greet_user(name: str, greeting: str = "Hello") → str`

Produce a personalized greeting message.

**Parameters**

* `name` – The user’s name.
* `greeting` *(optional)* – The salutation to use (defaults to `"Hello"`).

**Returns**

* A single string of the form `"{greeting}, {name}!"`.

**Example**

```python
>>> greet_user("Alice")
"Hello, Alice!"
>>> greet_user("Bob", "Hi")
"Hi, Bob!"
```

---

## `calculate_total(*prices: float, discount: float = 0) → float`

Sum an arbitrary number of item prices and optionally apply a percentage discount.

**Parameters**

* `*prices` – Any number of positional numeric arguments, each representing an item price.
* `discount` *(keyword-only, optional)* – A percentage to deduct from the total (e.g. `10` for 10% off).

**Returns**

* The total cost after applying the discount. If `discount=0`, returns the plain sum.

**Example**

```python
>>> calculate_total(10, 20, 30)
60.0
>>> calculate_total(10, 20, 30, discount=10)
54.0   # (10 + 20 + 30) * 0.9 = 54
```

---

## `create_multiplier(factor: float) → Callable[[float], float]`

Generate a one-argument function that scales its input by a fixed factor.

**Parameters**

* `factor` – The multiplier to embed in the returned function.

**Returns**

* A new function `multiplier(x)` that returns `factor * x`.

**Example**

```python
>>> double = create_multiplier(2)
>>> triple = create_multiplier(3)

>>> double(5)
10
>>> triple(5)
15
```

---
