"""Emit the chapter histogram as accessible, deterministic SVG."""
from xml.etree.ElementTree import Element, SubElement, tostring

from lab.measure import BINS, DELAYS, histogram


def draw():
    svg=Element("svg", {
        "xmlns":"http://www.w3.org/2000/svg","viewBox":"0 0 740 350",
        "role":"img","aria-labelledby":"chart-title chart-description",
    })
    def add(tag, attrs, text=None):
        node=SubElement(svg,tag,{k:str(v) for k,v in attrs.items()})
        node.text=text
        return node
    add("title",{"id":"chart-title"},"Delay distribution among 10 recorded arrivals")
    add("desc",{"id":"chart-description"},
        "Equal width three-minute bins. Counts from zero to twenty-one minutes are 5, 4, 0, 0, 0, 0, 1. Left edges are included and right edges are excluded.")
    add("rect",{"width":740,"height":350,"fill":"#ffffff"})
    def label(x,y,text,align="middle",size=21,weight="normal"):
        add("text",{"x":x,"y":y,"text-anchor":align,"font-family":"Arial, sans-serif",
                    "font-size":size,"font-weight":weight,"fill":"#172840"},text)
    def line(x1,y1,x2,y2,color="#526074",width=1):
        add("line",{"x1":x1,"x2":x2,"y1":y1,"y2":y2,"stroke":color,"stroke-width":width})
    label(92,37,"Delay distribution among 10 recorded arrivals","start",25,"bold")
    label(92,67,"Frequency: number of recorded trips","start",18)
    left,base,width,step=92,266,82,31
    for n in range(6):
        y=base-n*step
        line(left,y,left+width*7,y,"#ccd5df")
        label(left-15,y+7,str(n),"end",17)
    for i,count in enumerate(histogram(DELAYS,BINS)):
        if count:
            add("rect",{"id":f"bar-{i}","x":left+i*width,"y":base-count*step,
                        "width":width,"height":count*step,"fill":"#22607a","stroke":"#172840","stroke-width":2})
            label(left+i*width+width//2,base-count*step-8,str(count),size=17,weight="bold")
    line(left,base,left+width*7,base,width=2)
    line(left,base,left,base-step*5,width=2)
    for i,edge in enumerate(BINS):
        x=left+i*width
        line(x,base,x,base+7,width=2)
        label(x,base+31,str(edge),size=18)
    label(left+7*width//2,base+67,"Recorded lateness (minutes)",size=20)
    return tostring(svg,encoding="unicode")


if __name__=="__main__":
    print(draw())
