from openstaad import Load

load = Load()

load_Title = load.GetLoadCaseTitle(lc=1)

print(load_Title)
