#Purpose: Construct familiar algebraic classes from scratch
#Tbh I don't see this going anywhere so I'm going to put this one on indefinite hold.
#In progress: Finitized free product
import random
import math
import numpy

#The set-theoretic approach to algebraic objects:
class magma:
    #Note that a function is a relation, and a relation is a subset of the cartesian product
    #Hence, the binary operation a*b -> c is represented as a triple (a,b,c)
    #That's probably currying or something
    def __init__(self, elements={0},binop={(0,0,0)}):
        self._elements = elements
        self._binop = binop

    #Here's the multiplication function
    def mult(self,x,y):
        for z in self._elements:
            if (x,y,z) in self._binop:
                return z
        return

    def is_closed(self):
        for x in self._elements():
            for y in self._elements():
                if self.mult(x,y) == None:
                    return False
        return True

    def is_associative(self):
        for a in self._elements:
            for b in self._elements:
                for c in self._elements:
                    if self.mult(self.mult(a,b),c) != self.mult(a,self.mult(b,c)):
                        return False
        return True

    def is_commutative(self):
        for a in self._elements:
            for b in self._elements:
                if self.mult(a,b) != self.mult(b,a):
                    return False
        return True

    #If the magma has an identity element, this will return it, otherwise returns blank
    def id(self):
        for a in self._elements:
            isidentity = True
            for b in self._elements:
                if self.mult(a,b) != b:
                    isidentity = False
            if isidentity == True:
                return a
        return

    def has_id(self):
        if type(self.id()) != type(None):
            return True
        else:
            return False

    #If an element has an inverse, this will return it, otherwise returns blank
    def inverse(self, e):
        if self.has_id == False:
            return
        for a in self._elements:
            if self.mult(e,a) == self.id():
                return a
        return

    def has_inverse(self, e):
        if type(self.inverse(e)) != type(None):
            return True
        else:
            return False

    def has_inverses(self):
        for a in self._elements:
            if self.has_inverse(a) == False:
                return False
        return True

    def is_monoid(self):
        return self.has_id() and self.is_associative()

    def is_commutative_monoid(self):
        return self.is_monoid() and self.is_commutative()

    def is_group(self):
        return self.is_monoid() and self.has_inverses()

    def is_abelian_group(self):
        return self.is_commutative_monoid() and self.has_inverses()



    @property
    def elements(self):
        return self._elements

    @property
    def binop(self):
        return self._binop

def Z_mod(n):
    #try:
    G = []
    bo = []
    for i in range(0,n):
        G.append(i)
        for g in G:
            if i+g < n:
                bo.append((i,g,i+g))
                bo.append((g,i,g+i))
            else:
                bo.append((i,g,i+g-n))
                bo.append((g,i,g+i-n))
    return magma(set(G),set(bo))
    #except:
        #print("Invalid n")
        #return

def CartProd(G,H):
    #try:
    GxH = []
    bo = []
    for g in G.elements:
        for h in H.elements:
            GxH.append((g,h))
            for g2 in G.elements:
                for h2 in H.elements:
                    bo.append( ( (g,h), (g2,h2), (G.mult(g,g2),H.mult(h,h2)) ) )
                    bo.append( ( (g2,h2), (g,h), (G.mult(g2,g), H.mult(h2,h)) ) )
    return magma(set(GxH),set(bo))
    #except:
        #print("Invalid magmas")
        #return

class magma_action():
    def __init__(self, mag=magma(),set={0},binop={(0,0,0)}):
        self._mag = mag
        self._set = set
        self._binop = binop

    def mult(self,x,y):
        for z in self._set:
            if (x,y,z) in self._binop:
                return z
        return

    def is_closed(self):
        for x in self._mag.elements:
            for y in self._set:
                if self.mult(x,y) == None:
                    return False
        return True

    def respects_id(self):
        if self._mag.has_id == False:
            return False

        for x in self._set:
            if self.mult(self._mag.id,x) != x:
                return False

        return True

    def is_group_action(self):
        if self.is_closed and self.respects_id == False:
            return False

        for g in self._mag.elements:
            for h in self._mag.elements:
                for x in self._set:
                    if self.mult(self._mag.mult(g,h),x) != self.mult(g,self.mult(h,x)):
                        return False

        return True


def FinitizedFreeProduct(G=magma(),H=magma(),n=2):
    try:
        GUH = (G.elements).union(H.elements)
        gid = ''
        hid = ''
        bo = (G.binop).union(H.binop)
        if G.has_id() and H.has_id():
            gid = string(G.id())
            hid = string(H.id())
            GUH.remove(hid)
            i = len(GUH) * (3**(n-1))
            while len(GUH) <= i:
                for g in G.elements:
                    for h in H.elements:
                        if string(g) == string(G.id()):
                            bo.add(string(g),string(h),string(h))
                            bo.add(string(h),string(g),string(h))
                        elif string(h) == string(H.id()):
                            bo.add(string(g),string(h),string(g))
                            bo.add(string(h),string(g),string(g))
                        else:
                            GUH.add(string(g) + string(h))
                            GUH.add(string(h) + string(g))
                            bo.add((string(g),string(h),string(g) + string(h)))
                            bo.add((string(h),string(g),string(h) + string(g)))

        return magma(GUH,bo)
    except:
        print("Invalid magmas")
        return


def main():
    print(CartProd(Z_mod(3),Z_mod(4)).mult((1,2),(1,2)))
    print(CartProd(Z_mod(3),Z_mod(4)).is_abelian_group())

if __name__ == '__main__': main()