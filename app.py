from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "procurement_orders.csv"

st.set_page_config(page_title="ProcuraIQ", page_icon="📦", layout="wide")
st.title("ProcuraIQ")
st.caption("Procurement Intelligence MVP · Demo data is synthetic")

df = pd.read_csv(DATA, parse_dates=["order_date", "expected_delivery", "actual_delivery"])
df["order_value"] = df["quantity"] * df["unit_price"]
df["delivery_result"] = "Open / not delivered"
delivered = df["status"].eq("Delivered") & df["actual_delivery"].notna() & df["expected_delivery"].notna()
df.loc[delivered & (df["actual_delivery"] <= df["expected_delivery"]), "delivery_result"] = "On time"
df.loc[delivered & (df["actual_delivery"] > df["expected_delivery"]), "delivery_result"] = "Late"

with st.sidebar:
    st.header("Filters")
    suppliers = ["All"] + sorted(df["supplier"].dropna().unique().tolist())
    statuses = ["All"] + sorted(df["status"].dropna().unique().tolist())
    supplier = st.selectbox("Supplier", suppliers)
    status = st.selectbox("Order status", statuses)

view = df.copy()
if supplier != "All":
    view = view[view["supplier"] == supplier]
if status != "All":
    view = view[view["status"] == status]

total_value = view["order_value"].sum()
open_count = int((~view["status"].eq("Delivered")).sum())
late_count = int((view["delivery_result"] == "Late").sum())
delivered_valid = view[view["delivery_result"].isin(["On time", "Late"])]
on_time_rate = (delivered_valid["delivery_result"].eq("On time").mean() * 100) if len(delivered_valid) else None

c1, c2, c3, c4 = st.columns(4)
c1.metric("Orders shown", f"{len(view)}")
c2.metric("Total order value", f"₹{total_value:,.0f}")
c3.metric("Open orders", f"{open_count}")
c4.metric("Delivered late", f"{late_count}")

if on_time_rate is not None:
    st.caption(f"On-time delivery rate among delivered orders with valid dates: {on_time_rate:.1f}%")
else:
    st.caption("On-time delivery rate: not available for this selection")

left, right = st.columns(2)
with left:
    st.subheader("Order value by supplier")
    st.bar_chart(view.groupby("supplier")["order_value"].sum().sort_values(ascending=False))
with right:
    st.subheader("Orders by status")
    st.bar_chart(view["status"].value_counts())

st.subheader("Supplier comparison")
supplier_summary = view.groupby("supplier").agg(
    order_count=("order_id", "count"),
    total_order_value=("order_value", "sum"),
    delivered_orders=("delivery_result", lambda s: int(s.isin(["On time", "Late"]).sum())),
    on_time_orders=("delivery_result", lambda s: int((s == "On time").sum())),
).reset_index()
supplier_summary["on_time_rate_pct"] = supplier_summary.apply(
    lambda r: round(100 * r["on_time_orders"] / r["delivered_orders"], 1)
    if r["delivered_orders"] else None, axis=1
)
st.dataframe(supplier_summary, use_container_width=True, hide_index=True)

st.subheader("Orders requiring attention")
attention = view[view["status"].ne("Delivered") | view["delivery_result"].eq("Late")].copy()
cols = ["order_id", "supplier", "item", "status", "expected_delivery", "actual_delivery", "order_value", "delivery_result"]
st.dataframe(attention[cols], use_container_width=True, hide_index=True)
st.download_button("Download filtered orders", view.to_csv(index=False).encode("utf-8"), "procuraIQ_filtered_orders.csv", "text/csv")

with st.expander("How metrics are calculated"):
    st.markdown("- **Order value:** quantity × unit price.")
    st.markdown("- **Late delivery:** delivered order with actual delivery date later than expected date.")
    st.markdown("- **On-time rate:** on-time delivered orders divided by delivered orders with both dates available.")
    st.info("This is a portfolio prototype using synthetic sample data. It is not connected to real procurement systems.")
