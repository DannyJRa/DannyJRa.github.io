#%%
#The R code is

#m <- matrix(rnorm(100), ncol=5)
#pca <- princomp(m)
##plot(pca, main="Eigen values")
#biplot(pca, main="biplot")
#The rpy2.robjects code can be as close to the R code as possible:

import rpy2.robjects as robjects

r = robjects.r

m = r.matrix(r.rnorm(100), ncol=5)
pca = r.princomp(m)
r.plot(pca, main="Eigen values")
r.biplot(pca, main="biplot")