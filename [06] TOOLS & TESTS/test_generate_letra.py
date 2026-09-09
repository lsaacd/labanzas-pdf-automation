import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Google Fonts
script_dir = os.path.dirname(os.path.abspath(__file__))
fonts_dir = os.path.join(script_dir, 'fonts')

pdfmetrics.registerFont(TTFont('DancingScript-Bold', os.path.join(fonts_dir, 'DancingScript-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Economica-Regular', os.path.join(fonts_dir, 'Economica-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Economica-Bold', os.path.join(fonts_dir, 'Economica-Bold.ttf')))

output_pdf = os.path.join(script_dir, 'Con Gozo Cantemos a Cristo Letra_generated.pdf')
c = canvas.Canvas(output_pdf, pagesize=letter)
width, height = letter # 612, 792

# Data structure for the song
song_title = "Con Gozo Cantemos a Cristo"
sections = [
    {
        "heading": "CORO:",
        "lines": [
            "CON GOZO CANTEMOS A CRISTO (JESÚS) CON GOZO CANTEMOS A CRISTO (DIGNO ES)",
            "PORQUE EL ES DIGNO DE TODA HONRA DE TODA GLORIA Y HONOR",
            "CON GOZO TODOS UNIDOS CANTEMOS CON GRAN REGOCIJO (CRISTO EL REY, SOLO A ÉL)",
            "Y ENTRE SUS ATRIOS CON ALABANZA RINDAMOS ADORACIÓN"
        ]
    },
    {
        "heading": "1.",
        "lines": [
            "CON SU SANGRE NOS REDIMIÓ, CON SU MUERTE VIDA NOS DIO (OH, OH DIOS)",
            "ES POR ESO QUE SOLO A ÉL RINDO MI ADORACIÓN (OH DIOS)",
            "CON SU SANGRE NOS REDIMIÓ, CON SU MUERTE VIDA NOS DIO (NOS REDIMIÓ)",
            "ES POR ESO QUE SOLO A ÉL RINDO MI ADORACIÓN (HOY LE RINDO ADORACIÓN)"
        ]
    },
    {
        "heading": "2.",
        "lines": [
            "REY DE REYES EL ES MI DIOS, REY DE REYES MI REDENTOR (OH, OH DIOS)",
            "ES POR ESO QUE SOLO A ÉL RINDO MI ADORACIÓN (OH DIOS)",
            "REY DE REYES EL ES MI DIOS, REY DE REYES MI REDENTOR (EL ES MI DIOS)",
            "ES POR ESO QUE SOLO A ÉL RINDO MI ADORACIÓN (HOY LE CANTO CON FERVOR)"
        ]
    },
    {
        "heading": "3.",
        "lines": [
            "ALELUYA PORQUE VENCIÓ, ALELUYA RESUCITÓ (OH, OH DIOS)",
            "ES POR ESO QUE SOLO ÉL VIVE EN MI CORAZÓN (OH DIOS)",
            "ALELUYA PORQUE VENCIÓ, ALELUYA RESUCITÓ ( ÉL YA VENCIÓ)",
            "ES POR ESO QUE SOLO ÉL VIVE EN MI CORAZÓN (VIVE EN MI CORAZÓN)"
        ]
    },
    {
        "heading": "4.",
        "lines": [
            "CARA A CARA LE HE DE VER, CARA A CARA POR SIEMPRE AMÉN (OH, OH DIOS)",
            "ES POR ESO QUE SOLO A EL FIEL YO SIEMPRE SERÉ (OH DIOS)",
            "CARA A CARA LE HE DE VER, CARA A CARA POR SIEMPRE AMÉN (YO LE HE DE VER)",
            "ES POR ESO QUE SOLO A EL FIEL YO SIEMPRE SERÉ (SIEMPRE QUIERO SERLE FIEL)"
        ]
    },
    {
        "heading": "FINAL:",
        "lines": [
            "El ME SALVO CON SU SANGRE CARMESÍ (SU SANGRE QUE ES CARMESÍ)",
            "Y EN LA CRUZ DEMOSTRÓ SU AMOR POR MI (SU AMOR POR TI Y POR MI)",
            "JESUS"
        ]
    }
]

# ReportLab coordinate system: (0,0) is bottom-left, y goes UP.
# Original PDF y goes DOWN from top:
# Title at top y = 72 pt down from top -> in ReportLab y = 792 - 72 - 20 = 700 pt approx.
# Let's calibrate exact baseline positioning:

center_x = width / 2.0

# Draw Title
c.setFont('DancingScript-Bold', 26)
c.drawCentredString(center_x, 792 - 93, song_title) # baseline approx 792 - (72 + 21) = 699

# Now draw sections
# In original PDF:
# CORO heading y_top = 124.1, baseline is approx 792 - 134 = 658
# Let's inspect the exact font sizes and baselines.
c.setFont('Economica-Regular', 13)

# Notice original PDF has:
# line_height = 17.18
# blank_space between sections = 34.36 (i.e. 2 * line_height)
cur_y = 792 - 134.0

for sec in sections:
    if sec["heading"]:
        c.drawCentredString(center_x, cur_y, sec["heading"])
        cur_y -= 17.18
    for line in sec["lines"]:
        c.drawCentredString(center_x, cur_y, line)
        cur_y -= 17.18
    cur_y -= 17.18 # blank line between sections

c.showPage()
c.save()
print("Generated PDF successfully:", output_pdf)
