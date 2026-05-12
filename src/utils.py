import ee

def apply_cloud_mask(image):
    """Маскирование облаков для Sentinel-2."""
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = qa.bitwiseAnd(cloud_bit_mask).eq(0).And(
           qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    return image.updateMask(mask).divide(10000)

def calculate_indices(image):
    """Расчет индексов NDSI и SI."""
    # NDSI (Normalized Difference Snow/Salt Index)
    ndsi = image.normalizedDifference(['B3', 'B11']).rename('NDSI')
    
    # SI (Salinity Index)
    si = image.expression(
        'sqrt(blue * red)', {
            'blue': image.select('B2'),
            'red': image.select('B4')
        }
    ).rename('SI')
    
    return image.addBands([ndsi, si])