# DEEP LEARNING FOR COMPUTER VISION

## install
windwos 에서 tensorflow를 설치하기 위해서는 anaconda를 설치해야 함.

0. anaconda 설치 : https://www.anaconda.com/
1. python : https://www.python.org
2. python libraries
```
pip3 install numpy scipy scikit-learn pillow h5py
```
3. opencv : https://opencv.org/releases/
4. tensorflow
```
pip3 install tensorflow
```

## configuration

### Jupyter notebook 홈 디렉토리 변경

andconda prompt 실행후 configuration 파일 생성

```
(base) C:\Users\XXXXXX>jupyter notebook --generate-config
Writing default config to: C:\Users\XXXXX\.jupyter\jupyter_notebook_config.py
```

`jupyter_notebook_config.py` 파일에서 'c.NotebookApp.notebook_dir' 변수의 주석을 제거하고 홈디렉토리 경로 지증

```
c.NotebookApp.notebook_dir = 'C:\workspace\_Jupyter'
```


### tensorboard 실행


```python
summary_writer = tf.summary.FileWriter('./tmp/1',session.graph)
"""
실행결과
<tensorflow.python.summary.writer.writer.FileWriter at 0x2074aa39848>
"""
```

```
tensorboard --logdir=./tmp/1
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.0.0 at http://localhost:6006/ (Press CTRL+C to quit)
```

## Tips


### tensorflow 1.14 설치


아래와 같이 `input_data.read_data_sets("MNIST_data/", one_hot=True)` 가 정상동작하지 않고 `No module named 'tensorflow.examples.tutorials'` 에러가 나올 경우 Tensorflow 1.14.0을 설치한다. (python 3.7.4 일 경우이며, Python 버전에 맞는 tensorflow 설치 필요.)

> MNIST 데이터를 다운로드 한다. from tensorflow.examples.tutorials.mnist import input_data mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
> ImportError: No module named 'tensorflow.examples.tutorials'

```
pip install tensorflow==1.14.0 --user
```

출처: https://steadyandslow.tistory.com/128 [더디지만... 꾸준히...]


### tensorflow v1.x API 사용
tensorflow v1.x 사용을 위해서는 아래와 같이 코드를 추가해준다.

```python
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
print(tf.VERSION)
print(tf.version)

"""
실행결과 (jupyterlab)
2.0.0
<module 'tensorflow_core.compat.v1.version' from 'C:\\Users\\SuhyunKim\\Anaconda3\\lib\\site-packages\\tensorflow_core\\_api\\v2\\compat\\v1\\version\\__init__.py'>
"""
```



### jupyter notebook 단축키

### 주요단축키 (Command 모드)



|**단축키**|**설명**|
|---|---|
|`[a]`|위로 셀 추가|
|`[b]`|아래로 셀 추가|
|`[d][d]`|(d를 두번 누름) 선택 셀 삭제|
|`[x]`|선택 셀 잘라내기 (삭제로 써도 무방)|
|`[c]`|선택 셀 복사하기 |
|`[p]`|선택 셀 아래에 붙여넣기|
|`[shift] + [m]`|선택 셀과 아래 셀과 합치기|
|`[o]`|실행결과 열기/닫기|
|`[m]`|Markdown으로 변경|
|`[y]`|Code로 변경|
|`[ctrl] + [s]` 또는 `[s]`| 파일 저장|
|`[enter]`|선택 셀의 코드 입력 모드로 돌아가기|

### 주요단축키 (Edit 모드)

|**단축키**|**설명**|
|---|---|
|`[ctrl] + [a]`|선택 셀의 코드 전체 선택|
|`[ctrl] + [z]`|선택 셀 내 실행 취소|
|`[ctrl] + [y]`|선택 셀 내 다시 실행|
|`[ctrl] + [/]`|커서 위치 라인 주석처리|
|`[ctrl] + [enter]`|선택 셀 코드 실행|
|`[shift] + [enter]`|선택 셀 코드 실행 후 다음 Cell로 이동 (없으면 새로 추가)|
|`[shift] + [ctrl] + [-]`|커서 위치에서 셀 둘로 나누기|
|`[ctrl] + [s]`|파일 저장|
|`[esc]` 또는 `[ctrl] + [m]`|셀 선택 모드로 돌아가기|

출처: https://kkokkilkon.tistory.com/151 [꼬낄콘의 분석일지]
