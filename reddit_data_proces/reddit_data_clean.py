import pandas as pd

def data_merge():
    file_rising_post = 'reddit_rising_posts_and_best_comments_with_author.csv'
    file_top_post = 'reddit_top_posts_and_best_comments_with_author.csv'
    file_hot_post = 'reddit_hot_posts_and_best_comments_with_author.csv'

    # Read the CSV files
    df_rising = pd.read_csv(file_rising_post)
    df_top = pd.read_csv(file_top_post)
    df_hot = pd.read_csv(file_hot_post)

    print(df_rising.shape)
    print(df_top.shape)
    print(df_hot.shape)

    print("Headers of df_hot:", df_hot.columns.tolist())

    unique_titles_hot = df_hot['title'].unique().tolist()

    print('Unique post (rising) ', len(df_rising['title'].unique().tolist()))
    print('Unique post (hot) ', len(df_hot['title'].unique().tolist()))
    print('Unique post (top) ', len(df_top['title'].unique().tolist()))

    # Count the number of unique title matches with df_best
    match_count_top_hot = df_top['title'].isin(unique_titles_hot).sum()

    # Print the count of unique title matches
    print("Number of unique title matches in df_top:", match_count_top_hot)

    # Create a new dataframe with the matched titles
    matched_df_top_hot = df_top[df_top['title'].isin(unique_titles_hot)]

    print('Common post (top-hot) ', len(matched_df_top_hot['title'].unique().tolist()))

    # Save the new dataframe to a CSV file
    matched_df_top_hot.to_csv('matched_top_hot_titles.csv', index=False)

    print("CSV file with matched titles created successfully.")

    print('Unique Author (Top) ', len(df_top['post_author'].unique().tolist()))

    # Find the top 10 duplicate post_authors
    top_duplicate_authors = df_top['post_author'].value_counts().head(11)/3
    print("Top 10 duplicate post_authors (Top):")
    print(top_duplicate_authors)

    print('Unique Author (Hot) ', len(df_hot['post_author'].unique().tolist()))

    # Find the top 10 duplicate post_authors
    top_duplicate_authors = df_hot['post_author'].value_counts().head(11)/3
    print("Top 10 duplicate post_authors (Hot):")
    print(top_duplicate_authors)

    print('Unique Author (Rising) ', len(df_rising['post_author'].unique().tolist()))

    # Find the top 10 duplicate post_authors
    top_duplicate_authors = df_rising['post_author'].value_counts().head(11)/3
    print("Top 10 duplicate post_authors (Rising):")
    print(top_duplicate_authors)

if __name__=="__main__":
    data_merge()