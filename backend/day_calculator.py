from datetime import datetime, timedelta


def get_weekday_in_n_days(n: int) -> str:
    future_date = datetime.now() + timedelta(days=n)
    return future_date.strftime("%A")
