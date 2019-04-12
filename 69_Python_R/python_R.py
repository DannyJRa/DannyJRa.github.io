#%%
import rpy2.robjects as robjects
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
stats = importr('stats')
base = importr('base')

ctl = FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
trt = FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])
group = base.gl(2, 10, 20, labels = ["Ctl","Trt"])
weight = ctl + trt


#%%
robjects.globalenv["weight"] = weight
robjects.globalenv["group"] = group
lm_D9 = stats.lm("weight ~ group")
print(stats.anova(lm_D9))

# omitting the intercept
lm_D90 = stats.lm("weight ~ group - 1")
print(base.summary(lm_D90))
#teset

#%%
print(lm_D9.rx2('coefficients')




##################################
#%%
import rpy2.robjects as robjects

r = robjects.r

m = r.matrix(r.rnorm(100), ncol=5)
pca = r.princomp(m)
r.plot(pca, main="Eigen values")
r.biplot(pca, main="biplot")


####################################
#Since rpy2 release 2.4.0 converting data frames back and forth between rpy2 and pandas is included as an optional module. With it, no need to convert explicitly, it will be done on the fly

#%%
import rpy2.robjects as robjects
robjects.r.source("sample.R")
print(robjects.globalenv["a"])
print(robjects.globalenv["b"])
print(robjects.globalenv["c"])
print(robjects.globalenv["data"])