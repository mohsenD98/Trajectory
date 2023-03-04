import colorama
from colorama import Fore
import enum

class Runtype(enum.Enum):
   DEBUG = 1
   RELEASE = 2

class InputsType(enum.Enum):
   USER_TERMINAL = 1
   DEFAULT_TESTS = 2

runMode = Runtype.RELEASE
inputsType = InputsType.DEFAULT_TESTS

def log(input, important= False):
    if important:
       print(Fore.RED+input)

    if runMode == Runtype.DEBUG: 
      if type(input) == str:
         print(Fore.WHITE+input)
      else:
         print(input)

# get values from terminal
def get(message, inputLen):
    numList = list(map(float, input(Fore.RED+ message).strip().split()))[:inputLen]
    return numList

def run(command):
   if runMode == Runtype.DEBUG: 
      command()

def cartesianProductDictInList(mDict, mList):
   result = {}
   for key, value in mDict.items():
      for element in mList:
         result[str(key)+"-"+str(element)] = value
   return result

# pretty Log Dict
def plog(d, indent=0):
   if runMode == Runtype.DEBUG: 
      for key, value in d.items():
         print('\t' * indent + str(key))
         if isinstance(value, dict):
            plog(value, indent+1)
         else:
            print('\t' * (indent+1) + str(value))

# pretty Log Dict
def ploglist(mlist, indent=0):
   if runMode == Runtype.DEBUG: 
      for d in mlist:
         plog(d)

# ref: https://stackoverflow.com/questions/10104700/how-to-set-networkx-edge-labels-offset-to-avoid-label-overlap
def plotListOfGraphs(dicOfGraphs):
   if runMode == Runtype.DEBUG: 
      import matplotlib.pyplot as plt
      from matplotlib.pyplot import  text
      import networkx as nx

      graphs = list(dicOfGraphs.keys())

      for key in graphs:
         G=nx.Graph()
         edgesStruct = dicOfGraphs[int(key)]
         leafs = list(edgesStruct.keys())

         weights = dict()
         for leaf in leafs:
            G.add_edge(key,leaf,weight=0.5)
            weights[(key, leaf)] = str(dicOfGraphs[key][leaf])

         pos=nx.spring_layout(G) # positions for all nodes

         # nodes
         nx.draw_networkx_nodes(G,pos, node_size=700, node_color="red")

         # edges
         nx.draw_networkx_edges(G,pos,width=6,alpha=0.5,edge_color='black')
         
         # labels
         nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

         nx.draw_networkx_edge_labels(G,pos, weights, label_pos=0.3)

         plt.axis('off')
         # plt.savefig("weighted_graph.png") 
         plt.show() 




# test
if __name__ == "__main__":
   # c = {}
   # c["1,2"] = ([1], 1)
   # c["3,4,5"] = ([1], 1)
   st = ["1,2", "3,4", "1", "234", "2,3", "3,4"]
   st=[x for x in st if len(x)>=2]
   print(st, st)
   # print(cartesianProductDictInList(c, st))

