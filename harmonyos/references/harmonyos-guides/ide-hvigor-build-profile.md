---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile
title: 模块级build-profile.json5文件
breadcrumb: 指南 > 构建应用 > 配置文件 > 模块级build-profile.json5文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cd57ec9215f1db5be50adc5b59a036f5188b6cfc7857ed84268250e2391baf4
---

## 配置文件结构

模块级build-profile.json5文件整体的结构如下。

```
1. apiType
2. targets
3. └── name
4. └── runtimeOS
5. └── config
6. └── distroFilter / distributionFilter
7. └── apiVersion
8. └── policy
9. └── value
10. └── screenShape
11. └── policy
12. └── value
13. └── screenWindow
14. └── policy
15. └── value
16. └── screenDensity
17. └── policy
18. └── value
19. └── countryCode
20. └── policy
21. └── value
22. └── deviceType
23. └── buildOption
24. └── atomicService
25. └── preloads
26. └── moduleName
27. └── source
28. └── abilities
29. └── name
30. └── pages
31. └── res
32. └── icon
33. └── label
34. └── launchType
35. └── pages
36. └── sourceRoots
37. └── resource
38. └── directories
39. └── output
40. └── artifactName
41. showInServiceCenter
42. buildOption
43. buildOptionSet
44. └── name
45. └── debuggable
46. └── generateSharedTgz
47. └── copyFrom
48. └── resOptions
49. └── compression
50. └── media
51. └── enable
52. └── filters
53. └── method
54. └── type
55. └── blocks
56. └── files
57. └── path
58. └── size
59. └── resolution
60. └── exclude
61. └── path
62. └── size
63. └── resolution
64. └── resCompileThreads
65. └── copyCodeResource
66. └── enable
67. └── includes
68. └── excludes
69. └── ignoreResourcePattern
70. └── excludeHarRes
71. └── includeAppScopeRes
72. └── qualifiersConfig
73. └── Mcc&Mnc
74. └── Locale
75. └── Orientation
76. └── Device
77. └── ColorMode
78. └── Density
79. └── externalNativeOptions
80. └── path
81. └── abiFilters
82. └── arguments
83. └── cppFlags
84. └── cFlags
85. └── targets
86. └── sourceOption
87. └── workers
88. └── nativeLib
89. └── filter
90. └── excludes
91. └── pickFirsts
92. └── pickLasts
93. └── enableOverride
94. └── select
95. └── package
96. └── version
97. └── includePattern
98. └── excludePattern
99. └── include
100. └── exclude
101. └── debugSymbol
102. └── strip
103. └── exclude
104. └── headerPath
105. └── collectAllLibs
106. └── excludeFromHar
107. └── excludeSoFromInterfaceHar
108. └── excludeSoFromBinXO
109. └── librariesInfo
110. └── name
111. └── linkLibraries
112. └── napiLibFilterOption
113. └── excludes
114. └── pickFirsts
115. └── pickLasts
116. └── enableOverride
117. └── arkOptions
118. └── runtimeOnly
119. └── sources
120. └── packages
121. └── excludePackages
122. └── types
123. └── obfuscation
124. └── ruleOptions
125. └── enable
126. └── files
127. └── consumerFiles
128. └── buildProfileFields
129. └── integratedHsp
130. └── transformLib
131. └── branchElimination
132. └── byteCodeHar
133. └── bundledDependencies
134. └── packSourceMap
135. └── autoLazyImport
136. └── autoLazyFilter
137. └── include
138. └── exclude
139. └── reExportCheckMode
140. └── skipOhModulesLint
141. └── expandImportPath
142. └── enable
143. └── exclude
144. └── apPath
145. └── hostPGO
146. └── packingOptions
147. └── asset
148. └── include
149. └── exclude
150. └── customizedOptions
151. └── basePackage
152. └── removePermissions
153. └── name
154. buildModeBinder
155. └── buildModeName
156. └── mappings
157. └── targetName
158. └── buildOptionName
159. entryModules
```

## 配置文件字段说明

下表为"Ability"类型的Module（HAP）对应的模块级build-profile.json5中配置项包含的字段，"Library"类型的Module（HAR和HSP）对应的模块级build-profile.json5中配置项为下表罗列范围的子集。

**表1** 模块级build-profile.json5文件字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| apiType | 字符串 | 可选 | API模型类型：   * stageMode：Stage模型，后续长期演进的模型，推荐使用该模型。 * faMode：FA模型。 |
| [targets](ide-hvigor-build-profile.md#section517483765814) | 对象数组 | 可选 | 定义的target，可配置多个；若配置，数组长度至少为1。 |
| showInServiceCenter | 布尔值 | 可选 | 是否显示在服务中心：   * true：显示。 * false（缺省默认值）：不显示。 |
| [buildOption](ide-hvigor-build-profile.md#section1010733210421) | 对象 | 可选 | 模块在构建过程中的相关配置。  其中不支持配置name、debuggable和copyFrom字段。  在FA模型中，arkOptions配置中仅支持配置types字段。 |
| buildOptionSet | 对象数组 | 可选 | [表16](ide-hvigor-build-profile.md#table370712453588)buildOption的集合，其中name字段必填，每个配置都是当前支持的编译过程中所有可用工具的通用配置选项集。 |
| [buildModeBinder](ide-hvigor-build-profile.md#section642017215409) | 对象数组 | 可选 | 构建模式（debug、release 等）与构建配置（buildOption）的关联配置。通过该配置可以将不同的构建配置和target进行组合，并绑定到对应的构建模式上，其中构建模式需要在工程级别的构建模式列表中已定义。 |
| entryModules | 字符串数组 | 可选 | Feature类型模块所关联的入口模块，仅对FA模型工程生效。 |

## targets

targets用于给模块配置[多目标产物](ide-customized-multi-targets-and-products.md)，可配置多个；若配置，数组长度至少为1。

**表2** targets

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | target名称。 |
| runtimeOS | 字符串 | 可选 | target的目标运行环境：   * HarmonyOS * OpenHarmony |
| [config](ide-hvigor-build-profile.md#section1967714835919) | 对象 | 可选 | target相关配置。 |
| [source](ide-hvigor-build-profile.md#section1838814817017) | 对象 | 可选 | target的源码范围。 |
| [resource](ide-hvigor-build-profile.md#table2065415762214) | 对象 | 可选 | target包含的资源目录。 |
| [output](ide-hvigor-build-profile.md#table965613111225) | 对象 | 可选 | 定制产品生成的应用包的配置。 |

**表3** resource

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| directories | 字符串数组 | 可选 | 资源目录地址。 |

**表4** output

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| artifactName | 字符串 | 必选 | 自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |

targets字段示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "resource": {
5. "directories": ["./src/main/resources"]
6. },
7. "output": {
8. "artifactName": "customizedTargetOutputName-1.0.0"
9. }
10. }
11. ]
```

## config

config是target相关配置。

**表5** config

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [distroFilter](ide-hvigor-build-profile.md#section113212281909) | 对象 | 可选 | 应用市场分发规则。在FA模型中使用。 |
| [distributionFilter](ide-hvigor-build-profile.md#section113212281909) | 对象 | 可选 | 应用市场分发规则。在Stage模型中使用。 |
| deviceType | 字符串数组 | 可选 | target支持的设备类型，必须在module.json5中已定义。  在FA模型中，对应的文件为config.json。 |
| [buildOption](ide-hvigor-build-profile.md#section1010733210421) | 对象 | 可选 | 模块在构建过程中的相关配置。  其中不支持配置name、debuggable和copyFrom字段。 |
| [atomicService](ide-hvigor-build-profile.md#section106753237212) | 对象 | 可选 | 元服务相关配置，仅支持在Stage模型中配置。 |

## source

source用于指定target的源码范围。

**表6** source

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [abilities](ide-hvigor-build-profile.md#section1281869320) | 对象数组 | 可选 | 自定义target的能力范围。  在FA模型工程中支持对Ability源码目录下的page页面进行定制。 |
| [pages](ide-customized-multi-targets-and-products-guides.md#section73018336472) | 字符串数组 | 可选 | Stage模型工程中支持对pages源码目录的page页面进行定制，数组长度至少为1。 |
| [sourceRoots](ide-customized-multi-targets-and-products-guides.md#section18668905913) | 字符串数组 | 可选 | Stage模型工程中支持对差异化代码空间进行定制，数组长度至少为1。数组中的值有以下限制：   1. 必须唯一； 2. 必须为相对路径； 3. 类型必须为文件夹； 4. 文件夹必须真实存在； 5. 文件夹必须与src/main同级；   当数组中存在多个值时，寻址的优先级为数组中值的顺序。 |

source字段示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "source": {
5. "pages": [         // Stage模型
6. "pages/Index"
7. ],
8. "abilities": [     // FA模型
9. {
10. "name": ".MainAbility",
11. "pages": [
12. "pages/index"
13. ]
14. }
15. ],
16. "sourceRoots": [
17. "./src/default"
18. ]
19. }
20. }
21. ]
```

## distroFilter/distributionFilter

distroFilter/distributionFilter用于指定应用市场分发规则，distroFilter在FA模型中使用，distributionFilter在Stage模型中使用。

**表7** distroFilter/distributionFilter

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [apiVersion](ide-hvigor-build-profile.md#section10176358110) | 对象 | 可选 | 支持的apiVersion范围。 |
| [screenShape](ide-hvigor-build-profile.md#section1927031812114) | 对象 | 可选 | 屏幕形状的支持策略。 |
| [screenWindow](ide-hvigor-build-profile.md#section79432241314) | 对象 | 可选 | 应用运行时窗口的分辨率支持策略。 |
| [screenDensity](ide-hvigor-build-profile.md#section99812302013) | 对象 | 可选 | 屏幕的像素密度支持策略。 |
| [countryCode](ide-hvigor-build-profile.md#section04873351417) | 对象 | 可选 | 应用需要分发的国家地区码。 |

### apiVersion

**表8** apiVersion

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则：   * include：需要包含的value属性。 * exclude：需要排除的value属性。 |
| value | 整型数组 | 必选 | 支持的取值为API Version存在的整数值，例如10。 |

### screenShape

**表9** screenShape

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则：   * include：需要包含的value属性。 * exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 支持的取值范围：   * circle：圆形 * rect：矩形 |

### screenWindow

**表10** screenWindow

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 当前取值仅支持“include”。   * include：需要包含的value属性。 |
| value | 字符串数组 | 必选 | 单个字符串的取值格式为“宽\*高”，取值为整数像素值，例如"454\*454"。 |

### screenDensity

**表11** screenDensity

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则：   * include：需要包含的value属性。 * exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 取值范围：   * sdpi：小规模的屏幕密度（Small-scale Dots per Inch），适用于dpi取值为(0,120]的设备。 * mdpi：中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120,160]的设备。 * ldpi：大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160,240]的设备。 * xldpi：大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240,320]的设备。 * xxldpi：大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320，480]的设备。 * xxxldpi：表示大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。 |

### countryCode

**表12** countryCode

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则：   * include：需要包含的value属性。 * exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 国家地区码取值，具体值以ISO-3166-1标准为准。支持多个国家和地区枚举定义。 |

distroFilter/distributionFilter字段示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "distributionFilter": {
6. "apiVersion": {
7. "policy": "include",
8. "value": [12]
9. },
10. "screenShape": {
11. "policy": "include",
12. "value": [
13. "circle",
14. "rect"
15. ]
16. },
17. "screenWindow": {
18. "policy": "include",
19. "value": [
20. "454*454",
21. "466*466"
22. ]
23. },
24. "screenDensity": {
25. "policy": "exclude",
26. "value": [
27. "ldpi",
28. "xldpi"
29. ]
30. },
31. "countryCode": {
32. "policy": "include",
33. "value": [
34. "CN"
35. ]
36. }
37. }
38. },
39. }
40. ]
```

## atomicService

**表13** atomicService

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [preloads](ide-customized-multi-targets-and-products-guides.md#section206461457101917) | 对象数组 | 可选 | 定义当前模块运行时预加载的模块。 |

**表14** preloads

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| moduleName | 字符串 | 可选 | 预加载的模块名称。 |

atomicService字段示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "atomicService": {
6. "preloads": [
7. {
8. "moduleName": "preloadSharedLibrary"
9. }
10. ]
11. }
12. }
13. }
14. ]
```

## abilities

abilities用于自定义target的能力范围。

**表15** abilities

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 指定target选择的ability的名称。 |
| [pages](ide-customized-multi-targets-and-products-guides.md#section73018336472) | 字符串数组 | 可选 | FA模型中，指定target选择的ability的page。 |
| res | 字符串数组 | 可选 | 指定资源目录。 |
| icon | 字符串 | 可选 | 指定ability图标文件的索引，格式为"$media:ability\_icon"。 |
| label | 字符串 | 可选 | 指定对用户可见的名称，要求采用该名称的资源索引，以支持多语言。 |
| launchType | 字符串 | 可选 | 指定ability的启动模式：   * multiton：多实例模式，每次启动创建一个新实例。  * standard：同multiton，建议使用multiton替代。 * singleton（缺省默认值）：单实例模式，仅第一次启动创建新实例。 * specified：指定实例模式，运行时由开发者决定是否创建新实例。 |

abilities字段示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "source": {
5. "abilities": [
6. {
7. "name": "EntryAbility",
8. "icon": "$media:layered_image",
9. "label": "$string:EntryAbility_label",
10. "launchType": "singleton"
11. }
12. ]
13. }
14. }
15. ]
```

## buildOption

buildOption是模块在构建过程中的相关配置，buildOptionSet和targets中也支持配置buildOption。此外，工程级build-profile.json5中也支持配置buildOption。工程级别buildOption配置会与模块级别的buildOption进行合并，具体合并规则和优先级请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。

**表16** buildOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 可选 | 构建配置方案buildOption的名称。 |
| debuggable | 布尔值 | 可选 | 当前编译产物是否为可调试模式(debug)：   * true：可调试。 * false：不可调试。   如果未配置debuggable字段，使用release的编译模式时，默认值为false，使用其他编译模式时，默认值为true。 |
| generateSharedTgz | 布尔值 | 可选 | 编译HSP模块时是否生成tgz包。   * true：生成。 * false：不生成。   如果未配置generateSharedTgz，根据debuggable字段决定是否生成tgz包。debuggable为true时，不生成tgz包，debuggable为false时，生成tgz包。  从DevEco Studio 5.1.1 Beta1版本开始支持。  说明  该字段配置后仅对HSP模块生效。 |
| copyFrom | 字符串 | 可选 | 配置已定义的buildOption的name，表示从本模块已有的buildOption复制配置。 |
| [resOptions](ide-hvigor-build-profile.md#section754823013348) | 对象 | 可选 | 资源编译配置项。 |
| [externalNativeOptions](ide-hvigor-cpp.md#section0721057575) | 对象 | 可选 | Native编译配置项。 |
| [sourceOption](ide-hvigor-build-profile.md#section2611239115413) | 对象 | 可选 | 源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。 |
| [nativeLib](ide-hvigor-cpp.md#section15889929155720) | 对象 | 可选 | Native 库（.so）相关配置。 |
| [napiLibFilterOption](ide-hvigor-build-profile.md#section08781111115517) | 对象 | 可选 | NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用[nativeLib/filter](ide-hvigor-cpp.md#section15889929155720)。 |
| [arkOptions](ide-hvigor-build-profile.md#section8368152412552) | 对象 | 可选 | ArkTS编译配置。 |
| [packingOptions](ide-hvigor-build-profile.md#section1744183710558) | 对象 | 可选 | 打包配置项，仅支持HAR模块。 |
| [removePermissions](ide-hvigor-build-profile.md#section155111918175715) | 对象数组 | 可选 | 指定编译时需要删除的依赖包中的冗余权限，模块本身的权限不会被删除，仅HAP/HSP模块支持配置。 |

### resOptions

resOptions是资源编译配置项。

**表17** resOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [compression](ide-hvigor-build-profile.md#section2095319147103) | 对象 | 可选 | 对工程预置图片资源进行纹理压缩的编译配置参数。 |
| resCompileThreads | 整型数值 | 可选 | 资源编译的线程数量 ，最小为1，最大为主机的CPU核数。  该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| [copyCodeResource](ide-hvigor-build-profile.md#table1476161719356) | 对象 | 可选 | 对模块的src/main/ets目录下的资源文件（非源码文件）拷贝的编译配置参数。  说明  该字段对[不开启混淆的源码HAR](ide-hvigor-build-har.md#section197792874110)不生效。 |
| ignoreResourcePattern | 字符串数组 | 可选 | 根据glob语法，对资源目录resources或开发者自定义的资源目录下的文件/文件夹名称进行过滤，匹配到的文件不会被打包到产物中。  从DevEco Studio 5.1.1 Beta1版本开始支持。  说明  * 如果规则中带有路径（例如./src/main/a.png），该规则不生效。 * 如果未配置该字段，打包HAP/HSP时存在默认的过滤规则：默认不打包.git、.svn、.scc、.ds\_store、desktop.ini、picasa.ini、cvs、thumbs.db以及以.开头的隐藏文件/目录和以~结尾的文件。 * 配置该字段后，会覆盖默认的过滤规则；如果字段配置为空数组，则不应用任何过滤规则，即全部资源都打包。 |
| excludeHarRes | 字符串数组 | 可选 | 编译HAP/HSP模块时，指定不参与资源编译的三方HAR包的包名，配置后，依赖HAR包中的资源不会被打包到产物中，支持直接依赖和间接依赖。  从DevEco Studio 6.0.0 Beta2版本开始支持。  说明  仅支持在HAP/HSP中配置。 |
| includeAppScopeRes | 布尔值 | 可选 | 编译HSP时，是否将AppScope目录下的资源打包到产物中。   * true（缺省默认值）：打包。 * false：不打包。   从DevEco Studio 6.0.0 Beta2版本开始支持。  说明  * 该字段仅对HSP模块生效。 * 配置为false后，app.json5的icon和label字段不再对HSP模块生效。 |
| qualifiersConfig | 对象 | 可选 | 配置HAP/HSP模块的限定词目录，编译时会进行过滤，匹配到的限定词目录会被打包到产物中。支持六类限定词，具体请查看[表19](ide-hvigor-build-profile.md#table913204942018)，配置的目录要符合[限定词目录取值要求](resource-categories-and-access.md#限定词目录)。  如果某类限定词未配置过滤，则包含该类限定词的目录默认会打包。  从DevEco Studio 6.1.0 Beta1版本开始支持。  说明  * qualifiersConfig不能为{}，至少配置一类限定词。 * 如果配置了限定词，取值不能为空数组[]，数组中的值不能为空字符串""。 * 仅支持Stage模型。 |

**表18** copyCodeResource

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否将src/main/ets目录下的资源文件（.ets/.ts/.js以外的其他文件）打包到产物中。  从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认配置enable字段并且值为false，即默认不打包ets目录下的资源文件。   * true（缺省默认值）：打包。 * false：不打包。 |
| includes | 字符串数组 | 可选 | * 当enable为true时，用于指定打包的资源文件，其他资源文件均不会打包到产物中，支持glob语法，以"\*\*/"开头。 * 当enable为false时，includes不生效。   从DevEco Studio 6.0.0 Beta2版本开始支持。  说明  excludes和includes互斥，只能配置一个。 |
| excludes | 字符串数组 | 可选 | * 当enable为true时，用于指定不打包的资源文件，其他资源文件均会打包到产物中，支持glob语法，以"\*\*/"开头。 * 当enable为false时，excludes不生效。 |

注意

* 模块的src/main/ets目录下，编译时仅处理.ets/.ts/.js文件，其他文件会被当作资源文件打包进产物中，不会进行混淆或加密，如需过滤请配置excludes字段。
* 请勿将源码等文件放在以.开头的系统隐藏目录中，可能会导致过滤规则失效，会将src/main/ets目录下的所有文件作为资源文件打包进产物中，不会进行混淆或加密。

**表19** qualifiersConfig

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| Mcc&Mnc | 字符串数组 | 可选 | 配置移动国家码（MCC）和移动网络码（MNC）限定词目录，匹配到的目录会被打包到产物中，如['mcc460']表示过滤其他国家码，打包包含mcc460的目录。  如果未配置，默认所有的MCC或MNC都会打包。 |
| Locale | 字符串数组 | 可选 | 配置语言、文字、国家或地区限定词目录，匹配到的目录会被打包到产物中，如['zh\_CN']表示过滤其他语言，打包包含zh\_CN的目录。  如果未配置，默认所有的语言都会打包。 |
| Orientation | 字符串数组 | 可选 | 配置横竖屏限定词目录，匹配到的目录会被打包到产物中，如['vertical']表示过滤其他屏幕方向，打包包含vertical的目录。  如果未配置，默认所有的屏幕方向都会打包。 |
| Device | 字符串数组 | 可选 | 配置设备类型限定词目录，匹配到的目录会被打包到产物中，如['phone']表示过滤其他设备，打包包含phone的目录。  如果未配置，默认所有的设备都会打包。 |
| ColorMode | 字符串数组 | 可选 | 配置颜色模式限定词目录，匹配到的目录会被打包到产物中，如['dark']表示过滤其他模式，打包包含dark的目录。  如果未配置，默认所有的颜色模式都会打包。 |
| Density | 字符串数组 | 可选 | 配置屏幕密度限定词目录，匹配到的目录会被打包到产物中，如['sdpi']表示过滤其他屏幕密度，打包包含sdpi的目录。  如果未配置，默认所有的屏幕密度都会打包。 |

如果同时配置多类限定词，最终打包的目录要同时符合多类限定词的过滤条件，例如存在以下限定词目录：

```
1. phone-dark-Vertical
2. phone-dark-Horizontal
3. phone-light-Horizontal
4. car-dark-Vertical
```

配置如下：

```
1. "qualifiersConfig":{
2. "Device":['phone'],
3. "ColorMode":['dark'],
4. }
```

过滤步骤如下：

1. Device限定词配置了phone，所以phone-dark-Vertical、phone-dark-Horizontal、phone-light-Horizontal符合，car-dark-Vertical不符合，会过滤掉。
2. ColorMode限定词配置了dark，所以phone-dark-Vertical、phone-dark-Horizontal符合，phone-light-Horizontal不符合，会过滤掉。
3. Orientation限定词未配置，所以不过滤限定词目录，phone-dark-Vertical、phone-dark-Horizontal都符合。
4. 综上所述，最终打包到产物中的是phone-dark-Vertical和phone-dark-Horizontal。

resOptions字段示例：

```
1. "buildOption": {
2. "resOptions": {
3. "resCompileThreads": 2,
4. "copyCodeResource": {
5. "enable": true,
6. "excludes": ['**/entry/src/main/ets/component/big_picture.png', '**/*.yml', '**/subDir/**'],   // includes字段配置方式相同
7. },
8. "ignoreResourcePattern": ['*.png' ,'abc.json'],
9. "excludeHarRes": ['har'],
10. "qualifiersConfig":{
11. "Mcc&Mnc":['mcc460'],
12. "Locale":['zh_CN'],
13. "Orientation":['vertical'],
14. "Device":['phone','tv'],
15. "ColorMode":['dark'],
16. // "Density":['sdpi'],   不配置表示所有的屏幕密度都打包
17. },
18. }
19. }
```

### sourceOption

sourceOption是源码相关配置，使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。

**表20** sourceOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| workers | 字符串数组 | 可选 | 指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。 |

sourceOption字段示例：

```
1. "buildOption": {
2. "sourceOption": {
3. "workers": [
4. "./src/main/ets/common/constants/CommonConstants.ets"
5. ]
6. }
7. }
```

### napiLibFilterOption

napiLibFilterOption是NAPI库（.so）文件的筛选选项，字段已废弃，不建议使用，推荐使用[nativeLib/filter](ide-hvigor-cpp.md#section15889929155720)。

**表21** napiLibFilterOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| excludes | 字符串数组 | 可选 | 排除的.so文件。罗列的NAPI库将不会被打包。 |
| pickFirsts | 字符串数组 | 可选 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。 |
| pickLasts | 字符串数组 | 可选 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。 |
| enableOverride | 布尔值 | 可选 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：   * true：允许。 * false（缺省默认值）：不允许。 |

### arkOptions

arkOptions是ArkTS编译配置。

**表22** arkOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [runtimeOnly](ide-hvigor-build-profile.md#table19892123422118) | 对象 | 可选 | 配置变量动态import的文件和依赖的包名，仅支持在Stage模型中配置。  runtimeOnly为非必选配置，当工程需要以变量方式动态import文件、目录的相对路径或三方包时，需要通过配置runtimeOnly来确保其加入编译流程。详情请参考[动态import变量表达式](arkts-dynamic-import.md#动态import变量表达式)。 |
| [types](arkoptions-guide.md#types) | 字符串数组 | 可选 | 自定义类型，可配置包名或d.ts/d.ets文件路径。 |
| [obfuscation](ide-build-obfuscation.md) | 对象 | 可选 | 代码混淆配置。 |
| [buildProfileFields](ide-hvigor-get-build-profile-para.md) | 对象 | 可选 | 运行时可获取的自定义构建参数，支持键值对配置，key可由数字、英文、下划线、中划线组成，value类型仅支持string、number、boolean。 |
| integratedHsp | 布尔值 | 可选 | 是否为[集成态HSP](integrated-hsp.md)。   * true：是。 * false（缺省默认值）：否。   说明  * 从API 12开始支持。 * 需在工程级build-profile.json5中配置useNormalizedOHMUrl为true后使用。 * 该字段仅在HSP模块中配置后生效。 |
| [transformLib](customize-bytecode-during-compilation.md) | 字符串 | 可选 | 字节码插桩插件配置，允许开发者在编译时对字节码进行插桩修改，仅支持Stage模型，格式为相对路径，不同系统要求的文件类型如下，文件内容需要在对应平台生成，不能拷贝修改后缀名混用。   * Windows：.dll文件。 * Linux/Mac：.so文件。   说明  * Mac环境下添加配置后插桩未生效的问题请参考[FAQ](../harmonyos-faqs/faqs-compiling-and-building-133.md)。 * HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。 |
| branchElimination | 布尔值 | 可选 | 是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉，示例请参考[branchElimination示例](ide-hvigor-build-profile.md#li71611425123512)。   * true：启用（将导致使用"ApplyChanges"功能时，对const声明的常量的值进行的修改可能不生效）。 * false（缺省默认值）：不启用。   说明  * 仅支持API 11及以上的Stage模型。 * HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。 * 仅支持const声明的bool类型常量和const声明的string/number类型常量的判断表达式。 * 不支持间接导入，例如A文件中定义const变量A1，B文件导入A1，导出B1，ets导入B1进行判断，无法进行裁剪。 |
| byteCodeHar | 布尔值 | 可选 | 是否构建字节码HAR，仅在HAR模块中配置后生效。详情请参考[构建字节码HAR](ide-hvigor-build-har.md#section16598338112415)。   * true：支持。 * false：不支持。   说明  * 从API 12开始支持。 * 从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，byteCodeHar缺省默认值为true；当useNormalizedOHMUrl配置为false时，byteCodeHar缺省默认值为false。 |
| bundledDependencies | 布尔值 | 可选 | 是否支持将多个源码HAR（本地+远程）打包成一个字节码HAR。字节码HAR、HSP、npm不会被打包进去，仅会合并源码HAR。   * true：支持。 * false（缺省默认值）：不支持。   说明  * 仅支持[字节码HAR](ide-hvigor-build-har.md#section16598338112415)配置该字段。 * 从API 12开始支持。 * 仅支持Stage模型。 |
| packSourceMap | 布尔值 | 可选 | 编译[字节码HAR](ide-hvigor-build-har.md#section16598338112415)时，是否将sourceMap文件打包到产物中。仅HAR模块支持配置，并且只对字节码HAR生效。   * true：打包。 * false：不打包。   该字段从DevEco Studio 5.1.0 Release版本开始支持。  说明  * 如果不配置，debug模式默认值为true，release模式默认值为false。 * 将sourceMap打包到release的HAR包中，可能会导致HAR中的代码资产泄漏。 |
| autoLazyImport | 布尔值 | 可选 | 编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考[延迟加载（lazy import）](arkts-lazy-import.md)。   * true：添加。 * false（缺省默认值）：不添加。   说明  * 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。 * 仅支持Stage模型。 |
| [autoLazyFilter](ide-hvigor-build-profile.md#table1551310818378) | 对象 | 可选 | 自定义添加"lazy"关键字的模块，仅当autoLazyImport为true时生效。  从DevEco Studio 6.0.1 Beta1版本开始支持。 |
| reExportCheckMode | 字符串 | 可选 | 针对以下场景，编译时是否进行拦截报错：使用lazy import导入的变量，在同文件中被再次导出。   * noCheck（缺省默认值）：不检查，不报错。 * compatible：兼容模式，报Warning。 * strict：严格模式，报Error。   该字段从DevEco Studio 5.0.5 Release版本开始支持。 |
| skipOhModulesLint | 布尔值 | 可选 | 是否跳过工程中oh\_modules目录的[ArkTS规则检查](typescript-to-arkts-migration-guide.md)。从DevEco Studio 6.0.0 Beta1版本开始支持。   * true：跳过。 * false（缺省默认值）：不跳过。 |
| [expandImportPath](ide-hvigor-build-profile.md#table1921576135914) | 对象 | 可选 | import路径展开相关配置选项。  从DevEco Studio 6.0.0 Beta3版本开始支持。  说明  HAR模块不支持配置。 |
| apPath | 字符串 | 可选 | 说明  API 11及以上版本不再支持，即该字段配置后不再生效。  应用热点信息文件路径。 |
| hostPGO | 布尔值 | 可选 | 是否启用配置文件引导优化功能：   * true：启用。 * false（缺省默认值）：不启用。   从API 10开始废弃。 |

* branchElimination字段配置为true时，代码分支的裁剪情况示例如下：

  ```
  1. // 编译生成的BuildProfile文件
  2. export const DEBUG = false;
  3. export const VERSION_CODE = 100;
  4. // 开发者自定义的ets文件
  5. import { DEBUG } from 'BuildProfile';
  6. import { VERSION_CODE } from 'BuildProfile';
  7. if (DEBUG)
  8. {XXX} // 该分支会被裁剪掉
  9. else
  10. {XXX}
  11. if (VERSION_CODE){XXX} // 该语法发生了类型转换，不支持代码裁剪。
  12. if (VERSION_CODE === 100){XXX} // 若需要裁剪代码，使用该方式，显式指定判断条件为boolean类型。
  ```

**表23** runtimeOnly

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| sources | 字符串数组 | 可选 | 配置变量动态import的文件/文件夹的相对路径。  配置的文件/文件夹必须在工程中真实存在，且文件的后缀只能为ets或ts。 |
| packages | 字符串数组 | 可选 | 配置变量动态import依赖的包名。  该包名需要和工程级/模块级oh-package.json5的dependencies或dynamicDependencies中的名字保持一致。  从DevEco Studio 5.1.1 Beta1版本开始，packages中的三方包支持配置在dynamicDependencies中。 |
| excludePackages | 字符串数组 | 可选 | 编译HAP/HSP模块时，指定不参与变量动态import的源码HAR的包名，配置的源码HAR不会参与编译，支持直接/间接依赖。  仅支持在HAP/HSP模块中配置。  从DevEco Studio 6.0.0 Beta2版本开始支持。 |

**表24** expandImportPath

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否启用import路径展开，启用后可以提升应用的运行时性能。关于import路径展开的原理及开启后的副作用请参考[通过import路径展开优化性能](arkts-module-side-effects.md#通过import路径展开优化性能)。   * true：启用。 * false（缺省默认值）：不启用。   说明  import XXX from 'A'，A必须为本地HAR模块，并且仅当A为包名时支持进行展开，A为相对路径或包名+路径都不支持展开。 |
| exclude | 字符串数组 | 可选 | 配置oh-package.json5中的依赖别名，用于指定不展开import语句的依赖，仅支持本地HAR模块。 |

**表25** autoLazyFilter

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| include | 字符串数组 | 可选 | * 当autoLazyImport为true时，指定自动添加"lazy"关键字的包名（即oh-package.json5中的name），其他包不会添加"lazy"关键字，支持正则语法。 * 当autoLazyImport为false时，include不生效。   说明  * include和exclude互斥，只能配置一个。 * include不支持配置空数组或空字符串，至少配置一个包名，并且包名不能重复。 |
| exclude | 字符串数组 | 可选 | * 当autoLazyImport为true时，指定不添加"lazy"关键字的包名，其他包都会添加"lazy"关键字，支持正则语法。 * 当autoLazyImport为false时，exclude不生效。   说明  * include和exclude互斥，只能配置一个。 * exclude不支持配置空数组或空字符串，至少配置一个包名，并且包名不能重复。 |

arkOptions字段示例：

```
1. "buildOption": {
2. "arkOptions": {
3. "runtimeOnly": {
4. "sources": ["./src/main/ets/utils/Calc.ets"],
5. "packages": ["myHar"],
6. "excludePackages": ["har1","har2"],  // myHar依赖har1、har2
7. },
8. "buildProfileFields": {
9. "buildOptionSetData": "BuildOptionSetDataRelease",
10. "data": "DataRelease"
11. },
12. "transformLib": "./dll/example.dll",
13. "branchElimination": true,
14. "autoLazyImport": true,
15. "autoLazyFilter": {
16. "include": ['entry']
17. },
18. "reExportCheckMode": "compatible",
19. "expandImportPath": {
20. "enable": true,
21. "exclude": ['localhar']
22. },
23. }
24. }
```

### packingOptions

packingOptions是打包配置项，仅支持HAR模块。该字段从DevEco Studio 5.1.0 Release版本开始支持。

**表26** packingOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [asset](ide-hvigor-build-profile.md#table14927147191119) | 对象 | 可选 | 打包资产配置项。 |
| [customizedOptions](ide-hvigor-build-profile.md#table3942836112513) | 对象 | 可选 | HAR模块的定制化选项。  从DevEco Studio 6.0.2 Beta1版本开始支持。 |

**表27** asset

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| include | 字符串数组 | 可选 | 配置打包到HAR产物中的文件，遵循glob语法。  说明  * 以下目录配置后不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。  * 配置include字段后，构建源码HAR时，.gitignore和.ohpmignore文件不生效，详细请参考[以debug模式构建](ide-hvigor-build-har.md#section197792874110)。 |
| exclude | 字符串数组 | 可选 | 配置不打包到HAR产物中的文件，遵循glob语法。  说明  * 以下文件配置后不生效，默认会打包：oh-package.json5。 * 配置exclude字段后，构建源码HAR时，.gitignore和.ohpmignore文件不生效，详细请参考[以debug模式构建](ide-hvigor-build-har.md#section197792874110)。 |

**表28** customizedOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| basePackage | 字符串 | 可选 | 指定需要定制的字节码HAR的abc文件的相对路径。配置后，编译时支持替换掉abc中的同名文件，以实现对字节码HAR的定制修改，具体使用方式请参考[三方SDK定制修改部分源码](../harmonyos-faqs/faqs-compiling-and-building-192.md)。 |

packingOptions字段示例：

```
1. "buildOption": {
2. "packingOptions": {
3. "asset": {
4. "include": ["./src/router.json5", "router.json5"],
5. "exclude": ["./config/*"]
6. },
7. "customizedOptions": {
8. "basePackage": "./basePackage/modules.abc",
9. },
10. }
11. }
```

### removePermissions

removePermissions是一个对象数组，用于编译HAP/HSP模块时，指定需要删除的依赖包中的冗余权限，模块本身的权限不会被删除。

**表29** removePermissions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 待删除的权限名称，需要包含在依赖包的module.json的requestPermissions中。 |

removePermissions字段示例：

```
1. "buildOption": {
2. "removePermissions": [
3. {
4. "name": "ohos.permission.ABILITY_BACKGROUND_COMMUNICATION"
5. },
6. {
7. "name": "ohos.permission.ACCELEROMETER"
8. }
9. ]
10. }
```

## compression

compression是对工程预置图片资源进行纹理压缩的编译配置参数。

**表30** compression

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [media](ide-hvigor-build-profile.md#section1915545641714) | 对象 | 可选 | 对资源目录下media目录的图片进行纹理压缩的配置参数。 |
| [filters](ide-hvigor-build-profile.md#section185719543186) | 对象数组 | 可选 | 文件过滤配置参数。  说明  编译过程中会依次遍历图片文件，并与filters条件进行匹配，一旦匹配成功，则完成该图片的处理。当工程级和模块级同时配置时，先按照模块级的过滤条件匹配，一旦匹配成功，则忽略工程级的过滤条件；如果模块级的没有匹配成功，继续按工程级的条件进行匹配。 |

### media

media是对资源目录下media目录的图片进行纹理压缩的配置参数。

**表31** media

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否对media图片启用纹理压缩。   * true：启用。 * false（缺省默认值）：不启用。   说明  * 在linux系统的构建场景下，请确认系统环境已[安装libGL1库](ide-command-line-building-app.md#section1478651816216)。 * 对图片进行纹理压缩会改变文件名称和内容，在[分层图标](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor)以及二次编辑的场景下会引起图片显示异常，请进一步使用filters排除掉这部分文件。 |

### filters

filters是文件过滤配置参数。

**表32** filters

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [method](ide-hvigor-build-profile.md#table1568916396220) | 对象 | 必选 | 纹理压缩的方式。 |
| [files](ide-hvigor-build-profile.md#table19762944112414) | 对象 | 可选 | 指定用来参与压缩的文件，与exclude字段配合使用。 |
| [exclude](ide-hvigor-build-profile.md#table6219104952519) | 对象 | 可选 | 从files中剔除掉不需要压缩的文件。 |

**表33** method

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| type | 字符串 | 必选 | 转换类型。   * astc（Adaptive Scalable Texture Compression）：自适应可变纹理压缩，一种对GPU友好的纹理格式，可在设备侧更快地显示，有更少的内存占用。 * sut（SUper compression for Texture） ：纹理超压缩，可在设备侧更快地显示，有更少的内存占用，相比astc具备更大压缩率和更少ROM占用。 |
| blocks | 字符串 | 必选 | astc/sut转换类型的扩展参数，决定画质和压缩率，当前仅支持"4x4"。 |

**表34** files

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| path | 字符串数组 | 可选 | 指定“按路径匹配”的过滤条件，符合glob规范，格式为相对路径。 |
| size | 二维数组 | 可选 | 指定“按大小匹配”的过滤条件，格式为[min,max]，闭区间，表示大小从min到max之间的文件。   * 每个数值可以填数字、字符串或字符串中带单位（大小写均可），如[0, '1k']。 * 单位K/k=1024，M/m=1024\*1024，G/g=1024\*1024\*1024，T/t=1024\*1024\*1024\*1024。 * 区间最大值可省略，表示无限大，如['3K']。 |
| resolution | 二维数组 | 可选 | 指定“按分辨率匹配”的过滤条件，配置示例：  收起  自动换行  深色代码主题  复制  ``` 1. resolution:[ 2. [ 3. { width:32, height:32 },  // 最小宽高 4. { width:64, height:64 },  // 最大宽高 5. ],  // 分辨率在32*32到64*64之间的图片 6. [ 7. { width:200, height:200 },  // 最小宽高 8. // 此处第2个不填表示最大宽高是无限大 9. ],  // 分辨率大于200*200的图片 10. ] ```   * width和height只能是数字。 * 最大宽高可以省略，表示无限大。 |

**表35** exclude

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| path | 字符串数组 | 可选 | 同files/path。 |
| size | 二维数组 | 可选 | 同files/size。 |
| resolution | 二维数组 | 可选 | 同files/resolution。 |

compression字段示例：

```
1. "buildOption": {
2. "resOptions": {
3. "compression": {
4. "media": {
5. "enable": true // 是否对media图片启用纹理压缩
6. },
7. // 纹理压缩文件过滤，非必填，不填会压缩资源目录中的所有图片
8. "filters": [
9. {
10. "method": {
11. "type": "sut", // 转换类型
12. "blocks": "4x4" // 转换类型的扩展参数
13. },
14. // 指定用来参与压缩的文件，需要满足所有条件且不被exclude过滤的文件才会参与压缩
15. "files": {
16. "path": ["./**/*"], // 指定资源目录中的所有文件
17. "size": [[0, '10k']], // 指定大小10k以下的文件
18. // 指定分辨率小于2048*2048的图片
19. "resolution": [
20. [
21. { "width": 0, "height": 0 }, // 最小宽高
22. { "width": 2048, "height": 2048 } // 最大宽高
23. ]
24. ]
25. },
26. // 从files中剔除掉不需要压缩的文件，需要满足所有过滤条件的文件才会被剔除
27. "exclude": {
28. "path": ["./**/*.jpg"], // 过滤所有jpg文件
29. "size": [[0, '1k']], // 过滤大小1k以下的文件
30. // 过滤分辨率小于1024*1024的图片
31. "resolution": [
32. [
33. { "width": 0, "height": 0 }, // 最小宽高
34. { "width": 1024, "height": 1024 } // 最大宽高
35. ]
36. ]
37. }
38. }
39. ]
40. }
41. }
42. }
```

## buildModeBinder

buildModeBinder是构建模式（debug、release 等）与构建配置（buildOption）的关联配置。通过该配置可以将不同的构建配置和target进行组合，并绑定到对应的构建模式上。如果没有配置buildModeBinder，默认的绑定策略请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。

**表36** buildModeBinder

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| buildModeName | 字符串 | 可选 | 构建模式名称，需要在工程级别的buildModeSet中定义。 |
| [mappings](ide-hvigor-build-profile.md#table4672142011561) | 对象数组 | 可选 | target和buildOption之间的一对一映射关系。 |

**表37** mappings

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| targetName | 字符串 | 可选 | target名称。 |
| buildOptionName | 字符串 | 可选 | 构建配置buildOption名称。 |

buildModeBinder字段示例：

```
1. "buildModeBinder": [
2. {
3. "buildModeName": "debug",
4. "mappings": [
5. {
6. "targetName": "default",
7. "buildOptionName": "release"
8. }
9. ]
10. }
11. ]
```
