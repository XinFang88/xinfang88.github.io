#!/usr/bin/env python3
"""Generate Xin Fang's academic CV PDF from the website publication records."""

from __future__ import annotations

import argparse
import ast
import html
import re
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


CHARCOAL = colors.HexColor("#24323D")
TEAL = colors.HexColor("#0D766E")
BLUE = colors.HexColor("#2D5578")
GOLD = colors.HexColor("#B47A22")
GREEN = colors.HexColor("#4F7655")
PLUM = colors.HexColor("#735B7D")
CORAL = colors.HexColor("#A55E58")
MUTED = colors.HexColor("#58656E")
LIGHT = colors.HexColor("#F1F6F5")
LINE = colors.HexColor("#CFDAD8")
SOFT_BLUE = colors.HexColor("#EDF3F8")
SOFT_TEAL = colors.HexColor("#EAF5F3")
SOFT_GOLD = colors.HexColor("#FBF4E8")
SOFT_GREEN = colors.HexColor("#EEF5EE")
SOFT_PLUM = colors.HexColor("#F4EFF7")
SOFT_CORAL = colors.HexColor("#F8EEEE")
WHITE = colors.white


def clean_text(value: object) -> str:
    text = str(value or "")
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2212": "-",
        "\u00a0": " ",
        "\u00b7": " | ",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", " ", text).strip()


def parse_scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value[0:1] in {"'", '"'} and value[-1:] == value[0]:
        try:
            return str(ast.literal_eval(value))
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def parse_front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    key_pattern = re.compile(
        r"^(title|collection|permalink|date|venue|paperurl|citation|"
        r"publication_type|type|excerpt)\s*:"
    )
    index = 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "---":
            break
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if ":" not in line:
            index += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if raw in {">", "|", ">-", "|-"}:
            parts = []
            index += 1
            while index < len(lines):
                continuation = lines[index]
                if continuation.strip() == "---":
                    index -= 1
                    break
                if continuation and not continuation[0].isspace():
                    index -= 1
                    break
                if continuation.strip():
                    parts.append(continuation.strip())
                index += 1
            data[key] = " ".join(parts)
        else:
            parts = [raw]
            probe = index + 1
            while probe < len(lines):
                continuation = lines[probe]
                if continuation.strip() == "---":
                    break
                if key_pattern.match(continuation):
                    break
                if continuation.strip():
                    parts.append(continuation.strip())
                probe += 1
            index = probe - 1
            data[key] = parse_scalar(" ".join(parts))
        index += 1
    return data


def publication_records(repo_root: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    records: list[dict[str, str]] = []
    for path in sorted((repo_root / "_publications").glob("*.md")):
        record = parse_front_matter(path)
        if not record.get("title"):
            continue
        record["_path"] = str(path)
        records.append(record)

    def sort_key(record: dict[str, str]) -> tuple[str, str]:
        return (record.get("date", "1900-01-01")[:10], record.get("title", ""))

    records.sort(key=sort_key, reverse=True)
    conferences = [r for r in records if r.get("publication_type") == "conference"]
    journals = [r for r in records if r.get("publication_type") != "conference"]
    return journals, conferences


def highlighted_citation(record: dict[str, str], year: str) -> str:
    citation = clean_text(record.get("citation"))
    if not citation:
        citation = f'{clean_text(record.get("title"))}. {clean_text(record.get("venue"))}. {year}.'
    citation = re.sub(r",\s*,+", ",", citation)
    citation = re.sub(r",(?=\S)", ", ", citation)
    rendered = html.escape(citation)
    for name in ("Xin Fang", "X. Fang", "X Fang"):
        rendered = rendered.replace(name, f"<b>{name}</b>")
    link = clean_text(record.get("paperurl"))
    if link:
        rendered += (
            f' <link href="{html.escape(link, quote=True)}">'
            f'<font color="#0D766E">[paper]</font></link>'
        )
    return rendered


def register_fonts(repo_root: Path) -> tuple[str, str]:
    font_dir = repo_root / "assets" / "fonts"
    candidates = [
        ("OpenSans", font_dir / "OpenSans-Regular.ttf", "OpenSans-Bold", font_dir / "OpenSans-Bold.ttf"),
        ("Lato", font_dir / "Lato-Regular.ttf", "Lato-Bold", font_dir / "Lato-Bold.ttf"),
    ]
    for regular_name, regular_path, bold_name, bold_path in candidates:
        if regular_path.exists() and bold_path.exists():
            pdfmetrics.registerFont(TTFont(regular_name, regular_path))
            pdfmetrics.registerFont(TTFont(bold_name, bold_path))
            return regular_name, bold_name
    return "Helvetica", "Helvetica-Bold"


def make_styles(regular_font: str, bold_font: str) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName=bold_font,
            fontSize=24,
            leading=27,
            textColor=CHARCOAL,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=10.8,
            leading=13.8,
            textColor=BLUE,
            alignment=TA_CENTER,
            spaceAfter=3,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=8.8,
            leading=11.5,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName=bold_font,
            fontSize=13,
            leading=15.5,
            textColor=BLUE,
            spaceBefore=8,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "subsection": ParagraphStyle(
            "Subsection",
            parent=base["Heading3"],
            fontName=bold_font,
            fontSize=10,
            leading=12,
            textColor=TEAL,
            spaceBefore=3,
            spaceAfter=2,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName=regular_font,
            fontSize=9.4,
            leading=12.4,
            textColor=CHARCOAL,
            spaceAfter=3,
        ),
        "body_small": ParagraphStyle(
            "BodySmall",
            parent=base["BodyText"],
            fontName=regular_font,
            fontSize=8.7,
            leading=11.2,
            textColor=CHARCOAL,
            spaceAfter=2,
        ),
        "metric_value": ParagraphStyle(
            "MetricValue",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=13.5,
            leading=15.5,
            textColor=TEAL,
            alignment=TA_CENTER,
        ),
        "metric_label": ParagraphStyle(
            "MetricLabel",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=7.8,
            leading=9.6,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "table_head": ParagraphStyle(
            "TableHead",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=8.2,
            leading=10.2,
            textColor=WHITE,
        ),
        "table_body": ParagraphStyle(
            "TableBody",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=8,
            leading=10.2,
            textColor=CHARCOAL,
        ),
        "table_body_bold": ParagraphStyle(
            "TableBodyBold",
            parent=base["Normal"],
            fontName=bold_font,
            fontSize=8,
            leading=10.2,
            textColor=CHARCOAL,
        ),
        "publication": ParagraphStyle(
            "Publication",
            parent=base["BodyText"],
            fontName=regular_font,
            fontSize=8.25,
            leading=10.7,
            textColor=CHARCOAL,
            leftIndent=13,
            firstLineIndent=-13,
            spaceAfter=4,
            allowWidows=0,
            allowOrphans=0,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName=regular_font,
            fontSize=7.4,
            leading=8.8,
            textColor=MUTED,
            alignment=TA_RIGHT,
        ),
    }


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(clean_text(text)), style)


def rich(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def section_heading(title: str, styles: dict[str, ParagraphStyle]) -> list[object]:
    return [
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.7, color=LINE, spaceAfter=4),
    ]


def two_col_entries(
    left: list[tuple[str, str]],
    right: list[tuple[str, str]],
    styles: dict[str, ParagraphStyle],
) -> Table:
    def cell(title: str, detail: str) -> Paragraph:
        return rich(
            f"<b>{html.escape(clean_text(title))}</b><br/>"
            f'<font color="#58656E">{html.escape(clean_text(detail))}</font>',
            styles["body_small"],
        )

    size = max(len(left), len(right))
    rows = []
    for index in range(size):
        lcell = cell(*left[index]) if index < len(left) else ""
        rcell = cell(*right[index]) if index < len(right) else ""
        rows.append([lcell, rcell])
    table = Table(rows, colWidths=[3.72 * inch, 3.18 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def add_publication_section(
    story: list[object],
    title: str,
    records: list[dict[str, str]],
    styles: dict[str, ParagraphStyle],
) -> None:
    story.extend(section_heading(f"{title} ({len(records)})", styles))
    for index, record in enumerate(records, start=1):
        year = clean_text(record.get("date", ""))[:4] or "n.d."
        citation = highlighted_citation(record, year)
        story.append(rich(f"<b>{index}.</b> {citation}", styles["publication"]))


def draw_page(canvas, doc) -> None:
    canvas.saveState()
    width, height = A4
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, height - 27, width - doc.rightMargin, height - 27)
        canvas.setFillColor(MUTED)
        canvas.setFont(doc.regular_font, 7.4)
        canvas.drawString(doc.leftMargin, height - 20, "Xin Fang | Academic Curriculum Vitae")
        canvas.drawRightString(width - doc.rightMargin, height - 20, "Updated July 2026")
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 27, width - doc.rightMargin, 27)
    canvas.setFillColor(MUTED)
    canvas.setFont(doc.regular_font, 7.4)
    canvas.drawString(doc.leftMargin, 17, "IDEAL Lab | University of South Carolina")
    canvas.drawRightString(width - doc.rightMargin, 17, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(repo_root: Path, output_path: Path) -> None:
    journals, conferences = publication_records(repo_root)
    regular_font, bold_font = register_fonts(repo_root)
    styles = make_styles(regular_font, bold_font)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title="Xin Fang - Curriculum Vitae",
        author="Xin Fang",
        subject="Academic curriculum vitae for faculty applications",
    )
    doc.regular_font = regular_font
    story: list[object] = []

    story.append(Paragraph("Xin Fang, Ph.D.", styles["name"]))
    story.append(
        Paragraph(
            "Assistant Professor of Electrical Engineering | Director, IDEAL Lab | University of South Carolina",
            styles["role"],
        )
    )
    contact = (
        '<link href="mailto:fangxin@sc.edu"><font color="#0D766E">fangxin@sc.edu</font></link>'
        " | Columbia, South Carolina | "
        '<link href="https://xinfang88.github.io"><font color="#0D766E">xinfang88.github.io</font></link>'
        "<br/>"
        '<link href="https://scholar.google.com/citations?user=lr3EP0AAAAAJ">'
        '<font color="#0D766E">Google Scholar</font></link> | '
        '<link href="https://orcid.org/0000-0002-7979-803X">'
        '<font color="#0D766E">ORCID 0000-0002-7979-803X</font></link> | '
        '<link href="https://www.linkedin.com/in/xin-fang-82b90646/">'
        '<font color="#0D766E">LinkedIn</font></link>'
    )
    story.append(Paragraph(contact, styles["contact"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=2.2, color=TEAL, spaceAfter=7))

    metrics = [
        (str(len(journals)), "Journal articles"),
        (str(len(conferences)), "Conference papers"),
        ("$8.75M+", "Documented project portfolio"),
        (
            '<link href="https://scholar.google.com/citations?user=lr3EP0AAAAAJ">'
            '<font color="#0D766E">3,196</font></link>',
            "Google Scholar citations",
        ),
    ]
    metric_cells = []
    for value, label in metrics:
        metric_cells.append(
            [
                [Paragraph(value, styles["metric_value"])],
                [Paragraph(label, styles["metric_label"])],
            ]
        )
    metric_table = Table(
        [[Table(cell, colWidths=[1.63 * inch]) for cell in metric_cells]],
        colWidths=[1.72 * inch] * 4,
        hAlign="CENTER",
    )
    metric_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("BACKGROUND", (0, 0), (0, 0), SOFT_BLUE),
                ("BACKGROUND", (1, 0), (1, 0), SOFT_TEAL),
                ("BACKGROUND", (2, 0), (2, 0), SOFT_GOLD),
                ("BACKGROUND", (3, 0), (3, 0), SOFT_PLUM),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, WHITE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(metric_table)

    story.extend(section_heading("Academic Profile", styles))
    story.append(
        p(
            "Power-system researcher and educator developing optimization, dynamics, physics-informed "
            "and data-driven AI, grid-planning, and cyber-physical modeling methods for reliable, "
            "affordable, renewable-rich electricity systems. Research connects rigorous theory with "
            "deployable planning and operational tools for inverter-based resources, electricity "
            "markets, grid resilience, and digital twins.",
            styles["body"],
        )
    )
    focus_data = [
        [
            rich("<b>Optimization and Markets</b><br/>Learning-assisted dispatch, pricing, robust optimization, and market design", styles["body_small"]),
            rich("<b>Dynamics and Stability</b><br/>ML stability assessment, grid-forming resources, and dynamics-informed scheduling", styles["body_small"]),
        ],
        [
            rich("<b>Grid Planning with Renewables</b><br/>Capacity expansion, reliability, resilience, and resource adequacy", styles["body_small"]),
            rich("<b>Cyber-Physical Co-Simulation</b><br/>AI-enabled analytics, digital twins, DERs, and electric transportation", styles["body_small"]),
        ],
    ]
    focus_table = Table(focus_data, colWidths=[3.45 * inch, 3.45 * inch], hAlign="LEFT")
    focus_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, LINE),
                ("BACKGROUND", (0, 0), (0, 0), SOFT_BLUE),
                ("BACKGROUND", (1, 0), (1, 0), SOFT_CORAL),
                ("BACKGROUND", (0, 1), (0, 1), SOFT_GREEN),
                ("BACKGROUND", (1, 1), (1, 1), SOFT_PLUM),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(focus_table)

    story.extend(section_heading("Appointments and Education", styles))
    appointments = [
        ("2025-present | Assistant Professor", "University of South Carolina"),
        ("2022-2025 | Assistant Professor", "Mississippi State University"),
        ("2017-2022 | Senior Researcher", "National Renewable Energy Laboratory"),
        ("2016-2017 | Power System Engineer", "GE Grid Solutions"),
    ]
    education = [
        ("Ph.D., Electrical Engineering | 2016", "University of Tennessee, Knoxville"),
        ("M.S., Electrical Engineering | 2012", "China Electric Power Research Institute"),
        ("B.S., Electrical Engineering | 2009", "Huazhong University of Science and Technology"),
    ]
    story.append(two_col_entries(appointments, education, styles))

    story.extend(section_heading("Sponsored Research Leadership", styles))
    story.append(
        p(
            "Eight sponsored projects as PI or Co-PI: $962.5K in documented Fang/USC award share "
            "across at least $8.75M in collaborative project activity supported by NSF, DOE, NREL, and INL.",
            styles["body_small"],
        )
    )
    projects = [
        (
            "2027-2029",
            "PowerCyber: Scalable Workforce Development for AI-Enabled Power Grids (NSF Award #2612494)",
            "USC PI | NSF",
            "$200K award",
        ),
        ("2025-2026", "Accelerating Grid Resilience: Distribution-System Digital Twins", "USC Co-PI | INL", "$50K / $500K"),
        ("2024-2027", "DIAMOND: Digital Twin for IBR-Rich Grids", "USC Co-PI | DOE-SETO/NREL", "$330K / $3.2M"),
        ("2024-2027", "HVDC-Learn: Modular HVDC Education and Workforce Training", "MSU Co-PI | DOE/WETO", "$112.5K / $700K"),
        ("2024-2025", "PowerCyber: Computational Training for Power Engineering Researchers", "USC PI | NSF", "$120K / $300K"),
        ("2025", "Unlocking Dynamic Thermal Rating Benefits for Distribution Systems", "USC Co-PI | NREL", "$50K / $250K"),
        ("2024", "T&D Dynamic Co-Simulation for IBR-Rich Power-System Stability", "MSU Co-PI | NREL", "$50K / $400K"),
        ("2023-2025", "SAPPHIRE: Stability-Augmented Optimal Control of Hybrid PV Plants", "MSU Co-PI | DOE/NREL", "$50K / $3.2M"),
    ]
    project_rows = [
        [
            Paragraph("Period", styles["table_head"]),
            Paragraph("Project", styles["table_head"]),
            Paragraph("Role / Sponsor", styles["table_head"]),
            Paragraph("Funding", styles["table_head"]),
        ]
    ]
    for period, title, role, funding in projects:
        project_rows.append(
            [
                Paragraph(period, styles["table_body_bold"]),
                Paragraph(html.escape(title), styles["table_body"]),
                Paragraph(html.escape(role), styles["table_body"]),
                Paragraph(funding, styles["table_body"]),
            ]
        )
    project_table = Table(
        project_rows,
        colWidths=[0.68 * inch, 3.18 * inch, 1.78 * inch, 1.25 * inch],
        repeatRows=1,
        hAlign="LEFT",
    )
    project_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), BLUE),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F7F9F9")]),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
            ]
        )
    )
    story.append(project_table)

    story.append(PageBreak())
    story.extend(section_heading("Graduate Advising and Student Development", styles))
    advisees = [
        ("Yuxin Deng | Ph.D. researcher, Spring 2023-present", "Power-system optimization, planning, stability analysis, and renewable integration."),
        ("Prasant Basnet | Ph.D. researcher, Fall 2022-present; M.S. 2025", "IBR-aware capacity expansion, dynamics, cyber-physical modeling; NREL intern."),
        ("Bishal Rijal | Ph.D. researcher, Spring 2025-present", "Distribution planning, transformer replacement, renewable integration, and system strength; INL intern."),
        ("Adarsha Chalise | Ph.D. researcher, Spring 2026-present", "Island power systems, energy-storage sizing, flexible operation, and reliability."),
    ]
    advising_rows = []
    for index in range(0, len(advisees), 2):
        row = []
        for title, detail in advisees[index : index + 2]:
            row.append(
                rich(
                    f"<b>{html.escape(title)}</b><br/>"
                    f'<font color="#5D686E">{html.escape(detail)}</font>',
                    styles["body_small"],
                )
            )
        advising_rows.append(row)
    advising_table = Table(advising_rows, colWidths=[3.45 * inch, 3.45 * inch], hAlign="LEFT")
    advising_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(advising_table)

    story.extend(section_heading("Teaching Portfolio", styles))
    teaching = [
        ("ELCT 221 | Circuits II", "Spring and Fall 2026 | Undergraduate"),
        ("ELCT 451 | Power System Design and Analysis", "Fall 2025 | Undergraduate"),
        ("ECE 5990 | Power Systems Economics", "Spring 2025 | Undergraduate and graduate"),
        ("ECE 4613/6613 | Power Transmission Systems", "Fall 2023 and 2024 | Undergraduate and graduate"),
        ("ECE 4633/6633 | Power Distribution Systems", "Spring 2023 | Undergraduate and graduate"),
        ("ECE 3643 | Electronic Circuits I", "Fall 2022 | Undergraduate"),
    ]
    story.append(two_col_entries(teaching[:3], teaching[3:], styles))

    story.extend(section_heading("Selected Awards and Honors", styles))
    awards = [
        ("2025", "Best Paper Award, IEEE Open Access Journal of Power and Energy"),
        ("2024", "IEEE PES PSOPE Technical Committee Prize Paper Award"),
        ("2023", "Outstanding Associate Editor, IEEE Transactions on Power Systems"),
        ("2022", "Outstanding Associate Editor, IEEE Transactions on Sustainable Energy"),
        ("2019", "Best Journal Paper Award, Journal of Modern Power Systems and Clean Energy"),
        ("2018", "Best Conference Paper, IEEE PES General Meeting"),
        ("2016", "University of Tennessee Chancellor's Citation Award for Extraordinary Professional Promise"),
        ("2016-2023", "Outstanding/Excellent Reviewer recognition from IEEE and leading power and energy journals"),
        ("2012", "Outstanding Graduate Student, China Electric Power Research Institute"),
        ("2012-2013", "Department Fellowship, EECS Department, University of Tennessee"),
    ]
    award_table = Table(
        [
            [
                Paragraph(year, styles["table_body_bold"]),
                Paragraph(html.escape(title), styles["table_body"]),
            ]
            for year, title in awards
        ],
        colWidths=[0.78 * inch, 6.12 * inch],
        hAlign="LEFT",
    )
    award_table.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, colors.HexColor("#F7F9F9")]),
                ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(award_table)

    story.extend(section_heading("Editorial Leadership and Professional Service", styles))
    service_left = [
        (
            "Chair | 2026-present; Vice Chair | 2023-2025",
            "IEEE PSOPE Bulk Power System Planning Subcommittee",
        ),
        ("Associate Editor | from 2022", "IEEE Transactions on Sustainable Energy"),
        ("Associate Editor | from 2020", "IEEE Transactions on Power Systems"),
    ]
    service_right = [
        ("Associate Editor | from 2025", "Energy Internet"),
        ("Associate Editor | from 2024", "Energy Conversion and Economics"),
        ("Associate Editor | from 2017", "Journal of Modern Power Systems and Clean Energy"),
    ]
    story.append(two_col_entries(service_left, service_right, styles))

    story.extend(section_heading("Selected Research Contributions", styles))
    selected_titles = [
        "Short-Circuit Ratio Constrained Robust Unit Commitment with Grid-Forming Energy Storage: A Filter-Column-and-Constraint Generation Algorithm",
        "Analytical Small-signal Stability Analysis of Low-Inertia Power System Frequency Response Considering Secondary Frequency Regulation",
        "Frequency Nadir Constrained Unit Commitment for High Renewable Penetration Island Power Systems",
        "Transmission-and-Distribution Dynamic Co-Simulation Framework for Distributed Energy Resource Frequency Response",
        "DLMP of Competitive Markets in Active Distribution Networks: Models, Solutions, Applications, and Visions",
    ]
    journal_by_title = {
        clean_text(record.get("title")): record
        for record in journals
    }
    for index, title in enumerate(selected_titles, start=1):
        record = journal_by_title.get(title)
        if not record:
            continue
        year = clean_text(record.get("date", ""))[:4] or "n.d."
        story.append(
            rich(
                f"<b>{index}.</b> {highlighted_citation(record, year)}",
                styles["publication"],
            )
        )

    story.append(PageBreak())
    story.append(
        Paragraph(
            "Complete Publication Record",
            ParagraphStyle(
                "PublicationTitle",
                parent=styles["name"],
                fontSize=18,
                leading=21,
                alignment=TA_LEFT,
                textColor=CHARCOAL,
                spaceAfter=2,
            ),
        )
    )
    story.append(
        p(
            f"{len(journals)} journal articles and {len(conferences)} conference papers. "
            "Author names, venues, and links are generated from the website's publication records.",
            styles["body"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=2, color=TEAL, spaceAfter=5))
    add_publication_section(story, "Journal Articles", journals, styles)
    add_publication_section(story, "Conference Papers", conferences, styles)

    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Website repository root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output PDF path (defaults to assets/files/Xin_Fang_CV.pdf)",
    )
    args = parser.parse_args()
    repo_root = args.repo.resolve()
    output_path = (
        args.output.resolve()
        if args.output
        else repo_root / "assets" / "files" / "Xin_Fang_CV.pdf"
    )
    build_pdf(repo_root, output_path)
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
