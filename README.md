# Abstract: Multi-Index Spatiotemporal Analysis of the Aralkum Region (2020–2026)

---

### **Overview**
This project implements a dual-index remote sensing pipeline to monitor and quantify land cover transformation on the dried bed of the Aral Sea (Aralkum Desert). By leveraging the **Google Earth Engine (GEE)** cloud computing platform and **Sentinel-2 (MSI)** satellite imagery, the study provides a 7-year longitudinal audit of environmental degradation and salinization risks.

### **Methodology**
* **Data Source:** Multi-spectral data from the European Space Agency (ESA) with 10m spatial resolution.
* **Area of Interest (AOI):** ~20,000 km² [58.0°E, 43.5°N to 61.5°E, 46.5°N].
* **Core Indicators:**
    1.  **NDSI (Normalized Difference Snow/Salt Index):** Used for primary spatiotemporal analysis to track the evolution of bright surface deposits over time.
    2.  **SI (Salinity Index):** Applied specifically to identify and delineate potentially hazardous saline zones:
        $$\text{SI} = \sqrt{\text{Blue} \times \text{Red}}$$

### **Key Findings**
1.  **Dynamic Monitoring:** The **NDSI-based analysis** captures the steady progression of surface change across the 7-year period, effectively mapping the retreat of moisture and the advance of mineralized surfaces.
2.  **Risk Identification:** The **Salinity Index (SI)** successfully localized high-risk areas. Analysis revealed that while baseline sandy soils exhibit SI values between 1500–1800, extreme saline crusts reach a 98th percentile ($p_{98}$) value of **5471**, indicating critical mineralization levels.
3.  **Hazard Mapping:** Areas with $SI > 3800$ were classified as high-risk zones, serving as primary sources for salt-dust storms in the region.

### **Technical Stack**
`Python` | `Google Earth Engine API` | `Geemap` | `Folium` | `Matplotlib` | `Numpy`

---
*Developed by Qodirov Muhammadkarim Zokirovich

| Resource | Link |
| :--- | :--- |
| **Interactive Notebook** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1q7KJHXRgGi6Au2cQ8s4FipkWjqBmzppY?usp=sharing#scrollTo=TrQbZwV0iii3) |
