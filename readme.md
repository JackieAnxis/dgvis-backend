# DGVIS

**DGVIS** is a large scale dynamic graph visualization platform which support data-loading, searching, lay-outing, computing, and visual analytics.

**DGVIS-BACKEND** provides several algorithms for large scale visualization.

## Function

### Layout Algorithm

### Usage

supporting below:

| Method | Content-Type     | data                                                      | url                                        |
| ------ | ---------------- | --------------------------------------------------------- | ------------------------------------------ |
| POST   | application/json | {graph:<graph>,params:{<param-name>:<param-valid-value>}} | http://<host_address>/layout/<layout_name> |

#### FM^3

[more details referred](https://tulip.labri.fr/Documentation/current/tulip-python/html/tulippluginsdocumentation.html#layout	)

##### params

| name                      | type     | default                                                      | direction | description                                                  |
| :------------------------ | :------- | :----------------------------------------------------------- | :-------- | :----------------------------------------------------------- |
| Unit edge length          | `float`  | 10.0                                                         | input     | The unit edge length.                                        |
| New initial placement     | `bool`   | `True`                                                       | input     | Indicates the initial placement before running algorithm.    |
| Fixed iterations          | `int`    | 30                                                           | input     | The fixed number of iterations for the stop criterion.       |
| Threshold                 | `float`  | 0.01                                                         | input     | The threshold for the stop criterion.                        |
| Page Format               | `string` | Square  **Values:** Portrait *(A4 portrait page)* Landscape *(A4 landscape page)* Square *(Square format)* | input     | Possible page formats.                                       |
| Quality vs Speed          | `string` | BeautifulAndFast  **Values:** GorgeousAndEfficient *(Best quality)* BeautifulAndFast *(Medium quality and speed)* NiceAndIncredibleSpeed *(Best speed)* | input     | Trade-off between run-time and quality.                      |
| Edge Length Measurement   | `string` | BoundingCircle  **Values:** Midpoint *(Measure from center point of edge end points)* BoundingCircle *(Measure from border of circle surrounding edge end points)* | input     | Specifies how the length of an edge is measured.             |
| Allowed Positions         | `string` | Integer  **Values:** All Integer Exponent                    | input     | Specifies which positions for a node are allowed.            |
| Tip Over                  | `string` | NoGrowingRow  **Values:** None NoGrowingRow Always           | input     | Specifies in which case it is allowed to tip over drawings of connected components. |
| Pre Sort                  | `string` | DecreasingHeight  **Values:** None *(Do not presort)* DecreasingHeight *(Presort by decreasing height of components)* DecreasingWidth *(Presort by decreasing width of components)* | input     | Specifies how connected components are sorted before the packing algorithm is applied. |
| Galaxy Choice             | `string` | NonUniformProbLowerMass  **Values:** UniformProb NonUniformProbLowerMass NonUniformProbHigherMass | input     | Specifies how sun nodes of galaxies are selected.            |
| Max Iter Change           | `string` | LinearlyDecreasing  **Values:** Constant LinearlyDecreasing RapidlyDecreasing | input     | Specifies how MaxIterations is changed in subsequent multilevels. |
| Initial Placement Mult    | `string` | Advanced  **Values:** Simple Advanced                        | input     | Specifies how the initial placement is generated.            |
| Force Model               | `string` | New  **Values:** FruchtermanReingold *(The force-model by Fruchterman, Reingold)* Eades *(The force-model by Eades)* New *(The new force-model)* | input     | Specifies the force-model.                                   |
| Repulsive Force Method    | `string` | NMM  **Values:** Exact *(Exact calculation)* GridApproximation *(Grid approximation)* NMM *(Calculation as for new multipole method)* | input     | Specifies how to calculate repulsive forces.                 |
| Initial Placement Forces  | `string` | RandomRandIterNr  **Values:** UniformGrid *(Uniform placement on a grid)* RandomTime *(Random placement, based on current time)* RandomRandIterNr *(Random placement, based on randIterNr())* KeepPositions *(No change in placement)* | input     | Specifies how the initial placement is done.                 |
| Reduced Tree Construction | `string` | SubtreeBySubtree  **Values:** PathByPath SubtreeBySubtree    | input     | Specifies how the reduced bucket quadtree is constructed.    |
| Smallest Cell Finding     | `string` | Iteratively  **Values:** Iteratively *(Iteratively, in constant time)* Aluru *(According to formula by Aluru et al., in constant time)* | input     | Specifies how to calculate the smallest quadratic cell surrounding particles of a node in the reduced bucket quadtree. |



### Other Algorithms

Coming soon...