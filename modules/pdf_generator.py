
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def make_simple_pdf(title: str, fields: dict) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4
    c.setTitle(title)

    y = h - 30*mm
    c.setFont("Helvetica-Bold", 16)
    c.drawString(25*mm, y, title)
    y -= 10*mm
    c.setFont("Helvetica", 11)

    for k, v in fields.items():
        text = f"{k}: {v}"
        max_len = 95
        while len(text) > max_len:
            c.drawString(25*mm, y, text[:max_len])
            y -= 7*mm
            text = text[max_len:]
            if y < 25*mm:
                c.showPage()
                y = h - 25*mm
                c.setFont("Helvetica", 11)
        c.drawString(25*mm, y, text)
        y -= 7*mm
        if y < 25*mm:
            c.showPage()
            y = h - 25*mm
            c.setFont("Helvetica", 11)

    c.setFont("Helvetica-Oblique", 9)
    c.drawString(25*mm, 15*mm, "《影響力》傳承策略平台｜永傳家族辦公室  |  僅供教育性初評")
    c.save()
    buffer.seek(0)
    return buffer.read()
