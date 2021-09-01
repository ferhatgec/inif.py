with open('example.ini', 'r') as file:
    import inif

    data = ''

    for line in file:
        data += f'{line}\n'

    val = inif.inif()
    val.parse(data)
    print(val.get('name', 'name'),
          val.get('projects', 'test'),
          val.get('not', 'found'), sep='\n')
