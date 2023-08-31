for (i=0 ; i < roiManager("count"); i= i+ 1) {
roiManager("Select", i);
roiManager("Measure");
}

selectWindow("Results");

//means_array = newArray(roiManager("count"));

//for (i=0 ; i < roiManager("count"); i= i+1) {
//means_array[i] = getResult("Mean", i);
//}

//means_stats = Array.getStatistics(means_array,min,max,mean,stdDev);

//print(mean);
//print(0.3*stdDev);

h= 3892
w= 3912
newImage("Untitled", "8-bit black", h, w, 1);
setForegroundColor(1, 1, 1);
count_positive_nuclei = 0
print("All nuclei: " + roiManager("count"));

for (i = 0; i < roiManager("count"); i++) {
	
	if (getResult("Mean", i) > 12500) {
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

