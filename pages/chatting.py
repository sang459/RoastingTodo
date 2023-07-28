# 채팅은 아주 비싸다. 그러니까 제한해야 한다. 월초에 한번 컨설팅받을 수 있다는 느낌. (다시 상담받으려면 돈내야함)

# streamlit 채팅 ui 활용
# langchain 사용 필요한가?

# [system]
# Instruction: You are an AI chatbot that slightly roasts the user. But you don't really "mean it": You just want the user to be better. Answer in English. 
# Situation: The user wants to set this month's goal. Help them set it, and guide them to specify it into small goals for weeks, and then smaller goals for days step by step through conversation.

# [User]
# I'm ready to set a goal for this month.

# 이렇게 대화하다가, 대골 중골 소골 확정되면 종료하고 싸인하기
# 말하면서 함께 계획표를 채워나감 (중요)
# 1. table
# 2. markdown (처리하긴 더 쉬울듯..?)

# user가 메세지 한번 보낼 때마다 state 갱신
# 그럼 input이 어마어마하게 많아지는데... 유저가 table 수정했는지 안했는지 체크하고, 안했으면 prompt에서 (same as before)로 처리
# langchain structured output chain 사용(근데 비쌈, 직접 디자인 필요) 다음 형식에 맞게 답하도록.
# input과 output 모두 아래와 같은 형태. context를 전체 history 말고 table content만 줘도 될듯? 이건 실험해봐야 함.
{'message': '', 'table_content': {'Goal of the Month': '', 'Week 1': '', 'Week 2':'', 'Week 3':'', 'Week 4':'', 'Tip': ''}}

# 


# input
# output (message, table)
# 반복...
# 확정 버튼 누르거나, 대화가 20회 이상 진행되면 강제종료 (....아쉽지만 시간이 다 됐네요. 당신같은 게으름뱅이들이 한 둘이 아니거든요. 당신이 미루는 걸 잘 하는 건 알지만, 이제 그만 미루고 확정하는 건 어때요?)

# 싸인