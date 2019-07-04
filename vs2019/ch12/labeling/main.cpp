#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void labeling_basic();
void labeling_stats();

int main()
{
	labeling_basic();
	labeling_stats();

	return 0;
}

void labeling_basic()
{
	uchar data[] = {
		0, 0, 1, 1, 0, 0, 0, 0,
		1, 1, 1, 1, 0, 0, 1, 0,
		1, 1, 1, 1, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 1, 1, 0,
		0, 0, 0, 1, 1, 1, 1, 0,
		0, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 1, 1, 1, 1, 0,
		0, 0, 0, 0, 0, 0, 0, 0,
	};

	Mat src = Mat(8, 8, CV_8UC1, data) * 255;

	Mat labels;
	int cnt = connectedComponents(src, labels);

	cout << "src:\n" << src << endl;
	cout << "labels:\n" << labels << endl;
	cout << "number of labels: " << cnt << endl;
}

void labeling_stats()
{
	Mat src = imread("keyboard.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat bin;
	threshold(src, bin, 0, 255, THRESH_BINARY | THRESH_OTSU);

	Mat labels, stats, centroids;
	int cnt = connectedComponentsWithStats(bin, labels, stats, centroids);

	Mat dst;
	cvtColor(src, dst, COLOR_GRAY2BGR);

	for (int i = 1; i < cnt; i++) {
		int* p = stats.ptr<int>(i);
		
		if (p[4] < 20) continue;

		rectangle(dst, Rect(p[0], p[1], p[2], p[3]), Scalar(0, 255, 255));
	}


	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}