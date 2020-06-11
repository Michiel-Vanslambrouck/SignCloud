library(readr)
out <- read_table2("C:/Users/mcmic/AppData/Roaming/.minecraft/2B2T/signs/out.txt",col_names = FALSE)

colnames(out)=c("X","Y","Z")
attach(out)

out2 = subset(out, X>-100000 & X<100000 & Z>-100000 & Z<100000)
plot(out2$X,out2$Z,pch=".")
