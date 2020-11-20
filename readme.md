# DGVIS

**DGVIS** is a large scale dynamic graph visualization platform which support data-loading, searching, lay-outing, computing, and visual analytics.

**DGVIS-BACKEND** provides several algorithms for large scale visualization.

## Usage

```
cd src
pip install -r requirement.txt
```

## Function

### Layout Algorithm

### Usage

supporting below:

| Method | Content-Type     | data                                                      | url                                 |
| ------ | ---------------- | --------------------------------------------------------- | ----------------------------------- |
| POST   | application/json | {graph:<graph>,params:{<param-name>:<param-valid-value>}} | http://<host_address>/<layout_name> |

#### FM^3

[more details referred](https://tulip.labri.fr/Documentation/current/tulip-python/html/tulippluginsdocumentation.html#layout)

##### params

| name                      | type     | default                                                                                                                                                                                                                               | direction | description                                                                                                            |
| :------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------- | :--------------------------------------------------------------------------------------------------------------------- |
| Unit edge length          | `float`  | 10.0                                                                                                                                                                                                                                  | input     | The unit edge length.                                                                                                  |
| New initial placement     | `bool`   | `True`                                                                                                                                                                                                                                | input     | Indicates the initial placement before running algorithm.                                                              |
| Fixed iterations          | `int`    | 30                                                                                                                                                                                                                                    | input     | The fixed number of iterations for the stop criterion.                                                                 |
| Threshold                 | `float`  | 0.01                                                                                                                                                                                                                                  | input     | The threshold for the stop criterion.                                                                                  |
| Page Format               | `string` | Square **Values:** Portrait _(A4 portrait page)_ Landscape _(A4 landscape page)_ Square _(Square format)_                                                                                                                             | input     | Possible page formats.                                                                                                 |
| Quality vs Speed          | `string` | BeautifulAndFast **Values:** GorgeousAndEfficient _(Best quality)_ BeautifulAndFast _(Medium quality and speed)_ NiceAndIncredibleSpeed _(Best speed)_                                                                                | input     | Trade-off between run-time and quality.                                                                                |
| Edge Length Measurement   | `string` | BoundingCircle **Values:** Midpoint _(Measure from center point of edge end points)_ BoundingCircle _(Measure from border of circle surrounding edge end points)_                                                                     | input     | Specifies how the length of an edge is measured.                                                                       |
| Allowed Positions         | `string` | Integer **Values:** All Integer Exponent                                                                                                                                                                                              | input     | Specifies which positions for a node are allowed.                                                                      |
| Tip Over                  | `string` | NoGrowingRow **Values:** None NoGrowingRow Always                                                                                                                                                                                     | input     | Specifies in which case it is allowed to tip over drawings of connected components.                                    |
| Pre Sort                  | `string` | DecreasingHeight **Values:** None _(Do not presort)_ DecreasingHeight _(Presort by decreasing height of components)_ DecreasingWidth _(Presort by decreasing width of components)_                                                    | input     | Specifies how connected components are sorted before the packing algorithm is applied.                                 |
| Galaxy Choice             | `string` | NonUniformProbLowerMass **Values:** UniformProb NonUniformProbLowerMass NonUniformProbHigherMass                                                                                                                                      | input     | Specifies how sun nodes of galaxies are selected.                                                                      |
| Max Iter Change           | `string` | LinearlyDecreasing **Values:** Constant LinearlyDecreasing RapidlyDecreasing                                                                                                                                                          | input     | Specifies how MaxIterations is changed in subsequent multilevels.                                                      |
| Initial Placement Mult    | `string` | Advanced **Values:** Simple Advanced                                                                                                                                                                                                  | input     | Specifies how the initial placement is generated.                                                                      |
| Force Model               | `string` | New **Values:** FruchtermanReingold _(The force-model by Fruchterman, Reingold)_ Eades _(The force-model by Eades)_ New _(The new force-model)_                                                                                       | input     | Specifies the force-model.                                                                                             |
| Repulsive Force Method    | `string` | NMM **Values:** Exact _(Exact calculation)_ GridApproximation _(Grid approximation)_ NMM _(Calculation as for new multipole method)_                                                                                                  | input     | Specifies how to calculate repulsive forces.                                                                           |
| Initial Placement Forces  | `string` | RandomRandIterNr **Values:** UniformGrid _(Uniform placement on a grid)_ RandomTime _(Random placement, based on current time)_ RandomRandIterNr _(Random placement, based on randIterNr())_ KeepPositions _(No change in placement)_ | input     | Specifies how the initial placement is done.                                                                           |
| Reduced Tree Construction | `string` | SubtreeBySubtree **Values:** PathByPath SubtreeBySubtree                                                                                                                                                                              | input     | Specifies how the reduced bucket quadtree is constructed.                                                              |
| Smallest Cell Finding     | `string` | Iteratively **Values:** Iteratively _(Iteratively, in constant time)_ Aluru _(According to formula by Aluru et al., in constant time)_                                                                                                | input     | Specifies how to calculate the smallest quadratic cell surrounding particles of a node in the reduced bucket quadtree. |

### Circular (OGDF)

[more details referred](https://tulip.labri.fr/Documentation/current/tulip-python/html/tulippluginsdocumentation.html#layout)

##### params

| name           | type    | default | direction | description                                           |
| :------------- | :------ | :------ | :-------- | :---------------------------------------------------- |
| minDistCircle  | `float` | 20      | input     | The minimal distance between nodes on a circle.       |
| minDistLevel   | `float` | 20      | input     | The minimal distance between father and child circle. |
| minDistSibling | `float` | 10      | input     | The minimal distance between circles on same level.   |
| minDistCC      | `float` | 20      | input     | The minimal distance between connected components.    |
| pageRatio      | `float` | 1       | input     | The page ratio used for packing connected components. |

### Other Algorithms

Coming soon...
