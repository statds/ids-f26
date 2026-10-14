#!/usr/bin/env python3
"""Download the Fall 2026 midterm's NYC 311 honking data and volume control.

The public Socrata endpoint permits simple unauthenticated queries. Set
SOCRATA_APP_TOKEN to identify requests and reduce shared-IP throttling.
Run from the student's project directory; CSV files are written to ./data.
"""

import argparse
import os
from pathlib import Path

import pandas as pd
import requests

URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
START = pd.Timestamp("2023-01-01")
END = pd.Timestamp("2026-07-01")  # exclusive: includes requests through June 2026
PAGE_SIZE = 50_000
COLUMNS = [
    "unique_key",
    "created_date",
    "closed_date",
    "action_update_date",
    "agency",
    "complaint_type",
    "descriptor",
    "borough",
    "incident_zip",
    "latitude",
    "longitude",
    "status",
    "open_data_channel_type",
]


def fetch_rows(session, params):
    """Fetch all pages matching a Socrata query."""
    pages = []
    offset = 0
    while True:
        query = {**params, "$limit": PAGE_SIZE, "$offset": offset}
        response = session.get(URL, params=query, timeout=300)
        response.raise_for_status()
        rows = response.json()
        if not rows:
            break
        pages.extend(rows)
        offset += len(rows)
        print(f"Downloaded {offset:,} rows", flush=True)
        if len(rows) < PAGE_SIZE:
            break
    return pages


def download_honking(session, output_dir):
    """Download one row per honking service request."""
    where = (
        "complaint_type = 'Noise - Vehicle' "
        "AND descriptor = 'Car/Truck Horn' "
        f"AND created_date >= '{START:%Y-%m-%dT%H:%M:%S}' "
        f"AND created_date < '{END:%Y-%m-%dT%H:%M:%S}'"
    )
    rows = fetch_rows(session, {
        "$select": ", ".join(COLUMNS),
        "$where": where,
        "$order": "unique_key",
    })
    data = pd.DataFrame(rows, columns=COLUMNS)
    path = output_dir / "311_honking_raw.csv"
    data.to_csv(path, index=False)
    print(f"Saved {len(data):,} requests to {path}")


def download_volume(session, output_dir):
    """Download all 311 request counts by ZIP code and month."""
    rows = []
    months = pd.date_range(START, END, freq="MS", inclusive="left")
    for month in months:
        next_month = month + pd.offsets.MonthBegin(1)
        where = (
            f"created_date >= '{month:%Y-%m-%dT%H:%M:%S}' "
            f"AND created_date < '{next_month:%Y-%m-%dT%H:%M:%S}'"
        )
        page = fetch_rows(session, {
            "$select": "incident_zip, count(*) as n",
            "$where": where,
            "$group": "incident_zip",
        })
        for record in page:
            record["month"] = month.strftime("%Y-%m-%d")
            rows.append(record)
        print(f"Summarized total 311 volume for {month:%Y-%m}", flush=True)
    data = pd.DataFrame(rows, columns=["incident_zip", "n", "month"])
    path = output_dir / "311_volume_by_zip.csv"
    data.to_csv(path, index=False)
    print(f"Saved {len(data):,} ZIP-month counts to {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir", type=Path, default=Path.cwd() / "data",
        help="directory for downloaded CSV files (default: ./data)",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    token = os.getenv("SOCRATA_APP_TOKEN")
    if token:
        session.headers["X-App-Token"] = token
    download_honking(session, args.output_dir)
    download_volume(session, args.output_dir)


if __name__ == "__main__":
    main()
