# Code Review and Code Tracing Guide
## Starship Cargo Loader

A guide to review and trace the **Starship Cargo Loader** program.

The goal is to understand how the example solution works before making improvements to it later.

---

# 1. Example Solution

```python
def calculate_fuel(cargo_weight):
    starship_base_weight = 50000

    # return final fuel amount
    return (cargo_weight + starship_base_weight) * 3


is_loading = True
total_cargo_weight = 0
MAX_CARGO_WEIGHT = 10000

while is_loading:

    user_input = input("Choose which cargo to load:\n" +
                       "* Satellite\n" +
                       "* Rover\n" +
                       "* Supplies\n" + 
                       "Your choice: ")

    if user_input == "launch":
        break

    if user_input == "satellite":
        total_cargo_weight += 1000
        print("Satellite loaded successfully")
    elif user_input == "rover":
        total_cargo_weight += 2500
        print("Satellite loaded successfully")
    elif user_input == "supplies":
        total_cargo_weight += 500
        print("Satellite loaded successfully")
    else:
        print("Item not approved for the mission")

    print("\n Current cargo weight: ", total_cargo_weight, "\n")

    if total_cargo_weight > MAX_CARGO_WEIGHT:
        print("MAX WEIGHT REACH")
        break


print("Total cargo weight: ", total_cargo_weight)
print("Amount of Fuel needed: ", calculate_fuel(total_cargo_weight))
```

---

# 2. What Does the Program Do?

The program allows the user to load cargo into a starship.

The available cargo items are:

| Cargo | Weight |
|---|---:|
| `satellite` | 1,000 kg |
| `rover` | 2,500 kg |
| `supplies` | 500 kg |

The program keeps asking for cargo until:

- the user enters `launch`; or
- the cargo weight becomes greater than `10,000 kg`.

After loading is finished, the program calculates the amount of fuel needed.

---

# 3. Start with the Variables

Before tracing the loop, identify the starting values.

```python
is_loading = True
total_cargo_weight = 0
MAX_CARGO_WEIGHT = 10000
```

| Variable | Starting Value | Purpose |
|---|---:|---|
| `is_loading` | `True` | Controls whether the loop continues |
| `total_cargo_weight` | `0` | Stores the total weight of loaded cargo |
| `MAX_CARGO_WEIGHT` | `10000` | Stores the maximum cargo weight |
| `user_input` | Not yet assigned | Stores the user's current choice |

Questions to ask:

- Which variables can change?
- Which variables stay the same?
- Which variable keeps the running total?

---

# 4. Review the Function

The program starts with:

```python
def calculate_fuel(cargo_weight):
    starship_base_weight = 50000

    return (cargo_weight + starship_base_weight) * 3
```

The function receives one value:

```text
cargo_weight
```

It then uses the starship's base weight:

```text
50,000 kg
```

The calculation is:

```text
(cargo weight + 50,000) × 3
```

For example:

```python
calculate_fuel(4000)
```

becomes:

```text
(4000 + 50000) × 3
54000 × 3
162000
```

The function returns:

```text
162000
```

---

# 5. Review the Loop

The loop begins with:

```python
while is_loading:
```

At the start:

```text
is_loading = True
```

So the loop runs.

Inside the loop, the program asks the user to enter a cargo item.

```python
user_input = input(...)
```

The value entered by the user is stored in:

```text
user_input
```

---

# 6. First Check: Is the User Ready to Launch?

The first condition inside the loop is:

```python
if user_input == "launch":
    break
```

If the user types:

```text
launch
```

the condition becomes `True`.

The `break` statement immediately exits the loop.

No cargo is added.

---

# 7. Checking the Cargo Type

If the input is not `launch`, the program checks the cargo type.

```python
if user_input == "satellite":
    total_cargo_weight += 1000

elif user_input == "rover":
    total_cargo_weight += 2500

elif user_input == "supplies":
    total_cargo_weight += 500

else:
    print("Item not approved for the mission")
```

Only one branch will run for each input.

Example:

```text
user_input = "rover"
```

The checks are:

```text
user_input == "satellite" → False
user_input == "rover"     → True
```

So:

```python
total_cargo_weight += 2500
```

runs.

---

# 8. Understanding `+=`

This line:

```python
total_cargo_weight += 2500
```

means:

```python
total_cargo_weight = total_cargo_weight + 2500
```

If:

```text
total_cargo_weight = 1000
```

then:

```text
1000 + 2500 = 3500
```

The new value is:

```text
3500
```

---

# 9. Checking the Maximum Cargo Weight

After processing the cargo, the program checks:

```python
if total_cargo_weight > MAX_CARGO_WEIGHT:
    print("MAX WEIGHT REACH")
    break
```

Since:

```text
MAX_CARGO_WEIGHT = 10000
```

the loop stops only when:

```text
total_cargo_weight > 10000
```

Notice that the condition uses:

```python
>
```

not:

```python
>=
```

This means exactly `10,000 kg` is still allowed by the current code.

---

# 10. Full Code Trace

Suppose the user enters:

```text
satellite
rover
supplies
launch
```

Starting value:

```text
total_cargo_weight = 0
```

## Iteration 1

Input:

```text
satellite
```

Check:

```text
satellite == launch → False
```

Then:

```text
satellite == satellite → True
```

Add:

```text
1000 kg
```

New total:

```text
0 + 1000 = 1000
```

Maximum weight check:

```text
1000 > 10000 → False
```

The loop continues.

---

## Iteration 2

Input:

```text
rover
```

Add:

```text
2500 kg
```

New total:

```text
1000 + 2500 = 3500
```

Maximum weight check:

```text
3500 > 10000 → False
```

The loop continues.

---

## Iteration 3

Input:

```text
supplies
```

Add:

```text
500 kg
```

New total:

```text
3500 + 500 = 4000
```

Maximum weight check:

```text
4000 > 10000 → False
```

The loop continues.

---

## Iteration 4

Input:

```text
launch
```

Check:

```text
launch == launch → True
```

So:

```python
break
```

runs.

The loop ends.

Final cargo weight:

```text
4000 kg
```

---

# 11. Loop Trace Table

| Iteration | `user_input` | Weight Added | `total_cargo_weight` | Max Weight Exceeded? | Result |
|---|---|---:|---:|---|---|
| Start | — | — | 0 | No | Loop begins |
| 1 | `satellite` | 1000 | 1000 | No | Continue |
| 2 | `rover` | 2500 | 3500 | No | Continue |
| 3 | `supplies` | 500 | 4000 | No | Continue |
| 4 | `launch` | 0 | 4000 | — | `break` |

---

# 12. Trace the Fuel Calculation

After the loop, the program prints:

```python
print("Total cargo weight: ", total_cargo_weight)
```

At this point:

```text
total_cargo_weight = 4000
```

The next line is:

```python
print("Amount of Fuel needed: ", calculate_fuel(total_cargo_weight))
```

So the function call is:

```python
calculate_fuel(4000)
```

Inside the function:

```text
cargo_weight = 4000
starship_base_weight = 50000
```

Calculation:

```text
(4000 + 50000) × 3
= 54000 × 3
= 162000
```

Returned value:

```text
162000
```

---

# 13. Final Output

For the example above, the important final output is:

```text
Total cargo weight: 4000
Amount of Fuel needed: 162000
```

---

# 14. Trace an Invalid Input

Suppose the user enters:

```text
laptop
```

The conditions become:

```text
laptop == satellite → False
laptop == rover     → False
laptop == supplies  → False
```

The `else` block runs:

```python
print("Item not approved for the mission")
```

No weight is added.

If:

```text
total_cargo_weight = 1000
```

before entering `laptop`, it remains:

```text
1000
```

---

# 15. Trace the Maximum Weight Condition

Suppose the current cargo weight is:

```text
9000 kg
```

The user enters:

```text
rover
```

A rover adds:

```text
2500 kg
```

So:

```text
9000 + 2500 = 11500
```

The program then checks:

```python
if total_cargo_weight > MAX_CARGO_WEIGHT:
```

Substitute the values:

```text
11500 > 10000 → True
```

The program prints:

```text
MAX WEIGHT REACH
```

and exits the loop.

Final cargo weight:

```text
11500 kg
```

This happens because the current code checks the limit **after** adding the cargo.

---

# 16. Code Review Questions

Use these questions when reviewing the program.

## Function

- [ ] What is the name of the function?
- [ ] What parameter does it receive?
- [ ] What is the value of `starship_base_weight`?
- [ ] What calculation is performed?
- [ ] What value does the function return?

## Variables

- [ ] What is the starting value of `total_cargo_weight`?
- [ ] What is the value of `MAX_CARGO_WEIGHT`?
- [ ] What does `user_input` store?
- [ ] Does `is_loading` ever change its value?

## Loop

- [ ] Why does `while is_loading` run?
- [ ] What happens when the user enters `launch`?
- [ ] What does `break` do?
- [ ] What other condition can stop the loop?

## Conditions

- [ ] What happens when the user enters `satellite`?
- [ ] What happens when the user enters `rover`?
- [ ] What happens when the user enters `supplies`?
- [ ] What happens when the user enters an invalid item?

## Maximum Weight

- [ ] When is the maximum cargo weight checked?
- [ ] What happens if the total becomes exactly `10,000 kg`?
- [ ] What happens if the total becomes `10,500 kg`?

---

# 17. Things to Notice During Code Review

A code review is not only about finding errors. It also involves noticing how the program was written.

Look at these parts of the current solution.

## `is_loading`

```python
is_loading = True

while is_loading:
```

Ask:

```text
Does the value of is_loading ever change?
```

At the moment, the loop is stopped using `break`.

This can be discussed later when improving the program.

---

## Confirmation Messages

Look at these lines:

```python
elif user_input == "rover":
    total_cargo_weight += 2500
    print("Satellite loaded successfully")

elif user_input == "supplies":
    total_cargo_weight += 500
    print("Satellite loaded successfully")
```

Ask:

```text
Does the printed message match the cargo that was loaded?
```

The calculation is still correct, but the message can be improved.

---

## Case-Sensitive Input

The program checks:

```python
if user_input == "satellite":
```

So:

```text
satellite
```

works.

But:

```text
Satellite
SATELLITE
```

do not match the condition.

This can also be improved later.

---

## Maximum Weight Check

The current program adds the cargo first and checks the maximum afterward.

Example:

```text
Current cargo = 9000 kg
Rover = 2500 kg
New total = 11500 kg
```

Only after reaching `11500` does the program stop.

Ask:

```text
Should the cargo be added first, or should the program check first whether it will fit?
```

This is another possible improvement.

---

# 18. Blank Trace Table

Use this table for another set of inputs.

| Iteration | `user_input` | Condition Matched | Weight Added | `total_cargo_weight` | Max Weight Check | Action |
|---|---|---|---:|---:|---|---|
| Start | — | — | — | 0 | — | Start loop |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

---

# 19. Blank Fuel Trace

Final cargo weight:

```text
total_cargo_weight = __________
```

Function call:

```python
calculate_fuel(__________)
```

Inside the function:

```text
cargo_weight = __________
starship_base_weight = 50000
```

Calculation:

```text
(__________ + 50000) × 3
```

```text
= __________ × 3
```

```text
= __________
```

Returned fuel amount:

```text
__________ gallons
```

---

# 20. Practice Exercise

Trace the program using:

```text
rover
satellite
supplies
rover
launch
```

Complete the table.

| Iteration | Input | Weight Added | Total Cargo Weight |
|---|---|---:|---:|
| Start | — | — | 0 |
| 1 | `rover` | | |
| 2 | `satellite` | | |
| 3 | `supplies` | | |
| 4 | `rover` | | |
| 5 | `launch` | | |

Then answer:

1. What is the final cargo weight?
2. Was the maximum cargo weight reached?
3. What value is passed to `calculate_fuel()`?
4. How much fuel is needed?

---

# 21. Short Review Activity

Complete the statements.

1. `total_cargo_weight` starts at __________.
2. A satellite adds __________ kg.
3. A rover adds __________ kg.
4. Supplies add __________ kg.
5. Typing `launch` causes the program to execute __________.
6. The maximum cargo weight is __________ kg.
7. Fuel is calculated using `(cargo weight + __________) × __________`.
8. The function used to calculate fuel is called __________.

---

# 22. Simple Code Review Process

When reviewing similar programs, use this order:

1. Identify the program's purpose.
2. Find the variables and their starting values.
3. Identify the loop.
4. Find the condition that stops the loop.
5. Trace one user input at a time.
6. Record every change in the important variables.
7. Check each `if`, `elif`, and `else`.
8. Trace any function calls separately.
9. Check the final output.
10. Look for parts that work but could still be improved.

---

# Final Reminder

When tracing this program, keep watching these values:

```text
user_input
total_cargo_weight
is_loading
```

When the loop ends, trace:

```text
calculate_fuel(total_cargo_weight)
```

For each line, ask:

```text
What is the current value?
What condition is being checked?
What changes after this line?
```

That is enough to trace the program correctly.
