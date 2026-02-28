# Step 5: Correlation matrix
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 6: Scatter plot (example: MarketingSpend vs Revenue)
if 'MarketingSpend' in df.columns and 'Revenue' in df.columns:
    sns.scatterplot(x='MarketingSpend', y='Revenue', data=df)
    plt.title("Marketing Spend vs Revenue")
    plt.show()
