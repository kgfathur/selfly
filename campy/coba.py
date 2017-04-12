import cv2

cv2.namedWindow("w1")
camera_index = 0
capture = cv2.CaptureFromCAM(camera_index)

gx = gy = 1
grayscale = blur = canny = False

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    global gx, gy, grayscale, canny, blur
    frame = cv2.QueryFrame(capture)
    # import pdb; pdb.set_trace()

    if grayscale:
        gray = cv2.CreateImage(cv2.GetSize(frame), frame.depth, 1)
        cv2.CvtColor(frame, gray, cv2.CV_RGB2GRAY)
        frame = gray
        
    if blur:
        g = cv2.CreateImage(cv2.GetSize(frame), cv2.IPL_DEPTH_8U, frame.channels)
        cv2.Smooth(frame, g, cv2.CV_GAUSSIAN, gx, gy)
        frame = g
    
    if grayscale and canny:
        c = cv2.CreateImage(cv2.GetSize(frame), frame.depth, frame.channels)
        cv2.Canny(frame, c, 10, 100, 3)
        frame = c
    cv2.ShowImage("w1", frame)

    c = cv2.WaitKey(10)
    if c==ord('='): #in "n" key is pressed while the popup window is in focus
        gx += 2
        gy += 2
    elif c == ord('-'):
        gx = max(1, gx-2)
        gy = max(1, gy-2)
    elif c == ord('x'):
        gx += 2
    elif c == ord('X'):
        gx = max(1, gx-2)
    elif c == ord('q'):
        exit(0)

    elif c == ord('b'):
        blur = not blur
    elif c == ord('g'):
        grayscale = not grayscale
    elif c == ord('c'):
        canny = not canny
    



while True:
    repeat()
