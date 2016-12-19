import csv, yaml, sys, getopt, json
from Parser import Parser

def showHelp():
  print("Usage:")
  print("  python "+sys.argv[0] + ' filename.csv --format=standard')
  print("  python "+sys.argv[0] + ' filename.csv --format=detailed')

if __name__ == '__main__':
  if len(sys.argv) < 2:
    showHelp()
    sys.exit()

  filename=sys.argv[1]
  fileFormat=None

  try:
    opts, args = getopt.getopt(sys.argv[2:],"hf:",["help","format="])
  except getopt.GetoptError:
    showHelp()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h","--help"):
      showHelp()
      sys.exit()
    elif opt in ("-f","--format"):
      if(not arg in ['standard','detailed']):
        showHelp()
        sys.exit()

      fileFormat=arg
    else:
      showHelp()
      sys.exit()

  if fileFormat is None:
    showHelp()
    sys.exit()

  with open(filename) as stream:
    prs = Parser()
    if fileFormat=='standard':
        data = prs.standard(stream)
    elif fileFormat=='detailed':
        data = prs.detailed(stream)

    #print(data)
    #print(json.dumps(data, indent=4, sort_keys=True))
    print(yaml.dump(data, default_flow_style=False))

      #with open('accounts.yml', 'w') as outfile:
      #    yaml.dump(data, outfile, default_flow_style=False)


