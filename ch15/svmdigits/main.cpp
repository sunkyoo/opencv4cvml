#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace cv::ml;
using namespace std;

Ptr<SVM> train_hog_svm(const HOGDescriptor& hog);
void on_mouse(int event, int x, int y, int flags, void* userdata);

int main()
{
#if _DEBUG
	cout << "svmdigit.exe should be built as Relase mode!" << endl;
	return 0;
#endif

	HOGDescriptor hog(Size(20, 20), Size(10, 10), Size(5, 5), Size(5, 5), 9);

	Ptr<SVM> svm = train_hog_svm(hog);

	if (svm.empty()) {
		cerr << "Training failed!" << endl;
		return -1;
	}

	Mat img = Mat::zeros(400, 400, CV_8U);

	imshow("img", img);
	setMouseCallback("img", on_mouse, (void*)&img);

	while (true) {
		int c = waitKey();

		if (c == 27) {
			break;
		} else if (c == ' ') {
			Mat img_resize;
			resize(img, img_resize, Size(20, 20), 0, 0, INTER_AREA);

			vector<float> desc;
			hog.compute(img_resize, desc);

			Mat desc_mat(desc);
			int res = cvRound(svm->predict(desc_mat.t()));
			cout << res << endl;

			img.setTo(0);
			imshow("img", img);
		}
	}

	return 0;
}

Ptr<SVM> train_hog_svm(const HOGDescriptor& hog)
{
	Mat digits = imread("digits.png", IMREAD_GRAYSCALE);

	if (digits.empty()) {
		cerr << "Image load failed!" << endl;
		return 0;
	}

	Mat train_hog, train_labels;

	for (int j = 0; j < 50; j++) {
		for (int i = 0; i < 100; i++) {
			Mat roi = digits(Rect(i * 20, j * 20, 20, 20));

			vector<float> desc;
			hog.compute(roi, desc);

			Mat desc_mat(desc);
			train_hog.push_back(desc_mat.t());
			train_labels.push_back(j / 5);
		}
	}

	Ptr<SVM> svm = SVM::create();
	svm->setType(SVM::Types::C_SVC);
	svm->setKernel(SVM::KernelTypes::RBF);
	svm->setC(2.5);
	svm->setGamma(0.50625);
	svm->train(train_hog, ROW_SAMPLE, train_labels);

	return svm;
}

Point ptPrev(-1, -1);

void on_mouse(int event, int x, int y, int flags, void* userdata)
{
	Mat img = *(Mat*)userdata;

	if (event == EVENT_LBUTTONDOWN)
		ptPrev = Point(x, y);
	else if (event == EVENT_LBUTTONUP)
		ptPrev = Point(-1, -1);
	else if (event == EVENT_MOUSEMOVE && (flags & EVENT_FLAG_LBUTTON))
	{
		line(img, ptPrev, Point(x, y), Scalar::all(255), 40, LINE_AA, 0);
		ptPrev = Point(x, y);

		imshow("img", img);
	}
}