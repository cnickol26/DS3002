##########################################
##Heart example with classification tree##
##########################################

library(tree)
data.all<-read.csv("Heart.csv", header=TRUE)

##fit classification tree using all data 
tree.all<-tree::tree(AHD~., data.all)
summary(tree.all)

##create classification tree
plot(tree.all)
text(tree.all, cex=0.75, pretty=0) ##use pretty=0 to use words for internal nodes with categorical variables

##use 10 fold CV to find size of tree
set.seed(12)
cv.all<-tree::cv.tree(tree.all, K=10)
cv.all

##see size of tree which gives best tree based on pruning and 10-fold CV
plot(cv.all$size, cv.all$dev, type="b", xlab="Size of Tree", ylab="Deviance")
trees.num<-cv.all$size[which.min(cv.all$dev)]
trees.num
##7 nodes is chosen with pruning

##tree with 7 terminal nodes
prune.full<-tree::prune.tree(tree.all, best=trees.num)

##classification tree with pruning
plot(prune.full)
text(prune.full, cex=0.75, pretty=0) 

##numerical display of tree
prune.full


