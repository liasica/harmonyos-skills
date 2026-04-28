---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har
title: 构建HAR
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 构建HAR
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:480d1c4c840fc99854e668f751830dfd3c492476b717a41bf59b1f15c7b8283b
---

构建模式：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，默认构建字节码HAR，用于提升发布产物的安全性。

## 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)。

## 创建模块

1. 新建工程时选择API 10及以上的Stage模型，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[在工程中添加Module](ide-add-new-module.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/xO_kR5RBTUKfVc5bU0CvXQ/zh-cn_image_0000002561753161.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=3570E97E4D5A009704F379A9259FE1AB724F857E7705D68F03BB743E99B0DAEF)
2. 编写代码。

   ```
   1. library  // HAR根目录
   2. ├─libs  // 存放用户自定义引用的Native库，一般为.so文件
   3. └─src
   4. │   └─main
   5. │     ├─cpp
   6. │     │  ├─types  // 定义Native API对外暴露的接口
   7. │     │  │  └─liblibrary
   8. │     │  │      ├─index.d.ts
   9. │     │  │      └─oh-package.json5
   10. │     │  ├─CMakeLists.txt  // CMake配置文件
   11. │     │  └─napi_init.cpp  // C++源码文件
   12. │     └─ets  // ArkTS源码目录
   13. │     │  └─components
   14. │     │     └─MainPage.ets
   15. │     ├─resources  // 资源目录，用于存放资源文件，如图片、多媒体、字符串等
   16. │     └─module.json5  // 模块配置文件，包含当前HAR的配置信息
   17. ├─build-profile.json5  // Hvigor编译构建所需的配置文件，包含编译选项
   18. ├─hvigorfile.ts  // Hvigor构建脚本文件，包含构建当前模块的插件、自定义任务等
   19. ├─Index.ets  // HAR的入口文件，一般作为出口定义HAR对外提供的函数、组件等
   20. └─oh-package.json5  // HAR的描述文件，定义HAR的基本信息、依赖项等
   ```
3. 在oh-package.json5中“main”字段定义导出文件入口。若不设置“main”字段，默认以当前目录下Index.ets为入口文件，依据.ets>.ts>.js的顺序依次检索。以将ets/components/MainPage.ets文件设置为入口文件为例：

   ```
   1. {
   2. ...
   3. "main": "./src/main/ets/components/MainPage.ets",
   4. ...
   5. }
   ```

## 字节码HAR

默认产物是包含字节码的HAR包，其中包含abc字节码、资源文件、配置文件、readme、changelog声明文件、license证书文件，提升发布到ohpm中心仓产物的安全性。

字节码HAR包中包含的是编译后的abc字节码，当字节码HAR被其他应用模块(HAP/HSP)依赖时，执行应用模块的编译构建，不需要再对依赖的HAR进行语法检查和编译等操作，相比源码HAR，可以有效提升应用模块的编译构建效率，提高安全性，降低代码泄漏的风险。

说明

由于构建字节码HAR需要生成二进制的格式，所以单独构建字节码HAR会比构建非字节码HAR耗时更多。

### 收益

* 字节码HAR可以降低代码泄漏的风险，增加反编译获取代码逻辑的难度。

* 采用ArkTS/TS语言开发的字节码HAR，被HAP/HSP集成时，可以减少语法检查、转换的耗时，提高构建性能。
* 字节码HAR可以减少编译时node的进程占用，有效降低内存占用。
* 通过其他代码生成工具生成的js语言HAR包，编译构建成字节码HAR后，被HAP/HSP集成时，可以减少编译阶段处理的文件和代码数量，降低内存，提高构建性能。

### 使用场景

从功能上来说所有的源码HAR包都可以按照任意顺序切换成字节码HAR。但是由于字节码HAR编译和集成的特点，按照推荐场景或顺序来逐步切换字节码HAR可能会获得比较好的性能、内存收益。以下场景中推荐切换使用字节码HAR：

* 适用于SDK厂商对外提供SDK，以及高安全的场景，字节码HAR可以降低源码泄漏的风险。
* 采用muti-repo的开发模式，在被主工程合并集成时，所有依赖的HAR均可以发布成字节码HAR，从而提高主HAP的构建效率。
* 采用mono-repo的开发模式，工程中含有单个代码文件较大，或通过代码生成工具生成的代码量较大的ArkTS/TS/JS 的二方、三方SDK(HAR包)时，可考虑将这些HAR包构建成字节码HAR。
* 对内存要求较高的场景，可以通过切换字节码HAR，降低内存的占用。
* 通过ArkTS/TS/JS编写的HAR，且在依赖链条中处于较为底层的叶子节点，含有较少的源码依赖时，切换为字节码HAR会有较好的收益。

### 约束条件

* 字节码HAR使用的依赖需要配置在本模块的oh-package.json5的dependencies或dynamicDependencies中，如果不配置，后续字节码HAR被集成时可能会出现运行时异常。如果出现异常，部分场景可通过在hvigor-config.json5中配置ohos.byteCodeHar.integratedOptimization后重新编译，具体请参考[编译行为差异说明](ide-hvigor-dependencies.md#section957371853712)。
* 字节码HAR的oh-package.json5中配置的依赖名和依赖包的包名（即包内oh-package.json5中的name）需要保持一致。
* 依赖字节码HAR包时，该工程的build-profile.json5中的[useNormalizedOHMUrl](ide-hvigor-build-profile-app.md#section13181758123312)必须设置为true。
* HAP/HSP/HAR依赖字节码HAR包时，HAP/HSP/HAR的oh-package.json5中配置的依赖名和字节码HAR包的oh-package.json5中的name需要保持一致。
* HAP/HSP/HAR代码中import使用字节码HAR包时，`import xxx from 'yyy'`的依赖名yyy要和本模块oh-package.json5中配置的依赖名保持一致（包括大小写）。
* 依赖字节码HAR包时，字节码HAR的compatibleSdkVersion不能大于工程的compatibleSdkVersion。

### 操作步骤

1. 将工程级build-profile.json5的useNormalizedOHMUrl设置为true。

   说明

   从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，工程级build-profile.json5中useNormalizedOHMUrl字段默认为true，byteCodeHar缺省默认值为true，无需执行步骤1和2。

   ```
   1. {
   2. "app": {
   3. "products": [
   4. {
   5. "buildOption": {
   6. "strictMode": {
   7. "useNormalizedOHMUrl": true
   8. }
   9. }
   10. }
   11. ]
   12. }
   13. }
   ```
2. 在HAR模块的build-profile.json5中，将byteCodeHar设置为true。

   ```
   1. {
   2. "buildOption": {
   3. "arkOptions": {
   4. "byteCodeHar": true
   5. }
   6. }
   7. }
   ```
3. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/pmxLGGL1TRi4JzfHmHoPqw/zh-cn_image_0000002561833159.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=1DBE1809F439A7728A1711493442ACBE694C3A71BABC9F0BA17855AC7850454C)，选择**Build Mode，**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/l_VFMd2WSqutaNG-QDXBTw/zh-cn_image_0000002530753236.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=798DD54E3497C742AE505A5E81C275186B9CF6C0527A7B2EDB37C4F7B7C6351C)
4. （可选）在编译模式为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](ide-build-obfuscation.md)。

   ```
   1. {
   2. "apiType": "stageMode",
   3. "buildOption": {
   4. },
   5. "buildOptionSet": [
   6. {
   7. "name": "release",
   8. "arkOptions": {
   9. // 混淆相关参数
   10. "obfuscation": {
   11. "ruleOptions": {
   12. // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
   13. "enable": true,
   14. // 混淆规则文件
   15. "files": [
   16. "./obfuscation-rules.txt"
   17. ]
   18. },
   19. // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
   20. "consumerFiles": [
   21. "./consumer-rules.txt"
   22. ]
   23. }
   24. },
   25. },
   26. ],
   27. "targets": [
   28. {
   29. "name": "default"
   30. }
   31. ]
   32. }
   ```
5. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。

   ```
   1. "buildOption": {
   2. "packingOptions": {
   3. "asset": {
   4. "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
   5. "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
   6. }
   7. }
   8. }
   ```

   说明

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
6. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   说明

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/8d9SZav0T-mVCSiloSR_vg/zh-cn_image_0000002561833149.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=7925FFC57CCAAA3F97195FB02219113669D15EC3B79F42E0F6D0C78C7895B3CC)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/nOYHg2v4S1mdwGLarQvw8A/zh-cn_image_0000002561753149.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=A4EAC5E7DDE0125899A81986061FCD563E2278028C9236558CFFBC5193879F52)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/YWCwFEMBTmqDh2CCWqfX2g/zh-cn_image_0000002561833135.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=36B4FF13F45BA2339AA9BD503051E1736D4F2B74C8CE2262ABC672E33DE086D7)

## 源码HAR

### 以debug模式构建

产物是包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测，不包含build、node\_modules、oh\_modules、.cxx、.preview、.hvigor、.gitignore、.ohpmignore、.gitignore/.ohpmignore中配置的文件、cpp工程的CMakeLists.txt。

说明

* 源码HAR包中包含源代码，请谨慎分发，避免造成源代码泄露。
* 如果是native工程，以debug模式构建的native产物中不包含调试信息和符号表，如需调试，请参考[三方源码调试](ide-source-code-debugging.md)。
* 从5.0.3.403版本开始，不再建议使用相对路径跨模块引用代码文件，若历史工程存在此场景的跨模块引用，会出现warning告警，请尝试将该文件移至本模块内，再重新进行编译。
* 从5.0.3.403版本开始，以debug/release模式构建HAR的流程使用相同的语法校验规则，若历史工程出现ArkTS语法报错，请按照报错信息修改代码，以符合ArkTS语言规范。

1. 在HAR模块的build-profile.json5中，将byteCodeHar设置为false。

   ```
   1. {
   2. "buildOption": {
   3. "arkOptions": {
   4. "byteCodeHar": false
   5. }
   6. }
   7. }
   ```

   说明

   使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/EvlaY1zqTdipHwdPjDbFrQ/zh-cn_image_0000002530753214.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=54403089CD13375B059188B2AF4E53916B4F213580C12B7C6299D7BE3729563B)，**Build Mode**选择**debug。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/V_Ef_DGlQ8GMU6GVSswUMQ/zh-cn_image_0000002561753157.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=EE4E765A11360465BF045453A6663639302B654D930A0841A1A500DF9866417C)
3. （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ujjZcBfiSe-LobRulMt63Q/zh-cn_image_0000002530753222.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=6CFA5CC8368403B4C2016289C42C1B23804B5F681CE24D230428FAF8BBA6F517)
4. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。配置include或exclude字段后，.gitignore和.ohpmignore文件将不再生效。

   ```
   1. "buildOption": {
   2. "packingOptions": {
   3. "asset": {
   4. "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
   5. "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
   6. }
   7. }
   8. }
   ```

   说明

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
5. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   说明

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/sYBq0I6rT9iuwcEEWcxlog/zh-cn_image_0000002561833137.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=4A94DE02D4A3298CF8DEBB639254FCC7E9AC8786E8537BD615FBEB09274E74FC)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/b77OGoZvQAq8bMCTMCL-oQ/zh-cn_image_0000002530753238.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=3AACA003D8C6FE98A6E95241733FA8A70DB7793D21F17ACA02A4A68B03EFAA3F)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_Gt7s6XlSG6vPGIRSUj8Kg/zh-cn_image_0000002561833145.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=0F98AAC5FD1BA4348685960B7F0CCFD358297A4F12B83F1EE0991AF5D31094B9)

### 以release模式构建

从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆，构建产物和debug模式相同，请参考[以debug模式构建](ide-hvigor-build-har.md#section197792874110)。

为保护代码资产，建议开启混淆，开启后，构建产物是包含js中间码的HAR包，其中包含源码混淆后生成的js中间码文件、资源文件、配置文件、readme、changelog声明文件、license证书文件，用于发布到ohpm中心仓。

1. 在HAR模块的build-profile.json5中，将byteCodeHar设置为false。

   ```
   1. {
   2. "buildOption": {
   3. "arkOptions": {
   4. "byteCodeHar": false
   5. }
   6. }
   7. }
   ```

   说明

   使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/u02JpIOkRkGQT5CcM9eRow/zh-cn_image_0000002561753187.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=4876291ED73172F9AA57E35B71A8698759832A8DE246BB3BA05CE8FDFCC197FD)，**Build Mode**中选择**release。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/fIhq71xQSH2bRhfUiixFQw/zh-cn_image_0000002530913234.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=2CB4CA623D8853F1DCF800988701D198509D9A50919349EE57D26DAA7234EA66)
3. 在[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](ide-build-obfuscation.md)。

   ```
   1. {
   2. "apiType": "stageMode",
   3. "buildOption": {
   4. },
   5. "buildOptionSet": [
   6. {
   7. "name": "release",
   8. "arkOptions": {
   9. // 混淆相关参数
   10. "obfuscation": {
   11. "ruleOptions": {
   12. // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
   13. "enable": true,
   14. // 混淆规则文件
   15. "files": [
   16. "./obfuscation-rules.txt"
   17. ]
   18. },
   19. // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
   20. "consumerFiles": [
   21. "./consumer-rules.txt"
   22. ]
   23. }
   24. },
   25. },
   26. ],
   27. "targets": [
   28. {
   29. "name": "default"
   30. }
   31. ]
   32. }
   ```
4. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。

   ```
   1. "buildOption": {
   2. "packingOptions": {
   3. "asset": {
   4. "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
   5. "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
   6. }
   7. }
   8. }
   ```

   说明

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
5. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   说明

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Nb1PkptxRAG3Zr93-R-Khw/zh-cn_image_0000002561833151.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=641E2CEF95976E364A7B7BFB0368970D4FC6C2056B14EC41E31BE35D7487B9EB)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/aW4fKA7xTFK7LWiLHmnR8w/zh-cn_image_0000002530753226.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=791B1322074B629BD6E3E2BCB46684251FEE35FDD3659FA8CDD9DE4D20A019B5)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/q1r6tXPqR66KSiUemVEBwg/zh-cn_image_0000002530753244.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=7CD5E9E381798A27BA14DE4B819CBF3C95DE3B034DA0ECC8EC829F19A3FC39A5)

## 对HAR进行签名

DevEco Studio在构建HAR流程的基础上，支持对HAR进行签名。签名后的HAR包后续可用于接入生态市场，接入流程请参考[SDK类商品接入说明](../start/dev-mall-marketplace-sp-sdkservice-access-explain-0000001866499490.md)。

说明

1. 该能力只在Compatible SDK 5.0.0(12)及以上版本的SDK中支持。

2. 该能力需开启Hvigor的Daemon能力，请确保当前工程开启了Daemon，打开**File > Settings**（macOS为**DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor**，勾选字段**Enable the Daemon for tasks**。

1. 在hvigor-config.json5中，开启构建签名HAR开关：

   ```
   1. {
   2. "properties": {
   3. "ohos.sign.har": true
   4. }
   5. }
   ```
2. 配置工程签名信息，配置流程请参考[配置签名信息](ide-publish-app.md#section793484619307)。
3. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/dbqEmPcETVOBVomBkJ7xeA/zh-cn_image_0000002530913240.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=333D5B80573316167320EC38F8E6AFF78CF9A1FA4D40FB3D949DA7E18495585D)

   构建完成后，build目录下生成签名HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/veSdQMcCTSytZypDlyBwjQ/zh-cn_image_0000002530913244.png?HW-CC-KV=V1&HW-CC-Date=20260427T235713Z&HW-CC-Expire=86400&HW-CC-Sign=B529446D836A8EB9DFDEDF8229F52AD942E84F8A47A0EA0A63EE4160A70D4F0C)
