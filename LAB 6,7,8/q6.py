import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv')

if 'sentiment' not in df.columns or 'rating' not in df.columns:
    print("Error: The CSV file must contain 'sentiment' and 'rating' columns.")
else:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)
    df = df[df['rating'].between(1, 5)]

    sentiment_order = ['Negative', 'Neutral', 'Positive']
    plot_data = [df[df['sentiment'] == s]['rating'] for s in sentiment_order]
    box_colors = ['#dc3545', '#ffc107', '#28a745']

    fig, ax = plt.subplots(figsize=(10, 6))
    
    box_plot = ax.boxplot(
        plot_data, 
        labels=sentiment_order, 
        patch_artist=True,
        medianprops={'color': 'black', 'linewidth': 2},
        whiskerprops={'color': 'gray'},
        capprops={'color': 'gray'},
        flierprops={'marker': 'o', 'markerfacecolor': 'gray', 'alpha': 0.5}
    )
    
    for patch, color in zip(box_plot['boxes'], box_colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')
        patch.set_linewidth(1.5)

    ax.set_title('Distribution of Numeric Ratings by Review Sentiment', fontsize=16, fontweight='bold')
    ax.set_xlabel('Review Sentiment', fontsize=12)
    ax.set_ylabel('Numeric Rating Value', fontsize=12)

    ax.set_yticks(range(1, 6))
    ax.set_ylim(0.5, 5.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

    print("Plot displayed successfully.")
    print("\nStatistical Summary (Median Rating per Sentiment):")
    print(df.groupby('sentiment')['rating'].median().loc[sentiment_order].to_string())