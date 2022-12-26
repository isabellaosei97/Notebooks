import numpy as np

def average_object_intensity(label_image, raw):
    """ Computes and returns the average intensity 
    in a 1D raw microscopy image `raw` per unique label 
    in instance segmentation image `label_image`.
    
    Args:
    label_image: result of an instance segmentation in 2D. Pixels carry value of segment id, or 0 for background.
    raw: a raw microscopy image in 2D with the same dimensions as label_image from which the intensities are taken.
    
    Returns:
    an array of length max(labels)+1, with the i-th entry containing the average intensity observed in raw 
    over all places where label_image is of value i.
    """
    
    assert(raw.shape == label_image.shape)
    
    # create two arrays large enough to fit all segments contained 
    # in label_image (includin the background label 0)
    sumintensity= np.zeros(np.max(label_image)+1)
    numpix= np.zeros(np.max(label_image)+1)


    
    for y in range(label_image.shape[0]):
        for x in range(label_image.shape[1]):
            sumintensity[label_image[y,x]] += raw[y,x]
            numpix[label_image[y,x]] += 1 
    

    
    
    return sumintensity/numpix
    
def test_plus1(a):
    return a+1

def filter_expressing_cells(label_image, raw, threshold):
    """ Filters all labels that do not show an average intensity of >threshold in the given raw image.
    
    Args: 
    label_image: result of an instance segmentation in 2D. Pixels carry value of segment id, or 0 for background.
    raw: a raw microscopy image in 2D with the same dimensions as label_image from which the intensities are taken.
    threshold: any average intensity instance in label_image (given intensities in raw) larger than threshold will be maintained.
    
    Returns:
    the filtered label_image containing only the instances that have an average intensity of >threshold in the given raw channel.
    """
    assert(raw.shape == label_image.shape)
    avg_per_instance = average_object_intensity(label_image, raw)
    
    filtered_instances = np.zeros_like(raw)
    for y in range(filtered_instances.shape[0]):
        for x in range(len(filtered_instances[1])):
            if avg_per_instance[label_image[y,x]]>threshold:
                filtered_instances[y,x] = label_image[y,x]
    
    return filtered_instances, avg_per_instance