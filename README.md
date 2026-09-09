# Sistema de Automatización: Partitura a Letra de Alabanzas
> **IDDV El Buen Pastor — Coro Unido Filadelfia**

Este proyecto automatiza la conversión de partituras corales (arreglos SATB en PDF exportados de Sibelius, NoteWorthy Composer, MuseScore o Finale) en hojas de letra estandarizadas y limpias de **1 sola página** (PDF oficial, Markdown, TXT y previsualizaciones gráficas de alta resolución).

---

## 📂 Estructura Organizada del Proyecto

El espacio de trabajo sigue el estándar numérico institucional de carpetas de IDDV El Bu```
[07] PDF ALABANZAS AUTOMATION/
├── [01] INPUT PARTITURAS/               # Entrada: Partituras originales (.pdf)
│   ├── Coro Maranatha - El ADN del Reino (Congreso 2026).pdf
│   ├── Con Gozo Cantemos a Cristo Partitura.pdf
│   └── Yo Soy Hijo de Dios Partitura.pdf
│
├── [02] SONGS DATA/                     # Datos estructurados en formato JSON (9 del cancionero + extras)
│   ├── a_tu_nombre_gloria.json
│   ├── al_santo_senor.json
│   ├── aleluya.json
│   ├── como_no_agradecer.json
│   ├── elias.json
│   ├── estar_siempre_con_el.json
│   ├── cambiaste_mi_vida.json
│   ├── no_te_imaginas_cuanto_te_amo.json
│   ├── viene_pronto.json
│   └── ...
│
├── [03] OUTPUT LETRAS/                  # Salida organizada por formato
│   ├── [01] PDF/                        # PDFs finales listos para imprimir (1 página) y Cancionero Compilado
│   │   ├── Coro Maranatha - El ADN del Reino (Letras).pdf   # Cancionero completo (11 págs: Portada + Índice + 9 Alabanzas)
│   │   ├── A Tu Nombre Gloria Letra.pdf
│   │   └── ...
│   ├── [02] MARKDOWN/                   # Cancionero digital y repositorio
│   ├── [03] TEXT/                       # Texto plano para proyección (EasyWorship / ProPresenter)
│   └── [04] PREVIEWS/                   # Renders PNG de alta resolución (150 DPI)
│
├── [04] ASSETS/                         # Recursos oficiales y tipografías
│   ├── fonts/
│   │   ├── DancingScript-Bold.ttf       # Tipografía caligráfica para títulos de alabanza
│   │   ├── Economica-Regular.ttf        # Tipografía condensada para estrofas y coros
│   │   ├── Economica-Bold.ttf           # Variante negrita para encabezados
│   │   └── OpenSauceOne-Regular.ttf     # Tipografía del Índice de Alabanzas
│   └── og_ebp.svg                       # Escudo oficial vectorial IDDV El Buen Pastor
│
├── [05] DOCS/                           # Documentación técnica, reglas musicales y arquitectura
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
├── compile_himnario.py                  # Ensamblador de cancionero (Vectoriza portada, corrige índice y unifica tamaño)
├── process_alabanza.py                  # CLI Automatizador para procesar canciones y compilar
├── requirements.txt                     # Dependencias Python
└── README.md                            # Guía de uso del repositorio
```

---

## 🚀 Cómo Usar el Automatizador (CLI)

### 1. Procesar todas las canciones registradas:
```bash
python process_alabanza.py --all
```

### 2. Procesar todas las canciones y compilar el cancionero completo (11 págs):
```bash
python process_alabanza.py --all --compile
```
*(O ejecutar directamente `python compile_himnario.py`)*

### 3. Procesar una canción específica:
```bash
python process_alabanza.py --song yo_soy_hijo_de_dios
```
o
```bash
python process_alabanza.py --song viene_pronto
```

### 4. Listar canciones disponibles:
```bash
python process_alabanza.py --list
```

---

## 📚 Cancionero Oficial Compilado: "El ADN del Reino" (Congreso 2026)
> **Coro Maranatha — Iglesia del Dios Vivo Columna y Apoyo de la Verdad "El Buen Pastor"**

- 📕 **Cancionero Completo (11 páginas - Portada + Índice + 9 Alabanzas):**
  - [`[03] OUTPUT LETRAS/[01] PDF/Coro Maranatha - El ADN del Reino (Letras).pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Coro%20Maranatha%20-%20El%20ADN%20del%20Reino%20(Letras).pdf)
  *(Mantiene exactamente las Páginas 1 y 2 originales con Portada e Índice gráfico, seguidas de las 9 hojas de letra a 1 página cada una)*

### Alabanzas del Cancionero (1 página c/u):
1. **`01. A Tu Nombre Gloria`** (Irán Bautista Medrano | Arr. Iván Antonio & Alfonso García)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/A Tu Nombre Gloria Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/A%20Tu%20Nombre%20Gloria%20Letra.pdf)
2. **`02. Al Santo Señor`** (Uziel Bejarano C. | Arr. Ivan Antonio V. & Elías Delgado L.)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Al Santo Señor Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Al%20Santo%20Señor%20Letra.pdf)
3. **`03. Aleluya`** (Absalón Núñez N.)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Aleluya Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Aleluya%20Letra.pdf)
4. **`04. Como No Agradecer`** (Cristian P. Sanchez | Arr. Isaí Araujo)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Como No Agradecer Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Como%20No%20Agradecer%20Letra.pdf)
5. **`05. Elias`** (Isaías Sanchez C. & Absalón Núñez | Arr. Absalón Núñez)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Elias Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Elias%20Letra.pdf)
6. **`06. Estar Siempre Con El`** (Raúl Luna A. | Arr. Elías Delgado L.)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Estar Siempre Con El Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Estar%20Siempre%20Con%20El%20Letra.pdf)
7. **`07. Cambiaste Mi Vida`** (Jehú Ortiz Martínez | Arr. Amauri Montalvo Cruz)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Cambiaste Mi Vida Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Cambiaste%20Mi%20Vida%20Letra.pdf)
8. **`08. No te Imaginas Cuánto te Amo`** (Eder Seled Solís Silva)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/No te Imaginas Cuánto te Amo Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/No%20te%20Imaginas%20Cuánto%20te%20Amo%20Letra.pdf)
9. **`09. Viene Pronto`** (Absalón Nuñez N. | Arr. Joab A. Fuentes S. & Ivan Antonio V.)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Viene Pronto Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Viene%20Pronto%20Letra.pdf)

---

## 📄 Repertorio General Adicional Procesado

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

4. **`Todos Alaben`** (Irán Bautista Medrano — *Arr. Iván Antonio & Alfonso García E.*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Todos Alaben Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Todos%20Alaben%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Todos Alaben Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Todos%20Alaben%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Todos Alaben Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Todos%20Alaben%20Letra.txt)

5. **`El Espíritu de Cristo en Mí`** (Elías Delgado León — *Santa Cena 2008*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/El Espíritu de Cristo en Mí Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/El%20Espíritu%20de%20Cristo%20en%20Mí%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/El Espíritu de Cristo en Mí Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/El%20Espíritu%20de%20Cristo%20en%20Mí%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/El Espíritu de Cristo en Mí Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/El%20Espíritu%20de%20Cristo%20en%20Mí%20Letra.txt)

6. **`Espíritu de Dios`** (Ruth Sánchez C. — *Santa Cena 2014 | Dir. Juan A. Velázquez M.*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Espíritu de Dios Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Espíritu%20de%20Dios%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Espíritu de Dios Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Espíritu%20de%20Dios%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Espíritu de Dios Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Espíritu%20de%20Dios%20Letra.txt)

7. **`Somos Comprados`** (SdD Sara Montalvo Rodaleón — *Arm. Juan López Hernández | Santa Cena 2017*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Somos Comprados Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Somos%20Comprados%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Somos Comprados Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Somos%20Comprados%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Somos Comprados Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Somos%20Comprados%20Letra.txt)

8. **`Detente Mi Señor`** (Tradicional — *IDDV El Buen Pastor*)
   - PDF: [`[03] OUTPUT LETRAS/[01] PDF/Detente Mi Señor Letra.pdf`]([03]%20OUTPUT%20LETRAS/[01]%20PDF/Detente%20Mi%20Señor%20Letra.pdf)
   - Markdown: [`[03] OUTPUT LETRAS/[02] MARKDOWN/Detente Mi Señor Letra.md`]([03]%20OUTPUT%20LETRAS/[02]%20MARKDOWN/Detente%20Mi%20Señor%20Letra.md)
   - Texto: [`[03] OUTPUT LETRAS/[03] TEXT/Detente Mi Señor Letra.txt`]([03]%20OUTPUT%20LETRAS/[03]%20TEXT/Detente%20Mi%20Señor%20Letra.txt)

---

## 📖 Documentación de Arquitectura y Reglas Musicales
Para consultar el análisis exhaustivo de polifonía SATB, des-silabificación, tratamiento de casillas 1 y 2, y envoltura de respuestas en paréntesis:
👉 **[`[05] DOCS/PROCESO_AUTOMATIZACION_PARTITURA_A_LETRA.md`]([05]%20DOCS/PROCESO_AUTOMATIZACION_PARTITURA_A_LETRA.md)**
