---
name: doing-tests
description: Design and implement educational automated tests for Jupyter notebook labs using notebook-cell-tester.
---

# Purpose

Create automated tests for Jupyter notebook lab exercises in this repository using the [notebook-cell-tester](https://raw.githubusercontent.com/EnriqueVilchezL/notebook_cell_tester/main/README.md) framework. **YOU MUST Search the internet for this provided link only (library's documentation and examples) before writing any tests.**

Tests exist to help students learn, not to grade them strictly. Every test should give actionable feedback and help students find and fix their own mistakes.

---

# Core Principles

- Validate learning objectives, not implementation details.
- Allow multiple valid solutions; avoid brittle tests tied to formatting, variable names, or harmless differences.
- Prefer checking behavior, outputs, and concepts over exact code structure.
- Provide clear, educational feedback on every failure.
- Cover common mistakes students make (wrong formula, off-by-one, hardcoded answers, etc.).
- Keep the student experience positive.

Do **not**:
- Require a specific algorithm unless the exercise explicitly teaches it.
- Test irrelevant details or duplicate coverage.
- Make assumptions students cannot reasonably infer from the exercise.

---

# Workflow

## Step 1 — Read the Lab

Read the entire notebook before writing a single test. Identify:

- Learning objectives and concepts taught.
- Expected student outputs (printed text, variables, function return values).
- Common mistakes students are likely to make.
- **Also read the `TESTS.md` file in the notebook's directory** if one exists. It may impose hard constraints (e.g., "must not use `break`", "must have a `main` function").

## Step 2 — Plan Tests Into Sections

For each exercise, think about:
- What the student **must** demonstrate (essential outcomes).
- What **valid variations** are acceptable (different variable names, different pandas methods, different plot styles).
- What **common mistakes** tests should catch.
- Whether the student might **cheat** (hardcoded answers, modifying provided variables).

Structure every test suite using the sections below. **Only include a section if the exercise contains content that warrants it.** Do not force sections that are irrelevant to what students have seen. Remember, the topics are covered sequentially, starting with basic programming concepts and progressing to more advanced topics like data manipulation and visualization. Each lab exercise builds on previous ones, so you cannot test for concepts that have not yet been taught.

The sections must be of the following types:

### Section 1 — Correctness
Tests for the core expected behavior and main cases.
- Verify the result of the main computation or output.
- Use tolerances for floating-point comparisons.
- Cover the typical, "happy path" scenario.

### Section 2 — Edge Cases
Tests for boundary values, special inputs, and non-obvious scenarios.
- Empty inputs, zero, negative numbers, single elements.
- Maximum/minimum values.
- Only include if the exercise logic changes meaningfully at boundaries.

### Section 3 — Error Handling
Tests that verify the student's code handles bad input correctly.
- Only include if the exercise explicitly asks for input validation or error handling.

### Section 4 — Code Style / Structure
Tests that enforce structural or stylistic requirements.
- Use `regex` to confirm required constructs are present (e.g., a `for` loop, a comment, a `def` statement).
- Use `not_regex` to forbid forbidden constructs (e.g., `while True`, `break`, a specific built-in).
- Use these to reinforce the programming concept being taught, not to be pedantic.
- Only include if the exercise explicitly requires or forbids a specific construct, or if the TESTS.md file mandates it.

### Section 5 — Variables & State
Tests that verify variables hold the correct values and types after execution, if there are global variables in the cell.
- Verify that students are **not modifying provided starter variables** (e.g., given lists or datasets).
- Only include if the exercise defines specific variables that must exist with specific values.

### Section 6 — Functions
Tests for individual functions defined by the student.
- Call each function with controlled inputs and check its return value or printed output.
- Test both typical inputs and edge cases for each function.
- Only include if the exercise asks students to define functions.

Example of a test suite with only relevant sections:

```python
# Section 1 — Correctness
tests = [
  TestSection("Parte 1: Correctitud", [
    TestCase(
      name="Programa con 1 vehículo en zona de riesgo",
      test_type="regex_output",
      stdin_input="1\n1500\n20\n",
      pattern=r"300000.*Zona de riesgo.*1"
      error_message="El programa no calcula correctamente el área de la zona de riesgo o no identifica correctamente el número de vehículos en esa zona. Revise la fórmula del área de un círculo y cómo compara las distancias de los vehículos con el radio R."
    ),
    ...
  ]),
  TestSection("Parte 2: Casos extremos", [
    TestCase(
      name="Programa con 0 vehículos en zona de riesgo",
      test_type="regex_output",
      stdin_input="1\n1500\n5\n",
      pattern=r"300000.*Zona de riesgo.*0"
      error_message="El programa no maneja correctamente el caso donde ningún vehículo está dentro de la zona de riesgo. Asegúrese de que la comparación entre la distancia del vehículo y el radio R se realiza correctamente."
    ),
    ...
  ]),
  ...
]
```

---

## Step 4 — Write Good Failure Messages

Every failing test must answer three questions:

1. What is wrong?
2. Why does it matter?
3. What should the student investigate?

**Good:** "El promedio calculado no es correcto. Revisa si estás dividiendo entre el número total de elementos."

**Bad:** `assert resultado == 5`

---

## Step 5 — Validate the Tests

Before finishing:

- **Positive:** A correct solution passes all tests. Alternative correct solutions also pass.
- **Negative:** Intentionally wrong solutions (wrong formula, missing step, hardcoded answer) fail with useful messages.
- **Robustness:** Tests do not fail due to minor variations in variable names or cell ordering (unless those are the point of the test).

---

# Quality Checklist

Before delivering a test suite:

- [ ] Every test maps to a learning objective.
- [ ] Only sections relevant to the exercise content are included.
- [ ] Failure messages are educational and actionable.
- [ ] Floating-point comparisons use tolerances.
- [ ] Common student mistakes are detected.
- [ ] Alternative valid solutions pass.
- [ ] Hardcoding and variable mutation are checked where applicable.
- [ ] TESTS.md constraints are fully respected.
- [ ] Both correct and incorrect solutions have been mentally validated.

---

# Output Format

When delivering tests:

1. Summarize the notebook's learning objectives.
2. List which sections apply and why (skip sections that are not relevant).
3. For each section, briefly explain what each test checks and what mistake it catches.
4. Write the notebook-cell-tester test code, organized by section with clear comments.
5. Note any assumptions or limitations in the test suite.
