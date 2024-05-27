import time
import csv

time.sleep(5)
csv.writer("데이터저장")

# 우리가 그럼 객체를 통해서 데이터를 생성해서, 이걸 다시 파일로 저장해서, 나중에 이걸 다시 로딩할수 있나요?

# 1. 객체를 통해서 데이터를 생성한다
users = DetaGenerator().generate()

# 2. 내가 기록할 파일을 생성한다
csv_writer = csv.DataWriter('users.csv')

# 3. 내가 기록할 파일을 열고 생성할 데이터를 해당 팡리에 출력한다.
csv_writer.write(users)

#------------------------------

# 4. csv파일에 있는 사용자 데이터를 읽어온다
users = csv_reader.read('user.csv')

# 5. 주문 데이터를 생성할때 사용자id 를 참조한다
user_id = users.get_user_id(users)

# 6. 주문 데이터를 100개 생성한다.
order = DataGenerator(100)
order.generate_order(user_id)
