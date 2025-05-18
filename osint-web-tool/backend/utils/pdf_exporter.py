from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from database import load_result
import os

def export_to_pdf(username, platform="github"):
    data = load_result(username, platform)
    if not data:
        return None

    filename = f"report_{platform}_{username}.pdf"
    filepath = os.path.join("data", filename)
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"OSINT Report: {username} on {platform}")
    y -= 30

    c.setFont("Helvetica", 12)
    for key, value in data.items():
        if isinstance(value, (str, int, float)):
            c.drawString(50, y, f"{key}: {value}")
            y -= 20
        elif isinstance(value, list):
            c.drawString(50, y, f"{key}:")
            y -= 20
            for item in value[:5]:  # Show up to 5 items
                c.drawString(70, y, f"- {str(item)}")
                y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    return filepath