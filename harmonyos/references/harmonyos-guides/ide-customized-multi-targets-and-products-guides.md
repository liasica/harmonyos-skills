---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides
title: 能力说明
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 配置多目标产物 > 能力说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:402a17b2fef4793a901d88d006c730ba7112fb0d18bf6c3a0f36483995b9874a
---

通常情况下，应用厂商会根据不同的部署环境，不同的目标人群，不同的运行环境等，将同一个应用定制为不同的版本，如国内版、国际版、普通版、VIP版、免费版、付费版等。针对以上场景，DevEco Studio支持通过少量的代码配置以实例化不同的差异版本，在编译构建过程中实现一个应用构建出不同的目标产物版本，从而实现源代码、资源文件等的高效复用。

在了解HarmonyOS应用的多目标构建产物如何定制前，先了解target和product的概念：

* 工程内的每一个Entry/Feature模块，对应的构建产物为HAP，HAP是应用/元服务可以独立运行在设备中的形态。由于在不同的业务场景中，同一个模块可能需要定制不同的功能或资源，因此引入target的概念。一个模块可以定义多个target，每个target对应一个定制的HAP，通过配置可以实现一个模块构建出不同的HAP。
* 一个HarmonyOS工程的构建产物为APP包，APP包用于应用/元服务发布上架应用市场。由于不同的业务场景，需要定制不同的应用包，因此引入product概念。一个工程可以定义多个product，每个product对应一个定制化应用包，通过配置可以实现一个工程构建出多个不同的应用包。

更多关于多目标产物的实践请参考[多目标产物构建开发实践](../best-practices/bpta-multi-target.md)。

## 定制HAP多目标构建产物

每一个Entry/Feature模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持HAP包名、设备类型（deviceType）、源码集（source）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、分发规则（distributionFilter）的定制。

**定义目标产物target**

每一个target对应一个定制的HAP，因此，在定制HAP多目标构建产物前，应提前规划好需要定制的target名称。例如，以ArkTS Stage模型为例，定义一个免费版和付费版，模块级build-profile.json5文件示例如下：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [  //定义不同的target
6. {
7. "name": "default",  //默认target名称default
8. },
9. {
10. "name": "free",  //免费版target名称
11. },
12. {
13. "name": "pay",  //付费版target名称
14. }
15. ]
16. }
```

按照上述target的定义，在编译构建时，会同时打包生成default、free和pay三个不同的HAP。

### 定义产物的HAP包名

每一个target均可以指定产物命名。

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",
8. "output": {
9. "artifactName": "customizedTargetOutputName-1.0.0"  //产物名称为customizedTargetOutputName-1.0.0
10. }
11. },
12. {
13. "name": "free",
14. "output": {
15. "artifactName": "customizedTargetOutputName1-1.0.0"  //产物名称为customizedTargetOutputName1-1.0.0
16. }
17. },
18. {
19. "name": "pay",
20. "output": {
21. "artifactName": "customizedTargetOutputName2-1.0.0"  //产物名称为customizedTargetOutputName2-1.0.0
22. }
23. }
24. ]
25. }
```

如果已配置签名，target产物对应的HAP包名为开发者定制的名称；如果未配置签名，target产物对应的HAP包名为开发者定制的名称+unsigned。

### 定义产物的deviceType

每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持module.json5/[config.json](application-configuration-file-overview-fa.md)中定义的设备类型。

同时，在定义每个target的deviceType时，支持的设备类型必须在module.json5或config.json中已经定义。例如，在上述定义的3个target中，分别定义default默认支持所有设备类型，free和pay版本只支持phone设备。

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",  //未定义deviceType，默认支持config.json或module.json5中定义的设备类型

9. },
10. {
11. "name": "free",
12. "config": {
13. "deviceType": [  //定义free支持的设备类型为phone
14. "phone"
15. ]
16. }
17. },
18. {
19. "name": "pay",
20. "config": {
21. "deviceType": [  //定义pay支持的设备类型为phone
22. "phone"
23. ]
24. }
25. }
26. ]
27. }
```

### 定义产物的distributionFilter

在未定义target的分发规则distributionFilter时，以module配置[distributionFilter](module-configuration-file.md#distributionfilter标签)/[distroFilter](module-structure.md#distrofilter对象的内部结构)分发规则为准。

针对多target存在相同设备类型deviceType的场景，相同设备类型的target需要指定分发规则distributionFilter。

如果是FA工程，请将distributionFilter字段替换为distroFilter。

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",

9. },
10. {
11. "name": "free",
12. "config": {
13. "distributionFilter": {  // 具体请参考distributionFilter标签
14. "screenShape": { // 屏幕形状枚举
15. "policy": "include",
16. "value": ["circle"]
17. }
18. }
19. }
20. },
21. {
22. "name": "pay",
23. "config": {
24. "distributionFilter": {
25. "screenShape": {
26. "policy": "include",
27. "value": ["rect"]
28. }
29. }
30. }
31. }
32. ]
33. }
```

### 定义产物preloads的分包

对于元服务，每一个target均可以指定preloads的分包，也可以不定义。如果不定义，则以module.json5中的配置为准。

```
1. {
2. "apiType": 'stageMode',
3. "showInServiceCenter": true,
4. "buildOption": {
5. },
6. "targets": [
7. {
8. "name": "default",
9. },
10. {
11. "name": "free",
12. },
13. {
14. "name": "pay",
15. "config": {
16. "atomicService": {
17. "preloads": [  //指定preloads的分包
18. {
19. "moduleName": "preloadSharedLibrary"
20. }
21. ]
22. }
23. }
24. }
25. ]
26. }
```

### 定义产物的source源码集-pages

对于source源码集的定制，由于Stage模型和FA模型的差异，Stage模型支持对pages源码目录的page页面进行定制，FA模型则支持对Ability源码目录下的page页面进行定制。

* 例如，Stage模型中的工程，在模块的pages目录下分别定义了Index.ets、Page1.ets和Page2.ets三个页面。其中default使用了Index.ets页面；free使用了Index.ets和Page1.ets页面；pay使用了Index.ets和Page2.ets页面，则示例代码如下所示：

  ```
  1. {
  2. "apiType": 'stageMode',
  3. "buildOption": {
  4. },
  5. "targets": [
  6. {
  7. "name": "default",
  8. "source": {  //定义Stage模型中默认版target的pages源码文件
  9. "pages": [
  10. "pages/Index"
  11. ]
  12. }
  13. },
  14. {
  15. "name": "free",
  16. "config": {
  17. "deviceType": [
  18. "phone"
  19. ]
  20. },
  21. "source": {  //定义Stage模型中免费版target的pages源码文件
  22. "pages": [
  23. "pages/Index",
  24. "pages/Page1"
  25. ]
  26. }
  27. },
  28. {
  29. "name": "pay",
  30. "config": {
  31. "deviceType": [
  32. "phone"
  33. ]
  34. },
  35. "source": {  //定义Stage模型中付费版target的pages源码文件
  36. "pages": [
  37. "pages/Index",
  38. "pages/Page2"
  39. ]
  40. }
  41. }
  42. ]
  43. }
  ```

* 例如，FA模型中的工程，在模块的MainAbility中定义了index.ets、page1.ets和page2.ets，其中：default使用了index.ets 页面；free使用了index.ets和page1.ets页面；pay使用了index.ets和page2.ets页面。

  ```
  1. {
  2. "apiType": 'faMode',
  3. "buildOption": {
  4. },
  5. "targets": [
  6. {
  7. "name": "default",
  8. "source": {  //定义FA模型中默认版target的pages源码文件
  9. "abilities": [
  10. {
  11. "name": ".MainAbility",
  12. "pages": [
  13. "pages/index"
  14. ]
  15. }
  16. ],
  17. }
  18. },
  19. {
  20. "name": "free",
  21. "config": {
  22. "deviceType": [
  23. "phone"
  24. ]
  25. },
  26. "source": {  //定义FA模型中免费版target的pages源码文件
  27. "abilities": [
  28. {
  29. "name": ".MainAbility",
  30. "pages": [
  31. "pages/index",
  32. "pages/page1"
  33. ]
  34. }
  35. ],
  36. }
  37. },
  38. {
  39. "name": "pay",
  40. "config": {
  41. "deviceType": [
  42. "phone"
  43. ]
  44. },
  45. "source": {  //定义FA模型中付费版target的pages源码文件
  46. "abilities": [
  47. {
  48. "name": ".MainAbility",
  49. "pages": [
  50. "pages/index",
  51. "pages/page2"
  52. ]
  53. }
  54. ],
  55. }
  56. }
  57. ]
  58. }
  ```

### 定义产物的source源码集-sourceRoots

在模块的主代码空间（src/main）下，承载着开发者编写的公共代码。如果开发者需要实现不同target之间的差异化逻辑，可以使用差异化代码空间（sourceRoots）。配合差异化代码空间的能力，可以在主代码空间中代码不变的情况下，针对不同的target，编译对应的代码到最终产物中。

**概念说明**

* packageName：当前模块的oh-package.json5中的name字段对应的值。
* sourceRoot：<defaultSourceRoot> | <targetSourceRoot> ，其中<defaultSourceRoot>是 src/main，<targetSourceRoot>可自定义，寻址优先级为 <targetSourceRoot> > <defaultSourceRoot>。
* sourcePath：在sourceRoot中的代码结构目录。
* sourceFileName：代码目录下的ets文件名。

例如以下工程目录：

```
1. entry
2. |--src
3. |----main
4. |------ets
5. |--------code
6. |----------test.ets
7. |----target
8. |------util
9. |--------util.ets
```

* packageName为entry。
* sourceRoot为src/main、src/target。
* sourcePath为ets/code、util。
* sourceFileName为test.ets、util.ets。

**规格限制**

1. import xxx from '<packageName>/sourcePath/sourceFileName' ：通过packageName的方式，省略sourceRoot，可以实现不同target下的差异化构建。

2. 支持hap、hsp、har（请注意：开启[文件/文件夹名称混淆](source-obfuscation.md#section-enable-filename-obfuscation)的har模块需要使用-keep-file-name指定sourceRoot，sourcePath，sourceFileName对应的文件/文件夹名称不被混淆）。

3. 不支持跨模块引用。

4. 不支持动态import。

**编译时模块target的选择优先级说明**

在模块编译的过程中，该模块使用的sourceRoots由当前模块编译时的target来决定。当前模块编译时选择target的优先级则为：命令行显式指定 > 直接引用方target > default。

如以下示例：

hap -> hsp -> har（->表示依赖）

其中hap和hsp存在三个target：default、custom、static，而har存在两个target：default、static。

* 执行编译命令：hvigorw -p module=hap@custom assembleHap，hap指定target为custom进行编译，那么三个模块编译时的target分别为：

  hap: custom，命令行显式指定；

  hsp: custom，命令行没有显式指定，则基于直接引用方查找，hsp的直接引用方为hap，hap的target为custom，hsp存在该target，则hsp的target为custom；

  har: default，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为custom，har不存在该target，则har的target为default；

* 执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp，hap指定target为custom，hsp则指定target为static进行编译，那么三个模块编译时的target分别为：

  hap: custom，命令行显式指定；

  hsp: static，命令行显式指定；

  har: static，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为static，har存在该target，则har的target为static。
* 在当前依赖关系的基础上，添加依赖：hap -> har。执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp。由于har没有显式指定target，且存在两个target不同的直接引用方（hap和hsp，对应的target分别为custom和static），所以编译过程中har的target只能二选一。基于这种场景，建议开发者显式指定模块的target进行编译：hvigorw -p module=hap@custom,hsp@static,har@static assembleHap assembleHsp assembleHar。

**示例**

1. 在entry模块的build-profile.json5中添加sourceRoots：

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {},
4. "targets": [
5. {
6. "name": "default",
7. "source": {
8. "sourceRoots": ["./src/default"] // 配置target为default的差异化代码空间
9. }
10. },
11. {
12. "name": "custom",
13. "source": {
14. "sourceRoots": ["./src/custom"] // 配置target为custom的差异化代码空间
15. }
16. }
17. ]
18. }
```

2. 在src目录下新增default/Test.ets和custom/Test.ets，新增后的模块目录结构：

```
1. entry
2. |--src
3. |--main
4. |--ets
5. |--pages
6. |--Index.ets
7. |--default
8. |--Test.ets  // 新增
9. |--custom
10. |--Test.ets  // 新增
```

3. 在default/Test.ets中写入代码：

```
1. export const getName = () => "default"
```

4. 在custom/Test.ets中写入代码：

```
1. export const getName = () => "custom"
```

5. 修改src/main/ets/pages/Index.ets的代码：

```
1. import { getName } from 'entry/Test'; // 其中entry为模块级的oh-package.json5中的name字段的值
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = getName();
6. build() {
7. RelativeContainer() {
8. Text(this.message)
9. }
10. .height('100%')
11. .width('100%')
12. }
13. }
```

6. 在工程级的build-profile.json5中配置targets：

```
1. {
2. "app": {
3. "signingConfigs": [],
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.0(23)",
9. "runtimeOS": "HarmonyOS",
10. }
11. ],
12. "buildModeSet": [
13. {
14. "name": "debug",
15. },
16. {
17. "name": "release"
18. }
19. ]
20. },
21. "modules": [
22. {
23. "name": "entry",
24. "srcPath": "./entry",
25. "targets": [
26. {
27. "name": "default",
28. "applyToProducts": [
29. "default"
30. ]
31. },
32. {
33. "name": "custom",
34. "applyToProducts": [
35. "default"
36. ]
37. }
38. ]
39. }
40. ]
41. }
```

7. Sync完成后，选择entry的target为default，点击Run，界面展示default；选择entry的target为custom，点击Run，则界面展示custom。

### 定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",
8. "source": {
9. "pages": [
10. "pages/Index"
11. ]
12. },
13. "resource": {  // 定义默认版target使用的资源文件目录
14. "directories": [
15. "./src/main/resources_default"
16. ]
17. }
18. },
19. {
20. "name": "free",
21. "config": {
22. "deviceType": [
23. "phone"
24. ]
25. },
26. "source": {
27. "pages": [
28. "pages/Index",
29. "pages/Page1"
30. ]
31. },
32. "resource": {  // 定义免费版target使用的资源文件目录
33. "directories": [
34. "./src/main/resources_free",
35. "./src/main/resources_default"
36. ]
37. }
38. },
39. {
40. "name": "pay",
41. "config": {
42. "deviceType": [
43. "phone"
44. ]
45. },
46. "source": {
47. "pages": [
48. "pages/Index",
49. "pages/Page2"
50. ]
51. },
52. "resource": {  // 定义付费版target使用的资源文件目录
53. "directories": [
54. "./src/main/resources_pay",
55. "./src/main/resources_default"
56. ]
57. }
58. }
59. ]
60. }
```

编译构建时，资源文件存在以下优先级顺序：

* AppScope目录下的资源文件会合入到模块下相同路径的资源目录中。如果两个目录下存在重名文件，编译打包后AppScope目录下的资源文件会覆盖模块下的资源。
* 如果target引用的多个资源文件目录下，存在重名文件，则在构建打包过程中，将按照配置的资源文件目录顺序进行选择。例如，上述付费版target引用的资源中，resources\_pay和resources\_default中存在重名文件，则resources\_pay中的资源会被打包到HAP中。

### 定义产物的icon、label、launchType

针对每一个的target的ability，均可以定制不同的icon、label和launchType。如果不定义，则该target采用module.json5中module.abilities配置的icon、label，launchType默认为"singleton"。示例如下所示：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",
8. "source": {
9. "abilities": [
10. {
11. "name": "EntryAbility",
12. "icon":"$media:layered_image",
13. "label":"$string:EntryAbility_label",
14. "launchType": "singleton"
15. }
16. ]
17. }
18. },
19. {
20. "name": "free",
21. "source": {
22. "abilities": [
23. {
24. "name": "EntryAbility",
25. "icon":"$media:layered_image",
26. "label":"$string:EntryAbility_label",
27. "launchType": "multiton"
28. }
29. ]
30. }
31. }
32. ]
33. }
```

### 定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. "externalNativeOptions": {
5. "path": "./src/main/cpp/CMakeLists.txt",
6. "arguments": [],
7. "abiFilters": [
8. "arm64-v8a",
9. "x86_64"
10. ],
11. "cppFlags": "",
12. }
13. },
14. "targets": [  //定义不同的target
15. {
16. "name": "default",
17. "config": {
18. "buildOption": {
19. "nativeLib": {
20. "filter": {
21. //按照.so文件的优先级顺序，打包最高优先级的function1.so文件
22. "pickFirsts": [
23. "**/function1.so"
24. ],
25. //排除不打包的function3.so文件
26. "excludes": [
27. "**/function3.so"
28. ],
29. //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件
30. "enableOverride": true
31. }
32. }
33. }
34. }
35. },
36. {
37. "name": "vip",
38. "config": {
39. "buildOption": {
40. "nativeLib": {
41. "filter": {
42. //按照.so文件的优先级顺序，打包最高优先级的function1.so文件
43. "pickFirsts": [
44. "**/function1.so"
45. ],
46. //排除不打包的function2.so文件
47. "excludes": [
48. "**/function2.so"
49. ],
50. //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件
51. "enableOverride": true
52. }
53. }
54. }
55. }
56. }
57. ]
58. }
```

## 定制HAR多目标构建产物

每一个HAR模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持设备类型（deviceType）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、源码集（source）的定制。

DevEco Studio 6.0.2 Beta1版本之前，在DevEco Studio中构建HAR模块时，仅支持default target，若需指定其他target，需通过命令行来指定和构建。

例如构建自定义target为free的HAR，可参考执行以下命令：

```
1. hvigorw --mode module -p product=default -p module=library@free -p buildMode=debug assembleHar
```

从DevEco Studio 6.0.2 Beta1版本开始，支持在DevEco Studio中选择HAR模块的target，选择的target仅在单独构建HAR包时生效。如果是构建HAP/HSP，会动态计算依赖HAR的target，具体请参考[多产物构建target](ide-customized-multi-targets-and-products-guides.md#section7121513141619)。

### 定义产物的deviceType

每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持module.json5/[config.json](application-configuration-file-overview-fa.md)中定义的设备类型。

同时，在定义每个target的deviceType时，支持的设备类型必须在module.json5或config.json中已经定义。例如，在上述定义的2个target中，分别定义default默认支持所有设备类型，free版本只支持2in1设备。

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default"  //未定义deviceType，默认支持config.json或module.json5中定义的设备类型
8. },
9. {
10. "name": "free",
11. "config": {
12. "deviceType": [  //定义free支持的设备类型为2in1
13. "2in1"
14. ]
15. }
16. }
17. ]
18. }
```

### 定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. "externalNativeOptions": {
5. "path": "./src/main/cpp/CMakeLists.txt",
6. "arguments": [],
7. "abiFilters": [
8. "arm64-v8a",
9. "x86_64"
10. ],
11. "cppFlags": "",
12. }
13. },
14. "targets": [  //定义不同的target
15. {
16. "name": "default",
17. "config": {
18. "buildOption": {
19. "nativeLib": {
20. "filter": {
21. //按照.so文件的优先级顺序，打包最高优先级的function1.so文件
22. "pickFirsts": [
23. "**/function1.so"
24. ],
25. //排除不打包的function3.so文件
26. "excludes": [
27. "**/function3.so"
28. ],
29. //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件
30. "enableOverride": true
31. }
32. }
33. }
34. }
35. },
36. {
37. "name": "vip",
38. "config": {
39. "buildOption": {
40. "nativeLib": {
41. "filter": {
42. //按照.so文件的优先级顺序，打包最高优先级的function1.so文件
43. "pickFirsts": [
44. "**/function1.so"
45. ],
46. //排除不打包的function2.so文件
47. "excludes": [
48. "**/function2.so"
49. ],
50. //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件
51. "enableOverride": true
52. }
53. }
54. }
55. }
56. }
57. ]
58. }
```

### 定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

```
1. {
2. "apiType": 'stageMode',
3. "buildOption": {
4. },
5. "targets": [
6. {
7. "name": "default",
8. "resource": {  //定义默认版target使用的资源文件目录
9. "directories": [
10. "./src/main/resources_default"
11. ]
12. }
13. },
14. {
15. "name": "free",
16. "config": {
17. "deviceType": [
18. "2in1"
19. ]
20. },
21. "resource": {  //定义免费版target使用的资源文件目录
22. "directories": [
23. "./src/main/resources_free",
24. "./src/main/resources_default"
25. ]
26. }
27. },
28. ]
29. }
```

### 定义产物的source源码集-sourceRoots

请参考[定义产物的source源码集-sourceRoots](ide-customized-multi-targets-and-products-guides.md#section18668905913)。

## 配置APP多目标构建产物

APP用于应用/元服务上架发布，针对不同的应用场景，可以定制不同的product，每个product中支持对bundleName、bundleType、签名信息、icon和label以及包含的target进行定制。

**定义目标产物product**

每一个product对应一个定制的APP包，因此，在定制APP多目标构建产物前，应提前规划好需要定制的product名称。例如，定义productA和productB。工程级build-profile.json5文件示例如下：

在定制product时，必须存在"default"的product，否则编译时会出现错误。

说明

在编译构建流程中，default product或者default target都承载着兜底机制，其中，default target可以缺省。当某个模块的default target缺省时，Hvigor会默认加上default target并挂载到default product中，因此，构建default product时，默认会构建出default target。如果不想构建出default target，建议参考[定义product中包含的target](ide-customized-multi-targets-and-products-guides.md#section7613106105114)，自定义product以及包含的target。

```
1. "app": {
2. "signingConfigs": [],
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default",
7. "compatibleSdkVersion": "6.1.0(23)",
8. "runtimeOS": "HarmonyOS",
9. },
10. {
11. "name": "productA",
12. "compatibleSdkVersion": "6.1.0(23)",
13. "runtimeOS": "HarmonyOS",
14. },
15. {
16. "name": "productB",
17. "compatibleSdkVersion": "6.1.0(23)",
18. "runtimeOS": "HarmonyOS",
19. }
20. ],
21. "buildModeSet": [
22. {
23. "name": "debug",
24. },
25. {
26. "name": "release"
27. }
28. ]
29. }
```

### 定义产物的APP包名和供应商名称

每一个product均可以指定产物命名和供应商名称。

```
1. {
2. "app": {
3. "signingConfigs": [],
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.0(23)",
9. "runtimeOS": "HarmonyOS",
10. "output": {
11. "artifactName": "customizedProductOutputName-1.0.0"  //产物名称为customizedProductOutputName-1.0.0
12. },
13. "vendor": "customizedProductVendorName"   //供应商名称为customizedProductVendorName
14. },
15. {
16. "name": "productA",
17. "compatibleSdkVersion": "6.1.0(23)",
18. "runtimeOS": "HarmonyOS",
19. "output": {
20. "artifactName": "customizedProductOutputNameA-1.0.0"  //产物名称为customizedProductOutputNameA-1.0.0
21. },
22. "vendor": "customizedProductVendorNameA"   //供应商名称为customizedProductVendorNameA
23. },
24. {
25. "name": "productB",
26. "compatibleSdkVersion": "6.1.0(23)",
27. "runtimeOS": "HarmonyOS",
28. "output": {
29. "artifactName": "customizedProductOutputNameB-1.0.0" //产物名称为customizedProductOutputNameB-1.0.0
30. },
31. "vendor": "customizedProductVendorNameB"   //供应商名称为customizedProductVendorNameB
32. }
33. ],
34. "buildModeSet": [
35. {
36. "name": "debug",
37. },
38. {
39. "name": "release"
40. }
41. ]
42. },
43. }
```

如果已配置签名，product产物对应的APP包名为开发者定制的名称；如果未配置签名，product产物对应的APP包名为开发者定制的名称+unsigned。

### 定义product的bundleName

针对每个定义的product，均可以定制不同的bundleName，如果product未定义bundleName，则采用工程默认的bundleName。示例如下所示：

```
1. "app": {
2. "signingConfigs": [],
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default",
7. "compatibleSdkVersion": "6.1.0(23)",
8. "runtimeOS": "HarmonyOS",
9. "bundleName": "com.example00.com"  //定义default的bundleName信息
10. },
11. {
12. "name": "productA",
13. "signingConfig": "default",
14. "compatibleSdkVersion": "6.1.0(23)",
15. "runtimeOS": "HarmonyOS",
16. "bundleName": "com.example01.com"  //定义productA的bundleName信息
17. },
18. {
19. "name": "productB",
20. "signingConfig": "default",
21. "compatibleSdkVersion": "6.1.0(23)",
22. "runtimeOS": "HarmonyOS",
23. "bundleName": "com.example02.com"  //定义productB的bundleName信息
24. }
25. ],
26. "buildModeSet": [
27. {
28. "name": "debug",
29. },
30. {
31. "name": "release"
32. }
33. ]
34. }
```

### 定义product的bundleType

针对每个定义的product，均可以定制不同的bundleType。开发者可以通过定义每个product的bundleType，分别定义产物类型：

* bundleType值为app，表示产物为应用；
* bundleType值为atomicService，表示产物为元服务。

如果product未定义bundleType，则采用工程的bundleType（即创建工程时选择的Application/Atomic Service）。示例如下所示：

```
1. "app": {
2. "signingConfigs": [],
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default",
7. "compatibleSdkVersion": "6.1.0(23)",
8. "runtimeOS": "HarmonyOS",
9. "bundleName": "com.example00.com",
10. "bundleType": "app" //定义default的bundleType信息
11. },
12. {
13. "name": "productA",
14. "signingConfig": "default",
15. "compatibleSdkVersion": "6.1.0(23)",
16. "runtimeOS": "HarmonyOS",
17. "bundleName": "com.example01.com",
18. "bundleType": "atomicService"  //定义productA的bundleType信息
19. },
20. {
21. "name": "productB",
22. "signingConfig": "default",
23. "compatibleSdkVersion": "6.1.0(23)",
24. "runtimeOS": "HarmonyOS",
25. "bundleName": "com.example02.com",
26. "bundleType": "atomicService"  //定义productB的bundleType信息
27. }
28. ],
29. "buildModeSet": [
30. {
31. "name": "debug",
32. },
33. {
34. "name": "release"
35. }
36. ]
37. }
```

### 定义product的签名配置信息

针对每个定义的product，均可以定制不同的signingConfig签名文件，如果product未定义signingConfig，则构建生成未签名的APP包。

通常情况下，您首先需要在签名配置界面或工程的build-profile.json5文件中配置签名信息。例如在**File > Project Structure > Project > Signing Configs**界面，分别配置default、productA和productB的签名信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/3CWqXOkHSwWBX1TYCOiAkw/zh-cn_image_0000002561753291.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=E26E15D5B6A1721016988B64A654234688A929493C86B866B6E4792F780C2B39)

签名信息配置完成后，再添加各个product对应的签名文件，示例如下所示：

您也可以提前在product中定义签名文件信息，然后在签名界面对每个product进行签名，确保配置的product签名文件与签名界面配置的签名文件保持一致即可。

```
1. "app": {
2. "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default", //定义default的签名文件信息
7. "compatibleSdkVersion": "6.1.0(23)",
8. "runtimeOS": "HarmonyOS",
9. "bundleName": "com.example00.com"
10. },
11. {
12. "name": "productA",
13. "signingConfig": "productA", //定义productA的签名文件信息
14. "compatibleSdkVersion": "6.1.0(23)",
15. "runtimeOS": "HarmonyOS",
16. "bundleName": "com.example01.com"
17. },
18. {
19. "name": "productB",
20. "signingConfig": "productB", //定义productB的签名文件信息
21. "compatibleSdkVersion": "6.1.0(23)",
22. "runtimeOS": "HarmonyOS",
23. "bundleName": "com.example02.com"
24. }
25. ],
26. "buildModeSet": [
27. {
28. "name": "debug",
29. },
30. {
31. "name": "release"
32. }
33. ]
34. }
```

### 定义product的icon和label

针对每个定义的product，均可以定制不同的icon和label，如果product未定义icon和label，则采用工程默认的icon和label。示例如下所示：

说明

products中的icon和label字段在编译时会替换[app.json5](app-configuration-file.md)中对应的字段，app.json5和module.json5均可以配置这两个字段，如果都配置，优先级顺序请参考[配置优先级](layered-image.md#配置优先级和生成策略)。

```
1. {
2. "app": {
3. "signingConfigs": [],
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.0(23)",
9. "runtimeOS": "HarmonyOS",
10. "icon":"$media:default_icon", //定义default的icon
11. "label":"$string:default_name", //定义default的label
12. },
13. {
14. "name": "productA",
15. "signingConfig": "default",
16. "compatibleSdkVersion": "6.1.0(23)",
17. "icon":"$media:productA_icon", //定义productA的icon
18. "label":"$string:productA_name", //定义productA的label
19. },
20. {
21. "name": "productB",
22. "signingConfig": "default",
23. "compatibleSdkVersion": "6.1.0(23)",
24. "runtimeOS": "HarmonyOS",
25. "icon":"$media:productB_icon", //定义productB的icon
26. "label":"$string:productB_name",  //定义productB的label
27. }
28. ],
29. "buildModeSet": [
30. {
31. "name": "debug",
32. },
33. {
34. "name": "release"
35. }
36. ]
37. },
38. ...
39. }
```

### 定义product中包含的target

开发者可以选择需要将定义的target分别打包到哪一个product中，每个product可以指定一个或多个target。

同时每个target也可以打包到不同的product中，但是同一个module的不同target不能打包到同一个product中（除非该module的不同target配置了不同的deviceType或distributionFilter/distroFilter）。

例如，前面定义了default、free和pay三个target，现需要将default target打包到default product中；将free target打包到productA中；将pay target打包到productB中，对应的示例代码如下所示：

```
1. {
2. "app": {
3. "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.0(23)",
9. "runtimeOS": "HarmonyOS",
10. "bundleName": "com.example00.com"
11. },
12. {
13. "name": "productA",
14. "signingConfig": "productA",
15. "compatibleSdkVersion": "6.1.0(23)",
16. "runtimeOS": "HarmonyOS",
17. "bundleName": "com.example01.com"
18. },
19. {
20. "name": "productB",
21. "signingConfig": "productB",
22. "compatibleSdkVersion": "6.1.0(23)",
23. "runtimeOS": "HarmonyOS",
24. "bundleName": "com.example02.com"
25. }
26. ],
27. "modules": [
28. {
29. "name": "entry",
30. "srcPath": "./entry",
31. "targets": [
32. {
33. "name": "default",  //将default target打包到default APP中
34. "applyToProducts": [
35. "default"
36. ]
37. },
38. {
39. "name": "free",  //将free target打包到productA APP中
40. "applyToProducts": [
41. "productA"
42. ]
43. },
44. {
45. "name": "pay",  //将pay target打包到productB APP中
46. "applyToProducts": [
47. "productB"
48. ]
49. }
50. ]
51. }
52. ]
53. }
```

## 构建定义的目标产物

每个target对应一个HAP，每个product对应一个APP包，在编译构建时，如果存在多product或多target时，您可以指定编译具体的包。

单击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/4qEd38BhR3qO7iLBcHTh6g/zh-cn_image_0000002530913336.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=6365C85D5D306731857ED652DD7E50A878433AB91B2121193C8D4766BEDA8C2B)图标，指定需要打包的**Product**及**Target**，然后单击**Apply**保存。例如选择"ProductA"中，entry模块对应的"free" Target。

* **Product**：选择需要构建的APP包。
* **Build Mode**：选择[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
* **Product Info**：该APP包的BundleName和SigningConfig信息。
* **Target Select**：选择各个模块的Target，该Target需要包含在定义的Product中才能选择，如果未包含则显示"No Target to apply"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/12a03ystT2-nwN7NNkRwJQ/zh-cn_image_0000002530913342.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=03B18131BE0015FCB92C9351A71D6DA9C15C5C354A59B5C7A7BE2B883166B613)

然后执行编译构建APP/HAP的任务：

* 单击菜单栏的**Build > Build Hap(s)/APP(s) > Build APP(s)** ，构建指定的Product对应的APP。例如，按照[上述配置文件](ide-customized-multi-targets-and-products-guides.md#section7613106105114)和上图中的配置，此时DevEco Studio将构建生成ProductA的APP包。default和ProductB的APP均不会生成。
* 单击菜单栏的**Build > Build Hap(s)/APP(s) > Build Hap(s)**，构建指定Product下的所有Target对应的HAP。

如果您想将某个模块下的指定target打包生成HAP，可以在工程目录中，单击模块名，然后再单击**Build > Make Module** **‘模块名** **’**，此时DevEco Studio将构建生成模块下指定target对应的包。例如，按照上述配置，此时DevEco Studio将构建生成entry模块下free的HAP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/4x6tteGIQJenHJHN5-bnpA/zh-cn_image_0000002530913340.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=F4230B2A953604482253A584E03B097C70774922151618571CCC21129307B829)

## 调试和运行指定的Target

使用DevEco Studio调试或运行应用/元服务时，每个模块只能选择其中的一个target运行，可以通过单击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/0O8rh1U9SZ6k47aBEV-25w/zh-cn_image_0000002561833263.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=945BF1CD8568001B4D2BA62BA1721C9034981C0055A2246CD141C88773F4D246)图标，指定需要调试或运行的**Product**下对应的**Module Target**，然后单击**Apply**保存。

说明

在选择需要调试或运行的target时，需要注意选择该target所属的Product，否则将找不到可调试和运行的target。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/biNV7PehQ86Jg59eMYKeRA/zh-cn_image_0000002530753352.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=AB1E3648F3CDC7FC06BEB872385C90F06DD75613C8B4A7FCD9832C4F41365D33)

## 多产物构建target

* align target

  编译构建时，优先级最高的target。工程配置align target后，如果模块中存在align target，那么将自动选择align target进行构建。align target作用范围是整个工程，只能配置一个，支持命令行和配置文件两种方式。

  + 命令行方式示例如下：

    ```
    1. hvigorw -c properties.ohos.align.target=target1 assembleHap
    ```
  + 在hvigor-config.json5配置文件中添加ohos.align.target，示例如下：

    ```
    1. "properties": {
    2. 'ohos.align.target': 'target1'
    3. },
    ```

* fallback target

  当模块不存在指定的target时会选用default进行构建，但如果不想用default进行构建，那么可以配置fallback target，当找不到指定target时，如果模块中存在fallback target，则使用fallback target进行构建。fallback target作用范围是整个工程，可配置多个，配置多个时按数组顺序先命中的生效。

  + 命令行方式示例如下：

    ```
    1. hvigorw -c properties.ohos.fallback.target=target1,target2 assembleHap
    ```
  + 在hvigor-config.json5配置文件中添加ohos.fallback.target，示例如下：

    ```
    1. "properties": {
    2. 'ohos.fallback.target': ['target1', 'target2']
    3. }
    ```

说明

* align target和fallback target配置方式命令行优先级高于配置文件。

* 使用配置文件配置align target和fallback target，仅支持DevEco Studio界面**Build**菜单栏功能，不支持**Run**菜单栏功能，可通过[hdc命令行工具](hdc.md)进行推包运行、调试。

多个target的优先级顺序为：align target > 命令行指定模块target > 父级模块target > fallback target > default。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/VrNPRRv0TAG8rzGBWcsfxQ/zh-cn_image_0000002561833267.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=A4D74233EE65658D4852E16062ACC19C46F303851112D07F7A4ABD2E6F1B219D)

举例说明：

工程依赖entry->lib1->lib2，需要构建多个产品A、B、C，工程中target配置如下：

entry: A、B、default

lib1: B、C、default

lib2: A、C、default

指定align target为A，fallback target为C。那么构建hap时的编译命令为：

```
1. hvigorw --mode module -p module=entry -c properties.ohos.align.target=A -c properties.ohos.fallback.target=C assembleHap
```

编译的target选择就是：entry@A, lib1@C, lib2@A。

说明

以上所有说明仅针对非ohosTest模式。在ohosTest模式下，依赖的target固定为default，其他target均不生效。
