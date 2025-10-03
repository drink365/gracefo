
import csv
from io import StringIO

def to_csv_download(data_rows, fieldnames):
    """Return (filename, bytes) for CSV download."""
    sio = StringIO()
    writer = csv.DictWriter(sio, fieldnames=fieldnames)
    writer.writeheader()
    for r in data_rows:
        writer.writerow(r)
    content = sio.getvalue().encode("utf-8-sig")
    return "report.csv", content
