# MyHandy: 가사 도우미 로봇

### 현대인을 위한 아침 루틴 자동화 및 정서적 지원 로봇 프로젝트
- 프로젝트 기간: 2025년 진행  
- 주요 역할: Web + Manipulator Control, Robot Control & Code Integration (**기여도 60%**)

<br>

## 🎥 프로젝트 소개  
[![MyHandy Demo](https://img.youtube.com/vi/dJ__a5zE24s/0.jpg)](https://youtu.be/dJ__a5zE24s)
➡ 영상 클릭 시, YouTube 재생  

**MyHandy**는 바쁜 현대인을 위해 아침 루틴을 자동화하고, **TTS 대화**를 통해 정서적 지원을 제공하여 우울증과 번아웃 완화를 목표로 하는 가사 보조 로봇 시스템입니다.  

- **Doosan 협동로봇**을 활용한 정밀한 작업 수행  
- **Flask 기반 웹 UI**를 통한 사용자 친화적 인터페이스  
- **ROS2 기반** 안정적인 로봇 제어 아키텍처  
- **TTS (Text-to-Speech)** 기반 정서적 상호작용  

<br>

## 🔧 주요 기능
- 🤖 **아침 루틴 자동화**: 사용자가 웹 UI에서 작업을 선택하면, 로봇이 맞춤형 쉐이크 제조, 책/옷 꺼내기 등 아침 준비를 돕습니다.  
- 💬 **정서적 지원 (TTS)**: “오늘 하루도 화이팅입니다!” 같은 메시지로 사용자에게 위로와 동기 부여를 제공합니다.  
- 🖥️ **웹 UI 모니터링**: 로봇 작업 공간을 실시간 모니터링하고, 기능 선택 및 상태 로그 확인 가능  
- 🥤 **맞춤형 서비스 제공**:  
  - **쉐이크 제조**: 사용자의 선택에 따라 딸기, 블루베리, 딸기+블루베리 혼합 쉐이크를 제공합니다.  
  - **책 꺼내기**: 책장에 책이 꽉 차 있을 때와 헐렁하게 꽂혀 있을 때 각각 다른 방식으로 안전하게 책을 꺼냅니다.  
  - **옷 꺼내기**: 사용자가 선택한 옷을 집어 꺼내는 단일 기능 제공  

<br>

## 🚀 전체 실행 순서

시스템 구동을 위해 아래 명령어들을 각 터미널에서 순차적으로 실행해 주세요.

✅ **(1) Doosan 로봇 Bringup (실로봇 모드)**
```bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py \
  mode:=real host:=192.168.1.100 port:=12345 model:=m0609
```

✅ **(2) 로봇팔 제어 서버 실행**
```bash
ros2 run rokey ros2_server
```
* 실행 파일 위치: `src/DoosanBootcamInt1/dsr_rokey/rokey/rokey/basic/ros2_server.py`

✅ **(3) 웹 UI 및 서비스 클라이언트 실행**
```bash
ros2 run ros2_service ros2_client
```
* 실행 파일 위치: `src/ros2_service/ros2_service`

⚠️ **중요 사항**  
한 번 시나리오를 실행한 뒤, 다음 시나리오를 실행하려면 **(2)번 ros2_server**와 **(3)번 ros2_client**를 종료한 뒤 다시 실행해야 합니다.
