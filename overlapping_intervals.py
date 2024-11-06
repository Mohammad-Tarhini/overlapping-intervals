#The functions merges overlapping intervals and returns a list of the merged intervals
def merge_intervals(intervals):
    for i in range(len(intervals)):
        for j in range(i,len(intervals)):
            if intervals[j][1]<intervals[i][1]  :
                if intervals[j][0]>intervals[i][0]:
                    intervals.pop(j)
                elif intervals[j][0]>intervals[i][0]  and intervals[j][1]>intervals[i][0]:
                    intervals[i][0]=intervals[j][0]
                    intervals.pop(j)
            elif intervals[j][0]>intervals[i][0] and intervals[j][0]<intervals[i][1]:
                if intervals[i][1]<intervals[j][1]:
                    intervals[i][1]=intervals[j][1]
                    intervals.pop(j)
            elif intervals[i][0]>intervals[j][0] and intervals[i][1]<intervals[j][1]:
                intervals.pop(j)
    return intervals

intervals=[[1,3],[2,4],[6,8]]
m=merge_intervals(intervals)
print(m)




                

        
