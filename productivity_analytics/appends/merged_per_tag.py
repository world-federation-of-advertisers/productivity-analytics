import pandas as pd


def merged_per_tag(pr_df: pd.DataFrame) -> pd.DataFrame:

    # Convert timestamp into datetime
    pr_df['created_at'] = pd.to_datetime(pr_df['created_at'])
    
    # Create a temp dataframe for merged pr per tag
    merged_per_tag_data = pr_df[pr_df['created_at'] >= '2024-08-01']
    merged_per_tag_data = merged_per_tag_data[~pd.isna(pr_df['merged_at'])]
    
    # Create a temp column for cleaned tags
    tags_series = merged_per_tag_data['title'].str.split(':')
    tags_series = tags_series.str[0].str.lstrip().str.rstrip('!')
    tags_series = tags_series.str.split('[').str[0]
    tags_series = tags_series.str.split('(').str[0]
    
    # Add the cleaned tag data into a new column in the temp dataframe
    merged_per_tag_data['tag'] = tags_series
    
    # Define the logic for classifying labels into sustaining vs. transformative
    def _classify_commit(tag):
    
        if tag in ['fix', 'docs', 'chore', 'test', 'build', 'ci', 'style']:
            return 'sustaining'
        
        elif tag in ['feat', 'perf', 'refactor']:
            return 'transformative'
            
        else:
            print(tag)
            return 'unknown'
    
    # Create a new column using the tag classifier
    merged_per_tag_data['type_of_work'] = merged_per_tag_data['tag'].apply(_classify_commit)

    return merged_per_tag_data
