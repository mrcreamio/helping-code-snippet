import cv2
def point_reader(img_path):
    """
    This function helps to mark the points on the image and return the coordinates of the points
    
    input: image path
    return: list of coordinates of the points
    """
    
    # Create a list to store the points
    points = []
    
    
    img = cv2.imread(img_path)
    
    # To draw gird on image
    # GRID_SIZE = 20
    # height, width, channels = img.shape
    # for x in range(0, width -1, GRID_SIZE):
    #     cv2.line(img, (x, 0), (x, height), (255, 0, 0), 1, 1)
    #     cv2.line(img, (0, x), (width, x), (255, 0, 0), 1, 1)
    
    
    # Create a function to be called when the user clicks on the image
    def click(event, x, y, flags, param):
        
        # If the user left clicks, add the coordinates to the list
        if event == cv2.EVENT_LBUTTONDOWN: 
            points.append((x, y))
            # Draw a circle on the image at the point
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            
    cv2.namedWindow('image')
    # Call the function when the user clicks on the image
    cv2.setMouseCallback('image', click)
    # Display the image
    while(1):
        cv2.imshow('image', img)
        # close the window if the use press escape key or quits
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
            
    # Wait for the user to close the image
    # Close the image
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    return points


# pts = point_reader("Rubiks-Cube-1.jpeg")
# print(pts, len(pts))
