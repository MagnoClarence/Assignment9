import json
from fpdf import FPDF


resume = open('resumeContent.json')
data = json.load(resume)

basicInformation = data['basic information'][0]
profession = data['profession']
educationBackground = data['education background']
achievements = data['achievements']
skillsAbilities = data['skills and abilities']
references = data['references']

# --- PDF ---
# Page format
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

# Contents and formatting
# Basic Info
pdf.set_font('helvetica', 'B', 24)
pdf.cell(40, 10, f"{basicInformation['name']}", ln=1)
pdf.line(10, 20, 200, 20)

pdf.set_font('helvetica', 'I', 12)
pdf.cell(40, 10, f"{basicInformation['location']['address']} "
                 f"{basicInformation['location']['city']} "
                 f"{basicInformation['location']['province']}, "
                 f"{basicInformation['location']['postalCode']}", ln=1)
pdf.cell(10, 2.5,  f"{basicInformation['phone']} | {basicInformation['email']}", ln=1)
pdf.cell(20, 5, "", ln=1)

# Education
pdf.set_font('helvetica', 'B', 18)
pdf.cell(40, 10, "Education Background", ln=1)

for x in educationBackground:
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(20, 5, f"{x['education']}    -    {x['startDate']} - {x['endDate']} | {x['institution']}", ln=1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(20, 5, f"Graduation: {x['gradDate']}", ln=1)
    pdf.cell(20, 5, f"{x['location']}", ln=1)

    pdf.cell(20, 2, f"", ln=1)

# Work Experience
pdf.set_font('helvetica', 'B', 18)
pdf.cell(40, 10, "Work Experience", ln=1)

for x in profession:
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(20, 5, f"{x['startDate']} - {x['endDate']} | {x['position']} | {x['institution']}", ln=1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(20, 5, f"{x['location']}", ln=1)

    pdf.cell(20, 2, f"", ln=1)

# Achievements
pdf.set_font('helvetica', 'B', 18)
pdf.cell(40, 10, "Achievements", ln=1)


for x in achievements:
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(20, 5, f"{x['title']} | {x['date']}", ln=1)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(20, 5, f"{x['awarder']}", ln=1)

    pdf.cell(20, 2, f"", ln=1)

# References
pdf.set_font('helvetica', 'B', 18)
pdf.cell(40, 10, "References", ln=1)

for x in references:
    pdf.set_font('helvetica', '', 12)
    pdf.cell(20, 5, f"{x['name']} | {x['occupancy']}", ln=1)
    pdf.cell(20, 5, f"{x['contact']} | {x['email']}", ln=1)

    pdf.cell(20, 2, f"", ln=1)

# Output
pdf.output('Resume.pdf')