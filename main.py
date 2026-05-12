import ee
import geemap
from src.analyzer import AralAnalyzer

# Инициализация GEE
try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

# Настройки региона (твои 4 координаты)
REGION_COORDS = [[58.0, 43.5], [61.5, 43.5], [61.5, 46.5], [58.0, 46.5]]

def run_analysis():
    analyzer = AralAnalyzer(REGION_COORDS)
    years = range(2020, 2027)
    
    print(f"Starting analysis for Aralkum region...")
    
    for year in years:
        image = analyzer.get_annual_composite(year)
        stats = analyzer.get_stats(image, 'SI')
        print(f"Year {year}: SI p98 = {stats.get('SI_p98'):.2f}")

if __name__ == "__main__":
    run_analysis()