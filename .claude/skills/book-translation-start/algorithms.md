# Collaboration algorithms

Two algorithms from Wu et al. 2024, *(Perhaps) Beyond Human Translation* (arXiv:2405.11804). Both cap at **2 iterations** with early exit. They are not interchangeable — each is designed for a different kind of task.

---

## Algorithm 1 — Addition-by-Subtraction Collaboration

**Used for:** building the glossary and book summary during Preparation.
**Why:** the Addition agent tends to over-include generic terms; a dedicated Subtraction agent prunes them. Cheaper than Trilateral and well-suited to extractive tasks.

**Roles:**
- **Addition agent (A)** — Junior Editor. Extracts as much relevant information as possible.
- **Subtraction agent (S)** — Senior Editor. Reviews and removes redundant / generic / unhelpful entries; gives feedback to A.

**Procedure (max 2 iters, early exit if R = R′):**

```
H ← [context; instruction]      # conversation history
R ← ∅                            # current response
m ← 0
while m < 2:
    m ← m + 1
    R′ ← A(H)                    # Addition generates detailed response
    F  ← S(H, R′)                # Subtraction reviews + removes redundancies
    H  ← H + [R′; F]
    if R = R′:
        break                    # early exit: no further changes
    R ← R′
return R
```

---

## Algorithm 2 — Trilateral Collaboration

**Used for:** Translation, Localization, Proofreading sub-stages in the Execution phase.
**Why:** these are generative + judgment tasks where a separate critic and a separate decider produce higher-quality output than an Action agent self-evaluating.

**Roles (per sub-stage):**

| Sub-stage | Action (P) | Critique (Q) | Judgment (J) |
|---|---|---|---|
| Translation | Translator | Junior Editor | Senior Editor |
| Localization | Localization Specialist | Junior Editor | Senior Editor |
| Proofreading | Proofreader | Junior Editor | Senior Editor |

**Procedure (max 2 iters, early exit when J approves on iter ≥ 2):**

```
H ← [context; instruction]
m ← 0
while m < 2:
    m ← m + 1
    R ← P(H)                     # Action: generate response
    F ← Q(H, R)                  # Critique: feedback on R
    H ← H + [R; F]
    if m > 1:
        D ← J(context, instruction, R)   # Judgment: evaluate quality
        if D == TRUE:
            break                # early exit: quality acceptable
return R
```

Note: Judgment runs without conversation history (just the original context + instruction + final R) — agents have limited long-range context and the Judgment role benefits from a clean read.

---

## Why two iterations is the cap

Empirically the paper found diminishing returns past iter 2; further loops mostly thrash. If quality is still inadequate after 2 iters, the right move is to surface the defect to the user (or to the Final Review stage), not to keep iterating.
