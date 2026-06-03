COURSE: INFO 420 - Data Visualization Techniques
DATE: May 19, 2026
TOPIC: Human-Centric Design, Preattentive Attributes, and Quantitative Encoding

---

## 1. Visual Encodings and Perceptual Hierarchy
Data visualization maps abstract numerical or categorical data attributes to visual variables (shapes, positions, colors). Not all mappings are processed with equal accuracy by the human visual cortex.

### The Cleveland-McGill Perceptual Hierarchy
*Ranked from highest mathematical accuracy to lowest cognitive precision:*

[Most Accurate]
  1. Position along a common scale (e.g., standard Bar Chart, Scatter Plot)
  2. Position along non-aligned, identical scales (e.g., Faceted Multiples)
  3. Length, Direction, Orientation (e.g., Slope chart, Vector fields)
  4. Angle (e.g., Pie Chart - inherently difficult for judging small deltas)
  5. Area (e.g., Bubble chart, Treemap)
  6. Volume, Density, 3D space (Extremely prone to distortion)
  7. Color Saturation, Intensity, Hue (Best for categories, poor for quantities)
[Least Accurate]

### Practical Implications for Interface Design:
- The Circle/Bubble Trap: If you encode a metric into a circle's size, you MUST map the data value to the area (A = pi * r^2), not the radius (r). If you double the value and double the radius, the area quadruples, deceptively exaggerating the scale of the data change to the viewer.
- Pie Chart Overuse: Limit pie charts to 2–3 slices maximum, and only when looking for basic part-to-whole relationships (e.g., 50% split). For comparing 6 different values, a horizontal bar chart ordered by value is vastly superior.

---

## 2. Gestalt Principles in Visualization Design
The human brain automatically groups visual elements based on structural patterns. Leveraging these principles reduces cognitive load and removes the need for cluttered grids or heavy boundary borders.

- Proximity: Objects close to each other are perceived as a single conceptual group.
  * Application: Use whitespace intentionally to isolate independent chart components rather than solid lines.
- Similarity: Elements sharing visual features (color, shape, size) are grouped together.
  * Application: Use a singular accent color across different charts to signify the same data dimension or user selection.
- Enclosure: Elements bounded by a physical border or shaded background field are seen as connected.
  * Application: Use light gray or tinted background cards to group filters or KPI metrics together.
- Continuity: The eye naturally traces a continuous path or curve over abrupt directional shifts.
  * Application: Connect data points with smooth lines only when tracking a sequential trend (e.g., timeseries).

---

## 3. Human-Centric Ethics and Distortion Mitigation
Data charts are powerful rhetorical tools; small adjustments can fundamentally distort data honesty without changing the raw data numbers.

### Baseline Truncation: The Bar vs. Line Rule
- Bar Charts: The y-axis MUST start at zero. Bar charts rely on the reader comparing the relative length/area of the bars. Truncating the axis (e.g., starting a scale at 90 instead of 0 to show a drop to 88) magnifies trivial differences into visually cataclysmic shifts.
- Line Charts: The y-axis can be truncated if the primary analytical task is to track the rate of change or localized variance over time (e.g., monitoring a patient’s body temperature or stock market ticks). However, this must be explicitly signaled via gridlines and clear axis labels to avoid deceptive framing.

Deceptive (Truncated Bar)             Honest (Zero Baseline)
  100 +───┐                             100 +───┐   ┌───┐
   95 │   │   ┌───┐                      50 │   │   │   │
   90 ┴───┴───┴───┴───                    0 ┴───┴───┴───┴───
     Group A  Group B                       Group A  Group B

### Data-to-Ink Ratio (Tufte)
Maximize the proportion of ink/pixels used to display data directly vs. the ink used for structural decoration (like heavy borders, dark backgrounds, or 3D drop-shadow effects). Strip out non-essential components to maximize visual clarity for diverse end-users.