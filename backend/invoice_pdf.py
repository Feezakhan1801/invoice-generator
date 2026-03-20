

from fpdf import FPDF
from pathlib import Path

def generate_invoice_pdf(invoice):
    # Create 'invoices' folder inside backend if it doesn't exist
    invoices_dir = Path(__file__).parent / "invoices"
    invoices_dir.mkdir(exist_ok=True)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "INVOICE", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, f"Customer: {invoice.customer_name}", ln=True)
    pdf.cell(0, 8, f"PO No: {invoice.purchase_order_no}", ln=True)
    pdf.cell(0, 8, f"Bill Date: {invoice.bill_date}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 8, f"Billing Address: {invoice.billing_address}", ln=True)
    pdf.cell(0, 8, f"Shipping Address: {invoice.shipping_address}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 8, f"Item: {invoice.item_name}", ln=True)
    pdf.cell(0, 8, f"Qty: {invoice.quantity}", ln=True)
    pdf.cell(0, 8, f"Price: {invoice.price}", ln=True)
    pdf.cell(0, 8, f"Total: {invoice.total}", ln=True)

    pdf.ln(5)
    pdf.multi_cell(0, 8, f"Description: {invoice.item_description}")
    pdf.multi_cell(0, 8, f"Additional Details: {invoice.additional_details}")

    # Save PDF in invoices folder
    pdf_filename = f"invoice_{invoice.id}.pdf"
    pdf_path = invoices_dir / pdf_filename
    pdf.output(str(pdf_path))

    # Return full path
    return str(pdf_path)

'''


from fpdf import FPDF
from pathlib import Path

def generate_invoice_pdf(invoice):
    # Create 'invoices' folder inside backend if it doesn't exist
    invoices_dir = Path(__file__).parent / "invoices"
    invoices_dir.mkdir(exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    # ---------- HEADER ----------
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(33, 71, 123)
    pdf.cell(0, 10, "Your Company Name", ln=True)

    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "INVOICE", ln=True, align="R")
    pdf.ln(2)

    pdf.set_line_width(0.5)
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)

    # ---------- CUSTOMER & INVOICE DETAILS ----------
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(95, 8, "Customer Details", border=1, ln=0, fill=True)
    pdf.cell(95, 8, "Invoice Details", border=1, ln=1, fill=True)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(95, 8, f"Name: {invoice.customer_name}", border=1, ln=0)
    pdf.cell(95, 8, f"PO No: {invoice.purchase_order_no}", border=1, ln=1)

    pdf.cell(95, 8, f"Email: {getattr(invoice, 'email', '-')}", border=1, ln=0)
    pdf.cell(95, 8, f"Bill Date: {invoice.bill_date}", border=1, ln=1)

    pdf.ln(5)

    # ---------- ADDRESSES ----------
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(95, 8, "Billing Address", border=1, ln=0, fill=True)
    pdf.cell(95, 8, "Shipping Address", border=1, ln=1, fill=True)

    pdf.set_font("Helvetica", "", 11)
    billing = invoice.billing_address or "-"
    shipping = invoice.shipping_address or "-"
    pdf.multi_cell(95, 6, billing, border=1, ln=0)
    x = pdf.get_x()
    y = pdf.get_y() - (billing.count("\n") + 1) * 6
    pdf.set_xy(105, y)
    pdf.multi_cell(95, 6, shipping, border=1, ln=1)
    pdf.ln(5)

    # ---------- ITEM TABLE ----------
    pdf.set_font("Helvetica", "B", 12)
    fill_color = (230, 239, 251)
    pdf.set_fill_color(*fill_color)
    pdf.cell(90, 10, "Item", border=1, align="L", fill=True)
    pdf.cell(30, 10, "Qty", border=1, align="C", fill=True)
    pdf.cell(35, 10, "Price", border=1, align="R", fill=True)
    pdf.cell(35, 10, "Total", border=1, align="R", fill=True)
    pdf.ln()

    pdf.set_font("Helvetica", "", 11)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(90, 10, invoice.item_name or "-", border=1, align="L", fill=True)
    pdf.cell(30, 10, str(invoice.quantity), border=1, align="C", fill=True)
    pdf.cell(35, 10, f"{invoice.price:,.2f}", border=1, align="R", fill=True)
    pdf.cell(35, 10, f"{invoice.total:,.2f}", border=1, align="R", fill=True)
    pdf.ln(12)

    # ---------- NOTES / DESCRIPTION ----------
    if invoice.item_description or invoice.additional_details:
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "Notes", ln=1)
        pdf.set_font("Helvetica", "", 11)
        if invoice.item_description:
            pdf.multi_cell(0, 6, f"Description: {invoice.item_description}")
        if invoice.additional_details:
            pdf.multi_cell(0, 6, f"Additional Details: {invoice.additional_details}")
        pdf.ln(5)

    # ---------- TOTAL SECTION ----------
    pdf.set_xy(105, pdf.get_y())  # right-side align section
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(35, 8, "Subtotal", border=1, align="R")
    pdf.cell(35, 8, f"{invoice.total:,.2f}", border=1, align="R")
    pdf.ln()

    pdf.set_xy(105, pdf.get_y())
    pdf.cell(35, 8, "Total", border=1, align="R")
    pdf.cell(35, 8, f"{invoice.total:,.2f}", border=1, align="R")
    pdf.ln(12)

    # ---------- FOOTER ----------
    pdf.set_y(-40)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, "Thank you for your business!", ln=1, align="C")
    pdf.cell(0, 5, "Please contact us if you have questions about this invoice.", ln=1, align="C")
    pdf.cell(0, 5, "www.yourcompany.com | support@yourcompany.com", ln=1, align="C")

    # Save PDF in invoices folder
    pdf_filename = f"invoice_{invoice.id}.pdf"
    pdf_path = invoices_dir / pdf_filename
    pdf.output(str(pdf_path))

    return str(pdf_path)
'''