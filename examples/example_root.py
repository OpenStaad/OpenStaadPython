from openstaad import Root

root = Root()

staad_version = root.GetApplicationVersion()
units = root.GetBaseUnit()

print(staad_version)
print(units)