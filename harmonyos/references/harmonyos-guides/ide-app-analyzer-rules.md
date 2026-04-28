---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-rules
title: 规则体检
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 规则体检
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d13933651dd93c36bda7c094b9ab8e4e0b067e18cd85b39bebe39b4e72402a00
---

规则体检支持兼容性、性能、功耗等多种测试类型，开发者可自主选择不同的规则进行测试。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 单击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/eVLLsmEnQFqva0rHN-FJgw/zh-cn_image_0000002561752991.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=DED470CAF41E42D46F3B3E2E816D2962125D50827B2FDF38FF19962893C53D59)，打开AppAnalyzer页面。
2. 连接设备或启动模拟器，并对应用进行[签名](ide-signing.md)。
   * 真机：参考[使用本地真机运行应用](ide-run-device.md)连接真机。
   * 模拟器：在AppAnalyzer首页创建或启动模拟器，具体请参考[管理模拟器](ide-emulator-management.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。
4. 如果使用DevEco Studio 6.0.0 Beta2之前的版本，需要先编译生成HAP或HSP。使用Beta2及以上的版本，无需提前编译。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/3Q1Yk1gvSaWJFEGsDT0-fw/zh-cn_image_0000002561832963.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=91F169AE0DBFEB80C74C6395FB09338392D46E9F10C6AE39122DE7A5EFA12437)图标选择Product、Target和构建模式，点击**Apply**后，在AppAnalyzer的首页中可查看对应的编译产物和构建模式。关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/YG-O4mC_RCOsJK-fthKoaA/zh-cn_image_0000002561832957.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=D65C610D9C44DB1DF556DE6F294D8C4E9B905771BD9E869337A5B5ED7E0F0F1C)
2. 在**AppAnalyzer**页面，选择**规则体检**，选择预置的体检卡片，或根据需要自定义卡片。
   * 点击预置的体检卡片开始体检，如需查看卡片包含的体检规则，请点击卡片右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/dW2Y6w21Qe6rZ8I9NfqVaw/zh-cn_image_0000002561752985.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=A0D80F614A9B33D00DC74B45F60AA8778E9BC3A9EFB1CACDE32C2522FBD424AD)按钮，规则详情请参考[规则总览](ide-app-analyzer-all-rules.md)。
   * 如果需要自定义体检规则，点击**+**，选择自动/手动测试和体检规则，部分规则可修改单次录制时长，请根据界面提示进行修改。

     如果仅选择稳定性规则，从DevEco Studio 6.0.2 Beta1版本开始，支持录制回放遍历模式，开发者先手动录制在设备上的操作，录制结束后AppAnalyzer会自动保存录制文件，选择录制文件开始体检后，AppAnalyzer会按照设置的回放时长，自动循环执行录制的操作，体检结束后可[查看报告](ide-app-analyzer-rules.md#li22241112508)。

     说明

     请确保录制过程可循环，例如从B页面开始录制，最后结束录制时要停留在B页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/lqgDTbKdQzyq6jNGO1UJ4Q/zh-cn_image_0000002530913038.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=A7A108A28C8A56E29C28A8DCFD76812E4EE7DC871760C7DAD655170EFE0EF3DC)

   说明

   以下体检规则不支持在编译模式为release下运行，请把编译模式切换到debug再重新检测：组件树节点数目过大、执行函数耗时过长、渲染界面耗时过长、ForEach中item数量过大。
3. 开始体检后，请等待AppAnalyzer完成构建、签名、安装等操作。如果本次体检依赖Python三方库并且本地未安装，AppAnalyzer会同步下载安装三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。
   * 如果是自动测试，根据界面提示，登录应用账号后点击继续按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/9FNjDTkwQamjFRFLXclaGw/zh-cn_image_0000002530753052.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=EBF7927F37F4E59BBCF26B2882A8B65BC03BC9772479E2F5E8C1D522C60030EA)，继续测试；或者无需登录账号，直接点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/eUEr1qWKSGKKJr54u-YtBA/zh-cn_image_0000002530753038.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=6B1AF04174DF5C256B270CC4229C0FFF534CFCC61A66C6C791A8E25791EA4CA5)按钮继续测试。
   * 如果是手动测试，根据界面提示，点击开始按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/MeVq1owvQRe9WrfdafDh9Q/zh-cn_image_0000002561752983.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=86DFFE148AA8154B6E54366265FF6DBF718B68BB2A6B25DB1CCCA7D7972D9268)开始录制，并手动遍历应用/元服务的功能。如果在录制时间范围内未遍历完成，可继续点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/RK0UP9n6T8GIDC8cXMAdlQ/zh-cn_image_0000002530913036.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=13FA36DB0F4DF1D95DD87E7F801B0F8E3981B0C534668A1DB111399CE3C8640B)按钮，进行多次遍历，遍历完成后点击结束按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/WGWvIWPLSUK6n4qMhbIP2g/zh-cn_image_0000002530913044.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=7CDCCDB085E326A2D4C779697A8F478E8CA7C65028E42A4D4701CC4C30D18C6D)。
4. 查看测试报告，包含以下内容。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对检测出来的问题，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**用户反馈**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](ide-app-analyzer-history-reports.md#section78017171818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/DMk_nLAdQXKvk_ITsUEBAw/zh-cn_image_0000002561832955.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=02A95658B8ACA2D1680395739508243C084A5418B3A8AE402F3F21E65C077C4D)

### DevEco Studio 6.0.1 Beta1以下版本

1. 如果使用DevEco Studio 6.0.0 Beta2及以上的版本，支持在体检过程中自动编译构建打包。点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/b_0pvqYpR6qcADiDaSm_IA/zh-cn_image_0000002530753054.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=CC7AE0A1E6FA68B9A804445366C0D2ED7BAF2CFAB1BC2F9D0AEEEDBBDE555F52)图标选择Product、Target和构建模式，关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
2. 在**AppAnalyzer**页面，选择**规则体检**，选择自动或手动方式，**模块**选择框选择HarmonyOS应用/元服务工程模块。
   * 自动方式：体检时无需手动遍历，AppAnalyzer会自动检测。
   * 手动方式：体检时需要根据提示手动遍历HarmonyOS应用/元服务的功能。

   说明

   * 如果使用DevEco Studio 6.0.0 Beta2之前的版本，只有已经完成签名编译打包的模块才能被选中。
   * 支持同时添加多个模块，要求所有模块的“bundleName”相同，且多个模块中只能包含一个entry。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/mu6xy9rdSZG6d_WemqXMiQ/zh-cn_image_0000002530913034.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=A719734D2D0E849F37A0E1DE9E723AE38F56F12DD22790D9DD34C213827092D1)
3. 选择待测试的规则，规则详情请参考[规则总览](ide-app-analyzer-all-rules.md)，然后在**AppAnalyzer**页面底部单击**开始**按钮，开始测试。部分测试规则依赖Python，请根据AppAnalyzer的指引，下载Python及三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。

   说明

   * 请勿在测试完成前点击结束，如果提前结束测试会导致测试结果不准确。
   * 支持Python3.9~3.12版本，推荐使用Python 3.11.7版本。
   * 部分规则体检会进行投屏，如果测试过程中同时使用其他投屏工具，如DevEco Testing，可能会对UX测试的投屏造成干扰。如果投屏中断或不同步，可点击左上角刷新按钮重新投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/WJEqw1JtRvKLz-92nNP4Rw/zh-cn_image_0000002530753048.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=633B723F79176379A8B2F10CB19D55D178CA382766B0D49948E1FE23053EB364)
4. 如果是手动方式，在安装应用/元服务完成后，需要根据提示手动遍历HarmonyOS应用/元服务的功能。手动遍历完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。

   * 测试报告：检测结果的汇总信息，点击**详情链接**可跳转到对应的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/RTtqoS2gQRG5M5bV6QDqCw/zh-cn_image_0000002561752977.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=62135E71BB7DD50E80927316B10FEE64E6825BAE91BDFBE2417DCA0AF2EE1142)
   * 详情报告：只包含检测失败的规则，给出详细的测试结果、相关的定位文件和对应的优化建议。
     + **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行优化。
     + **Code Linter**：在“最佳实践测试”项目中，可直接在拉起Code Linter的同时，传递有问题的代码文件名，自动执行代码检查。在“快速性能测试”和“性能测试”项目中，因无代码文件名等信息，部分检测规则不支持自动执行代码检查，仅支持拉起Code Linter。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/lkN4AdQ_Q1q9ZqMQ9qo8fA/zh-cn_image_0000002561832971.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=39E8C4808A4825AC02ED35D29299FC3EE2E571A22AC48FF36ABAE816AF89E212)
