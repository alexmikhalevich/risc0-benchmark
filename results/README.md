# Benchmark results

## Introduction

This benchmark measures the performance of the RISC Zero (risc0) virtual machine based on the step size of the Cartesi machine executed within it. For each step size, we measured the following metrics: risc0 execution time, number of segments used, total cycles, user cycles, and the number of pages used by the Cartesi machine. The measurements were performed for the Cartesi machine with hashing enabled and hashing disabled to evaluate the impact of hashing on performance.

We evaluated the following payloads:
- `sort`: sorting 100,000 numbers using quicksort;
- `archive`: compressing a 50 MB file using gzip.
- `stress-loop`: a stress-ng loop benchmark.
- `stress-int64`: a stress-ng int64 benchmark.
- `stress-fp`: a stress-ng floating point benchmark.

## Test setup

- *Cartesi machine start mcycle*: `60,000,000` (an empty machine takes `42,051,629` mcycles to boot and halt).
- *Minimum measured Cartesi machine step size*: `50,000`
- *Maximum measured Cartesi machine step size*: `160,000`
- *Cartesi machine step size increment during measurements*: `10,000`
- *Log size at maximum Cartesi machine step size*: `1.6 MB`
- *Page size*: `4 KB`

## Results

### Sort

**risc0 metrics**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="sort_combined.png" alt="Sort: hashing enabled" width="45%">
  <img src="sort_nohash.png" alt="Sort: hashing disabled" width="45%">
</p>

**risc0 metrics, precompiled hash (SHA2)**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="sort_combined_precompiled.png" alt="Sort: hashing enabled" width="45%">
  <img src="sort_nohash.png" alt="Sort: hashing disabled" width="45%">
</p>


**Cartesi metrics**

<p align="center">
  <img src="sort_pages_combined.png" alt="Sort: hashing enabled" width="45%">
  <img src="sort_touches_combined.png" alt="Sort: hashing enabled" width="45%">
</p>

<img src="sort_memory_combined.png" alt="Sort: hashing enabled">
<img src="sort_tlb_combined.png" alt="Sort: hashing enabled">

<p align="center">
  <img src="sort_bytes_reads_nohash.png" alt="Sort: hashing disabled" width="45%">
  <img src="sort_bytes_writes_nohash.png" alt="Sort: hashing disabled" width="45%">
</p>
<img src="sort_bytes_unified_nohash.png" alt="Sort: hashing disabled">

### Archive

**risc0 metrics**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="archive_combined.png" alt="Archive: hashing enabled" width="45%">
  <img src="archive_nohash.png" alt="Archive: hashing disabled" width="45%">
</p>

**risc0 metrics, precompiled hash (SHA2)**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="archive_combined_precompiled.png" alt="Archive: hashing enabled" width="45%">
  <img src="archive_nohash.png" alt="Archive: hashing disabled" width="45%">
</p>

**Cartesi metrics**

<p align="center">
  <img src="archive_pages_combined.png" alt="Archive: hashing enabled" width="45%">
  <img src="archive_touches_combined.png" alt="Archive: hashing enabled" width="45%">
</p>

<img src="archive_memory_combined.png" alt="Archive: hashing enabled">
<img src="archive_tlb_combined.png" alt="Archive: hashing enabled">

<p align="center">
  <img src="archive_bytes_reads_nohash.png" alt="Archive: hashing disabled" width="45%">
  <img src="archive_bytes_writes_nohash.png" alt="Archive: hashing disabled" width="45%">
</p>
<img src="archive_bytes_unified_nohash.png" alt="Sort: hashing disabled">

### stress-loop

**risc0 metrics**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_loop_combined.png" alt="stress-loop: hashing enabled" width="45%">
  <img src="stress_loop_nohash.png" alt="stress-loop: hashing disabled" width="45%">
</p>

**risc0 metrics, precompiled hash (SHA2)**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_loop_combined_precompiled.png" alt="stress-loop: hashing enabled" width="45%">
  <img src="stress_loop_nohash.png" alt="stress-loop: hashing disabled" width="45%">
</p>

**Cartesi metrics**

<p align="center">
  <img src="stress_loop_pages_combined.png" alt="stress-loop: hashing enabled" width="45%">
  <img src="stress_loop_touches_combined.png" alt="stress-loop: hashing enabled" width="45%">
</p>

<img src="stress_loop_memory_combined.png" alt="stress-loop: hashing enabled">
<img src="stress_loop_tlb_combined.png" alt="stress-loop: hashing enabled">

<p align="center">
  <img src="stress_loop_bytes_reads_nohash.png" alt="stress-loop: hashing disabled" width="45%">
  <img src="stress_loop_bytes_writes_nohash.png" alt="stress-loop: hashing disabled" width="45%">
</p>
<img src="stress_loop_bytes_unified_nohash.png" alt="stress-loop: hashing disabled">

### stress-int64

**risc0 metrics**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_int64_combined.png" alt="stress-int64: hashing enabled" width="45%">
  <img src="stress_int64_nohash.png" alt="stress-int64: hashing disabled" width="45%">
</p>

**risc0 metrics, precompiled hash (SHA2)**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_int64_combined_precompiled.png" alt="stress-int64: hashing enabled" width="45%">
  <img src="stress_int64_nohash.png" alt="stress-int64: hashing disabled" width="45%">
</p>

**Cartesi metrics**

<p align="center">
  <img src="stress_int64_pages_combined.png" alt="stress-int64: hashing enabled" width="45%">
  <img src="stress_int64_touches_combined.png" alt="stress-int64: hashing enabled" width="45%">
</p>

<img src="stress_int64_memory_combined.png" alt="stress-int64: hashing enabled">
<img src="stress_int64_tlb_combined.png" alt="stress-int64: hashing enabled">

<p align="center">
  <img src="stress_int64_bytes_reads_nohash.png" alt="stress-int64: hashing disabled" width="45%">
  <img src="stress_int64_bytes_writes_nohash.png" alt="stress-int64: hashing disabled" width="45%">
</p>
<img src="stress_int64_bytes_unified_nohash.png" alt="stress-int64: hashing disabled">

### stress-fp

**risc0 metrics**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_fp_combined.png" alt="stress-fp: hashing enabled" width="45%">
  <img src="stress_fp_nohash.png" alt="stress-fp: hashing disabled" width="45%">
</p>

**risc0 metrics, precompiled hash (SHA2)**

> Cartesi machine hashing is enabled on the left and disabled on the right.

<p align="center">
  <img src="stress_fp_combined_precompiled.png" alt="stress-fp: hashing enabled" width="45%">
  <img src="stress_fp_nohash.png" alt="stress-fp: hashing disabled" width="45%">
</p>

**Cartesi metrics**

<p align="center">
  <img src="stress_fp_pages_combined.png" alt="stress-fp: hashing enabled" width="45%">
  <img src="stress_fp_touches_combined.png" alt="stress-fp: hashing enabled" width="45%">
</p>

<img src="stress_fp_memory_combined.png" alt="stress-fp: hashing enabled">
<img src="stress_fp_tlb_combined.png" alt="stress-fp: hashing enabled">

<p align="center">
  <img src="stress_fp_bytes_reads_nohash.png" alt="stress-fp: hashing disabled" width="45%">
  <img src="stress_fp_bytes_writes_nohash.png" alt="stress-fp: hashing disabled" width="45%">
</p>
<img src="stress_fp_bytes_unified_nohash.png" alt="stress-fp: hashing disabled">

## Raw data

<details>
  <summary>`sort` with hashing, metrics</summary>
  Execution Times: [24.40800225, 25.026591083, 25.52599125, 26.060533917, 26.940070958, 27.620274584, 27.911508291, 28.502488541, 28.871570667, 29.506068792, 30.088930791]
  Number of Segments: [1213, 1239, 1263, 1288, 1313, 1338, 1363, 1388, 1413, 1438, 1463]
  Total Cycles: [1271922688, 1298268160, 1324351488, 1350565888, 1376780288, 1402994688, 1429209088, 1454899200, 1481113600, 1507065856, 1533280256]
  User Cycles: [1203167107, 1226975354, 1250971773, 1274840140, 1298495028, 1322132204, 1345938345, 1369497504, 1393165231, 1417033128, 1440707744]
</details>

<details>
  <summary>`sort` with hashing (precompiled), mertrics</summary>
  Execution Times: [4.687593417, 5.288630958, 5.659733625, 6.1570415, 6.678371792, 7.332536041, 7.764924, 8.401712, 8.797254958, 9.363901334, 9.966878542]
  Number of Segments: [199, 224, 249, 273, 298, 323, 348, 373, 398, 422, 447]
  Total Cycles: [208142336, 234356736, 260308992, 286261248, 312475648, 338690048, 364380160, 390594560, 416415744, 442499072, 468713472]
  User Cycles: [189134323, 212705213, 236477101, 260119455, 283539105, 306937641, 330512367, 353834462, 377265740, 400904265, 424340936]
</details>

<details>
  <summary>`sort` with hashing, pages</summary>
  [(50000, 77), (60000, 77), (70000, 77), (80000, 77), (90000, 77), (100000, 77), (110000, 77), (120000, 77), (130000, 77), (140000, 77), (150000, 77)]
</details>

<details>
  <summary>`sort` with hashing, memory</summary>
  [(50000, Counter({'touch_page': 164861, 'read shadow': 72609, 'write shadow': 31347, 'read memory': 10007, 'write memory': 6477, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (60000, Counter({'touch_page': 197049, 'read shadow': 87006, 'write shadow': 37817, 'read memory': 11858, 'write memory': 7919, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (70000, Counter({'touch_page': 230602, 'read shadow': 102004, 'write shadow': 43632, 'read memory': 13950, 'write memory': 9535, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (80000, Counter({'touch_page': 263610, 'read shadow': 116926, 'write shadow': 49492, 'read memory': 16024, 'write memory': 11036, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (90000, Counter({'touch_page': 295779, 'read shadow': 131471, 'write shadow': 55814, 'read memory': 17926, 'write memory': 12435, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (100000, Counter({'touch_page': 327871, 'read shadow': 145822, 'write shadow': 62355, 'read memory': 19774, 'write memory': 13849, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (110000, Counter({'touch_page': 360655, 'read shadow': 160499, 'write shadow': 68515, 'read memory': 21751, 'write memory': 15353, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (120000, Counter({'touch_page': 392385, 'read shadow': 174916, 'write shadow': 74929, 'read memory': 23624, 'write memory': 16673, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (130000, Counter({'touch_page': 424535, 'read shadow': 189317, 'write shadow': 81351, 'read memory': 25517, 'write memory': 18085, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (140000, Counter({'touch_page': 457554, 'read shadow': 204092, 'write shadow': 87405, 'read memory': 27519, 'write memory': 19631, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54})), (150000, Counter({'touch_page': 489869, 'read shadow': 218504, 'write shadow': 93905, 'read memory': 29368, 'write memory': 21095, 'flush tlb': 2304, 'read pma': 173, 'translate vaddr': 67, 'replace tlb': 54}))]
</details>

<details>
  <summary>`archive` with hashing, metrics</summary>
  Execution Times: [27.688293583, 28.012971917, 28.845702625, 29.770802875, 30.685631541, 31.765195875, 31.868262375, 32.5664795, 32.985951584, 33.612534583, 33.948183084]
  Number of Segments: [1368, 1394, 1432, 1458, 1483, 1508, 1533, 1570, 1613, 1638, 1663]
  Total Cycles: [1434451968, 1460928512, 1501560832, 1528299520, 1554513920, 1581252608, 1607467008, 1646264320, 1690566656, 1716781056, 1743781888]
  User Cycles: [1356288424, 1380402286, 1417727682, 1441735190, 1465304163, 1489080960, 1512878678, 1548992276, 1588665658, 1612243220, 1636288957]
</details>

<details>
  <summary>`archive` with hashing (precompiled), metrics</summary>
  Execution Times: [4.87699675, 5.69764475, 6.057803, 6.56093175, 7.115237125, 7.638978291, 8.117960708, 8.521466291, 9.180443916, 11.114377292, 11.007183583]
  Number of Segments: [210, 236, 261, 287, 312, 337, 362, 386, 415, 440, 466]
  Total Cycles: [220200960, 246677504, 273678336, 300154880, 326369280, 352845824, 379584512, 404750336, 435159040, 461373440, 488112128]
  User Cycles: [198686013, 222530671, 246508444, 270246788, 293545083, 317051857, 340579753, 363496680, 389874280, 413181165, 436957741]
</details>

<details>
  <summary>`archive` with hashing, pages</summary>
  [(50000, 88), (60000, 88), (70000, 89), (80000, 89), (90000, 89), (100000, 89), (110000, 89), (120000, 90), (130000, 91), (140000, 91), (150000, 91)]
</details>

<details>
  <summary>`archive` with hashing, memory</summary>
  [(50000, Counter({'touch_page': 157754, 'read shadow': 70788, 'write shadow': 41796, 'read memory': 8037, 'write memory': 3964, 'flush tlb': 2304, 'read pma': 220, 'translate vaddr': 137, 'replace tlb': 66})), (60000, Counter({'touch_page': 188523, 'read shadow': 84843, 'write shadow': 50057, 'read memory': 9848, 'write memory': 4704, 'flush tlb': 2304, 'read pma': 220, 'translate vaddr': 157, 'replace tlb': 66})), (70000, Counter({'touch_page': 218488, 'read shadow': 99051, 'write shadow': 58534, 'read memory': 11190, 'write memory': 5510, 'flush tlb': 2304, 'read pma': 224, 'translate vaddr': 167, 'replace tlb': 67})), (80000, Counter({'touch_page': 249251, 'read shadow': 113109, 'write shadow': 66797, 'read memory': 13000, 'write memory': 6248, 'flush tlb': 2304, 'read pma': 224, 'translate vaddr': 187, 'replace tlb': 67})), (90000, Counter({'touch_page': 279198, 'read shadow': 127315, 'write shadow': 75276, 'read memory': 14340, 'write memory': 7051, 'flush tlb': 2304, 'read pma': 224, 'translate vaddr': 197, 'replace tlb': 67})), (100000, Counter({'touch_page': 309532, 'read shadow': 141458, 'write shadow': 83654, 'read memory': 15898, 'write memory': 7826, 'flush tlb': 2304, 'read pma': 224, 'translate vaddr': 210, 'replace tlb': 67})), (110000, Counter({'touch_page': 339904, 'read shadow': 155578, 'write shadow': 92018, 'read memory': 17489, 'write memory': 8592, 'flush tlb': 2304, 'translate vaddr': 227, 'read pma': 224, 'replace tlb': 67})), (120000, Counter({'touch_page': 369877, 'read shadow': 169781, 'write shadow': 100494, 'read memory': 18833, 'write memory': 9400, 'flush tlb': 2304, 'translate vaddr': 237, 'read pma': 228, 'replace tlb': 68})), (130000, Counter({'touch_page': 400657, 'read shadow': 183846, 'write shadow': 108756, 'read memory': 20646, 'write memory': 10138, 'flush tlb': 2304, 'translate vaddr': 257, 'read pma': 232, 'replace tlb': 69})), (140000, Counter({'touch_page': 430603, 'read shadow': 198050, 'write shadow': 117236, 'read memory': 21986, 'write memory': 10941, 'flush tlb': 2304, 'translate vaddr': 267, 'read pma': 232, 'replace tlb': 69})), (150000, Counter({'touch_page': 461366, 'read shadow': 212109, 'write shadow': 125498, 'read memory': 23796, 'write memory': 11679, 'flush tlb': 2304, 'translate vaddr': 287, 'read pma': 232, 'replace tlb': 69}))]
</details>

<details>
  <summary>`stress-loop` with hashing, metrics</summary>
  Execution Times: [59.823801667, 64.917657875, 68.254624666, 82.7117275, 91.909244792, 94.041541042, 95.812312667, 97.933236042, 100.387099833, 101.773493417, 104.3847305]
  Number of Segments: [2988, 3232, 3421, 4160, 4624, 4735, 4832, 4936, 5057, 5137, 5261]
  Total Cycles: [3132162048, 3388997632, 3586260992, 4362076160, 4848091136, 4964483072, 5066719232, 5175771136, 5302124544, 5386534912, 5516558336]
  User Cycles: [2959721419, 3200696602, 3385732634, 4102352093, 4557559224, 4661614808, 4751118801, 4851735009, 4965362580, 5039497478, 5157040769]
</details>

<details>
  <summary> `stress-loop` with hashing (precompiled), metrics</summary>
  Execution Times: [8.486942708, 9.675255333, 10.542885833, 13.025686541, 14.6224245, 15.4257435, 16.51911125, 17.06622275, 18.215802833, 19.073012875, 19.845554791]
  Number of Segments: [361, 411, 456, 579, 650, 696, 741, 779, 835, 877, 922]
  Total Cycles: [378535936, 430440448, 477626368, 606339072, 681574400, 729022464, 776208384, 816840704, 875560960, 919076864, 966787072]
  User Cycles: [336303987, 382520939, 424451593, 527606822, 591359933, 630017114, 667400391, 702923321, 751457553, 786344973, 825868781]
</details>

<details>
  <summary>`stress-loop` with hashing, pages</summary>
  [(50000, 200), (60000, 215), (70000, 226), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 322), (140000, 325), (150000, 331)]
</details>

<details>
  <summary>`stress-loop` with hashing, memory</summary>
  [(50000, Counter({'touch_page': 220500, 'read shadow': 72840, 'write shadow': 28732, 'write memory': 16540, 'read memory': 15294, 'flush tlb': 1536, 'translate vaddr': 1088, 'read pma': 690, 'replace tlb': 211})), (60000, Counter({'touch_page': 270405, 'read shadow': 87573, 'write shadow': 34159, 'write memory': 20693, 'read memory': 19626, 'flush tlb': 1536, 'translate vaddr': 1120, 'read pma': 760, 'replace tlb': 226})), (70000, Counter({'touch_page': 318134, 'read shadow': 102113, 'write shadow': 39716, 'write memory': 24465, 'read memory': 23682, 'flush tlb': 1536, 'translate vaddr': 1228, 'read pma': 822, 'replace tlb': 240})), (80000, Counter({'touch_page': 384283, 'read shadow': 116823, 'write shadow': 46777, 'read memory': 27767, 'write memory': 25946, 'flush tlb': 13056, 'read pma': 2818, 'translate vaddr': 1797, 'replace tlb': 840})), (90000, Counter({'touch_page': 448710, 'read shadow': 133196, 'write shadow': 51500, 'write memory': 30207, 'read memory': 30120, 'flush tlb': 21760, 'read pma': 3828, 'translate vaddr': 2144, 'replace tlb': 1139})), (100000, Counter({'touch_page': 493793, 'read shadow': 148056, 'write shadow': 57341, 'write memory': 33157, 'read memory': 32291, 'flush tlb': 24064, 'read pma': 4301, 'translate vaddr': 2508, 'replace tlb': 1287})), (110000, Counter({'touch_page': 533345, 'read shadow': 162539, 'write shadow': 62864, 'write memory': 36439, 'read memory': 34064, 'flush tlb': 24064, 'read pma': 4317, 'translate vaddr': 2874, 'replace tlb': 1292})), (120000, Counter({'touch_page': 574267, 'read shadow': 177581, 'write shadow': 67954, 'write memory': 40218, 'read memory': 35631, 'flush tlb': 24064, 'read pma': 4333, 'translate vaddr': 3198, 'replace tlb': 1297})), (130000, Counter({'touch_page': 615231, 'read shadow': 192636, 'write shadow': 73029, 'write memory': 44006, 'read memory': 37196, 'flush tlb': 24064, 'read pma': 4357, 'translate vaddr': 3526, 'replace tlb': 1304})), (140000, Counter({'touch_page': 653418, 'read shadow': 206710, 'write shadow': 78952, 'write memory': 46854, 'read memory': 39075, 'flush tlb': 24064, 'read pma': 4366, 'translate vaddr': 3913, 'replace tlb': 1307})), (150000, Counter({'touch_page': 694471, 'read shadow': 221803, 'write shadow': 83992, 'write memory': 50695, 'read memory': 40609, 'flush tlb': 24064, 'read pma': 4384, 'translate vaddr': 4231, 'replace tlb': 1313}))]
</details>

<details>
  <summary>`stress-int64` with hashing, metrics</summary>
  Execution Times: [59.784809792, 64.613296292, 67.856245708, 82.61569025, 92.175856625, 94.856283292, 95.945892625, 97.961629208, 100.971925416, 102.357587417, 104.633275292]
  Number of Segments: [2987, 3218, 3394, 4160, 4624, 4735, 4833, 4937, 5057, 5137, 5247]
  Total Cycles: [3132096512, 3374317568, 3558866944, 4362076160, 4848615424, 4965007360, 5066981376, 5176033280, 5302124544, 5386534912, 5501878272]
  User Cycles: [2959547330, 3186696333, 3358849830, 4102580526, 4557653509, 4661842940, 4751352431, 4851953257, 4965584253, 5039715298, 5143343987]
</details>

<details>
  <summary>`stress-int64` with hashing (precompiled), metrics</summary>
  Execution Times: [8.580115375, 9.563730084, 10.58655925, 12.997888792, 14.505975833, 15.43098525, 16.515428166, 17.186900084, 18.173005167, 18.953817709, 19.870356791]
  Number of Segments: [361, 410, 456, 579, 650, 696, 741, 780, 835, 877, 921]
  Total Cycles: [378535936, 429391872, 477364224, 606339072, 681050112, 729284608, 776470528, 817102848, 875560960, 919076864, 965738496]
  User Cycles: [336180015, 381547281, 423772649, 527633888, 591252560, 630044032, 667432792, 702940127, 751477967, 786361170, 824896329]
</details>

<details>
  <summary>`stress-int64` with hashing, pages</summary>
  [(50000, 200), (60000, 214), (70000, 224), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 322), (140000, 325), (150000, 330)]
</details>

<details>
  <summary>`stress-int64` with hashing, memory</summary>
  [(50000, Counter({'touch_page': 220179, 'read shadow': 72814, 'write shadow': 28757, 'write memory': 16490, 'read memory': 15242, 'flush tlb': 1536, 'translate vaddr': 1100, 'read pma': 690, 'replace tlb': 211})), (60000, Counter({'touch_page': 270228, 'read shadow': 87559, 'write shadow': 34162, 'write memory': 20673, 'read memory': 19588, 'flush tlb': 1536, 'translate vaddr': 1131, 'read pma': 754, 'replace tlb': 225})
), (70000, Counter({'touch_page': 318140, 'read shadow': 102124, 'write shadow': 39705, 'write memory': 24479, 'read memory': 23662, 'flush tlb': 1536, 'translate vaddr': 1234, 'read pma': 813, 'replace tlb': 237})), (80000, Counter({'touch_page': 384296, 'read shadow': 116842, 'write shadow': 46762, 'read memory': 27747, 'write memory': 25964, 'flush tlb': 13056, 'read pma': 2818, 'translate vaddr': 1796, 'replace tlb': 840})), (90000, Counter({'touch_page': 448322, 'read shadow': 133095, 'write shadow': 51599, 'read memory': 30143, 'write memory': 30089, 'flush tlb': 21760, 'read pma': 3819, 'translate vaddr': 2153, 'replace tlb': 1136})), (100000, Counter({'touch_page': 493829, 'read shadow': 148075, 'write shadow': 57323, 'write memory': 33174, 'read memory': 32278, 'flush tlb': 24064, 'read pma': 4301, 'translate vaddr': 2510, 'rep
lace tlb': 1287})), (110000, Counter({'touch_page': 533422, 'read shadow': 162566, 'write shadow': 62833, 'write memory': 36472, 'read memory': 34041, 'flush tlb': 24064, 'read pma': 4317, 'translate vaddr': 2880, 'replace tlb': 1292})), (120000, Counter({'touch_page': 574292, 'read shadow': 177612, 'write shadow': 67927, 'write memory': 40245, 'read memory': 35601, 'flush tlb': 24064, 'read pma': 4333, 'translate vaddr': 3199, 'replace tlb': 1297})), (130000, Counter({'touch_page': 615248, 'read shadow': 192650, 'write shadow': 73016, 'write memory': 44025, 'read memory': 37176, 'flush tlb': 24064, 'read pma': 4357, 'translate vaddr': 3526, 'replace tlb': 1304})), (140000, Counter({'touch_page': 653428, 'read shadow': 206701, 'write shadow': 78941, 'write memory': 46860, 'read memory': 39070, 'flush tlb': 24064, 'read pma': 4366, 'translate vaddr': 3920, 'replace tlb': 1307})), (150000, Counter({'touch_page': 694370, 'read shadow': 221768, 'write shadow': 84020, 'write memory': 50658, 'read memory': 40619, 'flush tlb': 24064, 'read pma': 4381, 'translate vaddr': 4239, 'replace tlb': 1312}))]
</details>

<details>
  <summary>`stress-fp` with hashing, metrics</summary>
  Execution Times: [59.579221041, 64.709322542, 69.335317917, 82.706369292, 91.994851042, 94.1272425, 96.252901958, 98.500104917, 101.194926209, 102.166719833, 104.606742834]
  Number of Segments: [2987, 3232, 3477, 4160, 4624, 4735, 4832, 4936, 5071, 5153, 5261]
  Total Cycles: [3132096512, 3388997632, 3645374464, 4362076160, 4848615424, 4965007360, 5066719232, 5175771136, 5316411392, 5402787840, 5516558336]
  User Cycles: [2959832749, 3200804513, 3441597326, 4102573980, 4557882755, 4661785317, 4751306776, 4851921152, 4979389220, 5054503219, 5157426314]
</details>

<details>
  <summary>`stress-fp` with hashing (precompiled), metrics</summary>
  Execution Times: [8.475657541, 10.064103167, 10.712215917, 13.091183709, 14.925844833, 15.634246917, 16.668791667, 17.118019, 18.391694375, 20.625816375, 20.225114834]
  Number of Segments: [362, 411, 460, 579, 650, 696, 741, 780, 837, 879, 922]
  Total Cycles: [378601472, 430964736, 481820672, 606339072, 681574400, 729022464, 776470528, 816971776, 876871680, 921698304, 966787072]
  User Cycles: [336465632, 382679170, 428160055, 527631075, 591482394, 629985577, 667386772, 702907860, 752356817, 788173298, 826053387]
</details>

<details>
  <summary>`stress-fp` with hashing, pages</summary>
  [(50000, 200), (60000, 215), (70000, 230), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 323), (140000, 326), (150000, 331)]
</details>

<details>
  <summary>`stress-fp` with hashing, memory</summary>
  [(50000, Counter({'touch_page': 220954, 'read shadow': 72834, 'write shadow': 28725, 'write memory': 16572, 'read memory': 15415, 'flush tlb': 1536, 'translate vaddr': 1080, 'read pma': 690, 'replace tlb': 211})), (60000, Counter({'touch_page': 270867, 'read shadow': 87571, 'write shadow': 34148, 'write memory': 20730, 'read memory': 19743, 'flush tlb': 1536, 'translate vaddr': 1112, 'read pma': 760, 'replace tlb': 226})), (70000, Counter({'touch_page': 318280, 'read shadow': 102049, 'write shadow': 39795, 'write memory': 24368, 'read memory': 23825, 'flush tlb': 1536, 'translate vaddr': 1248, 'read pma': 849, 'replace tlb': 249})), (80000, Counter({'touch_page': 384255, 'read shadow': 116772, 'write shadow': 46822, 'read memory': 27852, 'write memory': 25866, 'flush tlb': 13056, 'read pma': 2821, 'translate vaddr': 1810, 'replace tlb': 841})), (90000, Counter({'touch_page': 448840, 'read shadow': 133190, 'write shadow': 51568, 'read memory': 30215, 'write memory': 30124, 'flush tlb': 21760, 'read pma': 3900, 'translate vaddr': 2163, 'replace tlb': 1163})), (100000, Counter({'touch_page': 493599, 'read shadow': 147969, 'write shadow': 57412, 'write memory': 33078, 'read memory': 32327, 'flush tlb': 24064, 'read pma': 4301, 'translate vaddr': 2518, 'replace tlb': 1287})), (110000, Counter({'touch_page': 533208, 'read shadow': 162475, 'write shadow': 62911, 'write memory': 36373, 'read memory': 34099, 'flush tlb': 24064, 'read pma': 4317, 'translate vaddr': 2887, 'replace tlb': 1292})), (120000, Counter({'touch_page': 574150, 'read shadow': 177540, 'write shadow': 67987, 'write memory': 40172, 'read memory': 35646, 'flush tlb': 24064, 'read pma': 4333, 'translate vaddr': 3208, 'replace tlb': 1297})), (130000, Counter({'touch_page': 615104, 'read shadow': 192603, 'write shadow': 73063, 'write memory': 43968, 'read memory': 37201, 'flush tlb': 24064, 'read pma': 4360, 'translate vaddr': 3529, 'replace tlb': 1305})), (140000, Counter({'touch_page': 653954, 'read shadow': 206848, 'write shadow': 78803, 'write memory': 47026, 'read memory': 39035, 'flush tlb': 24064, 'read pma': 4369, 'translate vaddr': 3906, 'replace tlb': 1308})), (150000, Counter({'touch_page': 695139, 'read shadow': 221974, 'write shadow': 83808, 'write memory': 50905, 'read memory': 40564, 'flush tlb': 24064, 'read pma': 4384, 'translate vaddr': 4223, 'replace tlb': 1313}))]
</details>

<details>
  <summary>`sort` without hashing, metrics</summary>
  Execution Times: [4.116110958, 4.795842917, 5.25442475, 5.836159125, 6.714678416, 6.972458625, 7.541030542, 8.103924458, 8.693531667, 9.280503583, 9.850527]
  Number of Segments: [153, 178, 202, 227, 252, 277, 302, 327, 352, 377, 401]
  Total Cycles: [159449088, 185729024, 211812352, 238026752, 264241152, 290455552, 316145664, 342097920, 368312320, 394330112, 420478976]
  User Cycles: [144795148, 168603395, 192599814, 216468181, 240123069, 263760245, 287566386, 311125545, 334793272, 358661169, 382335785]
</details>

<details>
  <summary>`sort` without hashing, pages</summary>
  [(50000, 77), (60000, 77), (70000, 77), (80000, 77), (90000, 77), (100000, 77), (110000, 77), (120000, 77), (130000, 77), (140000, 77), (150000, 77)]
</details>

<details>
  <summary>`sort` without hashing, bytes</summary>
  reads: {'0x115685000': 43, '0x115686000': 8, '0x115aed000': 36, '0x116226000': 4, '0x115a4d000': 576, '0x115aec000': 36, '0x115611000': 29, '0x115684000': 53, '0x1156b7000': 12, '0x11626d000': 40, '0x11c5fd000': 32, '0x1156e9000': 24, '0x11569e000': 48, '0x1156b8000': 4, '0x1156e7000': 52, '0x1152f9000': 8, '0x114625000': 32, '0x114614000': 4, '0x114620000': 176, '0x114624000': 472, '0x114615000': 4, '0x114621000': 32, '0x11462b000': 28, '0x114623000': 8, '0x115a03000': 8, '0x115a4e000': 16, '0x115695000': 8, '0x11c5ff000': 8, '0x1156aa000': 4, '0x11626c000': 312, '0x11626f000': 8, '0x116271000': 8, '0x11626e000': 8, '0x116270000': 32, '0x11c352000': 2456, '0x11c32c000': 224, '0x11c354000': 292, '0x11c353000': 4096}
writes: {'0x115a4d000': 200, '0x115685000': 41, '0x115684000': 57, '0x1156e9000': 8, '0x11569e000': 8, '0x114625000': 8, '0x114624000': 552, '0x1156a9000': 8, '0x115aec000': 12, '0x11626c000': 16, '0x11c352000': 2456, '0x11c32c000': 224, '0x11c353000': 4096, '0x11c354000': 284}
</details>

<details>
  <summary>`archive` without hashing, metrics</summary>
  Execution Times: [4.445975875, 5.0563435, 5.8641285, 6.344612417, 6.644023125, 7.230039667, 7.78878725, 8.310911375, 9.048822458, 9.622858333, 10.206426417]
  Number of Segments: [157, 183, 208, 234, 259, 284, 309, 333, 362, 387, 412]
  Total Cycles: [164626432, 191889408, 218103808, 244449280, 270663680, 297271296, 324009984, 348258304, 378798080, 405012480, 432013312]
  User Cycles: [148108092, 172221954, 195884487, 219891995, 243460968, 267237765, 291035483, 313647258, 339711457, 363289019, 387334756]
</details>

<details>
  <summary>`archive` without hashing, pages</summary>
  [(50000, 97), (60000, 179), (70000, 273), (80000, 316), (90000, 372), (100000, 372), (110000, 380), (120000, 387), (130000, 395), (140000, 396), (150000, 407)]
</details>

<details>
  <summary>`archive` without hashing, bytes</summary>
  reads: {'0x133e85000': 43, '0x133e86000': 8, '0x1345d0000': 72, '0x134a27000': 4, '0x13424d000': 576, '0x133e11000': 29, '0x133e84000': 53, '0x133eb7000': 12, '0x134ac6000': 40, '0x13adfd000': 32, '0x133ee9000': 24, '0x133e9e000': 48, '0x133eb8000': 4, '0x133ee7000': 52, '0x133af9000': 8, '0x132e25000': 32, '0x132e14000': 4, '0x132e20000': 176, '0x132e24000': 472, '0x132e15000': 4, '0x132e21000': 32, '0x132e2b000': 28, '0x132e23000': 8, '0x134203000': 8, '0x13424e000': 16, '0x133e95000': 8, '0x13adff000': 8, '0x133eaa000': 4, '0x134ac5000': 312, '0x134ac8000': 16, '0x134aca000': 120, '0x13aa1f000': 2, '0x13aa3a000': 354, '0x13aa1b000': 36, '0x134ac7000': 8, '0x134ac9000': 8, '0x132ff2000': 64, '0x132ff7000': 44, '0x13aa19000': 4, '0x134ace000': 24, '0x13aa1c000': 18, '0x13aa1d000': 2, '0x13aa3b000': 4096, '0x13aa3c000': 1486}
writes: {'0x13424d000': 200, '0x133e85000': 41, '0x133e84000': 57, '0x133ee9000': 8, '0x133e9e000': 8, '0x132e25000': 8, '0x132e24000': 552, '0x133ea9000': 8, '0x1345d0000': 12, '0x134ac5000': 16, '0x13aa66000': 240, '0x13aa1f000': 2, '0x13aa1b000': 20, '0x132ff2000': 56, '0x13aa1c000': 19, '0x13aa60000': 23, '0x13aa1d000': 2, '0x13aa61000': 46, '0x13aa67000': 4096, '0x13aa68000': 4096, '0x13aa69000': 3204}
</details>

<details>
  <summary>`stress-loop` without hashing, metrics</summary>
  Execution Times: [6.844295417, 7.8594625, 8.765140083, 10.860310458, 12.083854792, 12.99840525, 14.048733542, 14.651155084, 15.7652835, 16.580864583, 17.534310542]
  Number of Segments: [242, 283, 322, 416, 470, 512, 555, 591, 645, 684, 726]
  Total Cycles: [252968960, 296222720, 336855040, 435224576, 492044288, 536870912, 581959680, 619708416, 675414016, 717225984, 761266176]
  User Cycles: [220012899, 257816577, 293634716, 369602654, 416104855, 452114524, 487450185, 520342558, 566246294, 599661003, 635978636]
</details>

<details>
  <summary>`stress-loop` without hashing, pages</summary>
  [(50000, 200), (60000, 215), (70000, 226), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 322), (140000, 325), (150000, 331)]
</details>

<details>
  <summary>`stress-loop` without hashing, bytes</summary>
  reads: {'0x11c2ef000': 679, '0x11be85000': 111, '0x11ca99000': 40, '0x122dfd000': 48, '0x11be12000': 24, '0x11c24d000': 584, '0x11be86000': 20, '0x11ca26000': 20, '0x11be11000': 157, '0x11be84000': 53, '0x11beb7000': 22, '0x11bee9000': 24, '0x11be9e000': 48, '0x11beb8000': 56, '0x11bee7000': 52, '0x11baf9000': 32, '0x11ae25000': 32, '0x11ae14000': 4, '0x11ae20000': 176, '0x11ae24000': 472, '0x11ae15000': 4, '0x11ae21000': 32, '0x11ae2b000': 28, '0x11ae23000': 8, '0x11c203000': 16, '0x11c24e000': 24, '0x11be95000': 8, '0x122dff000': 64, '0x11beaa000': 48, '0x11ca98000': 2360, '0x11bea9000': 204, '0x122bf0000': 114, '0x122c7c000': 3164, '0x11be8b000': 24, '0x11c653000': 129, '0x11c5c2000': 72, '0x11c266000': 28, '0x11beeb000': 12, '0x122bf1000': 152, '0x11be87000': 8, '0x11be8e000': 4, '0x11c64f000': 17, '0x11c661000': 267, '0x11c249000': 56, '0x11beea000': 64, '0x11be8a000': 129, '0x11ba1d000': 8, '0x11c543000': 74, '0x122c7b000': 72, '0x11c644000': 128, '0x11c5f5000': 16, '0x11be8f000': 8, '0x11c647000': 52, '0x122c01000': 8, '0x122dfe000': 8, '0x11afe6000': 128, '0x11c3d0000': 28, '0x122bf2000': 24, '0x11c59d000': 8, '0x11ca17000': 52, '0x11bef0000': 44, '0x11c2d3000': 56, '0x11c344000': 103, '0x11be93000': 10, '0x11c5c4000': 24, '0x11bef1000': 16, '0x11c612000': 26, '0x11c3f1000': 28, '0x11c52a000': 76, '0x122bf4000': 16, '0x11be94000': 4, '0x11c536000': 2, '0x11ba34000': 16, '0x11c508000': 16, '0x13ec39000': 4096, '0x13ec3a000': 4096, '0x13ec3b000': 4096, '0x13ec3c000': 4096, '0x13ec3d000': 4096, '0x13ec3e000': 4096, '0x13ec3f000': 4096, '0x13ec40000': 4096, '0x13ec41000': 4096, '0x13ec42000': 4096, '0x13ec43000': 4096, '0x13ec44000': 4096, '0x13ec45000': 4096, '0x13ec46000': 4096, '0x13ec47000': 4096, '0x13ec48000': 4096, '0x13ec49000': 4096, '0x13ec4a000': 4096, '0x13ec4b000': 4096, '0x13ec4c000': 4096, '0x13ec4d000': 4096, '0x13ec4e000': 4096, '0x13ec4f000': 4096, '0x13ec50000': 4096, '0x13ec51000': 4096, '0x13ec52000': 4096, '0x13ec53000': 4096, '0x13ec54000': 4096, '0x13ec55000': 4096, '0x13ec56000': 4096, '0x13ec57000': 4096, '0x13ec58000': 4096, '0x122c59000': 48, '0x122c4f000': 16, '0x11caa4000': 32, '0x11caa5000': 57, '0x11bc00000': 9, '0x11c5f0000': 120, '0x11caa2000': 160, '0x11ca9e000': 24, '0x11caa3000': 184, '0x11ba1c000': 16, '0x11be83000': 32, '0x11be0e000': 24, '0x11c27d000': 312, '0x11baf8000': 24, '0x11c2b3000': 320, '0x11c245000': 8, '0x11c297000': 8, '0x11bec4000': 8, '0x11c5ec000': 16, '0x11beb9000': 8, '0x11c202000': 64, '0x122c6c000': 16, '0x11ca9a000': 8, '0x11ca9c000': 8, '0x11afd1000': 64, '0x11ca9f000': 8, '0x122b47000': 32, '0x11caa8000': 8, '0x122aa7000': 8, '0x122aa9000': 24, '0x11ba00000': 32, '0x11caa9000': 16, '0x11caa7000': 16, '0x11c5d9000': 40, '0x122b28000': 8, '0x11c660000': 259, '0x122c7d000': 120}
writes: {'0x11c24d000': 208, '0x11be12000': 8, '0x11be85000': 41, '0x11be84000': 57, '0x11bee9000': 8, '0x11be9e000': 8, '0x11ae25000': 8, '0x11ae24000': 552, '0x11bea9000': 200, '0x11c2ef000': 522, '0x11ca98000': 2360, '0x122bf0000': 86, '0x122c7c000': 2960, '0x11be8b000': 24, '0x11ce94000': 4096, '0x122bf1000': 128, '0x11be8e000': 4, '0x11c661000': 58, '0x11c653000': 56, '0x11beaa000': 44, '0x11beea000': 64, '0x11be8a000': 129, '0x11ce95000': 4096, '0x11ce96000': 4096, '0x11ce97000': 4096, '0x11ce98000': 4096, '0x11ce99000': 4096, '0x11ce9a000': 4096, '0x122c7b000': 32, '0x11c543000': 24, '0x11c647000': 4, '0x122bf2000': 16, '0x11c644000': 80, '0x11c5c4000': 1024, '0x11c344000': 117, '0x122bf4000': 16, '0x11ce7b000': 4096, '0x11ce7c000': 4096, '0x11ce7d000': 4096, '0x11ce7e000': 4096, '0x11ce7f000': 4096, '0x11ce80000': 4096, '0x11ce81000': 4096, '0x11ce82000': 4096, '0x11ce83000': 4096, '0x11ce84000': 4096, '0x11ce85000': 4096, '0x11ce86000': 4096, '0x11ce87000': 4096, '0x11ce88000': 4096, '0x11ce89000': 4096, '0x11ce8a000': 4096, '0x11ce8b000': 4096, '0x11ce8c000': 4096, '0x11ce8d000': 4096, '0x11ce8e000': 4096, '0x11ce8f000': 4096, '0x11ce90000': 4096, '0x11ce91000': 4096, '0x11ce92000': 4096, '0x11ce93000': 4096, '0x11caa4000': 28, '0x11c5c2000': 36, '0x11caa3000': 144, '0x11be83000': 32, '0x11be11000': 108, '0x11c27d000': 213, '0x11c2b3000': 376, '0x11caa5000': 24, '0x11c5ec000': 16, '0x122c59000': 16, '0x122b28000': 48, '0x122aa7000': 24, '0x11caa9000': 64, '0x11c5d9000': 68, '0x11caa2000': 24, '0x11ce9b000': 4096, '0x11ce9c000': 4096, '0x11ce9d000': 4096, '0x11ce9e000': 4096, '0x11c660000': 242, '0x11ce9f000': 4096, '0x11cea0000': 4096, '0x11c249000': 32, '0x11cea1000': 4096, '0x11cea2000': 4096, '0x11cea3000': 4096, '0x11cea4000': 4096, '0x11cea5000': 4096, '0x11cea6000': 4096, '0x11cea7000': 4096, '0x11cea8000': 4096, '0x11cea9000': 4096, '0x11ceaa000': 4096, '0x11ceab000': 4096, '0x11ceac000': 4096, '0x11cead000': 4096, '0x11ceae000': 4096, '0x11ceaf000': 4096, '0x11ceb0000': 4096, '0x11ceb1000': 4096, '0x11ceb2000': 4096, '0x11ceb3000': 4096, '0x11ceb4000': 4096, '0x11ceb5000': 4096, '0x11ceb6000': 4096, '0x11ceb7000': 4096, '0x11ceb8000': 4096, '0x11ceb9000': 4096, '0x11ceba000': 4096, '0x122c7d000': 320, '0x11cebb000': 4096, '0x11cebc000': 856}
</details>

<details>
  <summary>`stress-int64` without hashing, metrics</summary>
  Execution Times: [7.225619167, 7.931633083, 8.775219834, 10.978940542, 12.176284209, 13.009211791, 13.9912865, 14.692022125, 15.804183375, 16.549565167, 17.474033708]
  Number of Segments: [242, 282, 323, 416, 470, 513, 555, 591, 645, 684, 725]
  Total Cycles: [252968960, 295698432, 338165760, 435421184, 491913216, 537001984, 581959680, 619708416, 675807232, 717225984, 760217600]
  User Cycles: [219892490, 257425491, 294131318, 369616367, 415984420, 452127936, 487469095, 520346086, 566253247, 599664103, 635568957]
</details>

<details>
  <summary>`stress-int64` without hashing, pages</summary>
  [(50000, 200), (60000, 214), (70000, 224), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 322), (140000, 325), (150000, 330)]
</details>

<details>
  <summary>`stress-int64` without hashing, bytes</summary>
  reads: {'0x144aef000': 679, '0x144685000': 111, '0x145279000': 40, '0x14b5fd000': 48, '0x144612000': 24, '0x144a4d000': 584, '0x144686000': 20, '0x145226000': 20, '0x144611000': 157, '0x144684000': 53, '0x1446b7000': 22, '0x1446e9000': 24, '0x14469e000': 48, '0x1446b8000': 56, '0x1446e7000': 52, '0x1442f9000': 32, '0x143625000': 32, '0x143614000': 4, '0x143620000': 176, '0x143624000': 472, '0x143615000': 4, '0x143621000': 32, '0x14362b000': 28, '0x143623000': 8, '0x144a03000': 16, '0x144a4e000': 24, '0x144695000': 8, '0x14b5ff000': 64, '0x1446aa000': 48, '0x145278000': 2360, '0x14b47c000': 3164, '0x144e53000': 129, '0x144e4f000': 17, '0x144e61000': 267, '0x1446a9000': 204, '0x14b3f0000': 114, '0x14468b000': 24, '0x144dc2000': 72, '0x144a66000': 28, '0x1446eb000': 12, '0x14b3f1000': 152, '0x144687000': 8, '0x14468e000': 4, '0x144a49000': 56, '0x1446ea000': 64, '0x14468a000': 129, '0x14421d000': 8, '0x144d43000': 74, '0x14b47b000': 72, '0x144e44000': 128, '0x144df5000': 16, '0x14468f000': 8, '0x144e47000': 52, '0x14b401000': 8, '0x14b5fe000': 8, '0x1437e6000': 128, '0x144bd0000': 28, '0x14b3f2000': 24, '0x144d9d000': 8, '0x145217000': 52, '0x1446f0000': 44, '0x144ad3000': 56, '0x144b44000': 103, '0x144693000': 10, '0x144dc4000': 24, '0x1446f1000': 16, '0x144e12000': 26, '0x144bf1000': 28, '0x144d2a000': 76, '0x14b3f4000': 16, '0x144694000': 4, '0x144d36000': 2, '0x144234000': 16, '0x144d08000': 16, '0x1103cd000': 4096, '0x1103ce000': 4096, '0x1103cf000': 4096, '0x1103d0000': 4096, '0x1103d1000': 4096, '0x1103d2000': 4096, '0x1103d3000': 4096, '0x1103d4000': 4096, '0x1103d5000': 4096, '0x1103d6000': 4096, '0x1103d7000': 4096, '0x1103d8000': 4096, '0x1103d9000': 4096, '0x1103da000': 4096, '0x1103db000': 4096, '0x1103dc000': 4096, '0x1103dd000': 4096, '0x1103de000': 4096, '0x1103df000': 4096, '0x1103e0000': 4096, '0x1103e1000': 4096, '0x1103e2000': 4096, '0x1103e3000': 4096, '0x1103e4000': 4096, '0x1103e5000': 4096, '0x1103e6000': 4096, '0x1103e7000': 4096, '0x1103e8000': 4096, '0x1103e9000': 4096, '0x1103ea000': 4096, '0x1103eb000': 4096, '0x1103ec000': 4096, '0x14b459000': 48, '0x14b44f000': 16, '0x1452a4000': 32, '0x1452a5000': 57, '0x144400000': 9, '0x144df0000': 120, '0x1452a2000': 160, '0x14529e000': 24, '0x1452a3000': 184, '0x14421c000': 16, '0x144683000': 32, '0x14460e000': 24, '0x144a7d000': 312, '0x1442f8000': 24, '0x144ab3000': 320, '0x144a45000': 8, '0x144a97000': 8, '0x1446c4000': 8, '0x144dec000': 16, '0x1446b9000': 8, '0x144a02000': 64, '0x14b46c000': 16, '0x14527a000': 8, '0x14529c000': 8, '0x1437d1000': 64, '0x14529f000': 8, '0x14b347000': 32, '0x1452a8000': 8, '0x14b2a7000': 8, '0x14b2a9000': 24, '0x144200000': 32, '0x1452a9000': 16, '0x1452a7000': 16, '0x144dd9000': 40, '0x14b327000': 8, '0x144e60000': 259, '0x14b47d000': 120}
writes: {'0x144a4d000': 208, '0x144612000': 8, '0x144685000': 41, '0x144684000': 57, '0x1446e9000': 8, '0x14469e000': 8, '0x143625000': 8, '0x143624000': 552, '0x1446a9000': 200, '0x144aef000': 522, '0x14b47c000': 2956, '0x145278000': 2360, '0x14b3f0000': 86, '0x14468b000': 24, '0x145694000': 4096, '0x14b3f1000': 128, '0x14468e000': 4, '0x144e61000': 58, '0x144e53000': 56, '0x1446aa000': 44, '0x1446ea000': 64, '0x14468a000': 129, '0x145695000': 4096, '0x145696000': 4096, '0x145697000': 4096, '0x145698000': 4096, '0x145699000': 4096, '0x14569a000': 4096, '0x14b47b000': 32, '0x144d43000': 24, '0x144e47000': 4, '0x14b3f2000': 16, '0x144e44000': 80, '0x144dc4000': 1024, '0x144b44000': 117, '0x14b3f4000': 16, '0x14567b000': 4096, '0x14567c000': 4096, '0x14567d000': 4096, '0x14567e000': 4096, '0x14567f000': 4096, '0x145680000': 4096, '0x145681000': 4096, '0x145682000': 4096, '0x145683000': 4096, '0x145684000': 4096, '0x145685000': 4096, '0x145686000': 4096, '0x145687000': 4096, '0x145688000': 4096, '0x145689000': 4096, '0x14568a000': 4096, '0x14568b0
00': 4096, '0x14568c000': 4096, '0x14568d000': 4096, '0x14568e000': 4096, '0x14568f000': 4096, '0x145690000': 4096, '0x145691000': 4096, '0x145692000': 4096, '0x145693000': 4096, '0x1452a4000': 28, '0x144dc2000': 36, '0x1452a3000': 144, '0x144683000': 32, '0x144611000': 108, '0x144a7d000': 213, '0x144ab3000': 376, '0x1452a5000': 24, '0x144dec000': 16, '0x14b459000': 16, '0x14b327000': 48, '0x14b2a7000': 24, '0x1452a9000': 64, '0x144dd9000': 68, '0x1452a2000': 24, '0x14569b000': 4096, '0x14569c000': 4096, '0x14569d000': 4096, '0x14569e000': 4096, '0x144e60000': 242, '0x14569f000': 4096, '0x1456a0000': 4096, '0x144a49000': 32, '0x1456a1000': 4096, '0x1456a2000': 4096, '0x1456a3000': 4096, '0x1456a4000': 4096, '0x1456a5000': 4096, '0x1456a6000': 4096, '0x1456a7000': 4096, '0x1456a8000': 4096, '0x1456a9000': 4096, '0x1456aa000': 4096, '0x14
56ab000': 4096, '0x1456ac000': 4096, '0x1456ad000': 4096, '0x1456ae000': 4096, '0x1456af000': 4096, '0x1456b0000': 4096, '0x1456b1000': 4096, '0x1456b2000': 4096, '0x1456b3000': 4096, '0x1456b4000': 4096, '0x1456b5000': 4096, '0x1456b6000': 4096, '0x1456b7000': 4096, '0x1456b8000': 4096, '0x1456b9000': 4096, '0x1456ba000': 4096, '0x14b47d000': 320, '0x1456bb000': 4096}
</details>

<details>
  <summary>`stress-fp` without hashing, metrics</summary>
  Execution Times: [6.857303958, 7.869118625, 8.826099792, 10.847246042, 12.111128, 13.002567667, 13.870791042, 14.659953583, 15.783684208, 16.582118958, 17.589230542]
  Number of Segments: [242, 283, 323, 416, 470, 512, 555, 591, 645, 686, 726]
  Total Cycles: [253231104, 296747008, 338165760, 435421184, 492830720, 536870912, 581959680, 619708416, 675545088, 718798848, 761266176]
  User Cycles: [220177909, 257978168, 295008996, 369609821, 416213666, 452070313, 487423440, 520313981, 566556391, 600896521, 636149461]
</details>

<details>
  <summary>`stress-fp` without hashing, pages</summary>
  [(50000, 200), (60000, 215), (70000, 230), (80000, 273), (90000, 303), (100000, 308), (110000, 312), (120000, 317), (130000, 323), (140000, 326), (150000, 331)]
</details>

<details>
  <summary>`stress-fp` without hashing, bytes</summary>
  reads: {'0x137aef000': 679, '0x137685000': 111, '0x138279000': 40, '0x13e5fd000': 48, '0x137612000': 24, '0x137a4d000': 584, '0x137686000': 20, '0x138226000': 20, '0x137611000': 157, '0x137684000': 53, '0x1376b7000': 22, '0x1376e9000': 24, '0x13769e000': 48, '0x1376b8000': 56, '0x1376e7000': 52, '0x1372f9000': 32, '0x136625000': 32, '0x136614000': 4, '0x136620000': 176, '0x136624000': 472, '0x136615000': 4, '0x136621000': 32, '0x13662b000': 28, '0x136623000': 8, '0x137a03000': 16, '0x137a4e000': 24, '0x137695000': 8, '0x13e5ff000': 64, '0x1376aa000': 48, '0x138278000': 2360, '0x13e47c000': 3156, '0x137e53000': 129, '0x137dc2000': 72, '0x137a66000': 28, '0x1376eb000': 12, '0x13e3f1000': 152, '0x137687000': 8, '0x13768e000': 4, '0x137e4f000': 17, '0x137e61000': 267, '0x137a49000': 56, '0x1376ea000': 64, '0x13768a000': 129, '0x1376a9000': 204, '0x13e3f0000': 114, '0x13768b000': 24, '0x13721d000': 8, '0x137d43000': 74, '0x13e47b000': 72, '0x137e44000': 128, '0x137df5000': 16, '0x13768f000': 8, '0x137e47000': 52, '0x13e401000': 8, '0x13e5fe000': 8, '0x1367e6000': 128, '0x137bd0000': 28, '0x13e3f2000': 24, '0x137d9d000': 8, '0x138217000': 52, '0x1376f0000': 44, '0x137ad3000': 56, '0x137b44000': 103, '0x137693000': 10, '0x137dc4000': 24, '0x1376f1000': 16, '0x137e12000': 26, '0x137bf1000': 28, '0x137d2a000': 76, '0x13e3f4000': 16, '0x137694000': 4, '0x137d36000': 2, '0x137234000': 16, '0x137d08000': 16, '0x10e451000': 4096, '0x10e452000': 4096, '0x10e453000': 4096, '0x10e454000': 4096, '0x10e455000': 4096, '0x10e456000': 4096, '0x10e457000': 4096, '0x10e458000': 4096, '0x10e459000': 4096, '0x10e45a000': 4096, '0x10e45b000': 4096, '0x10e45c000': 4096, '0x10e45d000': 4096, '0x10e45e000': 4096, '0x10e45f000': 4096, '0x10e460000': 4096, '0x10e461000': 4096, '0x10e462000': 4096, '0x10e463000': 4096, '0x10e464000': 4096, '0x10e465000': 4096, '0x10e466000': 4096, '0x10e467000': 4096, '0x10e468000': 4096, '0x10e469000': 4096, '0x10e46a000': 4096, '0x10e46b000': 4096, '0x10e46c000': 4096, '0x10e46d000': 4096, '0x10e46e000': 4096, '0x10e46f000': 4096, '0x10e470000': 4096, '0x13e459000': 48, '0x13e44f000': 16, '0x1382a4000': 32, '0x1382a5000': 57, '0x137400000': 9, '0x137df0000': 120, '0x1382a2000': 160, '0x13829e000': 24, '0x1382a3000': 184, '0x13721c000': 16, '0x137683000': 32, '0x13760e000': 24, '0x137a7d000': 312, '0x1372f8000': 24, '0x137ab3000': 320, '0x137a45000': 8, '0x137a97000': 8, '0x1376c4000': 8, '0x137dec000': 16, '0x1376b9000': 8, '0x137a02000': 64, '0x13e46c000': 16, '0x13827a000': 8, '0x13829c000': 8, '0x1367d1000': 64, '0x13829f000': 8, '0x13e347000': 32, '0x1382a8000': 8, '0x13e2a7000': 8, '0x13e2a9000': 24, '0x137200000': 32, '0x1382a9000': 16, '0x1382a7000': 16, '0x137dd9000': 40, '0x13e327000': 8, '0x137e60000': 259, '0x13e47d000': 120}
writes: {'0x137a4d000': 208, '0x137612000': 8, '0x137685000': 41, '0x137684000': 57, '0x1376e9000': 8, '0x13769e000': 8, '0x136625000': 8, '0x136624000': 552, '0x1376a9000': 200, '0x137aef000': 522, '0x138694000': 4096, '0x13e47c000': 2952, '0x138278000': 2360, '0x13e3f1000': 128, '0x13768e000': 4, '0x137e61000': 58, '0x137e53000': 56, '0x1376aa000': 44, '0x1376ea000': 64, '0x13768a000': 129, '0x13e3f0000': 86, '0x13768b000': 24, '0x138695000': 4096, '0x138696000': 4096, '0x138697000': 4096, '0x138698000': 4096, '0x138699000': 4096, '0x13869a000': 4096, '0x13e47b000': 32, '0x137d43000': 24, '0x137e47000': 4, '0x13e3f2000': 16, '0x137e44000': 80, '0x137dc4000': 1024, '0x137b44000': 117, '0x13e3f4000': 16, '0x13867b000': 4096, '0x13867c000': 4096, '0x13867d000': 4096, '0x13867e000': 4096, '0x13867f000': 4096, '0x138680000': 4096, '0x138681000': 4096, '0x138682000': 4096, '0x138683000': 4096, '0x138684000': 4096, '0x138685000': 4096, '0x138686000': 4096, '0x138687000': 4096, '0x138688000': 4096, '0x138689000': 4096, '0x13868a000': 4096, '0x13868b000': 4096, '0x13868c000': 4096, '0x13868d000': 4096, '0x13868e000': 4096, '0x13868f000': 4096, '0x138690000': 4096, '0x138691000': 4096, '0x138692000': 4096, '0x138693000': 4096, '0x1382a4000': 28, '0x137dc2000': 36, '0x1382a3000': 144, '0x137683000': 32, '0x137611000': 108, '0x137a7d000': 213, '0x137ab3000': 376, '0x1382a5000': 24, '0x137dec000': 16, '0x13e459000': 16, '0x13e327000': 48, '0x13e2a7000': 24, '0x1382a9000': 64, '0x137dd9000': 68, '0x1382a2000': 24, '0x13869b000': 4096, '0x13869c000': 4096, '0x13869d000': 4096, '0x13869e000': 4096, '0x137e60000': 242, '0x13869f000': 4096, '0x1386a0000': 4096, '0x137a49000': 32, '0x1386a1000': 4096, '0x1386a2000': 4096, '0x1386a3000': 4096, '0x1386a4000': 4096, '0x1386a5000': 4096, '0x1386a6000': 4096, '0x1386a7000': 4096, '0x1386a8000': 4096, '0x1386a9000': 4096, '0x1386aa000': 4096, '0x1386ab000': 4096, '0x1386ac000': 4096, '0x1386ad000': 4096, '0x1386ae000': 4096, '0x1386af000': 4096, '0x1386b0000': 4096, '0x1386b1000': 4096, '0x1386b2000': 4096, '0x1386b3000': 4096, '0x1386b4000': 4096, '0x1386b5000': 4096, '0x1386b6000': 4096, '0x1386b7000': 4096, '0x1386b8000': 4096, '0x1386b9000': 4096, '0x1386ba000': 4096, '0x13e47d000': 320, '0x1386bb000': 4096, '0x1386bc000': 3560}
</details>
