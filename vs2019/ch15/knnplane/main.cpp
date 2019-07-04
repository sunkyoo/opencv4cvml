#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace cv::ml;
using namespace std;

Mat img;
Mat train, label;
Ptr<KNearest> knn;
int k_value = 1;

void on_k_changed(int, void*);
void addPoint(const Point& pt, int cls);
void trainAndDisplay();

int main(void)
{
	img = Mat::zeros(Size(500, 500), CV_8UC3);
	knn = KNearest::create();

	namedWindow("knn");
	createTrackbar("k", "knn", &k_value, 5, on_k_changed);

	const int NUM = 30;
	Mat rn(NUM, 2, CV_32SC1);

	randn(rn, 0, 50);
	for (int i = 0; i < NUM; i++)
		addPoint(Point(rn.at<int>(i, 0) + 150, rn.at<int>(i, 1) + 150), 0);

	randn(rn, 0, 50);
	for (int i = 0; i < NUM; i++)
		addPoint(Point(rn.at<int>(i, 0) + 350, rn.at<int>(i, 1) + 150), 1);

	randn(rn, 0, 70); 
	for (int i = 0; i < NUM; i++) 
		addPoint(Point(rn.at<int>(i, 0) + 250, rn.at<int>(i, 1) + 400), 2);

	trainAndDisplay();

	waitKey();
	return 0;
}

void on_k_changed(int, void*)
{
	if (k_value < 1) k_value = 1;
	trainAndDisplay();
}

void addPoint(const Point& pt, int cls)
{
	Mat new_sample = (Mat_<float>(1, 2) << pt.x, pt.y);
	train.push_back(new_sample);

	Mat new_label = (Mat_<int>(1, 1) << cls);
	label.push_back(new_label);
}

void trainAndDisplay()
{
	knn->train(train, ROW_SAMPLE, label);

	for (int i = 0; i < img.rows; ++i) {
		for (int j = 0; j < img.cols; ++j) {
			Mat sample = (Mat_<float>(1, 2) << j, i);

			Mat res;
			knn->findNearest(sample, k_value, res);

			int response = cvRound(res.at<float>(0, 0));
			if (response == 0)
				img.at<Vec3b>(i, j) = Vec3b(128, 128, 255); // R
			else if (response == 1)
				img.at<Vec3b>(i, j) = Vec3b(128, 255, 128); // G
			else if (response == 2)
				img.at<Vec3b>(i, j) = Vec3b(255, 128, 128); // B
		}
	}

	for (int i = 0; i < train.rows; i++)
	{
		int x = cvRound(train.at<float>(i, 0));
		int y = cvRound(train.at<float>(i, 1));
		int l = label.at<int>(i, 0);

		if (l == 0)
			circle(img, Point(x, y), 5, Scalar(0, 0, 128), -1, LINE_AA);
		else if (l == 1)
			circle(img, Point(x, y), 5, Scalar(0, 128, 0), -1, LINE_AA);
		else if (l == 2)
			circle(img, Point(x, y), 5, Scalar(128, 0, 0), -1, LINE_AA);
	}

	imshow("knn", img);
}