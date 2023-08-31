from skimage.measure import label, regionprops, regionprops_table
def largest_bb(maskslist):
"""Computes the largest bounding box in instance segmentation images in order to then isolate each single object in the same resolution

Args:
maskslist: the list of labelled objects inside the image"""

    props_masks= regionprops(maskslist)
    bindingbx= [props_masks[i]['bbox'] for i in range(len(props_masks))]
    #minrow
    y=[]
    #mincol
    x=[]
    #maxrow
    ymax=[]
    #maxcol
    xmax=[]
    
    width=[]
    height=[]
    for i in range(len(bindingbx)):
        y.append(bindingbx[i][0])
        x.append(bindingbx[i][1])
        ymax.append(bindingbx[i][2])
        xmax.append(bindingbx[i][3])
        width.append(ymax[i]-y[i])
        height.append(xmax[i]-x[i])
        
    maxim_w= np.max(width)
    maxim_h= np.max(height)

    return maxim_w,maxim_h
    
"""
Example :
from operator import itemgetter
size_bb=[]
for i in range(len(masks)):
    size_bb.append(largest_bb(masks[i]))
"""
    
    
    
def isolate_object(maskslist):

"""Calls for each single object by its label, the result is an array containing only the given object with the others present in the original labelled image

Args:
maskslist, the labelled image"""

    isolated_object= []
    for i in range(len(maskslist)):
        for j in range(1,len(np.unique(maskslist[i]))):
            isolated_object.append(ko_only_masks[i]==j)
    return isolated_object
    
    
def center_object(isolated_object,size):
"""Puts the single object at the center of the new image array with dimensions as the same of the largest bounding box

Args:
isolated_object: the list of arrays containing single separated objects masks
size: size of the biggest binding box"""


    background= np.zeros((size,size))
    center= round(size/2)
    
    #Find mask centroid
    h, w = isolated_object.shape
    props= regionprops(isolated_object)
    
    centroid = props[0]['centroid']
    
    offy= round(centroid[0]) - center
    offx= round(centroid[1]) - center 
    coordinates = props[0]['coords']
    
    new_y=coordinates[:,0] - offy
    new_x=coordinates[:,1] - offx
    
    for i in range(len(new_y)):
        if (0 <= new_y[i] < size) and (0 <= new_x[i] < size):
            background[new_y[i], new_x[i]] = 1
    return background    