def every_nth(items, nth):
  results = []
  for index, value in enumerate(items):
    if index % nth == 0:
      results.append(value)
  return results

# Starting from the 2nd element
def every_nth2(items, nth):
  results = []
  for index, value in enumerate(items):
    if index % nth == 0:
      results.append(items[index + 1])
  return results