#include "opencv2/opencv.hpp"
#include <iostream>
#include <fstream>

using namespace cv;
using namespace cv::dnn;
using namespace std;

int main(int argc, char* argv[])
{
	// Load an image

	Mat img;

	if (argc < 2)
		img = imread("space_shuttle.jpg", IMREAD_COLOR);
	else
		img = imread(argv[1], IMREAD_COLOR);

	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	// Load network

	Net net = readNet("bvlc_googlenet.caffemodel", "deploy.prototxt");

	if (net.empty()) {
		cerr << "Network load failed!" << endl;
		return -1;
	}

	// Load class names

	ifstream fp("classification_classes_ILSVRC2012.txt");

	if (!fp.is_open()) {
		cerr << "Class file load failed!" << endl;
		return -1;
	}

	vector<String> classNames;
	string name;
	while (!fp.eof()) {
		getline(fp, name);
		if (name.length())
			classNames.push_back(name);
	}

	fp.close();

	// Inference

	Mat inputBlob = blobFromImage(img, 1, Size(224, 224), Scalar(104, 117, 123));
	net.setInput(inputBlob, "data");
	Mat prob = net.forward();

	// Check results & Display

	double maxVal;
	Point maxLoc;
	minMaxLoc(prob, NULL, &maxVal, NULL, &maxLoc);

	String str = format("%s (%4.2lf%%)", classNames[maxLoc.x].c_str(), maxVal * 100);
	putText(img, str, Point(10, 30), FONT_HERSHEY_SIMPLEX, 0.8, Scalar(0, 0, 255));
	imshow("img", img);

	waitKey();
	return 0;
}