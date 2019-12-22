def pageforQuran():
  print("""Usage: Choose a number between 1-30 to get the page.
       For exit this programe press 'q'. """)

  part = []
  while part != 'q':
    part = (input('Write a number of part: '))
    if part < 1 or part > 30:
      print('Number must be 1-30')
      continue
    else:
      n = 2 * (part - 1)
      page = str(n) + '2'
      print('Start on page:{}'.format(page))
      continue
  else:
    print('Assalamo Alikom!')


pageforQuran()
