from openstaad import Properties

properties = Properties()

section_name = properties.GetBeamSectionName(beam=1)
section_ref = properties.GetBeamSectionPropertyRefNo(beam=1)

print(section_name)
print(section_ref)