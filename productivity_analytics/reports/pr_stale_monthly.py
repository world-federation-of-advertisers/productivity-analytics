from datetime import datetime, timedelta
import pandas as pd
import pytz
import calendar


def pr_stale_monthly(month, pr_df, stale_for_days=90):

    year, month = map(int, month.split('-'))

    last_day = calendar.monthrange(year, month)[1]

    date_string = f"{year:04d}{month:02d}{last_day:02d}"

    end_date = datetime.strptime(date_string, "%Y%m%d").replace(tzinfo=pytz.UTC)

    ninety_days_ago = end_date - timedelta(days=stale_for_days)

    pr_df['created_at'] = pr_df['created_at'].dt.tz_convert('UTC')

    stale_prs = pr_df[(pr_df['created_at'] <= ninety_days_ago) & (pr_df['state'] == 'open')]

    return stale_prs
