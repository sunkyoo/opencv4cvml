# 『OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝』

<h3>컴퓨터 비전과 머신 러닝의 원리를 이해하고 OpenCV 코딩 스킬을 제대로 익히자!</h3>

『OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝』(길벗, 2019) 책은 컴퓨터 비전과 머신 러닝 알고리즘을 소개하고, OpenCV 라이브러리를 이용하여 구현하는 방법을 설명합니다. 저자의 오랜 OpenCV 강의 경험을 바탕으로 초보자도 쉽게 이해할 수 있는 커리큘럼과 실습 예제를 제공합니다. 간단한 밝기와 명암비 조절, 필터링, 에지 검출부터 객체 검출, 영상 매칭, 필기체 숫자 인식 등 컴퓨터 비전 고급 기법까지 OpenCV를 사용하여 구현합니다. 또한 k 최근방 이웃(kNN), 서포트 벡터 머신(SVM) 등의 머신 러닝 알고리즘과 OpenCV에서 딥러닝을 활용하는 방법까지 설명합니다.

[![Title](title_contents.png)](http://www.yes24.com/Product/Goods/71829618)

* 자세한 책 소개 및 구매: [예스24](http://bit.ly/2Ufo8nv), [교보문고](http://bit.ly/2FIF0J1), [인터파크](http://bit.ly/2FSApFz), [알라딘](http://bit.ly/2U7TTPb)

## 예제 소스 코드 다운로드

* 예제 소스 코드 파일을 웹으로 확인하려면 [[View on GitHub]](https://github.com/sunkyoo/opencv4cvml) 링크를 클릭하세요.
* 예제 소스 코드 전체를 다운로드 받으려면 [[Download .zip]](https://github.com/sunkyoo/opencv4cvml/zipball/master) 또는 [[Download .tar.gz]](https://github.com/sunkyoo/opencv4cvml/tarball/master) 링크를 클릭하세요.

## 소스 코드 빌드 및 실행 방법

이 책의 예제 프로그램은 Microsoft Windows 10(64비트), Visual Studio Community 2017, OpenCV 4.0.0을 기준으로 작성되었습니다. 책 부록B "리눅스에서 OpenCV 설치하고 사용하기"는 Ubuntu 18.04.2를 기준으로 설명합니다.

* Windows & Visual Studio 2017

    ```
    * 시스템 환경 변수에 OPENCV_DIR을 OpenCV 설치 폴더로 지정하세요. (책 '2.1.2절 OpenCV 설치하기' 참조)
    * Visual Studio 2017에서 *.sln 파일을 불러온 후 [빌드] -> [솔루션 빌드] 메뉴를 선택하세요.
    * 프로그램 실행은 [디버그] -> [디버그하지 않고 시작] 메뉴를 선택하세요.
    ```

* Linux

    ```bash
    $ cd <project>
    $ cmake .
    $ make
    $ ./<project>
    ```

## 파이썬으로 구현한 예제 소스 코드

『OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝』 책은 기본적으로 C/C++ 언어를 이용하여 OpenCV 라이브러리를 사용하는 방법을 설명합니다. 그러나 최근 OpenCV를 파이썬(Python) 언어로 사용하는 분들이 크게 늘어나고 있어서, 파이썬 사용자 분들도 이 책을 충분히 활용할 수 있도록 예제 프로그램을 파이썬 언어로 새롭게 구현한 소스 코드를 제공합니다.

파이썬 소스 코드는 [[여기]](https://github.com/sunkyoo/opencv4cvml/tree/master/python)에서 확인할 수 있습니다.

## Visual Studio 2019 예제 소스 코드

2019년 6월에 출시된 Visual Studio 2019 버전 사용자를 위한 예제 프로젝트 파일과 솔루션 파일을 새롭게 제공합니다. Visual Studio 2019를 사용하는 분들은 [vs2019](https://github.com/sunkyoo/opencv4cvml/tree/master/vs2019) 하위 폴더에 있는 파일을 사용하세요.

## 동영상 강의

책에서 설명하지 않은 Visual Studio 설치 방법과 일부 책 내용에 대한 동영상 강의를 제공합니다.

* [준비사항] Visual Studio 2017 설치하기 [![Youtube](youtube_icon.png)](https://youtu.be/jzVNiMeVcvs) [[동영상]](https://youtu.be/jzVNiMeVcvs){:target="_blank"}
* [준비사항] Visual Studio 2017 다운로드 방법 (2019년 6월 기준) [![Youtube](youtube_icon.png)](https://youtu.be/SRzKtZBMIIY) [[동영상]](https://youtu.be/SRzKtZBMIIY){:target="_blank"}
* [2.1.2] OpenCV 설치하기 [![Youtube](youtube_icon.png)](https://youtu.be/HxDfGHwDSmc) [[동영상]](https://youtu.be/HxDfGHwDSmc){:target="_blank"}
* [2.2.1] OpenCV 프로젝트 만들기 [![Youtube](youtube_icon.png)](https://youtu.be/fKWQIPwNsc8) [[동영상]](https://youtu.be/fKWQIPwNsc8){:target="_blank"}
* [2.2.2] 영상을 화면에 출력하기 [![Youtube](youtube_icon.png)](https://youtu.be/gcgScMU0XWE) [[동영상]](https://youtu.be/gcgScMU0XWE){:target="_blank"}
* [5.1.4] 트랙바를 이용한 영상의 밝기 조절 [![Youtube](youtube_icon.png)](https://youtu.be/znXuTOLs-4c) [[동영상]](https://youtu.be/znXuTOLs-4c){:target="_blank"}
* [16.2] 딥러닝 학습과 OpenCV 실행 [![Youtube](youtube_icon.png)](https://youtu.be/4FLAp9nXlyo) [[동영상]](https://youtu.be/4FLAp9nXlyo){:target="_blank"}
* [16.3] OpenCV와 딥러닝 활용 [![Youtube](youtube_icon.png)](https://youtu.be/DteTXf4_pcA) [[동영상]](https://youtu.be/DteTXf4_pcA){:target="_blank"}
* [부록A] OpenCV 소스 코드 빌드하여 설치하기 [![Youtube](youtube_icon.png)](https://youtu.be/ac75cFPYlOQ) [[동영상]](https://youtu.be/ac75cFPYlOQ){:target="_blank"}
* [부록B] 리눅스에서 OpenCV 설치하고 사용하기 [![Youtube](youtube_icon.png)](https://youtu.be/3RcQf0hJdFM) [[동영상]](https://youtu.be/3RcQf0hJdFM){:target="_blank"} / [[문서]](OpenCV4Linux.md){:target="_blank"}

OpenCV 프로그램 개발을 위해 필요한 몇몇 C++ 문법 동영상 강의도 제공합니다.

* 연산자 오버로딩 [![Youtube](youtube_icon.png)](https://youtu.be/vOxIJLGl_xo) [[동영상]](https://youtu.be/vOxIJLGl_xo){:target="_blank"}
* std::vector 클래스 [![Youtube](youtube_icon.png)](https://youtu.be/6Qba8vfg2AI) [[동영상]](https://youtu.be/6Qba8vfg2AI){:target="_blank"}
* 범위 기반 for [![Youtube](youtube_icon.png)](https://youtu.be/M3BBJTfWkgM) [[동영상]](https://youtu.be/M3BBJTfWkgM){:target="_blank"}
* std::sort() 함수 [![Youtube](youtube_icon.png)](https://youtu.be/9j4y1EhsOf0) [[동영상]](https://youtu.be/9j4y1EhsOf0){:target="_blank"}
* 람다 표현식 [![Youtube](youtube_icon.png)](https://youtu.be/faKvuQFBHE4) [[동영상]](https://youtu.be/faKvuQFBHE4){:target="_blank"}
* 스마트 포인터 [![Youtube](youtube_icon.png)](https://youtu.be/-tb-LQeiSKA) [[동영상]](https://youtu.be/-tb-LQeiSKA){:target="_blank"}

## 오프라인 강의

『OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝』 책은 패스트캠퍼스에서 진행 중인 [[OpenCV로 배우는 컴퓨터 비전 프로그래밍]](https://www.fastcampus.co.kr/dev_camp_cvocv/){:target="_blank"} 강의 내용을 기반으로 출간되었습니다. 오프라인 강의에서는 이 책에서 설명하는 내용과 더불어 실무에서 OpenCV를 사용하기 위해 필요한 기법을 추가적으로 다루고 있습니다. 패스트캠퍼스 강의는 [[링크]](https://www.fastcampus.co.kr/dev_camp_cvocv/){:target="_blank"}를 참고하세요.

## 오탈자 (Errata)

오탈자 목록은 추후 [[길벗]](https://www.gilbut.co.kr/book/view?bookcode=BN002402){:target="_blank"} 출판사에서 확인할 수 있습니다.
