import os

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img, img_to_array  # , array_to_img

from labeler_site.settings import BASE_DIR


# datagen = ImageDataGenerator(
#         rotation_range=40,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest')


datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')


image_path = os.path.join(BASE_DIR, *('user_uploads images HUNT0133.jpg'.split()))
img = load_img(image_path)  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
preview_path = os.path.join(BASE_DIR, *('user_uploads images preview'.split()))
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=preview_path, save_prefix='HUNT0133', save_format='jpeg'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely
