from flask import Flask, render_template, request, jsonify
import rclpy
from rclpy.node import Node
from button_interface.srv import SendButtons
import threading
import os

ROBOT_ID = "dsr01"
app = Flask(__name__, template_folder='/home/rokey/ros2_ws/src/ros2_service/ros2_service/templates',
            static_folder='/home/rokey/ros2_ws/src/ros2_service/ros2_service/static')
logs = []
response_text = ''

response_map = {
    "1": "① 쉐이크를 제조중 입니다..",
    "2": "② 쉐이크를 제조중 입니다..",
    "3": "③ 책을 꺼냅니다.",
    "4": "④ 오늘 입을 옷 입니다.",
    # "5": "⑤ 주변 정리를 시작합니다.."
}

# 버튼별 응답 메시지

# def send_to_ros(button_list):
#     client = ButtonClient()
#     success, message = client.send_buttons(button_list)
#     return success, message

@app.route('/')
def index():
    return render_template('index.html', logs=logs)

# ROS2 연동 함수 (여기에서 실제 서비스 호출 가능)
def send_to_log(selected_buttons):
    messages = []
    for btn in selected_buttons:
        print(btn)
        msg = response_map.get(btn, f"버튼 {btn}은(는) 정의되지 않았습니다.")
        messages.append(msg)
    return messages

@app.route('/submit', methods=['POST'])
def submit():
    global response_text
    selected = request.json.get('selected', [])
    # if not selected:
    #     selected = ['1']  # 1번이 자동 선택됨
    response_text = selected
    responses = send_to_log(selected)
    logs.extend(responses)
    # logs.append(f"[전송됨] {selected} -> [응답] {response_text}")
    return jsonify({'logs': logs})

def flask_thread():
    app.run(host='127.0.0.1', port=5000)

class ButtonClient(Node):
    def __init__(self):
        super().__init__('button_client',namespace=ROBOT_ID)
        self.cli = self.create_client(SendButtons, 'button_command')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('⏳ 서비스 대기 중...')

        self.req = SendButtons.Request()
        # self.send_buttons(response_text)

    def send_buttons(self, button_list):
        print("send buttons function start")
        self.req.buttons = button_list
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'응답: {future.result().message}')
            return True, future.result().message
        else:
            self.get_logger().error('응답 실패')
            return False, '서비스 응답 실패'

   


def main():
    rclpy.init()
    global response_text
    node = ButtonClient()
    print("hi")
    threading.Thread(target=flask_thread, daemon=True).start()
    while True:
        try:
            if response_text != '':
                node.send_buttons(response_text)
                rclpy.spin_once(node)
                response_text =''
        except KeyboardInterrupt:
            rclpy.shutdown()


if __name__ == '__main__':
    main()
