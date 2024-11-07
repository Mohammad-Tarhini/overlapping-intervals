def merge_intervals(intervals):
   i=0
   while i<len(intervals):
      j+=1
      while j<len(intervals):
         if intervals[i][0]<=intervals[j][0] and intervals[j][1]>=intervals[j][1]:
            intervals.pop(j)
         elif intervals[i][1]>intervals[j][0] and intervals[i][0]<intervals[j][1]:
            intervals[i][0]=min(intervals[i][0],intervals[j][0])
            intervals[i][1]=max(intervals[i][1],intervals[j][1])
            intervals.pop[j]
         else:
            j+=1
      i+=1
      
    
