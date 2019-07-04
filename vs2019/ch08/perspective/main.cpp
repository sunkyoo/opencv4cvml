#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

Mat src;
Point2f srcPts[4], dstPts[4];

void on_mouse(int event, int x, int y, int flags, void* userdata);

int main()
{
	src = imread("card.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	namedWindow("src");
	setMouseCallback("src", on_mouse);

	imshow("src", src);
	waitKey();

	return 0;
}

void on_mouse(int event, int x, int y, int flags, void*)
{
	static int cnt = 0;

	if (event == EVENT_LBUTTONDOWN) {
		if (cnt < 4) {
			srcPts[cnt++] = Point2f(x, y);

			circle(src, Point(x, y), 5, Scalar(0, 0, 255), -1);
			imshow("src", src);

			if (cnt == 4) {
				int w = 200, h = 300;

				dstPts[0] = Point2f(0, 0);
				dstPts[1] = Point2f(w - 1, 0);
				dstPts[2] = Point2f(w - 1, h - 1);
				dstPts[3] = Point2f(0, h - 1);

				Mat pers = getPerspectiveTransform(srcPts, dstPts);

				Mat dst;
				warpPerspective(src, dst, pers, Size(w, h));

				imshow("dst", dst);
			}
		}
	}
}