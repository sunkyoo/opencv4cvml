# Ubuntu 18.04에서 OpenCV 4.0.0 설치하기

최신 우분투(Ubuntu) 18.04.2 버전에서 OpenCV 라이브러리를 설치하는 방법을 설명합니다.

## OpenCV 소스 코드 빌드에 필요한 패키지 설치하기

(Optional) 리눅스를 최신 버전 상태로 업데이트합니다.

```bash
$ sudo apt -y update
$ sudo apt -y upgrade
```

OpenCV 소스 코드 빌드에 필요한 패키지를 설치합니다.

```bash
$ sudo apt -y install build-essential cmake pkg-config
```

정지 영상 파일을 불러오거나 저장하기 위해 필요한 패키지를 설치합니다.

```bash
$ sudo apt -y install libjpeg-dev libtiff5-dev libpng-dev
```

동영상 파일 또는 카메라를 활용하기 위해 필요한 패키지를 설치합니다.

```bash
$ sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt -y install libdc1394-22-dev libxvidcore-dev libx264-dev
$ sudo apt -y install libxine2-dev libv4l-dev v4l-utils
$ sudo apt -y install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

GUI 환경에서 영상을 새 창에 띄워서 보여주기 위해 필요한 그래픽 툴킷을 설치합니다. 그래픽 툴킷은 gtk 또는 qt 등을 선택할 수 있으며, 이 책에서는 GTK 3 패키지를 사용합니다.

```bash
$ sudo apt -y install libgtk-3-dev
```

OpenCV에서 함께 사용할 최적화 관련 패키지와 Python3 개발 환경을 위한 패키지를 설치합니다.

```bash
$ sudo apt -y install libatlas-base-dev libeigen3-dev gfortran
$ sudo apt -y install python3-dev python3-numpy libtbb2 libtbb-dev
```

## OpenCV 소스 코드 다운받아 빌드하기

OpenCV 소스 코드 다운로드 및 빌드 작업은 사용자 계정 홈 디렉터리 아래에 opencv 디렉터리를 만들고, 그 아래에서 진행하겠습니다.

```bash
$ cd ~
$ mkdir opencv
$ cd opencv
```

OpenCV 4.0.0 기본 모듈 소스 코드와 추가 모듈 소스 코드를 다운로드 합니다.

```bash
$ wget -O opencv-4.0.0.zip https://github.com/opencv/opencv/archive/4.0.0.zip
$ wget -O opencv_contrib-4.0.0.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
```

다운로드 받은 소스 코드 압축 파일의 압축을 해제합니다.

```bash
$ unzip opencv-4.0.0.zip
$ unzip opencv_contrib-4.0.0.zip
```

OpenCV 빌드 작업은 ~/opencv 디렉터리 아래에 build 디렉터리를 새로 만들고, 그 안에서 진행하겠습니다.

```bash
$ mkdir build
$ cd build
```

CMake 유틸리티를 이용하여 OpenCV 빌드에 필요한 Makefile 파일을 생성합니다.

```bash
$ cmake \
-D CMAKE_BUILD_TYPE=Release \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_EXAMPLES=ON \
-D BUILD_opencv_python3=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.0.0/modules \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D WITH_TBB=ON \
../opencv-4.0.0/
```

cmake 명령을 실행하고 약간의 시간이 흐르면 다음과 같은 메시지가 출력되는 것을 확인할 수 있습니다. 아래 메시지가 나타나면 현재 폴더에 Makefile 파일이 생성됩니다.

```
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sunkyoo/opencv/build
```

빌드 작업은 make 명령으로 실행할 수 있으며, 이때 사용하고 있는 컴퓨터의 CPU 코어 개수에 맞게 병렬 작업을 수행할 수 있습니다. 현재 컴퓨터의 CPU 코어 개수는 nproc 명령으로 확인할 수 있습니다

```bash
$ nproc
```

앞의 명령을 수행하여 콘솔 창에 나타나는 숫자를 기억하였다가 다음 명령어에서 -j 뒤에 숫자 4 대신 입력하세요. make 명령에서 -j 옵션은 병렬로 처리할 작업(job) 개수를 지정하는 옵션입니다.

```bash
$ make -j4
```

앞 명령을 수행하면 OpenCV 소스 코드를 빌드하여 *.so 라이브러리 파일을 생성합니다. OpenCV 빌드 작업은 컴퓨터 사양에 따라 수십 분의 시간이 소요됩니다. 에러가 발생하지 않고 빌드 작업이 완료되면 다음 두 명령을 입력하여 빌드된 *.so 파일을 시스템
에 설치합니다.

```bash
$ sudo make install
$ sudo ldconfig
```

이제 OpenCV 라이브러리를 빌드하고 설치하는 작업이 모두 완료되었습니다. 아래 명령어를 입력하였을 때 opencv4 메시지가 출력되면 정상입니다.

```
$ pkg-config --list-all | grep opencv
opencv4                        OpenCV - Open Source Computer Vision Library
```
