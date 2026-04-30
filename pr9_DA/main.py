import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.current_plot = None

    def __del__(self):
        plt.close('all')

    
    def load_data(self, file_path):
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path, parse_dates=['Date'])
        elif file_path.endswith(('.xlsx', '.xls')):
            self.data = pd.read_excel(file_path, parse_dates=['Date'])
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")
        print("Dataset loaded successfully!")

    
    def explore_data(self):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                print(self.data.head())
            elif choice == '2':
                print(self.data.tail())
            elif choice == '3':
                print("Columns:", self.data.columns.tolist())
            elif choice == '4':
                print(self.data.dtypes)
            elif choice == '5':
                self.data.info()
            elif choice == '6':
                break
            else:
                print("Invalid choice.")

    
    def dataframe_operations(self):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Mathematical operations on Sales column")
            print("2. Combine DataFrames (concat same data as demo)")
            print("3. Split data by Region")
            print("4. Back")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                arr = self.data['Sales'].dropna().to_numpy()
                print(f"  Sum    : {arr.sum():.2f}")
                print(f"  Mean   : {arr.mean():.2f}")
                print(f"  Std Dev: {arr.std():.2f}")
                print(f"  Min    : {arr.min():.2f}")
                print(f"  Max    : {arr.max():.2f}")
            elif choice == '2':
                combined = pd.concat([self.data, self.data], ignore_index=True)
                print(f"Original rows: {len(self.data)}  |  Combined rows: {len(combined)}")
            elif choice == '3':
                for region, grp in self.data.groupby('Region'):
                    print(f"\nRegion: {region}  ({len(grp)} rows)")
                    print(grp[['Product', 'Sales', 'Revenue']].head(3).to_string(index=False))
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    
    def handle_missing_data(self):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Fill missing values with a specific value")
            print("5. Back")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print(missing)
            elif choice == '2':
                num_cols = self.data.select_dtypes(include=np.number).columns
                before = self.data.isnull().sum().sum()
                self.data[num_cols] = self.data[num_cols].fillna(self.data[num_cols].mean())
                after = self.data.isnull().sum().sum()
                print(f"Filled {before - after} missing values with column means.")
            elif choice == '3':
                before = len(self.data)
                self.data.dropna(inplace=True)
                self.data.reset_index(drop=True, inplace=True)
                print(f"Dropped {before - len(self.data)} rows. Remaining: {len(self.data)}")
            elif choice == '4':
                val = input("Enter fill value: ").strip()
                try:
                    val = float(val)
                except ValueError:
                    pass
                before = self.data.isnull().sum().sum()
                self.data.fillna(val, inplace=True)
                print(f"Filled {before} missing cell(s) with '{val}'.")
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

    
    def generate_descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        print("\n== Descriptive Statistics ==")
        print(self.data.describe())
        print("\nPivot – Total Revenue by Region & Product:")
        pivot = self.data.pivot_table(values='Revenue', index='Region',
                                      columns='Product', aggfunc='sum', fill_value=0)
        print(pivot)

    
    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Back")
            choice = input("Enter your choice: ").strip()
            if choice == '7':
                break
            numeric_cols = self.data.select_dtypes(include=np.number).columns.tolist()
            all_cols = self.data.columns.tolist()

            fig, ax = plt.subplots(figsize=(10, 6))

            if choice == '1':
                col = input(f"Enter column for bar plot {numeric_cols}: ").strip()
                if col not in numeric_cols:
                    print("Invalid column."); plt.close(); continue
                grp = self.data.groupby('Product')[col].sum()
                grp.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
                ax.set_title(f'Total {col} by Product')
                ax.set_xlabel('Product'); ax.set_ylabel(col)
                plt.xticks(rotation=45)

            elif choice == '2':
                col = input(f"Enter column for line plot {numeric_cols}: ").strip()
                if col not in numeric_cols:
                    print("Invalid column."); plt.close(); continue
                ts = self.data.groupby('Date')[col].sum().sort_index()
                ts.plot(ax=ax, color='tomato', linewidth=2)
                ax.set_title(f'{col} Over Time')
                ax.set_xlabel('Date'); ax.set_ylabel(col)

            elif choice == '3':
                x = input(f"Enter x-axis column name: ").strip()
                y = input(f"Enter y-axis column name: ").strip()
                if x not in all_cols or y not in all_cols:
                    print("Invalid column(s)."); plt.close(); continue
                print("Generating scatter plot...")
                ax.scatter(self.data[x], self.data[y], alpha=0.6, color='mediumseagreen')
                ax.set_xlabel(x); ax.set_ylabel(y)
                ax.set_title(f'Scatter: {x} vs {y}')
                print("Scatter plot displayed successfully!")

            elif choice == '4':
                grp = self.data.groupby('Product')['Revenue'].sum()
                grp.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=140)
                ax.set_ylabel('')
                ax.set_title('Revenue Share by Product')

            elif choice == '5':
                col = input(f"Enter column for histogram {numeric_cols}: ").strip()
                if col not in numeric_cols:
                    print("Invalid column."); plt.close(); continue
                self.data[col].dropna().plot(kind='hist', bins=20, ax=ax,
                                              color='mediumpurple', edgecolor='black')
                ax.set_title(f'Distribution of {col}')
                ax.set_xlabel(col)

            elif choice == '6':
                regions = self.data['Region'].unique()
                months = self.data['Date'].dt.month.unique()
                monthly = self.data.groupby([self.data['Date'].dt.month, 'Region'])['Revenue'].sum().unstack(fill_value=0)
                monthly.plot(ax=ax, kind='bar', stacked=True)
                ax.set_title('Monthly Revenue by Region (Stacked)')
                ax.set_xlabel('Month'); ax.set_ylabel('Revenue')
                plt.xticks(rotation=0)

            else:
                print("Invalid choice."); plt.close(); continue

            plt.tight_layout()
            self.current_plot = fig
            plt.show()
            print("Visualization ready. Use 'Save Visualization' to save it.")

    
    def save_visualization(self):
        if self.current_plot is None:
            print("No visualization to save. Please generate one first.")
            return
        fname = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip()
        self.current_plot.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"Visualization saved as {fname} successfully!")

    
    def run(self):
        while True:
            print("\n" + "=" * 10 + " Data Analysis & Visualization Program " + "=" * 10)
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("=" * 60)
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                path = input("Enter the path of the dataset (CSV file): ").strip()
                try:
                    self.load_data(path)
                except Exception as e:
                    print(f"Error loading dataset: {e}")
            elif choice == '2':
                self.explore_data()
            elif choice == '3':
                self.dataframe_operations()
            elif choice == '4':
                self.handle_missing_data()
            elif choice == '5':
                self.generate_descriptive_statistics()
            elif choice == '6':
                self.visualize_data()
            elif choice == '7':
                self.save_visualization()
            elif choice == '8':
                print("Exiting program. Goodbye!")
                quit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    analyzer = SalesDataAnalyzer()
    analyzer.run()