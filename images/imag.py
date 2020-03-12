from PIL import Image


def resize_image(input_image_path,
                 output_image_path,
                 resizd_height, resizd_width):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    size = resizd_width, resizd_height
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(output_image_path)


if __name__ == '__main__':
    resize_image(input_image_path=str(input("first_name : ")),
                 output_image_path=str(input("second_name : ")),
                 resizd_height=int(input("height : ")), resizd_width=int(input("width : ")))
