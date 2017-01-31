//Get Switzerland Polygon
var countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw');
var Switzerland = countries.filter(ee.Filter.eq('Country', 'Switzerland'));
Map.addLayer(Switzerland, {'color': 'FF0000'}, "Switzerland")

//Get collection of Switzerland Landsat 8 data
var filteredCollection = ee.ImageCollection('LANDSAT/LC8_L1T')
  .filterBounds(Switzerland)
  .filterDate("2016-03-01", "2016-08-31")
  .sort('CLOUD_COVER', false);

// Create a cloud-free composite with the collection
var composite = ee.Algorithms.Landsat.simpleComposite({
  collection: filteredCollection,
  percentile: 75,
  cloudScoreRange: 2
});

//Display true colors image
var raw = composite.select(['B4','B3','B2']);
Map.addLayer(raw, {bands: ['B4','B3','B2']}, 'raw' );

//Compute NDBI 
var swir = composite.select(['B6'])
var nir = composite.select(['B5'])
var ndbi = nir.subtract(swir).divide(nir.add(swir))

//Display NDBI
var ndbi_viz = {palette: ['000000','00FF00']};
Map.addLayer(ndbi, ndbi_viz, 'NDBI');

// Define a low-pass kernel.
var boxcar = ee.Kernel.square({
  radius: 5, units: 'pixels', normalize: true
});

// Smoothen and use threshold of 0.2 for NDBI
var inter = ndbi.convolve(boxcar).lt(0.2);

// Define morphological kernels.
var kernel_small = ee.Kernel.circle({radius: 5});
var kernel = ee.Kernel.circle({radius: 10});

// Perform an dilatation, display.
var Dilatation = inter
             //.focal_min({kernel: kernel_small, iterations: 2})
             .focal_max({kernel: kernel, iterations: 2});
Map.addLayer(Dilatation, {}, 'Dilatation');

// Export the image, specifying scale and region.
Export.image.toDrive({
  image: Dilatation,
  description: 'Dilatation',
  scale: 50,
  region: Switzerland
});

