from numpy.numarray import random_array

display = [ {"VGA" : (640, 480)} \
          , {"SVGA" : (800, 600)} \
          , {"XGA" : (1024, 768)} \
          , {"XGA+" : (1152, 864)} \
          , {"WXGA" : (1280, 800)} \
          , {"SXGA" : (1280, 960)} \
          , {"HD" : (1366, 768)} \
          , {"WSXGA" : (1440, 900)} \
          , {"HD+" : (1600, 900)} \
#          , {"UXGA" : (1600, 1200)} \
#          , {"WSXGA+" : (1680, 1050)} \
#          , {"HD-1080" : (1920, 1080)} \
#          , {"WUXGA" : (1920, 1200)} \
          ]

def generate_dataset(width, height, depth):
    dat = random_array.random([height, width, depth])
    return dat

def popular_resolution():
    for resolute in display:
        name, resolution = resolute.items()[0]
        width = resolution[0]
        height = resolution[1]
        element = width * height
        print name + " : " + resolution.__str__() + " resolution\n"
        dst = cv.CreateImageHeader((width, height), 8, 3)
        cv.SetData(dst, generate_dataset(width, height, 3))
        yield dst 

if __name__ == '__main__':
    main()



