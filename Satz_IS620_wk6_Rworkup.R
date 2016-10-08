library(tnet)

setwd("/Users/alexandersatz/Documents/Cuny/IS620/")
data2 <- read.csv("wk6_Matrix.csv", stringsAsFactors=TRUE)
data2 = head(data2, -1)
head(data2)

#generate person-event lists from matrix
i = 0
p = 0
count = 1
for (x in 1:nrow(data2)){
  for (y in 1:ncol(data2)){
    print(data2[x,y])
    if (data2[x,y] == 1){
      i[count] = x
      p[count] = y-1
      count = count +1
    }
      
  }       
    
}

net <- cbind(i,p)
 
#project where edges are summed.
s.t <- projecting_tm(net, method="sum")

#convert numbers to names
i = 0
for (x in 1:nrow(s.t)){
  y = s.t$i[x]
  i[x] = toString(data2$X[y])
}

s.t$i = i


j = 0
for (x in 1:nrow(s.t)){
  y = s.t$j[x]
  j[x] = toString(data2$X[y])
}

s.t$j = j




write.table(s.t, file = "wk6_people.csv", sep = ",", col.names = NA,
            qmethod = "double")

######################################################

#redo above, this time looking at events and not people
data2 <- read.csv("wk6_Matrix.csv", stringsAsFactors=TRUE)
data2 = head(data2, -1)
head(data2)

i = 0
p = 0
count = 1
for (x in 1:nrow(data2)){
  for (y in 1:ncol(data2)){
    print(data2[x,y])
    if (data2[x,y] == 1){
      i[count] = x
      p[count] = y-1
      count = count +1
    }
    
  }       
  
}

i2 = i
p2 = p
p = i2
i = p2

net <- cbind(i,p)

s.t2 <- projecting_tm(net, method="sum")

write.table(s.t2, file = "wk6_events.csv", sep = ",", col.names = NA,
            qmethod = "double")
