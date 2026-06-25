from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus import Image
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER

from reportlab.pdfgen import canvas


class createPDF:
    def __init__(self,filename):
        self.filename = filename
        self.doc = SimpleDocTemplate(self.filename, pagesize=A4)
        self.story = []
        self.canvas = canvas.Canvas(self.filename)  # Initialize the canvas
        self.page_width, self.page_height = A4

    def add_cover_page(self, ai_percent=None):
    # Define styles for the cover page with more elegant fonts and colors
        cover_style = ParagraphStyle(
            name="CoverTitle",
            fontName='Helvetica-Bold',  # Elegant and classic font
            fontSize=48,  # Larger font for an impactful title
            leading=54,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2C3E50"),  # Dark Slate for a premium feel
            spaceAfter=50,  # Larger space below title
        )

        subtitle_style = ParagraphStyle(
            name="Subtitle",
            fontName='Helvetica-Oblique',  # Italic for a stylish subtitle
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2980B9"),  # Lighter blue for contrast
            spaceAfter=40,
        )

        footer_style = ParagraphStyle(
            name="Footer",
            fontName='Helvetica-Oblique',
            fontSize=16,
            leading=20,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#7F8C8D"),  # Light grey for the footer text
            spaceAfter=20,
        )

        # Add decorative line style for visual enhancement
        line_style = ParagraphStyle(
            name="Line",
            fontSize=2,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#95A5A6"),  # Subtle grey line
            spaceAfter=30,
        )

        # Add background color to the cover page
        self.canvas.setFillColor(colors.HexColor("#ECF0F1"))  # Soft light background
        self.canvas.rect(0, 0, self.page_width, self.page_height, stroke=0, fill=1)

        # Add content to the cover page
        self.story.append(Spacer(1, 3.5 * inch))  # Adjusted for better vertical balance
        self.story.append(Paragraph("AI Detection Report", cover_style))
        self.story.append(Spacer(1, 0.5 * inch))

        # Adding a subtle decorative line
        self.story.append(Paragraph('<hr width="75%">', line_style))

        self.story.append(Spacer(1, 0.2 * inch))
        self.story.append(Paragraph("Developed by Ayan and Raghunandan", subtitle_style))
        self.story.append(Spacer(1, 1.5 * inch))

        # If AI detection percentage is available, show it prominently
        if ai_percent:
            detection_style = ParagraphStyle(
                name="Detection",
                fontName='Helvetica-Bold',
                fontSize=26,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#E74C3C"),  # Bold red for emphasis
                spaceAfter=20,
            )
            self.story.append(Paragraph(f"AI Content Detected: {ai_percent}%", detection_style))
        

        # Add AI percentage text if provided
        if ai_percent is not None:
            self.story.append(Spacer(1, 1 * inch))
            ai_text = f"This text is {ai_percent:.2f}% likely to be AI-generated."
            self.story.append(Paragraph(ai_text, footer_style))

        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(PageBreak())  # Add a page break to move to the next page


    def draw_cover_background(self, canvas, doc):
        # Draw dark background on the first page (cover page)
        canvas.setFillColor(colors.HexColor("#1c1c1c"))  # Dark color (hex)
        canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

        # Adding a decorative line
        canvas.setStrokeColor(colors.HexColor("#1c1c1c"))  # Gold color
        canvas.setLineWidth(5)
        canvas.line(0.5 * inch, 10.8 * inch, 7.5 * inch, 10.8 * inch)  # Top horizontal line


    def add_text(self, text, generated_by):
        # Define styles
        styles = getSampleStyleSheet()
        style = styles["Normal"]

        # Create a Paragraph object
        color = colors.red if generated_by == "AI" else colors.black
        style.textColor = color

        # Split the text into sentences or paragraphs as needed
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            self.story.append(Paragraph(paragraph, style))
            self.story.append(Spacer(1, 0.2 * inch))  # Add space between paragraphs

    def save_pdf(self):
        self.doc.build(self.story)
        print(f"PDF saved as {self.filename}")