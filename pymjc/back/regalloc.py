from __future__ import annotations
from abc import abstractmethod
import sys
from typing import Set
from pymjc.back import assem, flowgraph, graph
from pymjc.front import frame, temp


class RegAlloc (temp.TempMap):
    def __init__(self, frame: frame.Frame, instr_list: assem.InstrList):
        self.frame: frame.Frame = frame
        self.instrs: assem.InstrList = instr_list
        #TODO

    def temp_map(self, temp: temp.Temp) -> str:
        #TODO
        return temp.to_string()
    

class Color(temp.TempMap):
    def __init__(self, ig: InterferenceGraph, initial: temp.TempMap, registers: temp.TempList):
        #TODO
        pass
    
    def spills(self) -> temp.TempList:
        #TODO
        return None

    def temp_map(self, temp: temp.Temp) -> str:
        #TODO
        return temp.to_string()

class InterferenceGraph(graph.Graph):
    
    @abstractmethod
    def tnode(self, temp:temp.Temp) -> graph.Node:
        pass

    @abstractmethod
    def gtemp(self, node: graph.Node) -> temp.Temp:
        pass

    @abstractmethod
    def moves(self) -> MoveList:
        pass
    
    def spill_cost(self, node: graph.Node) -> int:
      return 1


class Liveness (InterferenceGraph):

    def __init__(self, flow: flowgraph.FlowGraph):
        self.live_map = {}
        
        #Flow Graph
        self.flowgraph: flowgraph.FlowGraph = flow
        
        #IN, OUT, GEN, and KILL map tables
        #The table maps complies with: <Node, Set[Temp]>
        self.in_node_table = {}
        self.out_node_table = {}
        self.gen_node_table = {}
        self.kill_node_table = {}

        #Util map tables
        #<Node, Temp>
        self.rev_node_table = {}
        #<Temp, Node>
        self.map_node_table = {}
        
        #Move list
        self.move_list: MoveList = None

        self.build_gen_and_kill()
        self.build_in_and_out()
        self.build_interference_graph()
    
    def add_ndge(self, source_node: graph.Node, destiny_node: graph.Node):
        if (source_node is not destiny_node and not destiny_node.comes_from(source_node) and not source_node.comes_from(destiny_node)):
            super.add_edge(source_node, destiny_node)

    def show(self, out_path: str) -> None:
        if out_path is not None:
            sys.stdout = open(out_path, 'w')   
        node_list: graph.NodeList = self.nodes()
        while(node_list is not None):
            temp: temp.Temp = self.rev_node_table.get(node_list.head)
            print(temp + ": [ ")
            adjs: graph.NodeList = node_list.head.adj()
            while(adjs is not None):
                print(self.rev_node_table.get(adjs.head) + " ")
                adjs = adjs.tail

            print("]")
            node_list = node_list.tail
    
    def get_node(self, temp: temp.Temp) -> graph.Node:
      requested_node: graph.Node = self.map_node_table.get(temp)
      if (requested_node is None):
          requested_node = self.new_node()
          self.map_node_table[temp] = requested_node
          self.rev_node_table[requested_node] = temp

      return requested_node

    def node_handler(self, node: graph.Node):
        def_temp_list: temp.TempList = self.flowgraph.deff(node)
        while(def_temp_list is not None):
            got_node: graph.Node  = self.get_node(def_temp_list.head)

            for live_out in self.out_node_table.get(node):
                current_live_out = self.get_node(live_out)
                self.add_edge(got_node, current_live_out)

            def_temp_list = def_temp_list.tail

  
    def move_handler(self, node: graph.Node):
        source_node: graph.Node  = self.get_node(self.flowgraph.use(node).head)
        destiny_node: graph.Node = self.get_node(self.flowgraph.deff(node).head)

        self.move_list = MoveList(source_node, destiny_node, self.move_list)
    
        for temp in self.out_node_table.get(node):
            got_node: graph.Node = self.get_node(temp)
            if (got_node is not source_node ):
                self.addEdge(destiny_node, got_node)

    def _in(self, node: graph.Node) -> Set[temp.Temp]:
        temp_set = self.in_node_table.get(node)
        return temp_set

    def out(self, node: graph.Node) -> Set[temp.Temp]:
        temp_set = self.out_node_table.get(node)
        return temp_set


    def tnode(self, temp:temp.Temp) -> graph.Node:
        node: graph.Node = self.map_node_table.get(temp)
        if (node is None ):
            node = self.new_node()
            self.map_node_table[temp] = node
            self.rev_node_table[node] = temp
        
        return node

    def gtemp(self, node: graph.Node) -> temp.Temp:
        temp: temp.Temp = self.rev_node_table.get(node)
        return temp

    def moves(self) -> MoveList:
        return self.move_list

    def build_gen_and_kill(self):
        #TODO
        pass

    #until in'[n] = in[n] and out'[n] = out[n] for all n
    def check_if_same(self, in_old, out_old) -> bool:
        while aux.head != None:
            if((self.in_node_table[aux.head] != in_old[aux.head]) or (self.out_node_table[aux.head] != out_old[aux.head])):
                return False
            aux = aux.tail
        return True

    def temp_list_to_set(self, temp_list:temp.TempList)-> set:
        aux = temp_list
        temp_list_set : set = {}
        while aux.head != None:
            temp_list_set.add(aux.head)
            aux = aux.tail
        return temp_list_set


    def build_in_and_out(self):
        node_list: graph.NodeList = self.flowgraph.nodes()
        aux = node_list

        #Initializing in_node_table and out_node_table
        while aux.head != None:
            self.in_node_table[aux.head.to_string()] = {}
            self.out_node_table[aux.head.to_string()] = {}
            aux = aux.tail

        aux = node_list
        do = True
        in_old = {}
        out_old = {}
        
        while do or (self.check_if_same(in_old, out_old)):
            do = False
            while aux.head is not None:
                in_old[aux.head.to_string()] = self.in_node_table[aux.head.to_string()]
                out_old[aux.head.to_string()] = self.out_node_table[aux.head.to_string()]

                diff = (self.out_node_table[aux.head.to_string()].difference
                        (self.flowgraph.deff(aux.head)))

                self.in_node_table[aux.head.to_string()] = (self.temp_list_to_set
                                                            (self.flowgraph.use
                                                                (aux.head)).union(diff))

                # Para todo sucessor de aux.head, devemos fazer a união
                # de seus conjuntos de arestas
                succs: graph.NodeList = aux.head.succ()
                aux_succs = succs
                all_succs: set
                while aux_succs.head is not None:
                    all_succs.union(self.in_node_table[aux_succs.head.to_string()])  
                    aux_succs = aux_succs.tail
                self.out_node_table[aux.head.to_string] = all_succs
                aux = aux.tail
        return None

    def build_interference_graph(self):
        # TODO
        # Em uma key de in_node_table vamos adicionar arestas entre todos os valores key -> valor
        # for key in self.in_node_table:
        #   for value in self.in_node_table[key]:
        #       add_edge(value, key)~~o valor node1 seria referente ao nó que está na lista de in_node_table[key],
        #                                                                                já key seria o nó da key
        pass

class Edge():

    edges_table = {}

    def __init__(self):
        super.__init__()
    
    def get_edge(self, origin_node: graph.Node, destiny_node: graph.Node) -> Edge:
        
        origin_table = Edge.edges_table.get(origin_node)
        destiny_table = Edge.edges_table.get(destiny_node)
        
        if (origin_table is None):
            origin_table = {}
            Edge.edges_table[origin_node] = origin_table

        if (destiny_table is None):
            destiny_table = {}
            Edge.edges_table[destiny_node] = destiny_table
        
        requested_edge: Edge  = origin_table.get(destiny_node)

        if(requested_edge is None):
            requested_edge = Edge()
            origin_table[destiny_node] = requested_edge
            destiny_table[origin_node] = requested_edge

        return requested_edge



class MoveList():

   def __init__(self, s: graph.Node, d: graph.Node, t: MoveList):
      self.src: graph.Node = s
      self.dst: graph.Node = d
      self.tail: MoveList = t