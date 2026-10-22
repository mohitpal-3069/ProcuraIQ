# ProcuraIQ — Procurement Intelligence MVP

A small product-management portfolio project: a prototype for procurement teams to compare suppliers, monitor purchase orders, and spot delivery risks.

## Problem
Procurement users may need to compare supplier reliability and order status across multiple purchase orders. A simple, unified view can help them identify orders that need follow-up.

## MVP users
- Procurement executive: checks order status and delivery dates.
- Procurement manager: compares supplier performance and prioritizes follow-up.

## MVP scope
1. Filter orders by supplier and status.
2. View order value, open orders, and late-delivery indicators.
3. Compare suppliers by order value and on-time delivery rate.
4. Review a simple prioritized list of orders needing attention.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Repository contents
- `app/app.py`: interactive Streamlit prototype
- `data/procurement_orders.csv`: synthetic demonstration dataset
- `docs/product_brief.md`: problem, users, scope, and assumptions
- `docs/user_stories.md`: user stories and acceptance criteria
- `docs/prioritization.md`: MVP prioritization using MoSCoW
- `docs/metrics.md`: proposed success metrics and measurement plan

## Important limitations
The dataset is synthetic and small. Supplier metrics are illustrative, not evidence about real suppliers. This is a portfolio MVP, not a production procurement system. No user research or usability testing has been conducted yet; those are proposed next steps.

## Suggested resume entry (after running the app)
**ProcuraIQ — Procurement Intelligence MVP | Product Thinking, Python, Pandas, Streamlit**
- Defined an MVP for procurement users to compare supplier performance and identify orders requiring delivery follow-up; documented user stories, acceptance criteria, and feature priorities.
- Built an interactive prototype with supplier/status filters, order-value KPIs, and delivery-performance summaries using synthetic procurement data.
