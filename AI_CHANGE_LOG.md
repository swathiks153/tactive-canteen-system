# AI Change-Loop Evidence Log

## 1. AI-Assisted Development

AI tools were used throughout the development process to support implementation,
debugging, testing, documentation, and refinement of the Tactive Canteen System.

The developer reviewed, tested, and validated all AI-assisted changes before
including them in the project.

## 2. Change Loop

### Attempt 1 — Core Application

**Goal:** Build the basic canteen ordering workflow.

**AI assistance:** Used AI to help structure the Flask application, database
operations, templates, and ordering workflow.

**Result:** The application successfully supported food listing, ordering,
stock handling, and order history.

**Validation:** The application was manually tested through the web interface.

---

### Attempt 2 — Input Validation

**Goal:** Handle invalid order quantities safely.

**Problem identified:** The application needed explicit validation for invalid
quantities and insufficient stock.

**AI assistance:** Used AI to identify validation cases and improve the
application's error-handling logic.

**Changes made:**
- Added zero/invalid quantity validation.
- Added insufficient-stock validation.
- Added maximum order quantity validation.

**Validation:** Corresponding automated tests and manual UI tests were added.

---

### Attempt 3 — Automated Testing

**Goal:** Verify the application behaviour automatically.

**AI assistance:** Used AI to help design and refine pytest test cases.

**Test coverage included:**
- Home page
- Successful order
- Zero quantity
- Insufficient stock
- Maximum order quantity

**Initial result:**

`5 passed`

---

### Attempt 4 — Deliberate Failure / Red Run

**Goal:** Verify that the test suite correctly detects an incorrect expectation.

The maximum-quantity test was deliberately changed from:

`assert response.status_code == 400`

to:

`assert response.status_code == 200`

The test suite was executed again.

**Result:**

`1 failed, 4 passed`

The failure showed that the application returned HTTP 400 while
the deliberately incorrect test expected HTTP 200.

Evidence:

`tests/deliberate_red_run.png`

---

### Attempt 5 — Correction

**Problem diagnosis:** The application correctly returned HTTP 400 for an
order exceeding the maximum allowed quantity. The test expectation had been
intentionally changed to the incorrect value.

**Correction:** Restored the assertion to:

`assert response.status_code == 400`

**Final validation:**

`5 passed`

This confirmed that the test suite and application were working correctly
after the correction.

---

## 3. Documentation Loop

AI assistance was also used to improve and organize project documentation,
including:

- README
- Project documentation
- User guide
- Feature descriptions
- Testing documentation

The final documentation was reviewed against the implemented application.

## 4. Human Verification

AI-generated suggestions were not accepted blindly. Changes were checked by:

1. Running the application.
2. Running automated tests.
3. Performing manual UI checks.
4. Reviewing failures.
5. Correcting incorrect test expectations.
6. Re-running the complete test suite.

The final implementation was verified with:

`5 passed`

## 5. Evidence Summary

| Stage | Result |
|---|---|
| Initial automated test | 5 passed |
| Deliberate red run | 1 failed, 4 passed |
| Correction | Test expectation restored |
| Final automated test | 5 passed |
| Manual UI validation | Completed |
| Documentation update | Completed |

## 6. AI Tools Used

**ChatGPT** — Used for implementation guidance, debugging, test design,
documentation, validation strategies, and refinement.

AI assistance was used as a development aid while the final implementation,
testing, and verification were performed by the developer.