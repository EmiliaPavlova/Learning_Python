first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())
sum_all = first_competitor + second_competitor + third_competitor
minutes = int(sum_all / 60)
print('{0}:{1:02}'.format(minutes, sum_all % 60))
