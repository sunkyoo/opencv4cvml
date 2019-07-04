#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void template_matching();

int main()
{
	template_matching();

	return 0;
}

void template_matching()
{
	Mat img = imread("circuit.bmp", IMREAD_COLOR);
	Mat templ = imread("crystal.bmp", IMREAD_COLOR);

	if (img.empty() || templ.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	img = img + Scalar(50, 50, 50);

	Mat noise(img.size(), CV_32SC3);
	randn(noise, 0, 10);
	add(img, noise, img, Mat(), CV_8UC3);

	Mat res, res_norm;
	matchTemplate(img, templ, res, TM_CCOEFF_NORMED);
	normalize(res, res_norm, 0, 255, NORM_MINMAX, CV_8U);

	double maxv;
	Point maxloc;
	minMaxLoc(res, 0, &maxv, 0, &maxloc);
	cout << "maxv: " << maxv << endl;

	rectangle(img, Rect(maxloc.x, maxloc.y, templ.cols, templ.rows), Scalar(0, 0, 255), 2);

	imshow("templ", templ);
	imshow("res_norm", res_norm);
	imshow("img", img);

	waitKey();
	destroyAllWindows();
}
