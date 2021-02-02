T = int(input()) # 학기의 수

sum_class = []
avg_score = []
semester = []
N_list = []
for i in range(T):
    N = int(input()) # 과목의 수
    N_list.append(N)
    class_list = [] # 학점 리스트
    score_list = [] # 성적 리스트
    for j in range(N):
        C, G = input().split() # 학점, 성적
        C = int(C)
        G = float(G)
        class_list.append(C)
        score_list.append(G*C)
    sum_class.append(sum(class_list))
    avg_score.append(sum(score_list)/sum_class[-1])

for k in range(T):
    print(sum_class[k], round(avg_score[k],1))