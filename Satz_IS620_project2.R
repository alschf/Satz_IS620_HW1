library(tnet)

setwd("/Users/alexandersatz/Documents/Cuny/IS620/")
data2 <- read.csv("Source_Target_P2IS620.txt", stringsAsFactors=FALSE)
#data2 = head(data2, -1)
head(data2)

uniq = unique(data2)

## assign number IDs to journal names
u.j = unique(data2$Source)
u.a = unique(data2$Target)
d.journals <- vector(mode="list", length=length(u.j))
d.journals <- seq(1,length(u.j),1)
names(d.journals) <- u.j

d.a <- vector(mode="list", length=length(u.a))
d.a <- seq(1,length(u.a),1)
names(d.a) <- u.a

##generate dataframe after conversion to numbers
i <-0
p <-0
for (x in 1:nrow(uniq)){
  i[x] = d.journals[[uniq$Source[x]]]
  p[x] = d.a[[uniq$Target[x]]]
  
}


net <- cbind(i,p)
 
#project where edges are summed.
s.t <- projecting_tm(net, method="sum")
s.t.n <- projecting_tm(net, method="Newman")



#convert numbers back to names
i.name = 0
j.name = 0
for (x in 1:nrow(s.t)){
  i.name[x] = names(d.journals[s.t$i[x]])
  j.name[x] = names(d.journals[s.t$j[x]])
}

s.t$i = i.name
s.t$j = j.name

i.name = 0
j.name = 0
for (x in 1:nrow(s.t)){
  i.name[x] = names(d.journals[s.t.n$i[x]])
  j.name[x] = names(d.journals[s.t.n$j[x]])
}

s.t.n$i = i.name
s.t.n$j = j.name

##write out dataframes to a file
write.table(s.t.n, file = "IS620_proj2_net_newman.csv", sep = ",", col.names = NA,
            qmethod = "double")

