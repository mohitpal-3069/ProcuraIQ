# Product Brief — ProcuraIQ

## Problem statement
Procurement teams may need to review purchase orders across suppliers and identify which orders require follow-up. When order status, expected delivery, and supplier history are spread across records, prioritizing follow-up can take extra manual effort.

## Target users
**Primary:** Procurement executive who checks daily purchase-order status.
**Secondary:** Procurement manager who compares supplier reliability and allocates follow-up effort.

## User need
"I need to quickly identify open or late orders and understand supplier performance so I can prioritize follow-up."

## Product hypothesis
If procurement users can see order status, delivery performance, and supplier comparisons in one view, they may identify follow-up actions faster than by scanning raw rows.

This is a hypothesis to validate, not a proven result.

## MVP goals
- Make open and potentially delayed orders easy to identify.
- Provide a consistent view of supplier order value and delivery performance.
- Let users filter the order list by supplier and status.

## Non-goals for this MVP
- Placing or approving orders
- Supplier onboarding or payments
- Live ERP integrations
- Automated alerts
- Predictive ML or production deployment

## Key assumptions
- Order records contain expected delivery dates and status.
- Users need both order-level details and supplier-level summaries.
- A spreadsheet/CSV export is sufficient for a prototype.

## Risks and edge cases
- Missing actual delivery dates are normal for orders not yet delivered.
- Duplicate order IDs could distort totals.
- Small or synthetic samples can make supplier performance look more certain than it is.
- "Late" should be based on actual delivery date for delivered orders; open orders past the expected date should be labeled overdue only if the current date is available and defined.

## Validation plan
1. Interview 3–5 procurement users about how they currently track orders.
2. Ask them to complete: "Find open orders from a selected supplier."
3. Ask them to identify the supplier with the highest on-time rate.
4. Record completion rate, time on task, and confusing labels.
5. Prioritize changes based on observed friction.
