"""
Generate Lebalelo TowerCo security proposal PDF (standalone, no external assets).
Requires: pip install fpdf2
"""
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Lebalelo_Site_Security_Proposal.pdf"
NOTE = ROOT / "lebalelo_proposal_note.txt"


def ascii_safe(s: str) -> str:
    return (
        s.replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2022", "*")
        .replace("\u2122", "(TM)")
        .replace("\u2019", "'")
    )


class ProposalPDF(FPDF):
    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def section_title(pdf: ProposalPDF, title: str) -> None:
    pdf.ln(4)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(180, 30, 30)
    pdf.multi_cell(pdf.epw, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "", 10)


def body_text(pdf: ProposalPDF, text: str) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(pdf.epw, 4.2, ascii_safe(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def para(pdf: ProposalPDF, text: str, size: int = 10) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "", size)
    pdf.multi_cell(pdf.epw, 5, ascii_safe(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def main() -> None:
    pdf = ProposalPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)

    # --- Cover
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(25, 25, 25)
    pdf.ln(40)
    w = pdf.epw
    pdf.multi_cell(w, 10, "Aggressive Intelligence", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(90, 90, 90)
    pdf.ln(6)
    pdf.multi_cell(w, 6, "Security  |  IoT  |  Intelligence", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(180, 30, 30)
    pdf.ln(28)
    pdf.set_font("Helvetica", "B", 16)
    pdf.multi_cell(w, 9, "Lebalelo Site Security Solution", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("Helvetica", "", 12)
    pdf.ln(8)
    pdf.multi_cell(
        w,
        7,
        "Securing Lebalelo - Complete IoT Perimeter Protection\nPowered by On-Site Sigfox Base Station",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(16)
    pdf.set_font("Helvetica", "B", 11)
    pdf.multi_cell(w, 6, "Presented to: TowerCo", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 10)
    pdf.ln(4)
    pdf.multi_cell(w, 6, "Site: Lebalelo", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(50)
    pdf.set_text_color(100, 100, 100)
    pdf.set_font("Helvetica", "I", 9)
    pdf.multi_cell(
        w,
        5,
        "Commercial proposal - RAMAC(TM) G-Matrix sensors | Sigfox Access Station Micro",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # --- Summary one-pager
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(25, 25, 25)
    pdf.cell(0, 8, "Executive summary", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(40, 40, 40)
    summary = (
        "TowerCo requires dependable perimeter and asset visibility at Lebalelo. "
        "Macro Sigfox coverage is weak across the compound: RF margin, not hardware quality, "
        "limits alarm delivery. We propose a tower-mounted Sigfox Access Station Micro using "
        "existing site power and fiber/microwave backhaul - full local coverage, no new civil "
        "infrastructure, immediate activation. Field devices are RAMAC(TM) G-Matrix (Sigfox-native, "
        "long battery life), integrated with control room and mobile alerting."
    )
    para(pdf, summary)

    section_title(pdf, "Turnkey solution (high level)")
    bullets = [
        "Install Sigfox Access Station Micro on the Lebalelo tower (uses site backhaul; no extra connectivity OPEX model).",
        "Full local Sigfox coverage for the site footprint.",
        "RAMAC(TM) G-Matrix sensors: fence/perimeter, intrusion, assets, environment, CCTV triggers - all via Sigfox.",
        "Traffic to cloud dashboards over existing tower backhaul.",
        "Next step: schedule tower access for survey and base-station installation.",
    ]
    for b in bullets:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(pdf.epw, 5, f"* {ascii_safe(b)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(2)
    section_title(pdf, "Benefits")
    benefits = [
        "100% site coverage (under the new local cell).",
        "Zero additional OPEX for wide-area IoT connectivity (uses existing utilities/backhaul).",
        "Real-time alerts to control room / mobile app.",
        "ROI model: under 9 months (theft reduction + insurance) - subject to TowerCo validation.",
        "Scalable pattern to other TowerCo sites.",
    ]
    for b in benefits:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(pdf.epw, 5, f"* {ascii_safe(b)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(2)
    section_title(pdf, "Contact")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(40, 40, 40)
    para(pdf, "Aggressive Intelligence")
    para(pdf, "Email: info@aggressiveintelligence.example")
    para(pdf, "Phone: +27 (0) 00 000 0000")

    # --- Full proposal note (from file)
    if NOTE.exists():
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(25, 25, 25)
        pdf.cell(0, 8, "Proposal summary note (full text)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(40, 40, 40)
        raw = NOTE.read_text(encoding="utf-8")
        body_text(pdf, raw)

    pdf.output(OUT)
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
