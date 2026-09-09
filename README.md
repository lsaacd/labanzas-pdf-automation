# Sistema de Automatización: Partitura a Letra de Alabanzas
> **IDDV El Buen Pastor — Coro Unido Filadelfia**

Este proyecto automatiza la conversión de partituras corales (arreglos SATB en PDF exportados de Sibelius, NoteWorthy Composer, MuseScore o Finale) en hojas de letra estandarizadas y limpias de **1 sola página** (PDF oficial, Markdown, TXT y previsualizaciones gráficas de alta resolución).

---

## 📂 Estructura Organizada del Proyecto

El espacio de trabajo sigue el estándar numérico institucional de carpetas de IDDV El Buen Pastor:

```
[07] PDF ALABANZAS AUTOMATION/
├── [01] INPUT PARTITURAS/               # Entrada: Partituras originales (.pdf)
│   ├── Con Gozo Cantemos a Cristo Partitura.pdf
│   └── Yo Soy Hijo de Dios Partitura.pdf
│
├── [02] SONGS DATA/                     # Datos estructurados en formato JSON
│   ├── con_gozo_cantemos_a_cristo.json
│   └── yo_soy_hijo_de_dios.json
│
├── [03] OUTPUT LETRAS/                  # Salida organizada por formato
│   ├── [01] PDF/                        # PDFs finales listos para imprimir (1 página)
│   │   ├── Con Gozo Cantemos a Cristo Letra.pdf
│   │   └── Yo Soy Hijo de Dios Letra.pdf
│   ├── [02] MARKDOWN/                   # Cancionero digital y repositorio
│   │   ├── Con Gozo Cantemos a Cristo Letra.md
│   │   └── Yo Soy Hijo de Dios Letra.md
│   ├── [03] TEXT/                       # Texto plano para EasyWorship / ProPresenter
│   │   ├── Con Gozo Cantemos a Cristo Letra.txt
│   │   └── Yo Soy Hijo de Dios Letra.txt
│   └── [04] PREVIEWS/                   # Renders PNG de alta resolución (150 DPI)
│       ├── Con Gozo Cantemos a Cristo Letra_preview.png
│       └── Yo Soy Hijo de Dios Letra_preview.png
│
├── [04] ASSETS/                         # Recursos oficiales y fuentes
│   └── fonts/
│       ├── DancingScript-Bold.ttf       # Tipografía para títulos
│       ├── Economica-Regular.ttf        # Tipografía para letras
│       └── Economica-Bold.ttf           # Variante negrita
│
├── [05] DOCS/                           # Documentación técnica y reglas
│   └── PROCESO_AUTOMATIZACION_PARTITURA_A_LETRA.md
│
├── [06] TOOLS & TESTS/                  # Scripts de inspección, análisis y pruebas
│   ├── analyze_positions.py
│   ├── inspect_letra.py
│   └── test_generate_letra.py
│
├── src/                                 # Motor modular en Python
│   ├── __init__.py
│   ├── models.py                        # Modelos Song y SongSection
│   ├── pdf_generator.py                 # Motor ReportLab con Auto-Fit a 1 página
│   └── exporter.py                      # Exportador a JSON, MD y TXT
│
├── process_alabanza.py                  # CLI Automatizador para procesar canciones
└── README.md                            # Guía de uso del repositorio
```

---

## 🚀 Cómo Usar el Automatizador (CLI)

### 1. Procesar todas las canciones registradas:
```bash
python process_alabanza.py --all
```

### 2. Procesar una canción específica:
```bash
python process_alabanza.py --song yo_soy_hijo_de_dios
```
o
```bash
python process_alabanza.py --song con_gozo
```

### 3. Listar canciones disponibles:
```bash
python process_alabanza.py --list
```

---

## 📄 Repertorio Procesado Actualmente

1. **`Con Gozo Cantemos a Cristo`** (03, Absalón Núñez N)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Con Gozo Cantemos a Cristo Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Con%20Gozo%20Cantemos%20a%20Cristo%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Con Gozo Cantemos a Cristo Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Con%20Gozo%20Cantemos%20a%20Cristo%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Con Gozo Cantemos a Cristo Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Con%20Gozo%20Cantemos%20a%20Cristo%20Letra.txt)

2. **`¡Yo Soy Hijo de Dios!`** (Uziel León Alcántara — *IV Congreso Regional Juvenil Zona 8*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Yo Soy Hijo de Dios Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Yo%20Soy%20Hijo%20de%20Dios%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Yo Soy Hijo de Dios Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Yo%20Soy%20Hijo%20de%20Dios%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Yo Soy Hijo de Dios Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Yo%20Soy%20Hijo%20de%20Dios%20Letra.txt)

3. **`Así Venceré`** (Isaías Sánchez Catalán — *Arr. Juan López H.*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Así Venceré Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Así%20Venceré%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Así Venceré Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Así%20Venceré%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Así Venceré Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Así%20Venceré%20Letra.txt)

---

## 📖 Documentación de Arquitectura y Reglas Musicales
Para consultar el análisis exhaustivo de polifonía SATB, des-silabificación, tratamiento de casillas 1 y 2, y envoltura de respuestas en paréntesis:
👉 **[`[05] DOCS/PROCESO_AUTOMATIZACION_PARTITURA_A_LETRA.md`]([05]%20DOCS/PROCESO_AUTOMATIZACION_PARTITURA_A_LETRA.md)**
