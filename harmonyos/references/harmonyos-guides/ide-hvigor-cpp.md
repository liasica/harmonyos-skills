---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-cpp
title: 配置CPP
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 配置CPP
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:230c877594e661c67614b276f0f2803b1905d2ac62b1ddb2bf97714b38ceb79c
---

Hvigor集成CMake、Ninja为cpp代码的构建工具。在初始状态下，无需额外配置，您也可以添加以下自定义配置，定制cpp代码编译。

CPP配置包含externalNativeOptions和nativeLib，除特殊说明外，在工程级和模块级build-profile.json5文件中均支持配置，工程级配置会与模块级配置进行合并，模块级配置优先，具体合并规则和优先级请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。

## externalNativeOptions

externalNativeOptions是Native编译配置项。

**表1** externalNativeOptions字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| path | 字符串 | 可选 | CMake构建脚本地址，即CMakeLists.txt文件地址。 |
| abiFilters | 字符串数组 | 可选 | HarmonyOS当前支持的ABI编译环境，包括：   * arm64-v8a * x86\_64   如不配置该参数，编译时默认为arm64-v8a。 |
| arguments | 字符串/字符串数组 | 可选 | CMake编译参数。  Hvigor将会把此处的自定义参数传递给CMake构建工具，您可通过CMake官方文档查找您所需的编译参数，同时它也将覆盖默认同名参数。 |
| cppFlags | 字符串 | 可选 | C++编译器参数。  从DevEco Studio 6.0.1 Beta1版本开始，新增"-iclang"参数，提升编译效率，具体请参考[通过IClang提升C++增量编译效率](ide-hvigor-experimental-properties.md#section324586847)。 |
| cFlags | 字符串 | 可选 | C编译参数。仅模块级build-profile.json5文件支持配置。  从DevEco Studio 6.0.1 Beta1版本开始，新增"-iclang"参数，提升编译效率，具体请参考[通过IClang提升C++增量编译效率](ide-hvigor-experimental-properties.md#section324586847)。 |
| targets | 字符串数组 | 可选 | 指定hvigor应构建的CMake项目中的库和可执行目标。仅模块级build-profile.json5文件支持配置。 |

## nativeLib

nativeLib是Native库（.so）相关配置。

**表2** nativeLib字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [filter](ide-hvigor-cpp.md#section17675528161517) | 对象 | 可选 | Native 库（.so）文件的筛选选项。配置后优先级高于[napiLibFilterOption](ide-hvigor-build-profile-app.md#section1488712919295)。 |
| [debugSymbol](ide-hvigor-cpp.md#section2182144382320) | 对象 | 可选 | 移除.so文件中的符号表、调试信息。 |
| headerPath | 字符串/字符串数组 | 可选 | 指定要导出的头文件路径。  注意  请勿将源码等文件放置在该路径下，可能会被打包到产物中，请谨慎配置。 |
| collectAllLibs | 布尔值 | 可选 | 对libs目录收集打包时，是否收集所有后缀的文件。   * true：不限制后缀，即收集所有文件（包括无后缀文件）。 * false（缺省默认值）：限制后缀为.so，即只收集后缀为.so的文件。 |
| excludeFromHar | 布尔值 | 可选 | 构建HAR时，是否排除依赖HAR模块中的.so文件，排除时，依赖HAR模块的.so文件不会被打包到产物中。   * true（缺省默认值）：排除。 * false：不排除。   说明  仅针对HAR模块生效。 |
| excludeSoFromInterfaceHar | 布尔值 | 可选 | [编译HSP模块](ide-hsp.md#section67683213597)时，打包的HAR产物是否排除.so文件，减少.tgz包体积大小。   * true：排除。HAR产物不包含.so文件，HSP产物包含.so文件。 * false（缺省默认值）：不排除。HAR产物和HSP产物都包含.so文件。   说明  * 仅针对HSP模块生效。 * 当HSP模块的工程级或模块级build-profile.json5文件中配置headerPath字段时，excludeSoFromInterfaceHar字段不生效。 |
| excludeSoFromBinXO | 字符串数组 | 可选 | 开启BinXO检测时，指定不需要进行二进制插桩的无源码so文件，支持正则匹配，具体使用方式请参考[使用HWASan检测内存错误](ide-hwasan.md)。  从DevEco Studio 6.1.0 Beta1版本开始支持。 |
| [librariesInfo](ide-hvigor-cpp.md#section969845819510) | 对象数组 | 可选 | 声明so的透传依赖信息。仅模块级build-profile.json5文件支持配置。 |

### filter

filter是Native 库（.so）文件的筛选选项。配置后优先级高于[napiLibFilterOption](ide-hvigor-build-profile-app.md#section1488712919295)。

**表3** filter字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| excludes | 字符串数组 | 可选 | 根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包。 |
| pickFirsts | 字符串数组 | 可选 | 按照.so文件的[优先级顺序](ide-hvigor-cpp.md#li143214241919)，打包最高优先级的.so文件。 |
| pickLasts | 字符串数组 | 可选 | 按照.so文件的[优先级顺序](ide-hvigor-cpp.md#li143214241919)，打包最低优先级的.so文件。 |
| enableOverride | 布尔值 | 可选 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：   * true：允许。 * false（缺省默认值）：不允许。 |
| [select](ide-hvigor-cpp.md#li1737916541996) | 对象数组 | 可选 | select提供native产物的精准选择能力，根据包名、版本、产物名称等，选择打包或排除native产物到HAP/HSP/HAR产物。  select的优先级高于excludes、pickFirsts等配置项。 |

* **库文件so的优先级**

  库文件so的优先级顺序，可以通过pickFirsts，pickLasts选项来选择，其中pickFirsts选择高优先级的库文件，pickLasts选择低优先级的库文件。

  这个优先级是由本模块的依赖模块或三方包的收集顺序决定的，本模块的依赖在oh-package.json5文件的dependencies配置中声明，优先级顺序如下。

  + 三方包（包括远程三方包及本地har包）的优先级高于本地依赖模块的优先级。
  + 按照广度优先的遍历方式来收集依赖，如下图，优先级顺序为current > library0 > library1 > library5 > library2 > library3 > library4。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/n9Tb3mRtRWqEIoGAKNkzsQ/zh-cn_image_0000002561752999.png?HW-CC-KV=V1&HW-CC-Date=20260429T054712Z&HW-CC-Expire=86400&HW-CC-Sign=59ECDEB0A1F2DAC767CEDD136F55DB3A213946E01DC1AFCFBB4B5C760BC54C7E "点击放大")
* **select**

  **表4** select字段说明

  | 字段名称 | 类型 | 可选/必选 | 含义 |
  | --- | --- | --- | --- |
  | package | 字符串 | 可选 | 包名。 |
  | version | 字符串 | 可选 | 包版本。 |
  | includePattern | 字符串数组 | 可选 | 当依赖的多个包中存在重名的native产物时，指定需要打包的native产物，支持glob语法。  从DevEco Studio 6.0.0 Beta2版本开始支持。 |
  | excludePattern | 字符串数组 | 可选 | 指定排除的native产物，默认打包所有产物，支持glob语法。excludePattern优先级比includePattern高。  从DevEco Studio 6.0.0 Beta2版本开始支持。 |
  | include | 字符串数组 | 可选 | 当依赖的多个包中存在重名的native产物时，指定需要打包的native产物。  从DevEco Studio 6.0.0 Beta2版本开始，字段标记为废弃，推荐使用includePattern字段。 |
  | exclude | 字符串数组 | 可选 | 指定排除的native产物，默认打包所有产物。  从DevEco Studio 6.0.0 Beta2版本开始，字段标记为废弃，推荐使用excludePattern字段。 |

  说明

  includePattern/excludePattern字段和include/exclude字段不能同时配置。

  **示例一：**entry模块依赖har包@ohos/curl和har1包@ohos/curl1，har包和har1包中的.so文件如下，两个包中存在重名的libcurl.so，可通过includePattern选择需要打包的libcurl.so，同时通过excludePattern排除不需要的产物。

  ```
  1. // har包@ohos/curl的目录结构
  2. └── har
  3. └── libs
  4. └── x86_64
  5. └── libcurl.so
  6. └── libcurl1.so
  7. └── arm64-v8a
  8. └── libcurl2.so
  9. └── libcurl3.so
  10. └── libcurl4.so
  11. // har1包@ohos/curl1的目录结构
  12. └── har1
  13. └── libs
  14. └── x86_64
  15. └── libcurl.so
  16. // build-profile.json5
  17. {
  18. buildOption: {
  19. nativeLib: {
  20. filter: {
  21. select: [ // select的优先级高于excludes、pickFirsts等配置项
  22. {
  23. package: "@ohos/curl", // 包名
  24. version: "1.3.5", // 包版本
  25. excludePattern: ['**/arm64-v8a/**'],    // 排除har包arm64-v8a目录下的所有.so文件
  26. },
  27. {
  28. package: "@ohos/curl1", // 包名
  29. version: "1.3.5", // 包版本
  30. includePattern: ['**/x86_64/libcurl.so'],  // 针对重名的libcurl.so，指定打包har1包中的libcurl.so
  31. // include: ["libcurl.so"]  // 针对重名的libcurl.so，指定打包har1包中的libcurl.so
  32. },
  33. ]
  34. }
  35. }
  36. }
  37. }
  38. // 打包后hap包的目录结构
  39. └── entry-default.hap
  40. └── libs
  41. └── x86_64
  42. └── libcurl.so    // 来自har1包
  43. └── libcurl1.so   // 来自har包
  ```

  **示例二：**har包中存在多个.so文件，需要打包其中的libcurl1.so和libcurl2.so。

  ```
  1. // har包@ohos/curl的目录结构
  2. └── libs
  3. └── arm64-v8a
  4. └── libcurl.so
  5. └── libcurl1.so
  6. └── libcurl2.so
  7. // build-profile.json5
  8. {
  9. buildOption: {
  10. nativeLib: {
  11. filter: {
  12. select: [  // select的优先级高于excludes、pickFirsts等配置项
  13. {
  14. package: "@ohos/curl", // 包名
  15. version: "1.3.5", // 包版本
  16. includePattern: [],
  17. excludePattern: ['**/arm64-v8a/!(*(libcurl1|libcurl2).so*)'], // 打包arm64-v8a目录下的libcurl1.so和libcurl2.so
  18. // include: [],
  19. // exclude: ["libcurl.so"] // 打包arm64-v8a目录下的libcurl1.so和libcurl2.so
  20. }
  21. ]
  22. }
  23. }
  24. }
  25. }
  ```

### debugSymbol

debugSymbol用于移除.so文件中的符号表、调试信息。

**表5** debugSymbol字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| strip | 布尔值 | 可选 | 是否移除.so文件中的符号表、调试信息。   * true（缺省默认值）：移除。 * false：不移除。   说明  从DevEco Studio NEXT Developer Beta2（5.0.3.502）版本开始，缺省默认值由false改为true。 |
| exclude | 字符串数组 | 可选 | 需要排除的.so文件，支持正则表达式写法。   * 如果strip配置为true，匹配的.so文件将不会执行strip。 * 如果strip配置为false，只有匹配的.so文件会执行strip。 |

### librariesInfo

librariesInfo用于声明so的透传依赖信息。仅模块级build-profile.json5文件支持配置。

**表6**

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 本模块so库的名称。 |
| linkLibraries | 字符串数组 | 必选 | so库的依赖信息，格式为"依赖包名::依赖so名称"。 |

如果需要声明库之间的依赖关系，例如entry依赖curl，可在模块内build-profile.json5中配置librariesInfo。

```
1. "buildOption": {
2. "nativeLib": {
3. "librariesInfo": [
4. {
5. "name": "libentry.so",
6. "linkLibraries": ["curl::curl"]
7. }
8. ]
9. }
10. }
```

当其他模块依赖声明了依赖透传的模块并使用libentry.so时，libentry.so会将依赖curl::curl添加到参数INTERFACE\_LINK\_LIBRARIES，开发者无需关注它的依赖。

```
1. add_library(library::library SHARED IMPORTED)
2. set_target_properties(library::library PROPERTIES
3. IMPORTED_LOCATION "/path/to/file"
4. INTERFACE_LINK_LIBRARIES "curl::curl")
```

## 配置字段示例

以模块级build-profile.json5为例：

```
1. {
2. ...
3. "buildOptionSet": [
4. {
5. "name": "release",
6. "arkOptions": {
7. "obfuscation": {
8. "ruleOptions": {
9. "enable": true,
10. "files": [
11. "./obfuscation-rules.txt"
12. ]
13. }
14. }
15. },
16. "externalNativeOptions": {
17. "path": "./src/main/cpp/CMakeLists.txt", // 自定义CMake配置脚本CMakeLists.txt的位置，它是以模块根目录为起始位置的相对路径
18. "arguments": ["-DCMAKE_BUILD_TYPE=Debug"], // Hvigor将会把此处的自定义参数传递给CMake构建工具，您可通过CMake官方文档查找您所需的编译参数，同时它也将覆盖默认同名参数
19. "cppFlags": "-g", // 自定义cpp flags参数
20. "abiFilters": ["arm64-v8a"] // 自定义cpp编译架构，默认编译架构为arm64-v8a
21. },
22. "nativeLib": {
23. "debugSymbol": { // 可通过此配置对cpp编译产物so执行strip，移除so中的调试信息与符号表等
24. "strip": true, // 执行strip
25. "exclude": [] //执行strip的过滤正则表达式规则
26. },
27. "filter": { // 可通过此选项自定义此cpp产物so是否打包到应用包中
28. "excludes": [ // 根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包，可用于打包时缩小包体积
29. "**/3.so", // 排除所有名称为“3”的so文件
30. "**/x86_64/*.so" // 排除所有x86_64架构的so文件
31. ],
32. "pickFirsts": ["**/1.so"], // 按照.so文件的优先级顺序，打包最高优先级的.so文件
33. "pickLasts": ["**/2.so"], // 按照.so文件的优先级顺序，打包最低优先级的.so文件
34. "enableOverride": true, // 当.so重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件
35. },
36. "headerPath": "./src/main/cpp/include", // 声明模块打包共享的c/cpp接口
37. "librariesInfo":[
38. {
39. "name": "libentry.so",
40. "linkLibraries": ["curl::curl"]
41. }
42. ]
43. },
44. },
45. ],
46. ...
47. }
```
