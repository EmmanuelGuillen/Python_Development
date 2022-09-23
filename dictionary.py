#        Dictionary = a changeable, unordered collection of unique key: Value pairs
#        Fast because they use hashing, allows us to access a value qucikly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

#print(capitals['Russia'])

## used to set if key is in dictionary
#print(capitals.get('Germany'))

## What keys we have
#print(capitals.keys())

## What values we have
#print(capitals.values())

## To print everything in dictionary
#print(capitals.items())

#for key,values in capitals.items():
#    print(key, values)

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
#capitals.pop('China')          REMOVES SPECIFIC KEY
#capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany'))

