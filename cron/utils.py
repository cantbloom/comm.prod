def strip_quotes(string):
  """
      Remove leading or trailing quotes from a string
  """
  string = string.strip()
  if (string.startswith('"') or string.startswith("'")):
    string = string[1:]
  if (string.endswith('"') or string.endswith("'")):
    string = string[:-1]
  return string


def strip_old(query):
  """
      shitty hack
  """
  strip_params = [
      "---------- Forwarded message ----------",
      "-----Original message-----",
      "wrote:",
      "________________________________________",
      'Quoting',
      '\r\n>',
      '\n>',
      'From:',
  ]
  if query is not None:
    for param in strip_params:
      query = query.split(param)[0]
    # if there is not newline at the end,
    # add it to pick up the commprod
    query += "\n"
    return query


def clean_content(query, content_type="commprod"):
  """
      remove weird email encodings
  """
  if content_type == "email":
    query = query.replace('=\r\n', '\n')
  elif content_type == "commprod":
    query = query.replace('=\r\n', '')
  query = query.replace('=92', '\'')
  query = query.replace('=93', '"')
  query = query.replace('=94', '"')
  query = query.replace('=20', '')
  return query


def get_first_text_block(msg):
  """
      Helper to read message content
  """
  for part in msg.walk():
    if part.get_content_type() == 'text/plain':
      return part.get_payload()
