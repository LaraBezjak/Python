% PURP:     Ensures that all segmented nuclear images are binarized and
%           converts all images into TIFF format.

clear;

% Set input path to folder SegImages
bwInPath='~/Desktop/WBC_PCAPipeline/Data/SegImgs_1/';
clInPath='~/Desktop/WBC_PCAPipeline/Data/RawImgs/';

% Set output path to folder BWImages
bwOutPath='~/Desktop/WBC_PCAPipeline/Data/BWImgs_1/';
clOutPath='~/Desktop/WBC_PCAPipeline/Data/ColNuc_1/';

% Iterate through and collect all files names in SegImages
files=dir(fullfile(bwInPath, 'Blood*.jpg'));

% For each image in SegImgs_i, convert the image to black/white and save it
% as a TIFF file in BWImgs_i.
for i = 1:numel(files)
    % Determine the new image name
    filename = files(i).name;
    removeExt = strsplit(filename, '.');
    % Add the TIFF extension to the file
    bwName = strcat(bwOutPath, 'bwSeg_',removeExt{1}, '.tiff');
    clName = strcat(clOutPath, 'clSeg_',removeExt{1}, '.tiff');
    
    % Load and read the image
    CUR = fullfile(bwInPath, files(i).name);
    [IMG, map] = imread(CUR);
    
    % Convert to black and white with a default threshold of 0.4.
    IMG2 = im2bw(IMG, map, 0.4);
    
    RAW = fullfile(clInPath, files(i).name);
    [IMG3, map] = imread(RAW);
    
    % For each pixel in the raw image, if the corresponding pixel in the 
    % binarized image is black, set all three channels to 0 to make that 
    % pixel black.
    [ row, col, dim ] = size(IMG3);
    for r = 1:(row - 1)
        for c = 1:(col - 1)
            if IMG2(r, c) == 0
                IMG3(r, c, 1) = 0;
                IMG3(r, c, 2) = 0;
                IMG3(r, c, 3) = 0;
            end
        end
    end
        
    % Save the images with their updated image names
    imwrite(IMG2, bwName);
    imwrite(IMG3, clName);
end