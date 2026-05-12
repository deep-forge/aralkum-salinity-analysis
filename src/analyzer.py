import ee
from src.utils import apply_cloud_mask, calculate_indices

class AralAnalyzer:
    def __init__(self, region_coords):
        self.roi = ee.Geometry.Polygon(region_coords)

    def get_annual_composite(self, year):
        """Создает медианный снимок за год с индексами."""
        start_date = f'{year}-01-01'
        end_date = f'{year}-12-31'
        
        collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                      .filterBounds(self.roi)
                      .filterDate(start_date, end_date)
                      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
                      .map(apply_cloud_mask)
                      .map(calculate_indices))
        
        return collection.median().clip(self.roi)

    def get_stats(self, image, band='SI'):
        """Получение статистики (процентилей) для выбранного слоя."""
        stats = image.select(band).reduceRegion(
            reducer=ee.Reducer.percentile([50, 90, 98]),
            geometry=self.roi,
            scale=100,
            maxPixels=1e9
        )
        return stats.getInfo()