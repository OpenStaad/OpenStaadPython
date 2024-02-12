from openstaad import Output

output = Output()

end_forces = output.GetMemberEndForces(beam=1,start=False,lc=1)
support_reaction = output.GetSupportReactions(node=1,lc=1)

print(end_forces)
print(support_reaction)