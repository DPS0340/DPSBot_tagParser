# DPSBot_tagParser
태그에 있는 스크립트를 파싱해서 실행하는 코드입니다.

디피스크립트 설명
디피스크립트는 파이썬으로 이루어진 파서를 이용해서 실행되는 스크립트입니다.
디피 maketag 제목 내용을 이용해서 태그를 만들고, 디피 t제목을 이용해서 사용할 수 있습니다.

문법 설명
단순한 텍스트를 제외하고 모든 명령어는 () 괄호를 이용합니다.
괄호 안의 첫번째 인자가 명령어입니다.
실행 순서는 기초적으로 왼쪽에서 오른쪽으로 읽되, 괄호 속에 있는 괄호를 먼저 계산합니다.

명령어 설명
사칙연산은 기본적으로 지원합니다.
+= -= *= /= 명령어는 첫 인자인 명령어를 제외한 첫 인자를 첫 인자와 두번째 인자를 계산한 값으로 다시 정의합니다.
randchoice는 명령어를 제외한 모든 인자중에 하나를 고릅니다.
string은 randchoice 함수 안에 있는 string의 문자열을 하나로 취급합니다.
range는 시작값과 종료값까지 있는 모든 숫자를 띄어쓰기와 함께 반환합니다.
if A equal B do C or D 문은 생각하시는 것과 같이 A가 B면 C를 실행하고, 같지 않으면 D를 실행합니다.

변수/함수 설명
디피스크립트에서는 변수와 함수를 같은 명령어를 이용해서 정의합니다.
(declare 이름 내용)을 이용해서 변수/함수를 선언할 수 있으며, (use 이름)을 사용해서 변수/함수를 사용할 수 있습니다.
declare 문에 있는 내용이 함수라면 use문에서 실행됩니다.
같은 이름으로 declare 문을 재사용하면 재정의됩니다.
ex) (declare k 1) (declare num (+= k 1)) (declare k 5) (use num)의 결과는 6입니다.

마지막으로 드릴 말씀
일주일동안 나름대로 공들여서 만들었습니다.
부디 잘 써주세요!
