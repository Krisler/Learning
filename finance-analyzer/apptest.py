import os
import json
import streamlit as st
import pandas as pd
import pdfplumber
import plotly.express as px
import requests
from matplotlib.ticker import FixedLocator
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
from transaction_categorizer import TransactionCategorizer

load_dotenv()


class FinancialAnalyzer:
    def __init__(self):
        self.api_url = "https://api.together.xyz/v1/completions"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        }
        self.categorizer = TransactionCategorizer()

    def process_statement(self, file):
        """Handle PDF/CSV input"""
        if file.name.endswith('.pdf'):
            with pdfplumber.open(file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            return self._parse_pdf_text(text)
        else:
            df = pd.read_csv(file)
            return self.clean_data(df)

    def _parse_pdf_text(self, text):
        """Extract transactions from PDF text using AI"""
        prompt = f"""Extract financial transactions from this text:
        {text}
        
        Return a valid JSON array with:
        [{{"date":"MM/DD/YYYY", "description":"...", "amount":float}}]"""

        response = requests.post(self.api_url, json={
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            "messages": [{"role": "system","content": prompt}],
            "max_tokens": 2000,
            "temperature": 0.1
        }, headers=self.headers)
    
        # Handle API errors
        if response.status_code != 200:
            st.error(f"API Request Failed: {response.status_code}")
            return pd.DataFrame()

        response_json = response.json()
        if 'choices' not in response_json:
            st.error("Error: Missing 'choices' key in API response.")
            return pd.DataFrame()

        try:
            extracted_text = response_json['choices'][0].get('text', '[]')
            transactions = json.loads(extracted_text)  # Convert JSON string to list
            return pd.DataFrame(transactions)
        except json.JSONDecodeError:
            st.error("Failed to parse AI response (Invalid JSON).")
            return pd.DataFrame()

    def clean_data(self, df):
        """Data cleaning pipeline"""
        df = df.copy()

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])
        df = df.assign(
        amount=pd.to_numeric(df['amount'], errors='coerce').fillna(0),  # Convert to numeric, fill NaN
        category=df.apply(self.categorize_transaction, axis=1),  # Apply categorization
        month=df['date'].dt.strftime("%Y-%m"))  # Extract year-month
                
        return df

    def categorize_transaction(self, row):
          """Hybrid categorization: Keyword-based, AI model, and semantic matching"""
          
          # Step 1: Try keyword-based categorization
          category = self.categorizer.categorize_keyword(row['description'])
          if category != "other":
              return category

          # Step 2: Try AI model categorization (if trained)
          category = self.categorizer.categorize_ai(row['description'])
          if category != "other":
              return category

          # Step 3: Use Semantic Matching as final fallback
          return self.categorizer.categorize_semantic(row['description'])

    def generate_recommendations(self, df):
        """Generate AI-powered financial recommendations"""
        prompt = f"""Analyze this spending data:
        {df.to_csv()}
        
        Apply these personal finance rules:
        1. 50/30/20 budget rule
        2. CFPB debt-to-income guidelines
        3. Fidelity retirement savings recommendations
        
        Output markdown with:
        - Top 3 recommended changes
        - Estimated savings
        - Supporting research sources"""

        response = requests.post(self.api_url, json={
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            "messages": [{"role": "system","content": prompt}],
            "max_tokens": 2000,
            "temperature": 0.1
        }, headers=self.headers)

        # Handle API errors
        if response.status_code != 200:
            return "AI failed to generate recommendations."

        response_json = response.json()
        if 'choices' not in response_json:
            return "AI failed to generate recommendations."

        try:
            return response_json['choices'][0].get('text', "No recommendations available.")
        except Exception as e:
            st.error(f"Error parsing AI recommendation response: {e}")
            return "AI failed to generate recommendations."


# Streamlit UI
def main():
    st.title("📊 Financial Health Analyzer")

    uploaded_file = st.file_uploader("Upload Statement", type=['pdf', 'csv'])
    analyzer = FinancialAnalyzer()

    if uploaded_file:
        df = analyzer.process_statement(uploaded_file)

        if df.empty:
            st.warning("No transactions found. Please upload a valid file.")
            return

        # Show raw data
        st.subheader("📋 Processed Transactions")
        st.dataframe(df)

        # Visualizations
        expenses = df[df["amount"] > 0].copy()
        expenses["amount"] = abs(expenses["amount"])  # Convert to positive for visualization
        category_spending = expenses.groupby("category")["amount"].sum().sort_values(ascending=False)
        monthly_spending = expenses.groupby("month")["amount"].sum()
        st.subheader("📊 Spending Breakdown")
        fig = px.pie(df, names='category', values='amount')
        st.plotly_chart(fig)

        # Pie Chart - Spending by Category
        st.subheader("💰 Spending by Category")
        fig, ax = plt.subplots()
        ax.pie(category_spending, labels=category_spending.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
        ax.axis("equal")
        st.pyplot(fig)

        # Bar Chart - Monthly Spending Trends
        st.subheader("📅 Monthly Spending Trend")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=monthly_spending.index, y=monthly_spending.values, hue = monthly_spending.index,palette="coolwarm",legend=False,ax=ax)
        ax.set_xticks(range(len(monthly_spending.index)))  # Set tick positions
        ax.set_xticklabels(monthly_spending.index, rotation=45) 
        ax.set_ylabel("Total Spending ($)")
        st.pyplot(fig)

        # Summary
        st.subheader("📌 Summary")
        st.write(f"**Total Spending:** ${expenses['amount'].sum():,.2f}")
        st.write(f"**Highest Spending Category:** {category_spending.idxmax()} (${category_spending.max():,.2f})")
        st.write(f"**Most Expensive Month:** {monthly_spending.idxmax()} (${monthly_spending.max():,.2f})")

        # Recommendations
        st.subheader("💡AI Recommendations")
        recommendations = analyzer.generate_recommendations(df)
        st.markdown(recommendations)


if __name__ == "__main__":
    main()
