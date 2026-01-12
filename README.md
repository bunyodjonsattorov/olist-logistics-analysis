# Olist Logistics Analysis

A data analysis project exploring the Olist e-commerce dataset from Brazil, focusing on logistics and seller performance metrics.

## 📊 Project Overview

This project analyzes order data from the Brazilian e-commerce platform Olist to uncover insights about:
- Seller performance and revenue distribution
- Pricing patterns and trends
- Logistics and delivery metrics

## 🗂️ Project Structure

```
olist-logistics-analysis/
├── data/                          # Dataset files (not tracked in git)
│   ├── olist_orders_dataset.csv
│   └── olist_order_items_dataset.csv
├── src/                           # Python scripts
│   ├── 01_exploration.py          # Initial data exploration
│   └── 02_logistics.py            # Logistics and order status analysis
├── .gitignore                     # Git ignore rules
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/bunyodjonsattorov/olist-logistics-analysis.git
cd olist-logistics-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset:
   - The Olist dataset is available from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
   - Place the CSV files in the `data/` directory

### Usage

Run the analysis scripts:
```bash
# Initial data exploration
python3 src/01_exploration.py

# Logistics and order status analysis
python3 src/02_logistics.py
```

## 📈 Analysis Highlights

### Data Exploration (`01_exploration.py`)
- Dataset overview: 112,650 orders across 7 columns
- High-value items: 40,313 items priced over R$100 (35.79%)
- Top 5 sellers by total revenue identified
- Revenue leaders earn R$187K - R$229K

### Logistics Analysis (`02_logistics.py`)
- Total platform revenue: **R$13.59M**
- Order status breakdown:
  - Delivered orders: 97% of revenue (R$13.22M)
  - Shipped orders: R$150K
  - Canceled orders: R$95K
- Key insight: 97% revenue concentration in delivered status

## 📦 Dataset

**Source:** Olist Brazilian E-commerce Dataset  
**Platform:** Kaggle  
**Description:** Real commercial data from orders made at Olist Store in Brazil (2016-2018)

### Key Fields
- `order_id`: Unique order identifier
- `order_item_id`: Sequential number identifying items in the same order
- `product_id`: Unique product identifier
- `seller_id`: Unique seller identifier
- `price`: Item price
- `freight_value`: Freight value

## 🛠️ Technologies

- **Python 3.9+**
- **pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing (if needed for advanced analysis)

## 📝 Future Work

- [ ] Add data visualization scripts
- [ ] Perform time-series analysis on order trends
- [ ] Analyze seller geographical distribution
- [ ] Create interactive dashboards
- [ ] Add statistical testing

## 👤 Author

**Bunyodjonsattorov**

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Olist for providing the dataset
- Kaggle for hosting the data
