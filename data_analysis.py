#!/usr/bin/env python3
"""
Molecular Descriptor Data Description
Provides statistical summaries and visualizations of molecular descriptor data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class MolecularDataAnalyzer:
    def __init__(self, results_dir="./results"):
        self.results_dir = results_dir
        self.plots_dir = f"{results_dir}/analysis_plots"
        self.data = {}
        self.combined_data = None
        
        # Create plots directory
        import os
        os.makedirs(self.plots_dir, exist_ok=True)
        
    def load_data(self):
        """Load all descriptor CSV files"""
        print("Loading molecular descriptor data...")
        
        files = {
            'Neg_test': 'Neg_test_descriptors.csv',
            'Neg_train': 'Neg_train_descriptors.csv', 
            'Pos_test': 'Pos_test_descriptors.csv',
            'Pos_train': 'Pos_train_descriptors.csv'
        }
        
        for name, filename in files.items():
            filepath = f"{self.results_dir}/{filename}"
            try:
                df = pd.read_csv(filepath)
                df['Dataset'] = name
                df['Class'] = 'Negative' if 'Neg' in name else 'Positive'
                df['Split'] = 'Test' if 'test' in name else 'Train'
                self.data[name] = df
                print(f"  ✓ Loaded {name}: {len(df)} molecules, {df.shape[1]-3} descriptors")
            except FileNotFoundError:
                print(f"  ✗ File not found: {filepath}")
        
        # Combine all data
        self.combined_data = pd.concat(list(self.data.values()), ignore_index=True)
        print(f"\nTotal dataset: {len(self.combined_data)} molecules")
        print(f"Descriptors: {self.combined_data.shape[1]-3}")
        
        return self.combined_data
    
    def basic_statistics(self):
        """Generate basic statistical summary"""
        print("\n" + "="*60)
        print("DESCRIPTIVE STATISTICS")
        print("="*60)
        
        # Dataset composition
        print("\nDataset Composition:")
        composition = self.combined_data.groupby(['Class', 'Split']).size().unstack(fill_value=0)
        print(composition)
        
        # Descriptor statistics
        descriptor_cols = [col for col in self.combined_data.columns if col not in ['Name', 'Dataset', 'Class', 'Split']]
        print(f"\nDescriptor Statistics (showing first 10):")
        desc_stats = self.combined_data[descriptor_cols[:10]].describe()
        print(desc_stats.round(3))
        
        # Missing values
        missing = self.combined_data[descriptor_cols].isnull().sum()
        missing_pct = (missing / len(self.combined_data)) * 100
        print(f"\nMissing Values:")
        print(f"Descriptors with missing values: {(missing > 0).sum()}")
        print(f"Max missing %: {missing_pct.max():.2f}%")
        
        # Class-specific statistics
        print(f"\nClass-specific Statistics:")
        for class_name in ['Positive', 'Negative']:
            class_data = self.combined_data[self.combined_data['Class'] == class_name]
            print(f"\n{class_name} Allergens ({len(class_data)} molecules):")
            print(f"  Mean molecular weight: {class_data['MW'].mean():.2f}")
            print(f"  Mean LogP: {class_data['ALogP'].mean():.2f}")
            print(f"  Mean atom count: {class_data['nAtom'].mean():.2f}")
            print(f"  Mean ring count: {class_data['nRing'].mean():.2f}")
        
        return composition, desc_stats
    
    def plot_dataset_distribution(self):
        """Plot dataset composition and class distribution"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Dataset composition
        composition = self.combined_data.groupby(['Class', 'Split']).size().unstack(fill_value=0)
        composition.plot(kind='bar', ax=axes[0], color=['skyblue', 'lightcoral'])
        axes[0].set_title('Dataset Composition by Class and Split')
        axes[0].set_xlabel('Class')
        axes[0].set_ylabel('Number of Molecules')
        axes[0].legend(title='Split')
        axes[0].tick_params(axis='x', rotation=0)
        
        # Class distribution pie chart
        class_counts = self.combined_data['Class'].value_counts()
        axes[1].pie(class_counts.values, labels=class_counts.index, autopct='%1.1f%%', 
                   colors=['lightcoral', 'skyblue'])
        axes[1].set_title('Class Distribution')
        
        plt.tight_layout()
        plt.savefig(f'{self.plots_dir}/dataset_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_descriptor_distributions(self, n_descriptors=12):
        """Plot distributions of key molecular descriptors"""
        descriptor_cols = [col for col in self.combined_data.columns if col not in ['Name', 'Dataset', 'Class', 'Split']]
        
        # Select key descriptors for visualization
        key_descriptors = ['MW', 'ALogP', 'nAtom', 'nBonds', 'nHBAcc', 'nHBDon', 
                          'TopoPSA', 'nRotB', 'nRing', 'LipinskiFailures', 'XLogP', 'Zagreb']
        
        available_descriptors = [desc for desc in key_descriptors if desc in descriptor_cols]
        if len(available_descriptors) < n_descriptors:
            available_descriptors.extend([col for col in descriptor_cols if col not in available_descriptors][:n_descriptors-len(available_descriptors)])
        
        n_cols = 4
        n_rows = (len(available_descriptors) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 5*n_rows))
        axes = axes.flatten() if n_rows > 1 else [axes] if n_rows == 1 else axes
        
        for i, desc in enumerate(available_descriptors[:n_descriptors]):
            if i < len(axes):
                for class_name in ['Positive', 'Negative']:
                    data = self.combined_data[self.combined_data['Class'] == class_name][desc]
                    axes[i].hist(data, alpha=0.7, label=class_name, bins=30)
                
                axes[i].set_title(f'{desc} Distribution')
                axes[i].set_xlabel(desc)
                axes[i].set_ylabel('Frequency')
                axes[i].legend()
                axes[i].grid(True, alpha=0.3)
        
        # Hide unused subplots
        for i in range(len(available_descriptors), len(axes)):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        plt.savefig(f'{self.plots_dir}/descriptor_distributions.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def correlation_analysis(self):
        """Analyze correlations between descriptors"""
        descriptor_cols = [col for col in self.combined_data.columns if col not in ['Name', 'Dataset', 'Class', 'Split']]
        
        # Calculate correlation matrix
        corr_matrix = self.combined_data[descriptor_cols].corr()
        
        # Plot correlation heatmap
        plt.figure(figsize=(15, 12))
        
        # Select a subset of descriptors for visualization (too many to show all)
        subset_descriptors = descriptor_cols[:50]  # First 50 descriptors
        corr_subset = corr_matrix.loc[subset_descriptors, subset_descriptors]
        
        mask = np.triu(np.ones_like(corr_subset, dtype=bool))
        sns.heatmap(corr_subset, mask=mask, annot=False, cmap='coolwarm', center=0,
                   square=True, cbar_kws={"shrink": .8})
        plt.title('Descriptor Correlation Matrix (First 50 Descriptors)')
        plt.tight_layout()
        plt.savefig(f'{self.plots_dir}/descriptor_correlations.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Find highly correlated pairs
        high_corr_pairs = []
        for i in range(len(corr_subset.columns)):
            for j in range(i+1, len(corr_subset.columns)):
                corr_val = corr_subset.iloc[i, j]
                if abs(corr_val) > 0.9:  # High correlation threshold
                    high_corr_pairs.append((corr_subset.columns[i], corr_subset.columns[j], corr_val))
        
        print(f"\nHighly Correlated Descriptor Pairs (|r| > 0.9): {len(high_corr_pairs)}")
        for pair in high_corr_pairs[:10]:  # Show first 10
            print(f"  {pair[0]} - {pair[1]}: {pair[2]:.3f}")
        
        return corr_matrix
    
    def dimensionality_reduction(self):
        """Apply PCA and t-SNE for dimensionality reduction visualization"""
        descriptor_cols = [col for col in self.combined_data.columns if col not in ['Name', 'Dataset', 'Class', 'Split']]
        
        # Prepare data
        X = self.combined_data[descriptor_cols].fillna(0)  # Fill missing values
        
        # Handle infinite values
        X = X.replace([np.inf, -np.inf], np.nan)
        X = X.fillna(0)
        
        y = self.combined_data['Class']
        
        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # PCA
        print("\nApplying PCA...")
        pca = PCA(n_components=0.95)  # Keep 95% of variance
        X_pca = pca.fit_transform(X_scaled)
        print(f"PCA: {X_scaled.shape[1]} → {X_pca.shape[1]} components (95% variance)")
        
        # t-SNE
        print("Applying t-SNE...")
        tsne = TSNE(n_components=2, random_state=42, perplexity=30)
        X_tsne = tsne.fit_transform(X_pca[:, :50])  # Use first 50 PCA components
        
        # Plot results
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # PCA plot
        for class_name in ['Positive', 'Negative']:
            mask = y == class_name
            axes[0].scatter(X_pca[mask, 0], X_pca[mask, 1], alpha=0.7, label=class_name)
        axes[0].set_title('PCA Visualization')
        axes[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
        axes[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # t-SNE plot
        for class_name in ['Positive', 'Negative']:
            mask = y == class_name
            axes[1].scatter(X_tsne[mask, 0], X_tsne[mask, 1], alpha=0.7, label=class_name)
        axes[1].set_title('t-SNE Visualization')
        axes[1].set_xlabel('t-SNE 1')
        axes[1].set_ylabel('t-SNE 2')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.plots_dir}/dimensionality_reduction.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        return X_pca, X_tsne, pca
    
    def generate_report(self):
        """Generate comprehensive data description report"""
        print("\n" + "="*80)
        print("MOLECULAR DESCRIPTOR DATA DESCRIPTION")
        print("="*80)
        
        # Load data
        self.load_data()
        
        # Basic statistics
        composition, desc_stats = self.basic_statistics()
        
        # Visualizations
        print("\nGenerating visualizations...")
        self.plot_dataset_distribution()
        self.plot_descriptor_distributions()
        self.correlation_analysis()
        
        # Dimensionality reduction
        print("\nPerforming dimensionality reduction...")
        X_pca, X_tsne, pca = self.dimensionality_reduction()
        
        print("\n" + "="*80)
        print("DATA DESCRIPTION COMPLETE!")
        print("="*80)
        print(f"Generated files in {self.plots_dir}/:")
        print("  - dataset_distribution.png")
        print("  - descriptor_distributions.png") 
        print("  - descriptor_correlations.png")
        print("  - dimensionality_reduction.png")
        print(f"\nAll plots saved to: {self.plots_dir}/")
        print("Use these visualizations for your research paper!")

def main():
    """Main data analysis function"""
    analyzer = MolecularDataAnalyzer()
    analyzer.generate_report()

if __name__ == "__main__":
    main()
