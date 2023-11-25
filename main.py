import cv2

def roundlogoEdges(logo_image, kernet_size, kernel_type):
    # Load the image
    image = cv2.imread(logo_image, cv2.IMREAD_COLOR)
    # Define a circular kernel for dilation
    kernel = cv2.getStructuringElement(kernel_type, (kernet_size, kernet_size))
    Final_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE,
                     kernel, iterations=2)
    # Final_image = cv2.GaussianBlur(Final_image, (3,3), 0)
    # Display the modified image
    cv2.imshow('Rounded Logo', Final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the modified image
    cv2.imwrite('resultImg.png', Final_image)

    return Final_image

result = roundlogoEdges(logo_image="logo.png", kernel_type=cv2.MORPH_ELLIPSE, kernet_size=3)

