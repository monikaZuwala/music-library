#def import_album():
filename = '/home/monika/python/text_albums_data.txt'
with open(filename, 'r') as f:
    albums_from_file = f.readlines()  

    albums = [list(album.rstrip().split(',')) for album in albums_from_file]

#def view():
for album in albums:
    print(album)
    print('-' * 70)
    print('   Artist name   |          Album name          |Release year|      Genre      |Length')
    print('-' * 70)


#def main():
    #import_album()
    #view()

#main()