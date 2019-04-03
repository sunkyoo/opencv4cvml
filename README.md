## 『OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝』 (길벗, 2019) 

[![Title](/docs/title.png)](https://sunkyoo.github.io/opencv4cvml/)

책 소개와 예제 코드, 동영상 강의 등의 자료는 [**[링크]**](https://sunkyoo.github.io/opencv4cvml/)를 참고하세요.

##

## 소스 코드 빌드 및 실행 방법

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
