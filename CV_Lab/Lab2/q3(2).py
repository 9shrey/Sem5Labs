import cv2
def resize_image(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image
def crop_image(image, x, y, width, height):
    cropped_image = image[y:y + height, x:x + width]
    return cropped_image
def main(input_image_path, output_resize_path, output_crop_path):
    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error: Unable to load image at path {input_image_path}")
        return

    new_width = 300
    new_height = 200
    resized_image = resize_image(image, new_width, new_height)

    crop_x = 50
    crop_y = 50
    crop_width = 200
    crop_height = 150
    cropped_image = crop_image(image, crop_x, crop_y, crop_width, crop_height)
    cv2.imshow(output_crop_path, cropped_image)
    cv2.imshow(output_resize_path, resized_image)
    cv2.waitKey(0)

if __name__ == "__main__":
    input_image_path = 'sample.jpeg'
    output_resize_path = 'resized_image.png'
    output_crop_path = 'cropped_image.png'
    main(input_image_path, output_resize_path, output_crop_path)
