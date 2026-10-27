# ProcuraIQ — Procurement Intelligence Dashboard

A Streamlit-based procurement analytics MVP that helps teams monitor purchase orders, compare suppliers, and identify delivery risks through interactive charts and KPIs.

### 🚀 Live Demo

**[Open ProcuraIQ Dashboard](https://procuraiq.streamlit.app/)**

### 📊 Dashboard Preview

The live dashboard provides an overview of procurement performance, including order value by supplier, order status, open orders, and late deliveries.

### Key Metrics

- **Total Orders:** 20
- **Total Order Value:** ₹258,175
- **Open Orders:** 7
- **Late Deliveries:** 5
- **On-time Delivery Rate:** 61.5%

*Metrics shown are from the current synthetic demo dataset.*

### ✨ Features

- Filter purchase orders by supplier and order status.
- Track total order value and open orders.
- Compare suppliers by purchase order value.
- Monitor late deliveries and on-time delivery performance.
- Identify orders that may need follow-up.

### 🛠️ Tech Stack

- **Language:** Python
- **Dashboard:** Streamlit
- **Data Analysis:** Pandas
- **Visualization:** Interactive charts
- **Data Source:** Synthetic procurement order dataset

### 💻 Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mohitpal-3069/ProcuraIQ.git
   cd ProcuraIQ
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:

   ```bash
   streamlit run app/app.py
   ```

### 📁 Project Structure

```text
ProcuraIQ/
├── app/
│   └── app.py
├── data/
├── docs/
├── procurement_orders.csv
├── requirements.txt
└── README.md
```

### 🎯 Project Objective

ProcuraIQ demonstrates how procurement data can be transformed into actionable insights using KPIs, supplier comparisons, and delivery-risk monitoring.

---

**Developed by [Mohit Pal](https://github.com/mohitpal-3069)**
