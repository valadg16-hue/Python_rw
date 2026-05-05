import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
 

 
class RetailAnalyzer:
 
    def __init__(self):
        self.df = None
 
 
   
    def load_data(self):
        path = input("Enter CSV file name (e.g. retail_sales.csv): ").strip()
 
        # validate file format
        if path.endswith('.csv'):
            self.df = pd.read_csv(path)
        elif path.endswith(('.xlsx', '.xls')):
            self.df = pd.read_excel(path)
        else:
            print("Unsupported format. Use CSV or Excel.")
            return
 
        # convert Date column
        self.df['Date'] = pd.to_datetime(self.df['Date'])
 
        print("Dataset loaded successfully!")
        print(self.df.shape)
        print(self.df.head())
 
 
   
    def explore_data(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        while True:
            print("\n== Explore Data ==")
            print("1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Basic info")
            print("6. Descriptive statistics")
            print("7. Selected columns statistics")
            print("8. Back")
            choice = input("Choice: ").strip()
 
            if choice == '1':
                print(self.df.head())
 
            elif choice == '2':
                print(self.df.tail())
 
            elif choice == '3':
                print(self.df.columns)
 
            elif choice == '4':
                print(self.df.dtypes)
 
            elif choice == '5':
                self.df.info()
 
            elif choice == '6':
                print(self.df.describe())
 
            elif choice == '7':
                # only numeric columns
                num_cols = self.df.select_dtypes(include=np.number).columns.tolist()
                print(self.df[num_cols].describe())
 
            elif choice == '8':
                break
 
            else:
                print("Invalid choice.")
 
 
  
    def handle_missing_data(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        while True:
            print("\n== Handle Missing Data ==")
            print("1. Check missing values")
            print("2. Drop missing rows")
            print("3. Fill with mean")
            print("4. Fill with custom value")
            print("5. Back")
            choice = input("Choice: ").strip()
 
            if choice == '1':
                print(pd.isnull(self.df).sum())
 
            elif choice == '2':
                before = len(self.df)
                self.df.dropna(inplace=True)
                self.df.reset_index(drop=True, inplace=True)
                print(f"Dropped {before - len(self.df)} rows. Remaining: {len(self.df)}")
 
            elif choice == '3':
                num_cols = self.df.select_dtypes(include=np.number).columns
                self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
                print("Filled missing values with column mean.")
 
            elif choice == '4':
                val = input("Enter fill value: ").strip()
                try:
                    val = float(val)
                except ValueError:
                    pass
                self.df.fillna(val, inplace=True)
                print(f"Filled missing values with '{val}'.")
 
            elif choice == '5':
                break
 
            else:
                print("Invalid choice.")
 
 
    
    def dataframe_operations(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        while True:
            print("\n== DataFrame Operations ==")
            print("1. Math operations on Sales (NumPy)")
            print("2. Math operations on Total Sales (NumPy)")
            print("3. Combine DataFrames demo (concat)")
            print("4. Split data by Category")
            print("5. Back")
            choice = input("Choice: ").strip()
 
            if choice == '1':
                
                arr = self.df['Quantity Sold'].to_numpy()
                print("\n== NumPy on Quantity Sold ==")
                print("Sum     :", arr.sum())
                print("Mean    :", arr.mean())
                print("Std Dev :", arr.std())
                print("Min     :", arr.min())
                print("Max     :", arr.max())
 
                
                avg = arr.mean()
                above = []
                for i in range(len(arr)):
                    if arr[i] > avg:
                        above.append(arr[i])
                print(f"Items above average quantity ({avg:.1f}): {len(above)}")
 
            elif choice == '2':
                arr2 = self.df['Total Sales'].to_numpy()
                print("\n== NumPy on Total Sales ==")
                print("Sum     :", arr2.sum())
                print("Mean    :", arr2.mean())
                print("Std Dev :", arr2.std())
                print("Min     :", arr2.min())
                print("Max     :", arr2.max())
 
                
                growth = np.diff(arr2)
                print("Sales growth (first 5):", growth[:5])
 
            elif choice == '3':
                combined = pd.concat([self.df, self.df], ignore_index=True)
                print(f"Original rows: {len(self.df)}  |  Combined rows: {len(combined)}")
 
            elif choice == '4':
                for cat, grp in self.df.groupby('Category'):
                    print(f"\nCategory: {cat}  ({len(grp)} rows)")
                    print(grp[['Product', 'Quantity Sold', 'Total Sales']].head(3).to_string(index=False))
 
            elif choice == '5':
                break
 
            else:
                print("Invalid choice.")
 
 
   
    def calculate_metrics(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        arr = np.array(self.df['Total Sales'])
 
        total_sales   = np.sum(arr)
        average_sales = np.mean(arr)
        max_sale      = np.max(arr)
        min_sale      = np.min(arr)
 
        product_qty  = self.df.groupby('Product')['Quantity Sold'].sum()
        most_popular = product_qty.idxmax()
 
        cat_revenue = self.df.groupby(['Category'], as_index=False)['Total Sales'].sum().sort_values(by='Total Sales', ascending=False)
 
        print("\n== Sales Metrics ==")
        print(f"Total Sales    : Rs. {total_sales:.2f}")
        print(f"Average Sales  : Rs. {average_sales:.2f}")
        print(f"Highest Sale   : Rs. {max_sale:.2f}")
        print(f"Lowest Sale    : Rs. {min_sale:.2f}")
        print(f"Most Popular   : {most_popular} ({product_qty[most_popular]} units)")
        print("\nRevenue by Category:")
        print(cat_revenue)
 
 
 
    def filter_data(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        while True:
            print("\n== Filter Data ==")
            print("1. Filter by Category")
            print("2. Filter by Product")
            print("3. Filter by Date From")
            print("4. Filter by Date To")
            print("5. Back")
            choice = input("Choice: ").strip()
 
            if choice == '1':
                cats = self.df['Category'].unique()
                print("Available categories:", cats)
                val = input("Enter category: ").strip()
                filtered = self.df[self.df['Category'].str.lower() == val.lower()]
                print(f"\nFiltered ({len(filtered)} rows):")
                print(filtered.to_string(index=False))
 
            elif choice == '2':
                prods = self.df['Product'].unique()
                print("Available products:", prods)
                val = input("Enter product: ").strip()
                filtered = self.df[self.df['Product'].str.lower() == val.lower()]
                print(f"\nFiltered ({len(filtered)} rows):")
                print(filtered.to_string(index=False))
 
            elif choice == '3':
                val = input("Enter date (YYYY-MM-DD): ").strip()
                filtered = self.df[self.df['Date'] >= pd.to_datetime(val)]
                print(f"\nFiltered from {val} ({len(filtered)} rows):")
                print(filtered.to_string(index=False))
 
            elif choice == '4':
                val = input("Enter date (YYYY-MM-DD): ").strip()
                filtered = self.df[self.df['Date'] <= pd.to_datetime(val)]
                print(f"\nFiltered up to {val} ({len(filtered)} rows):")
                print(filtered.to_string(index=False))
 
            elif choice == '5':
                break
 
            else:
                print("Invalid choice.")
 
 
  
    def display_summary(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        print("\n== Dataset Summary ==")
        print(self.df.describe())
 
        print("\n== Total Sales by Category ==")
        cat_sales = self.df.groupby(['Category'], as_index=False)['Total Sales'].sum().sort_values(by='Total Sales', ascending=False)
        print(cat_sales)
 
        print("\n== Total Quantity Sold by Product ==")
        prod_qty = self.df.groupby(['Product'], as_index=False)['Quantity Sold'].sum().sort_values(by='Quantity Sold', ascending=False)
        print(prod_qty)
 
        print("\n== Pivot Table - Total Sales by Category & Product ==")
        pivot = self.df.pivot_table(values='Total Sales', index='Category', columns='Product', aggfunc='sum', fill_value=0)
        print(pivot)
 
 

    def visualize_data(self):
        if self.df is None:
            print("Load dataset first!")
            return
 
        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Chart - Total Sales by Category")
            print("2. Bar Chart - Quantity Sold by Product")
            print("3. Line Chart - Sales Trend Over Time")
            print("4. Count Plot - Orders by Category")
            print("5. Histogram - Distribution of Total Sales")
            print("6. Heatmap - Category vs Product")
            print("7. Top Products by Total Sales")
            print("8. Back")
            choice = input("Choice: ").strip()
 
            if choice == '1':
                sales_cat = self.df.groupby(['Category'], as_index=False)['Total Sales'].sum().sort_values(by='Total Sales', ascending=False)
                sns.set(rc={'figure.figsize': (10, 5)})
                sns.barplot(x='Category', y='Total Sales', data=sales_cat)
                plt.title('Total Sales by Category')
                plt.xlabel('Category')
                plt.ylabel('Total Sales')
                plt.tight_layout()
                plt.savefig('bar_sales_category.png')
                plt.show()
                print("Saved as bar_sales_category.png")
 
            elif choice == '2':
                prod_qty = self.df.groupby(['Product'], as_index=False)['Quantity Sold'].sum().sort_values(by='Quantity Sold', ascending=False)
                sns.set(rc={'figure.figsize': (12, 5)})
                sns.barplot(x='Product', y='Quantity Sold', data=prod_qty)
                plt.title('Quantity Sold by Product')
                plt.xlabel('Product')
                plt.ylabel('Quantity Sold')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig('bar_qty_product.png')
                plt.show()
                print("Saved as bar_qty_product.png")
 
            elif choice == '3':
                sales_time = self.df.groupby('Date')['Total Sales'].sum().reset_index()
                sns.set(rc={'figure.figsize': (14, 5)})
                sns.lineplot(x='Date', y='Total Sales', data=sales_time, color='tomato', linewidth=2)
                plt.title('Sales Trend Over Time')
                plt.xlabel('Date')
                plt.ylabel('Total Sales')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig('line_sales_trend.png')
                plt.show()
                print("Saved as line_sales_trend.png")
 
            elif choice == '4':
                sns.set(rc={'figure.figsize': (10, 5)})
                ax = sns.countplot(x='Category', data=self.df)
                for bars in ax.containers:
                    ax.bar_label(bars)
                plt.title('Number of Orders by Category')
                plt.tight_layout()
                plt.savefig('count_orders_category.png')
                plt.show()
                print("Saved as count_orders_category.png")
 
            elif choice == '5':
                sns.set(rc={'figure.figsize': (8, 5)})
                self.df['Total Sales'].plot(kind='hist', bins=20, color='mediumpurple', edgecolor='black')
                plt.title('Distribution of Total Sales')
                plt.xlabel('Total Sales')
                plt.tight_layout()
                plt.savefig('histogram_totalsales.png')
                plt.show()
                print("Saved as histogram_totalsales.png")
 
            elif choice == '6':
                pivot = self.df.pivot_table(values='Total Sales', index='Category', columns='Product', aggfunc='sum', fill_value=0)
                sns.set(rc={'figure.figsize': (14, 6)})
                sns.heatmap(pivot, annot=True, fmt='g', cmap='YlOrRd')
                plt.title('Heatmap: Total Sales - Category vs Product')
                plt.tight_layout()
                plt.savefig('heatmap_sales.png')
                plt.show()
                print("Saved as heatmap_sales.png")
 
            elif choice == '7':
                fig1, ax1 = plt.subplots(figsize=(12, 6))
                self.df.groupby('Product')['Total Sales'].sum().nlargest(5).sort_values(ascending=False).plot(kind='bar', ax=ax1, color='steelblue', edgecolor='black')
                plt.title('Top 5 Products by Total Sales')
                plt.xlabel('Product')
                plt.ylabel('Total Sales')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig('top5_products.png')
                plt.show()
                print("Saved as top5_products.png")
 
            elif choice == '8':
                break
 
            else:
                print("Invalid choice.")
 
 
   
    def run(self):
        while True:
            print("\n" + "=" * 50)
            print("       Retail Sales Data Analyzer")
            print("=" * 50)
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Handle Missing Data")
            print("4. DataFrame Operations (NumPy & Pandas)")
            print("5. Calculate Metrics")
            print("6. Filter Data")
            print("7. Display Summary")
            print("8. Data Visualization")
            print("9. Exit")
            print("=" * 50)
            choice = input("Choice: ").strip()
 
            if choice == '1':
                self.load_data()
 
            elif choice == '2':
                self.explore_data()
 
            elif choice == '3':
                self.handle_missing_data()
 
            elif choice == '4':
                self.dataframe_operations()
 
            elif choice == '5':
                self.calculate_metrics()
 
            elif choice == '6':
                self.filter_data()
 
            elif choice == '7':
                self.display_summary()
 
            elif choice == '8':
                self.visualize_data()
 
            elif choice == '9':
                print("Goodbye!")
                quit()
 
            else:
                print("Invalid choice. Try again.")
 
 

 
analyzer = RetailAnalyzer()
analyzer.run()