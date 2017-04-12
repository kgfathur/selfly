#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int, char**)
{
	VideoCapture cap(0); // open the default camera
	cap.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	cap.set(CV_CAP_PROP_FRAME_HEIGHT, 240);

	if(!cap.isOpened())  // check if we succeeded
		return -1;

	for(;;)
	{
	    Mat frame;

	    cap >> frame;      // get a new frame from camera
	    if (frame.empty()) // skip invalid images
		 continue;

	    bool ok = imwrite("images.png", frame);
	    // we've written the image, can go home now:
	    if (ok)
		break;    
	}
	// the camera will be deinitialized automatically in VideoCapture destructor
	return 0;
}
