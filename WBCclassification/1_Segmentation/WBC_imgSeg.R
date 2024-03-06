# Required Libraries
library("EBImage")
library("jpeg")
library("tiff")

# Set path for raw image files
path="~Desktop/WBC_PCAPipeline/Data/"
rawImgs=paste(path, "RawImgs/", sep="")

# Set up directory path for segemented images
segImgs=paste(path, "SegImgs_", sep="")
colImgs=paste(path, "ColNuc_", sep="")
bwImgs=paste(path, "BWImgs_", sep="")

# Check if unique seg directory exists, otherwise create one
# dir Counter
i = 1
while (file.exists(paste(segImgs, toString(i), sep=""))) {
  i = i + 1
}
print(noquote(paste("Creating", paste(segImgs, toString(i), sep=""), "directory for segmented images.")))
dir.create(paste(segImgs, toString(i), sep=""), showWarnings = FALSE);
print(noquote(paste("Creating", paste(bwImgs, toString(i), sep=""), "directory for binarized images.")))
dir.create(paste(bwImgs, toString(i), sep=""), showWarnings = FALSE)
print(noquote(paste("Creating", paste(colImgs, toString(i), sep=""), "directory for nucleus in color images.")))
dir.create(paste(colImgs, toString(i), sep=""), showWarnings = FALSE)

outDir=paste(segImgs, toString(i), sep="")
setwd(rawImgs)

# Gather all files within the directory above
all.files <- list.files()
my.files <- grep("*.jpg", all.files, value=T)

print(noquote("Starting nucleus segmentation..."))

# Loop through each file and process each image individually
for (i in my.files) {
  print(noquote(paste("Segmenting nucleus from file", i)))
  # Read the image, change to its directory
  nuc = readImage(paste(rawImgs, i, sep=""))

  # Each nuclear stain has low red, low green and high blue.

  # Need to invert the red and green channels, and then threshold according to
  # the above criteria
  nuc_r = channel(nuc, 'r')
  nuc_g = channel(nuc, 'g')
  nuc_b = channel(nuc, 'b')

  # Assigned thresholds for low red, low green, and high blue.
  r_threshold = 0.65
  g_threshold = 0.60
  b_threshold = 0.5975

  # Apply the thresholds accordingly
  nuc_rTH = nuc_r < r_threshold
  nuc_gTH = nuc_g < g_threshold
  nuc_bTH = nuc_b > b_threshold

  nucleusComp = nuc_rTH & nuc_gTH & nuc_bTH
  nucleusBW = bwlabel(fillHull(nucleusComp))


  # Compute features for objects that have made the threshold boundaries
  features = computeFeatures.shape(nucleusBW)

  # Assigned area threshold
  area_threshold <- 1500

  # Find all features that do not meet the area threshold
  indices = which(features < area_threshold)
  nucleusFin = rmObjects(nucleusBW, indices)

  newFeatures = computeFeatures.shape(nucleusFin)

  # Write final nucleus image to disk
  filename = paste(outDir, i, sep="/")
  writeImage(nucleusFin, filename)
}
print(noquote("DONE!"))
