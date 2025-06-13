from model.model import Model

mymodel = Model()

mymodel.buildGraph()
print(mymodel.getNumNodes(), mymodel.getNumEdges())