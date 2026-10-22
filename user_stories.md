# User Stories and Acceptance Criteria

## Story 1 — Filter orders
**As a** procurement executive, **I want** to filter orders by supplier and status, **so that** I can focus on the records relevant to my follow-up.

Acceptance criteria:
- Supplier filter includes all suppliers in the loaded dataset.
- Status filter supports all available statuses.
- The table updates when either filter changes.
- An empty result set displays a clear message.

## Story 2 — Identify late deliveries
**As a** procurement executive, **I want** to see which delivered orders arrived after their expected date, **so that** I can investigate delivery issues.

Acceptance criteria:
- Late delivery is calculated only when both expected and actual dates exist.
- A delivered order is late when actual delivery is after expected delivery.
- Orders without actual delivery dates are not incorrectly counted as delivered late.

## Story 3 — Compare suppliers
**As a** procurement manager, **I want** to compare supplier order value and on-time delivery rate, **so that** I can decide where to investigate performance.

Acceptance criteria:
- The comparison shows order count and total order value per supplier.
- On-time rate uses delivered orders with both expected and actual dates as the denominator.
- Suppliers with no eligible delivered orders show N/A rather than 0%.

## Story 4 — Review order details
**As a** procurement executive, **I want** to inspect order details in one table, **so that** I can follow up without opening multiple files.

Acceptance criteria:
- The table shows order ID, supplier, item, status, expected date, actual date, order value, and delivery result.
- Currency values are derived from quantity multiplied by unit price.
