import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer

# Ensure necessary nltk tokenizers are available
nltk.download('punkt')

class TransactionCategorizer:
    """ML-powered transaction categorizer with keyword-based and ML classification."""
    def __init__(self):
        # Define the categories with relevant keywords
        self.categories = {
                "Housing": ["rent", "mortgage", "property tax", "house", "apartment", "building", "lease"],
                "Food": ["grocery", "restaurant", "dining", "food", "supermarket", "cafe", "coffee"],
                "Transportation": ["uber", "bus", "train", "gas", "fuel", "taxi", "metro", "parking"],
                "Utilities": ["electricity", "water bill", "internet", "phone bill", "gas bill"],
                "Entertainment": ["netflix", "spotify", "movie", "concert", "game", "amusement", "club"],
                "Investment": ["stock", "dividend", "crypto", "bitcoin", "investment", "ETF", "mutual fund"],
                "Health & Wellness": ["hospital", "pharmacy", "doctor", "gym", "fitness", "medicine", "clinic"],
                "Income": ["salary", "paycheck", "bonus", "freelance", "commission", "wages"],
                "Insurance": ["insurance", "policy", "premium", "health insurance", "life insurance"],
                "Other": []  # Default category
        }
    
        # Machine Learning Model (TF-IDF + logistic Regression)
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

        # Word Embedding Model (for Semantic Matching)
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def categorize_keyword(self, description):
        """Categorize transaction based on predefined keyword matching."""
        description = description.lower()
        for category, keywords in self.categories.items():
            if any(keyword in description for keyword in keywords):
                return category
        return "other"
    
    def train_model(self, descriptions, labels):
        """Train the AI model using labeled transaction data."""
        X_train, X_test, y_train, y_test = train_test_split(descriptions, labels, test_size=0.2, random_state=42)
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        X_test_tfidf = self.vectorizer.transform(X_test)
        self.model.fit(X_train_tfidf, y_train)

    def categorize_ai(self, description):
        """Use the AI model to categorize transactions."""
        if not hasattr(self.model, "classes_"):
            return "other"  # Return default category if model isn't trained yet

        description_tfidf = self.vectorizer.transform([description])
        return self.model.predict(description_tfidf)[0]
    
    def categorize_semantic(self, description):
        """Use semantic similarity to categorize transactions."""
        # Get the embedding for the description
        description_embedding = self.embedding_model.encode([description])[0].flatten()  # Ensure 1D vector
        
        best_category = "other"
        best_score = -1  # Track highest similarity score
        
        # Iterate over each category and its keywords
        for category, keywords in self.categories.items():
            # Get the embeddings for each keyword in the category
            keyword_embeddings = self.embedding_model.encode(keywords)
            
            # Handle cases where there is only one keyword
            if len(keyword_embeddings.shape) == 1:
                # If the embedding is already 1D (single keyword), use it directly
                category_embedding = keyword_embeddings.flatten()
            else:
                # Otherwise, calculate the mean across all keyword embeddings
                category_embedding = keyword_embeddings.mean(axis=0).flatten()  # Ensure 1D vector
            
            # Debugging: Print shapes to verify alignment
            print(f"Description embedding shape: {description_embedding.shape}")
            print(f"Category embedding shape: {category_embedding.shape}")
            
            # Ensure both embeddings are 1D vectors
            if description_embedding.ndim != 1 or category_embedding.ndim != 1:
                raise ValueError("Embeddings must be 1D vectors.")
            
            # Align dimensions by truncating the larger embedding
            min_dim = min(description_embedding.shape[0], category_embedding.shape[0])
            description_embedding_aligned = description_embedding[:min_dim]
            category_embedding_aligned = category_embedding[:min_dim]
            
            # Debugging: Print aligned shapes
            print(f"Aligned description embedding shape: {description_embedding_aligned.shape}")
            print(f"Aligned category embedding shape: {category_embedding_aligned.shape}")
            
            # Calculate cosine similarity
            similarity = np.dot(description_embedding_aligned, category_embedding_aligned) / (
                np.linalg.norm(description_embedding_aligned) * np.linalg.norm(category_embedding_aligned)
            )
            
            # Ensure similarity is a scalar
            similarity = float(similarity)  # Convert to scalar if necessary
            
            # Update best category if this similarity is higher
            if similarity > best_score:
                best_score = similarity
                best_category = category
        
        # Set a threshold for similarity (you can adjust this threshold)
        return best_category if best_score > 0.5 else "other"


    def categorize_transactions(self, df):
        """Apply categorization to a DataFrame with transactions."""
        if "description" not in df.columns:
            df["description"] = np.random.choice(
                ["Grocery store", "Uber ride", "Netflix subscription", "Salary deposit", "Doctor visit"],
                len(df)
            )

        df["category"] = df["description"].apply(self.categorize_keyword)

        # Train model on non-"Other" transactions
        train_data = df[df["category"] != "other"]
        if not train_data.empty:
            self.train_model(train_data["description"], train_data["category"])

            # Apply AI categorization to "Other" transactions
            df.loc[df["category"] == "other", "category"] = df["description"].apply(self.categorize_ai)

        # Apply Semantic Matching to remaining "Other" transactions
        df.loc[df["category"] == "other", "category"] = df["description"].apply(self.categorize_semantic)
