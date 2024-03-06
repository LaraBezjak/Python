% PRPS:     Trains a 2D framework PCA nuclear model using the white blood
%           cell nuclear images.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% OPTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;

options.verbose = true;
options.debug = false;
options.display = false;
options.model.name = 'WBC_PCA';
options = ml_initparam( options, struct( ...
    'train', struct( 'flag', 'framework' )));
options.nucleus.class = 'framework';
options.nucleus.type = 'pca';
options.cell.class = 'framework';
options.cell.type = 'pca';
options.skip_preprocessing = true;

% Latent Dimension for the Model
options.latent_dim = 15;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Set path to the binarized segmented images
directory = 'C:/Users/Lara/Desktop/WBC_PCAPipeline/Data';
dna = [ directory filesep 'BWImgs_1' filesep 'bw*.tiff' ];
cellm = [ directory filesep 'BWImgs_1' filesep 'bw*.tiff' ];


options.model.resolution = [ 0.049, 0.049 ];
options.model.filename = 'WBC_PCA.xml';
options.model.id = 'WBC_PCA';
% Set nuclei and cell model name
options.nucleus.name = 'WBC_NUC';
options.cell.model = 'WBC_CELL';

% Set the dimensionality of the model
dimensionality = '2D';

% Documentation
options.documentation.description = 'Trained using demo2D08 from CellOrganizer.';

% Set model type
options.train.flag = 'framework';

tic; answer = img2slml( dimensionality, dna, cellm, [], options ); toc;

if exist( [pwd filesep 'WBC_PCA.mat'] )
  load( [pwd filesep 'WBC_PCA.mat'] );
  scr = array2table(model.nuclearShapeModel.score);
  lbls = readtable('C:/Users/Lara/Desktop/WBC_PCAPipeline/Data/WBC_Labels.csv');
  mtrx = [lbls scr];
  writetable(mtrx, 'C:/Users/Lara/Desktop/WBC_PCAPipeline/Step4_Visualization/WBC_PCA.csv');
  slml2info({'WBC_PCA.mat'});
end
