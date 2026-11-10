"""Calendar calculation for a worked example, not an email parser."""

from datetime import date, timedelta


def latest_sessions(due, available_dates, sessions, buffer_days=1):
    """Reserve full buffer days before the due date; one session per date."""
    if sessions < 1 or buffer_days < 0:
        raise ValueError("Invalid session count or buffer")
    work_before = due - timedelta(days=buffer_days)
    eligible = sorted({day for day in available_dates if day < work_before})
    if len(eligible) < sessions:
        raise ValueError("Not enough available sessions before the buffer")
    return eligible[-sessions:]


if __name__ == "__main__":
    import json
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    prefs = json.loads((root / "fixtures/inbox/preferences.json").read_text())
    availability = prefs["project_work_availability"]
    available = [date.fromisoformat(s) for s in availability["available_dates"]]
    due = date(2026, 11, 23)  # Explicit deadline from fixture message E3.
    planned = latest_sessions(due, available, 3, 2)
    assert planned == [date(2026, 11, day) for day in (18, 19, 20)]
    # Removing one available day must move preparation earlier.
    fewer = [d for d in available if d != date(2026, 11, 19)]
    assert latest_sessions(due, fewer, 3, 2)[0] == date(2026, 11, 17)
    try:
        latest_sessions(due, [date(2026, 11, 22)], 3, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("An impossible schedule was accepted")
    print("Calendar checks passed:", ", ".join(d.isoformat() for d in planned))
