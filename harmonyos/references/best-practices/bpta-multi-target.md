---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-target
title: 多目标产物构建
breadcrumb: 最佳实践 > 编译构建 > 多目标产物构建
category: best-practices
scraped_at: 2026-04-28T08:23:11+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3e927360fb22ecfba552a718bc0f756f5d18dcd370ad528b8f8e6d7335a31325
---

## 概述

多目标产物在HarmonyOS系统中的应用主要体现在软件开发与分发方面，特别是针对不同用户群体、不同业务场景的需求进行定制化开发。多目标产物为开发者提供了更加灵活和高效的开发方式，使得应用能够更好地适应市场需求和变化。通过定制化开发，还可以更好地满足用户的个性化需求，提升用户体验。

### 基本概念

* target：对应HAR、HSP、HAP的多目标产物。工程内的每一个模块可以定义多个target，每个Target对应一个定制的HAP、HAR包，通过配置可以实现一个模块构建出不同的HAP、HAR包。
* product：对应App的多目标产物。一个HarmonyOS工程的构建产物为App包，一个工程可以定义多个product，每个product对应一个定制化应用包，通过配置可以实现一个工程构建出多个不同的应用包。

在构建过程中，鸿蒙构建系统会根据配置文件中定义的product和target信息，生成相应的构建产物。对于每个target，构建系统会生成一个对应的HAP/HSP/HAR。这个HAP/HSP/HAR包含了该target所需的所有代码和资源。对于每个product，构建系统会生成一个包含了其所有依赖的target的App包。这个App包可以用于发布和上架到应用市场。

### 应用场景

主要应用场景:

* 不同用户群体：针对不同的用户群体（如国内用户与国际用户等），系统支持构建不同的应用版本。这些版本在功能、界面、语言等方面可能有所不同，以满足不同用户群体的需求。
* 不同业务场景：在不同的业务场景中，同一个应用可能需要提供不同的功能或资源。例如，一个在线教育应用可能需要为学生提供学习资料，而为教师提供教学资料。HarmonyOS系统支持通过配置不同的Target来实现这种差异化定制。

针对以上场景，开发者需要通过修改build-profile.json5、module.json5等配置文件，定义出不同的product和target。在这些配置文件中，开发者不仅可以为每个target指定不同的设备类型、源码集、资源等，并且还可以根据业务需要为不同的product分配不同的target。然后在构建过程中，构建工具会根据这些配置生成不同的target，然后通过不同的target搭配构建出不同的product产物。

本文将通过一个具体的案例来介绍如何配置不同资源以及如何构建出多目标产物。

## 实现原理

HarmonyOS多目标产物支持[HAP](../harmonyos-guides/hap-package.md)（应用安装的基本单位，每个HAP都对应一个应用模块）、[HAR](../harmonyos-guides/har-package.md)（静态共享包）、[HSP](../harmonyos-guides/in-app-hsp.md)（动态共享包）以及App（由多个HAP打包一起上架的完整应用程序）包多种类型的包，以满足不同业务场景下的应用开发和定制需求。

### 多目标产物定制项

目前多目标产物支持的定制项信息如下表所示，表中已给出每一项的作用。详细的每一个定制项的配置方法可以参考：[配置多目标产物](../harmonyos-guides/ide-customized-multi-targets-and-products.md)。

**表1** 产物定制项

| 多目标模块 | 定制项 | 作用 |
| --- | --- | --- |
| HAP | HAP包名（artifactName） | 产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |
| 设备类型（deviceType） | 用于配置支持的设备类型，如Phone、Tablet等。 |
| 源码集（source） | target的源码范围：   * pages：定制pages源码目录的page页面，数组长度至少为1。 * sourceRoots：定制差异化代码空间，数组长度至少为1。 |
| 资源（resource） | 配置需要的资源文件路径，支持配置多个资源文件路径。 |
| 分发规则（distributionFilter） | 针对多target存在相同设备类型deviceType的场景，相同设备类型的target需要指定分发规则distributionFilter。 |
| 产物分包（preloads） | 对于元服务，每一个target均可以指定preloads的分包。 |
| abilities能力项（icon、label和launchType） | 定制产物图标、名称、启动模式。 |
| so库依赖（nativeLib-filter） | 定制打包so库的过滤规则。 |
| HAR/HSP | 设备类型（deviceType） | 用于配置支持的设备类型，如Phone、Tablet等。 |
| so库依赖（nativeLib-filter） | 定制打包so库的过滤规则。 |
| 源码集（source） | target的源码范围：   * pages：定制pages源码目录的page页面，数组长度至少为1。 * sourceRoots：定制差异化代码空间，数组长度至少为1。 |
| 资源（resource） | 配置需要的资源文件路径，支持配置多个资源文件路径。 |
| App | App包名和供应商名称(artifactName、vendor) | 指定产物命名和供应商名称。 |
| bundleName | 定义工程的bundleName信息，在签名的时候可以选择对应的bundleName进行签名。如果product未定义bundleName，则采用工程默认的bundleName。 |
| bundleType | 定义产物类型：   * bundleType值为app，表示产物为应用； * bundleType值为atomicService，表示产物为元服务。 |
| 签名配置信息(signingConfig) | 为不同产物定制不同的签名文件。 |
| 应用图标、名称（icon、label） | 为不同产物定制不同的图标和名称。 |
| 依赖的模块（modules） | 定义product中包含的target，每个product可以指定一个或多个target。 |

综上所述，App、HAP、HAR、HSP包目前并不支持配置所有配置项的差异化定制，开发者在开发过程中需要根据已支持的配置项合理的进行多目标定制。

### 构建原理图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Vfng891ESKibOJDHnvpGYQ/zh-cn_image_0000002523454541.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=74A0A33D5C2F303461704C2F360566B153500FB4C5B4D43B6A001E56F2607A23 "点击放大")

如图所示，在HarmonyOS应用开发过程中，一个应用通常包含多个HAR/HAP/HSP模块。每个HAR/HAP/HSP模块可以通过配置模块级的build-profile.json文件定义多个target，每个target可以定制不同的资源（具体可参考上文定制项介绍）。因此形成了具有差异性的target，如：Module A通过定制生成了TargetA-1、TargetA-2；Module B通过定制生成了TargetB-1、TargetB-2、TargetB-3；Module C通过定制生成了TargetC-1、TargetC-2。然后通过配置工程级的build-profile.json定义多个product，每个product可以依赖不同的Target并且配置不同的App产物定制项。因此形成了具有差异的product，如：依赖TargetA-1、TargetB-1、TargetC-1构建出App-product1；依赖TargetB-3、TargetC-2构建出App-product2。最终在构建工程时选择相应的product就可以显示出对应的定制效果。

### 开发流程

1. 首先需要拆解需求，根据具体的业务场景判断出product、target信息。即确认我们要构建哪些product，每个product依赖哪些target以及每个target的定制项有哪些。
2. 分别定制每个target定制项的内容。
3. 分别定制product定制项并为其依赖需要的target。
4. 实现不同目标产物需要定制的业务逻辑。
5. 选择不同的product构建出不同目标产物。

## 场景案例

本节主要根据一个案例介绍构建多目标产物的流程和方法，该案例可以由同一套源代码构建出Official版本（官方版）和Test版本（测试版）两个product工程。两个工程的实现效果如下：

Official版本：工程会在首页中显示Official版的资源以及一个页面跳转按钮，该页面是一个HAP模块页面。通过点击按钮可以跳转到Official版定制页面，该页面是一个HAR模块页面，其中包含了一个运算器。该运算器支持加法和减法。

Test版本：工程会在首页中显示Test版的资源以及一个页面跳转按钮，该页面是一个HAP模块页面。通过点击按钮可以跳转到Test版定制页面，该页面是一个HAR模块页面，其中包含了一个普通版的运算器。该运算器仅支持减法。

该案例包含了HAP、HAR、APP相关定制项，具体差异项信息如下：

**表2** 定制项信息

| 定制模块 | Official版本定制项 | Test版本定制项 |
| --- | --- | --- |
| HAP模块(target) | 1. target名称official 2. source源码集-pages 3. 资源文件目录 4. source源码集-sourceRoots | 1. target名称test 2. source源码集-pages 3. 资源文件目录 4. source源码集-sourceRoots |
| HAR模块(target) | 1. target名称official 2. buildProfileFields自定义参数 3. 产物名称 4. source源码集-sourceRoots 5. 资源文件目录 6. 剔除的.so文件 | 1. target名称test 2. buildProfileFields自定义参数 3. 产物名称 4. source源码集-sourceRoots 5. 资源文件目录 |
| App工程（product） | 1. product名称official 2. 产物bundleName 3. 签名配置信息 4. 应用图标 5. 依赖的target | 1. product名称test 2. 产物bundleName 3. 签名配置信息 4. 应用图标 5. 依赖的target |

1. 拆解需求，根据具体的业务场景判断出product、target信息。

   首先，根据上面案例设计和定制项表格可以确认我们需要定制两个product版本，即Official版本和Test版本。每个product需要依赖两个模块，即一个HAP模块和一个HAR模块。
2. 定制target内容。

   HAP模块：在模块级build-profile.json5文件中配置。

   ```
   1. "targets": [
   2. {
   3. "name": "official",
   4. "source": {
   5. "pages": [
   6. "pages/Index"
   7. ],
   8. "sourceRoots": [
   9. "./src/official_pages"
   10. ]
   11. },
   12. "resource": {
   13. "directories": [
   14. "./src/main/official/resources",
   15. "./src/main/resources"
   16. ]
   17. }
   18. },
   19. {
   20. "name": "test",
   21. "source": {
   22. "pages": [
   23. "pages/Index"
   24. ],
   25. "sourceRoots": [
   26. "./src/test_pages"
   27. ]
   28. },
   29. "resource": {
   30. "directories": [
   31. "./src/main/test/resources",
   32. "./src/main/resources"
   33. ]
   34. }
   35. },
   36. ]
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/entry/build-profile.json5#L21-L56)

   上述配置文件代码中，配置了official版本与test版本的target名称、source源码集-pages、source源码集-sourceRoots以及资源文件路径，因此我们需要在对应的目录结构下创建我们配置的文件以及目录。针对以上配置信息，我们需要创建pages目录下的Index.ets文件、src目录下的test\_pages和official\_pages目录以及src/main目录下的resource\_test和resource\_official目录。

   在配置不同target的资源文件目录时，可以配置多个资源文件目录，建议将共有的资源文件放置到默认的资源文件目录中，将有差异的资源部分放置到定制的资源文件目录中，然后在配置资源目录时将默认的资源目录和定制的资源目录都加上。例如：案例中即给不同版本配置了两个资源目录，一个用于存放共有资源，一个存放不同target的差异性资源。

   如果target引用的多个资源文件目录下，存在同名的资源，则在构建打包过程中，将按照配置的资源文件目录顺序进行选择。例如，上述official版target引用的资源中，resource\_official和resource中存在同名的资源文件，则resource\_official中的资源会被打包到HAP中。

   \* 配置文件中，default为创建工程时默认生成的target，一般无需特殊处理。

   HAR模块：在模块级build-profile.json5文件中配置。

   ```
   1. "targets": [
   2. {
   3. "name": "official",
   4. "config": {
   5. "buildOption": {
   6. "arkOptions": {
   7. "buildProfileFields": {
   8. "productName": "official"
   9. }
   10. },
   11. "nativeLib": {
   12. "filter": {
   13. "excludes": [
   14. "../libs/arm64-v8a/libentry.so"
   15. ]
   16. }
   17. }
   18. }
   19. },
   20. "runtimeOS": "HarmonyOS",
   21. "output": {
   22. "artifactName": "official"
   23. },
   24. "source": {
   25. "sourceRoots": [
   26. "./src/official_pages"
   27. ]
   28. },
   29. "resource": {
   30. "directories": [
   31. "./src/main/official/resources",
   32. "./src/main/resources"
   33. ]
   34. }
   35. },
   36. {
   37. "name": "test",
   38. "config": {
   39. "buildOption": {
   40. "arkOptions": {
   41. "buildProfileFields": {
   42. "productName": "test"
   43. }
   44. }
   45. }
   46. },
   47. "runtimeOS": "HarmonyOS",
   48. "output": {
   49. "artifactName": "test"
   50. },
   51. "source": {
   52. "sourceRoots": [
   53. "./src/test_pages"
   54. ]
   55. },
   56. "resource": {
   57. "directories": [
   58. "./src/main/test/resources",
   59. "./src/main/resources"
   60. ]
   61. }
   62. }
   63. ]
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/myhar/build-profile.json5#L22-L84)

   上述配置文件代码中，配置了official版本与test版本的target名称、buildProFields自定义参数、产物名称、source源码集-sourceRoots以及资源文件目录，并且在official版本中剔除了无需打包的.so文件。同样的，我们也需要创建我们需要的文件目录，因此我们需要在该HAR模块的src/main/目录下创建resources\_test和resources\_official文件夹，在src/目录下创建official\_pages和test\_pages文件夹。
3. 定制product内容。

   App工程：在工程级build-profile.json5文件中配置。

   ```
   1. {
   2. "app": {
   3. "signingConfigs": [],
   4. "products": [
   5. {
   6. "name": "official",
   7. "compatibleSdkVersion": "5.0.5(17)",
   8. "targetSdkVersion": "5.0.5(17)",
   9. "runtimeOS": "HarmonyOS",
   10. "buildOption": {
   11. "strictMode": {
   12. "caseSensitiveCheck": true,
   13. "useNormalizedOHMUrl": true
   14. }
   15. },
   16. "bundleName": "com.official.com",
   17. "bundleType": "app",
   18. "icon": "$media:startIcon",
   19. "label": "$string:official_app_name"
   20. },
   21. {
   22. "name": "test",
   23. "compatibleSdkVersion": "5.0.5(17)",
   24. "targetSdkVersion": "5.0.5(17)",
   25. "runtimeOS": "HarmonyOS",
   26. "buildOption": {
   27. "strictMode": {
   28. "caseSensitiveCheck": true,
   29. "useNormalizedOHMUrl": true
   30. }
   31. },
   32. "bundleName": "com.test.com",
   33. "bundleType": "app",
   34. "icon": "$media:app_icon",
   35. "label": "$string:test_app_name"
   36. },
   37. {
   38. "name": "default",
   39. "compatibleSdkVersion": "5.0.5(17)",
   40. "targetSdkVersion": "5.0.5(17)",
   41. "runtimeOS": "HarmonyOS",
   42. }
   43. ],
   44. "buildModeSet": [
   45. {
   46. "name": "debug",
   47. },
   48. {
   49. "name": "release"
   50. }
   51. ]
   52. },
   53. "modules": [
   54. {
   55. "name": "entry",
   56. "srcPath": "./entry",
   57. "targets": [
   58. {
   59. "name": "official",
   60. "applyToProducts": [
   61. "official"
   62. ]
   63. },
   64. {
   65. "name": "test",
   66. "applyToProducts": [
   67. "test"
   68. ]
   69. }
   70. ]
   71. },
   72. {
   73. "name": "myhar",
   74. "srcPath": "./myhar"
   75. }
   76. ]
   77. }
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/build-profile.json5#L2-L78)

   在该配置文件中，配置了product名称、产物bundleName、签名配置信息、应用图标、依赖的target信息。这里需要注意的是，依赖的HAR模块需要在引用他的模块内配置依赖关系。我们的案例是在entry模块里调用的HAR包，所以需要在其对应的oh-package.json5文件中配置dependencies依赖。
4. 实现不同目标产物需要定制的业务逻辑。
   * 通过[source源码集-sourceRoots配置](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section18668905913)的差异性代码空间，实现标题（代码文件）多目标效果。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/CWU4jbxHSWebQ1_pZoUoNw/zh-cn_image_0000002229335589.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=43FFCCC1EF2E5A71448C59232519A2202E6FD5190F831FE6A5165315DC89570A) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Q0P7Br13TMOf3pU7S_VmFg/zh-cn_image_0000002193850196.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=286A9ED40AF86060AB3281B467A5D1887DB9970AEA225DA61200881FCD2FA055)

     在上述配置文件中，配置了HAP模块的source源码集-sourceRoots目录，official版本与test版本分别对应src/official\_pages和src/test\_pages。

     分别在对应的sourceRoots目录下创建同名ets文件并创建同名同类型的方法，例如：示例中创建的是VersionInfo.ets文件。添加如下代码：

     src/official\_pages/VersionInfo.ets

     ```
     1. export const getName = () => "This is official version."
     2. export const getTitleName = () => $r('app.string.title')
     ```

     [VersionInfo.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/entry/src/official_pages/VersionInfo.ets#L16-L17)

     src/test\_pages/VersionInfo.ets

     ```
     1. export const getName = () => "This is test version."
     2. export const getTitleName = () => $r('app.string.title')
     ```

     [VersionInfo.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/entry/src/test_pages/VersionInfo.ets#L16-L17)

     在Index.ets文件中，通过import packageName的方式，省略sourceRoot，可以实现不同target下的差异化构建（ import xxx from '<packageName>/sourceFileName'）。该能力具体可参考：[source源码集-sourceRoots配置](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section18668905913)。

     ```
     1. import { MainPage } from 'myhar'
     2. import { getName, getTitleName } from 'entry/VersionInfo'

     4. @Entry
     5. @Component
     6. struct Index {
     7. @State message: string = getName();
     8. @State titleMessage: Resource = getTitleName();

     10. build() {
     11. Column() {
     12. Column() {
     13. Text(this.titleMessage)
     14. .height(40)
     15. .fontSize(30)
     16. .fontWeight(FontWeight.Medium)
     17. Text(this.message)
     18. .fontSize(14)
     19. .fontWeight(FontWeight.Normal)
     20. .fontColor(Color.Black)
     21. .opacity(0.6)
     22. .height(19)
     23. .margin({ top: 2 })
     24. }
     25. .height(78)
     26. .width('100%')
     27. .alignItems(HorizontalAlign.Start)
     28. .padding({
     29. left: 12,
     30. right: 12,
     31. top: 8,
     32. bottom: 12
     33. })

     35. Row() {
     36. MainPage()
     37. .backgroundColor('#F1F3F5')
     38. }
     39. .layoutWeight(1)
     40. }
     41. .width('100%')
     42. .height('100%')
     43. .backgroundColor('#F1F3F5')
     44. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
     45. }
     46. }
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/entry/src/main/ets/pages/Index.ets#L16-L61)
   * 在HAR模块引用差异性资源，实现页面中资源多目标效果。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/nD9bXVNxSqOQrRRRxof_kA/zh-cn_image_0000002194009792.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=9FBAA34F7FFA777F50773689F05A273EEBE6422A59408FFC87B67BEB7BBD08FA) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NN0depcgQmGYfGY1v3dWow/zh-cn_image_0000002194009796.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=0BA0F541037A84B9010C725E5A4B24E6D10E19E23C7042EE4E729C6A53F8F934)

     在上述配置文件中，我们配置了HAR模块的资源文件路径，official版本和test版本分别对应src/main/official/resources和src/main/test/resources文件。

     分别在对应的资源文件目录下添加同名图片资源和json字符串。例如：示例中分别在资源文件目录下的media文件中放入同名的HarImage.jpg图片（图片内容不同），并在element文件下的string.json中添加同名参数"title\_description"（其对应的"value"值不相同）。

     在页面中直接引用对应同名资源即可，代码如下：

     ```
     1. TextArea({ text: $r('app.string.title_description') })
     2. .fontSize(16)
     3. .width('100%')
     4. .fontColor('#e6000000')
     5. .fontWeight(FontWeight.Normal)
     6. .borderRadius(16)
     7. .focusable(false)
     8. Image($r('app.media.HarImage'))
     9. .width('100%')
     10. .borderRadius(12)
     11. .padding({ top: 16 })
     ```

     [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/myhar/src/main/ets/components/MainPage.ets#L41-L51)
   * 在HAR模块中通过不同自定义参数信息跳转到不同页面，实现路由跳转多目标效果。

     效果对比如下：

     **图1** official版本  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/W1AG4WmGRTeEYRf-9W5Ktw/zh-cn_image_0000002229335573.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=BC7D02DFE70FF77143B427C4389C5840CDD46E93E5D0FCB21F2D45E997D3BCD2)

     **图2** test版本  
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/k-jnAMX4ThyspsxPh2JsAw/zh-cn_image_0000002193850204.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=FC8AA8828DBDA92BCB6A8D7D74ACAE0F2924F9220010C799BE3714CCF4721D56)

     在先前的案例中，已经介绍了如何在sourceRoots目录配置的差异性代码空间中实现对同名文件中的同名方法的调用。这里主要介绍在不同的target中如何调用不同名的文件中的不同方法。

     首先，需要通过配置文件中配置的自定义参数[生成相应的BuildProfile.ets文件](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md#section8279154125918)。上述HAR模块的配置文件中，我们配置了buildProfileFields自定义参数"productName"，在official和test版本中分别配置了不同的值"official"和"test"。这样我们构建不同的产物版本就会生成不同的"productName"值，用于在代码工程中区分不同的产物版本。

     然后，分别在official和test的对应的sourceRoots目录下创建不同的ets文件，并导出相应的组件。如示例中在HAR模块的src/official\_pages目录下创建了OfficialSecondPages.ets并export了一个OfficialSecond组件，然后在src/test\_pages目录下创建了TestSecondPages.ets并export了一个TestSecond组件。这两个组件中分别包含了不同的页面信息。

     最后在首页中import相应的方法实现跳转逻辑。具体代码如下：

     导入方法及组件：

     ```
     1. import BuildProfile from '../../../../BuildProfile';
     2. import { OfficialSecond } from '../../../official_pages/OfficialSecondPage';
     3. import { TestSecond } from '../../../test_pages/TestSecondPage';
     ```

     [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/myhar/src/main/ets/components/MainPage.ets#L16-L18)

     定义页面跳转逻辑：接收到不同的参数值跳转不同页面。

     ```
     1. @Builder
     2. PagesMap(name: string) {
     3. if (name == 'official') {
     4. OfficialSecond();
     5. } else {
     6. TestSecond();
     7. }
     8. }
     ```

     [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/myhar/src/main/ets/components/MainPage.ets#L26-L33)

     为按钮添加点击属性，并传递自定义参数，用于实现Navigation路由跳转：

     ```
     1. Button($r('app.string.button_describe'))
     2. .fontSize(16)
     3. .height(40)
     4. .width('100%')
     5. .onClick(() => {
     6. this.pageInfos.pushPath({ name: BuildProfile.productName });
     7. })
     ```

     [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/MultiTarget/blob/master/myhar/src/main/ets/components/MainPage.ets#L55-L61)
5. 选择不同的product构建出不同的目标产物。

   **图3** 构建图示  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8ATZvCZfQW2-LqviuwsfBw/zh-cn_image_0000002229450045.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=C5D8374447F1B8A0FF87E01E9E10F8D56170BB7B17C9903BAA50D681396942B0)

   首先点击DevEco Studio工具右上角的Product按钮，即图中的1号标识处，然后在2号标识处选择对应的product工程，选择完工程之后会自动映射出我们文件中已经依赖的target，最后点击Apply应用。上述操作完成之后就可以点击运行按钮查看多目标产物效果了。本案例运行效果图如下：

   **图4** Official版本

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/6RR9FvRlSeWhD4CIo8npdg/zh-cn_image_0000002194009800.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=D15670DAA20A841DEBDBD327C78285F386DA4FB5AF0EB0878044E5B90050488C)

   **图5** Test版本  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/WqnyDnGXSJChjIWCI0ovRQ/zh-cn_image_0000002229335577.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=28DE3CC2EE86515E83E93981BE22C5FC52CC32CD3D66E33F7DCC7DDD0BCB090D)

## 常见问题

### 如何为不同的product产物配置签名信息？

配置工程级的build-profile.json5文件.

首先需要在每个product下添加配置项"signingConfig"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/7Q0LaCjWRC6cnYA6BP0yfw/zh-cn_image_0000002229335565.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=2D28B1032C19A9707E0227F783CB8BEB8E7608EB0AF3ADE98BCFCB18137B4F5B "点击放大")

然后进入到签名配置页面，点击加号，添加签名信息：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/VZjjueAzSieTSDmudgdyog/zh-cn_image_0000002229450081.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=442FE7754EE3C3454AFFD8BCFA16A0C56A82576B011A48A3AA61B8F726D44C3A "点击放大")

然后选择对应的bundle name，并填写上面配置的"signingConfig"信息（每个product产物都需要配置）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/42oudhPPSgan1h72xeCi_w/zh-cn_image_0000002193850180.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=C746C46FB426090C1E8D62BBE778478BC6EF0BA0876CA6B0A6511910841D68CD "点击放大")

点击ok之后，进行签名即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/WY1EP5quQO-kdOp3DUncAQ/zh-cn_image_0000002193850208.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=96073687527D0C36072FF1DBDEC75DA8082395500E9414C41D1D4387DF57421F "点击放大")

## 示例代码

* [构建多目标产物工程](https://gitcode.com/harmonyos_samples/MultiTarget)
