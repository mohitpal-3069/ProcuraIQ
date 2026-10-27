# MVP Prioritization — MoSCoW

## Must have
- Load the sample procurement dataset.
- Calculate order value.
- Filter by supplier and status.
- Display open orders and delivered-late orders.
- Compare suppliers using order count, order value, and on-time rate.

## Should have
- Download filtered results as CSV.
- Explain how each KPI is calculated.
- Handle missing actual delivery dates without marking them as late deliveries.

## Could have
- Upload a user-provided CSV.
- Add date-range filters.
- Add a lightweight feedback prompt.

## Won't have in this MVP
- Live ERP integration.
- User authentication and permissions.
- ML-based delay prediction.
- Automatic notifications.

## Trade-off
The MVP prioritizes clear, reliable visibility into existing records over complex integrations or prediction. This reduces build time and makes the core user need testable.
