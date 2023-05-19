import os, cv2

path = 'Images/'

images = []
 
for i in os.listdir(path):
    name, ext = os.path.splitext(i)

    if ext in ['.gif', '.png', '.jpg', '.jfif']:
        file_name = path + '/' + i

        print(file_name)
        images.append(file_name)
    
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width, height)

out = cv2.VideoWriter('projet.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for o in range(0, count):
    print(images[o])
    frame = cv2.imread(images[o])
    out.write(frame)

out.release()
print('finished')

