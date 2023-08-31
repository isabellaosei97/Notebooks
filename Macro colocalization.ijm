//Fiji/ImageJ Macro for colocalization of segmented nuclei in multiple channels of the image.
//Nuclei can be positive for multiple markers, used to assess the presence of certain proteins in example. In order to determine which nuclei show 
//signal for more than one marker, 
// we perform Segmentation using Stardist plugin in Fiji (check repository for the Stardist model training) 
//The resulted region of interests (ROIs) are stored in Fiji in the roiManage which we can iterate.

for (i=0 ; i < roiManager("count"); i= i+ 1) {
roiManager("Select", i);
roiManager("Measure");
}

selectWindow("Results");



h= 3892
w= 3912
newImage("Untitled", "8-bit black", h, w, 1);
setForegroundColor(1, 1, 1);
count_positive_nuclei = 0
print("All nuclei: " + roiManager("count"));

for (i = 0; i < roiManager("count"); i++) {
	
	if (getResult("Mean", i) > 12500) {  //12500 corresponds to our threshold to assess presence of signal in the other channel we are interested in
		// print(i + " larger than mean");
		selectWindow("Untitled");
		roiManager("Select", i);
		roiManager("Fill");
		count_positive_nuclei = count_positive_nuclei + 1;
	}
}
print("Positive nuclei: " + count_positive_nuclei);
selectWindow("Untitled");
run("Color Balance...");
run("Apply LUT");

