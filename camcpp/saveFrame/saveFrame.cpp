#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"
 
using namespace cv;
using namespace std;
 
int main( )
{
	Mat src = imread("filename.jpg",CV_LOAD_IMAGE_COLOR); //load  image

	Mat bgr[3];   //destination array
	split(src,bgr);//split source  

	//Note: OpenCV uses BGR color order
	imwrite("blue.jpg",bgr[0]); //blue channel
	imwrite("green.jpg",bgr[1]); //green channel
	imwrite("red.jpg",bgr[2]); //red channel
}
