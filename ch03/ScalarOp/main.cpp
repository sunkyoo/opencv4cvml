#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void VecOp();
void ScalarOp();

int main(void)
{
	VecOp();
	ScalarOp();

	return 0;
}

void VecOp()
{
	Vec3b p1, p2(0, 0, 255);
	p1[0] = 100;
	cout << "p1: " << p1 << endl;
	cout << "p2: " << p2 << endl;
}

void ScalarOp()
{
	Scalar gray = 128;
	cout << "gray: " << gray << endl;

	Scalar yellow(0, 255, 255);
	cout << "yellow: " << yellow << endl;

	Mat img1(256, 256, CV_8UC3, yellow);

	for (int i = 0; i < 4; i++)
		cout << yellow.val[i] << ", " << yellow[i] << endl;
}
