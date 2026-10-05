# Code Review and Code Tracing Guide
## Pizza Topping and Discount Program

Use this guide to review and trace the **Pizza Topping and Discount** program.

The program is still a direct solution. The main goal for now is to understand how it works before improving it in later lessons.

---

# 1. Example Solution

```python
def calculate_total(topping_count):
    base_price = 10.00

    return (topping_count * 1.50) + base_price


is_topping = True
num_of_toppings = 0

while is_topping:

    user_input = input("Choose three toppings to add: \n" +
                       "* Pepperoni \n" +
                       "* Mushrooms \n" +
                       "* Extra Cheese \n" +
                       "Your choice: ")

    user_input = user_input.lower()

    if user_input == "done":
        break

    if user_input == "pepperoni" or user_input == "mushrooms" or user_input == "extra cheese":
        num_of_toppings += 1

    print("No. of toppings: ", num_of_toppings)
    print("\n")


final_total = calculate_total(num_of_toppings)

user_discount = input("Enter any discount code: ")

if user_discount == "PYTHON20":
    discount = calculate_total(num_of_toppings) * 0.20
else:
    discount = 0

print("Total toppings: ", num_of_toppings)
print("Sub-Total: ", final_total)
print("Discount: ", discount)
print("Final Total: ", final_total - discount)
```

---

# 2. What Does the Program Do?

The program allows the user to choose pizza toppings.

Available toppings are:

- `pepperoni`
- `mushrooms`
- `extra cheese`

Each topping costs:

```text
$1.50
```

The pizza has a base price of:

```text
$10.00
```

The user can keep entering toppings until they type:

```text
done
```

Afterward, the program asks for a discount code.

If the user enters:

```text
PYTHON20
```

the program gives a:

```text
20% discount
```

---

# 3. Identify the Main Variables

Before tracing the code, identify the important variables.

| Variable | Starting Value | Purpose |
|---|---:|---|
| `is_topping` | `True` | Controls the topping loop |
| `num_of_toppings` | `0` | Counts accepted toppings |
| `user_input` | Not yet assigned | Stores the topping entered by the user |
| `final_total` | Not yet assigned | Stores the subtotal before discount |
| `user_discount` | Not yet assigned | Stores the discount code entered |
| `discount` | Not yet assigned | Stores the amount deducted from the subtotal |

Inside the function:

| Variable | Purpose |
|---|---|
| `topping_count` | Receives the number of toppings |
| `base_price` | Stores the starting pizza price |

---

# 4. Review the Function

The function is:

```python
def calculate_total(topping_count):
    base_price = 10.00

    return (topping_count * 1.50) + base_price
```

The function receives:

```text
topping_count
```

The calculation is:

```text
(number of toppings × 1.50) + 10.00
```

For example:

```python
calculate_total(3)
```

becomes:

```text
(3 × 1.50) + 10.00
= 4.50 + 10.00
= 14.50
```

The function returns:

```text
14.50
```

---

# 5. Review the Loop

The loop begins with:

```python
while is_topping:
```

Since:

```text
is_topping = True
```

the loop starts.

The program asks the user to choose a topping.

```python
user_input = input(...)
```

Then:

```python
user_input = user_input.lower()
```

converts the input to lowercase.

For example:

```text
Pepperoni
```

becomes:

```text
pepperoni
```

This makes the topping input easier to compare.

---

# 6. Stopping the Loop

The first condition is:

```python
if user_input == "done":
    break
```

If the user types:

```text
done
```

the loop stops immediately.

No topping is added.

---

# 7. Checking the Topping

The program checks:

```python
if user_input == "pepperoni" or user_input == "mushrooms" or user_input == "extra cheese":
    num_of_toppings += 1
```

If the user's input matches any approved topping, the program increases:

```text
num_of_toppings
```

by `1`.

For example:

```text
num_of_toppings = 2
```

then:

```python
num_of_toppings += 1
```

becomes:

```text
num_of_toppings = 3
```

---

# 8. Full Code Trace

Suppose the user enters:

```text
Pepperoni
Mushrooms
Extra Cheese
done
```

Starting value:

```text
num_of_toppings = 0
```

## Iteration 1

Input:

```text
Pepperoni
```

After:

```python
user_input = user_input.lower()
```

the value becomes:

```text
pepperoni
```

Check:

```text
pepperoni == done → False
```

Then:

```text
pepperoni == pepperoni → True
```

So:

```python
num_of_toppings += 1
```

New value:

```text
num_of_toppings = 1
```

---

## Iteration 2

Input:

```text
Mushrooms
```

After `.lower()`:

```text
mushrooms
```

The topping is valid, so:

```text
num_of_toppings = 2
```

---

## Iteration 3

Input:

```text
Extra Cheese
```

After `.lower()`:

```text
extra cheese
```

The topping is valid, so:

```text
num_of_toppings = 3
```

---

## Iteration 4

Input:

```text
done
```

Check:

```text
done == done → True
```

So:

```python
break
```

runs.

The loop ends.

Final topping count:

```text
3
```

---

# 9. Loop Trace Table

| Iteration | Original Input | Input After `.lower()` | Valid Topping? | `num_of_toppings` |
|---|---|---|---|---:|
| Start | — | — | — | 0 |
| 1 | `Pepperoni` | `pepperoni` | Yes | 1 |
| 2 | `Mushrooms` | `mushrooms` | Yes | 2 |
| 3 | `Extra Cheese` | `extra cheese` | Yes | 3 |
| 4 | `done` | `done` | — | 3 |

---

# 10. Trace the Subtotal

After the loop:

```python
final_total = calculate_total(num_of_toppings)
```

At this point:

```text
num_of_toppings = 3
```

So the function call becomes:

```python
calculate_total(3)
```

Inside the function:

```text
topping_count = 3
base_price = 10.00
```

Calculation:

```text
(3 × 1.50) + 10.00
= 4.50 + 10.00
= 14.50
```

So:

```text
final_total = 14.50
```

---

# 11. Review the Discount

The program asks:

```python
user_discount = input("Enter any discount code: ")
```

Then it checks:

```python
if user_discount == "PYTHON20":
```

If the user enters:

```text
PYTHON20
```

then:

```python
discount = calculate_total(num_of_toppings) * 0.20
```

For three toppings:

```text
discount = 14.50 × 0.20
discount = 2.90
```

If the code does not match:

```python
else:
    discount = 0
```

---

# 12. Trace the Final Total

Using:

```text
final_total = 14.50
discount = 2.90
```

the final calculation is:

```python
final_total - discount
```

So:

```text
14.50 - 2.90 = 11.60
```

Final output:

```text
Total toppings: 3
Sub-Total: 14.5
Discount: 2.9
Final Total: 11.6
```

---

# 13. What Happens with an Invalid Topping?

Suppose the user enters:

```text
pineapple
```

After `.lower()`:

```text
pineapple
```

The condition:

```python
if user_input == "pepperoni" or user_input == "mushrooms" or user_input == "extra cheese":
```

is `False`.

So:

```text
num_of_toppings
```

does not change.

For example, if the current count is:

```text
2
```

it stays:

```text
2
```

---

# 14. Example with Invalid Input

Suppose the inputs are:

```text
pepperoni
pineapple
mushrooms
done
```

Trace:

| Iteration | Input | Valid? | Toppings Added | `num_of_toppings` |
|---|---|---|---:|---:|
| Start | — | — | — | 0 |
| 1 | `pepperoni` | Yes | 1 | 1 |
| 2 | `pineapple` | No | 0 | 1 |
| 3 | `mushrooms` | Yes | 1 | 2 |
| 4 | `done` | — | 0 | 2 |

---

# 15. Code Review Questions

## Function

- [ ] What is the function name?
- [ ] What parameter does it receive?
- [ ] What is the base price?
- [ ] How much does each topping cost?
- [ ] What value does the function return?

## Variables

- [ ] What is the starting value of `num_of_toppings`?
- [ ] What does `user_input` store?
- [ ] What does `final_total` store?
- [ ] What does `discount` store?
- [ ] Does `is_topping` ever change?

## Loop

- [ ] Why does the loop run?
- [ ] What causes the loop to stop?
- [ ] What does `break` do?
- [ ] Why is `.lower()` used?

## Conditions

- [ ] Which topping names are accepted?
- [ ] What happens when an invalid topping is entered?
- [ ] What happens when the user enters `done`?
- [ ] What happens when the discount code is correct?
- [ ] What happens when the discount code is incorrect?

---

# 16. Things to Notice During Code Review

The current solution works as a direct version, but there are parts that can be discussed and improved later.

## `is_topping`

The program contains:

```python
is_topping = True

while is_topping:
```

Ask:

```text
Does is_topping ever change?
```

At the moment, the loop is stopped using:

```python
break
```

---

## The Instruction Says "Choose Three Toppings"

The prompt says:

```text
Choose three toppings to add:
```

However, the current loop does not automatically stop after three toppings.

A user can enter more than three approved toppings before typing:

```text
done
```

This is something that can be improved later.

---

## Invalid Toppings

If the user enters an invalid topping, the count does not increase.

However, the program does not display a message telling the user that the topping was invalid.

A later version could add an `else` statement for this.

---

## Repeated Toppings

The current code allows the same topping to be entered more than once.

For example:

```text
pepperoni
pepperoni
pepperoni
```

will result in:

```text
num_of_toppings = 3
```

Whether this is allowed depends on the intended rules of the program.

---

## Discount Code Is Case-Sensitive

The program checks:

```python
if user_discount == "PYTHON20":
```

So:

```text
PYTHON20
```

works.

But:

```text
python20
Python20
```

do not.

This can be improved later if needed.

---

## Recalculating the Total

The program already stores:

```python
final_total = calculate_total(num_of_toppings)
```

But inside the discount condition, it calls the function again:

```python
discount = calculate_total(num_of_toppings) * 0.20
```

This still gives the correct result.

Later, students can discuss whether the existing value of:

```text
final_total
```

can be reused instead.

---

# 17. Blank Loop Trace Table

Use this table to trace another set of inputs.

| Iteration | User Input | Input After `.lower()` | Valid Topping? | Count Added | `num_of_toppings` | Action |
|---|---|---|---|---:|---:|---|
| Start | — | — | — | — | 0 | Start |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

# 18. Blank Function Trace

Final topping count:

```text
num_of_toppings = __________
```

Function call:

```python
calculate_total(__________)
```

Inside the function:

```text
topping_count = __________
base_price = 10.00
```

Calculation:

```text
(__________ × 1.50) + 10.00
```

```text
= __________ + 10.00
```

```text
= __________
```

Subtotal:

```text
final_total = __________
```

---

# 19. Blank Discount Trace

Discount code entered:

```text
____________________
```

Condition:

```text
user_discount == "PYTHON20" → __________
```

If the condition is `True`:

```text
discount = __________ × 0.20
discount = __________
```

If the condition is `False`:

```text
discount = 0
```

Final calculation:

```text
final_total - discount
```

```text
__________ - __________ = __________
```

---

# 20. Practice Exercise 1

Trace the program using:

```text
pepperoni
mushrooms
extra cheese
done
```

Then use:

```text
PYTHON20
```

as the discount code.

Complete:

| Iteration | Input | Valid? | `num_of_toppings` |
|---|---|---|---:|
| Start | — | — | 0 |
| 1 | `pepperoni` | | |
| 2 | `mushrooms` | | |
| 3 | `extra cheese` | | |
| 4 | `done` | | |

Then answer:

```text
Subtotal = __________
Discount = __________
Final Total = __________
```

---

# 21. Practice Exercise 2

Trace:

```text
Pepperoni
Pineapple
Mushrooms
done
```

Discount code:

```text
NONE
```

Answer:

1. What does `.lower()` do to `Pepperoni`?
2. Does `Pineapple` increase the topping count?
3. What is the final number of toppings?
4. What is the subtotal?
5. Is a discount applied?
6. What is the final total?

---

# 22. Practice Exercise 3

Trace:

```text
pepperoni
pepperoni
pepperoni
pepperoni
done
```

Answer:

1. What is the final value of `num_of_toppings`?
2. Does the current program stop automatically after three toppings?
3. What subtotal is calculated?
4. What part of the program could be changed later if the rule is exactly three toppings?

---

# 23. Short Review Activity

Complete the statements.

1. The pizza base price is __________.
2. Each topping costs __________.
3. `num_of_toppings` begins at __________.
4. Typing __________ causes the loop to stop.
5. `.lower()` converts the user's input to __________.
6. The discount code is __________.
7. The discount percentage is __________%.
8. The function used to calculate the subtotal is called __________.
9. The final amount is calculated using `__________ - __________`.

---

# 24. Simple Code Review Process

When reviewing similar programs:

1. Identify the purpose of the program.
2. Find the variables and their starting values.
3. Identify the loop.
4. Find what causes the loop to stop.
5. Trace one input at a time.
6. Record any variable that changes.
7. Check each condition.
8. Trace the function separately.
9. Follow the discount calculation.
10. Check the final output.
11. Identify parts that can be improved later.

---

# Final Reminder

For this program, keep track of:

```text
user_input
num_of_toppings
final_total
user_discount
discount
```

When tracing a line, ask:

```text
What is the current value?
What condition is being checked?
Does anything change after this line?
```

Tracing the values step by step will make the program easier to understand.
