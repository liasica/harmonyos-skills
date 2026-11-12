---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-rules
title: 规则体检
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 规则体检
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:d7a2f9358d8a82803425f2a5277e02c67c66145cf1834ea6a17d5ce0675fcbb9
---

规则体检支持兼容性、性能、功耗等多种测试类型，开发者可自主选择不同的规则进行测试。

## 使用约束

使用26.0.0以下版本的DevEco Studio进行[性能](ide-app-analyzer-all-rules.md#section832281319229)相关的测试时，要求DevEco Studio版本与设备API版本配套；从DevEco Studio 26.0.0版本开始，DevEco Studio兼容API 20及以上的设备，无需与设备API版本配套，对于API 20以下的设备，DevEco Studio版本仍需与设备API版本配套。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ULW8ObPYQ220milKB7_i-w/zh-cn_image_0000002779407000.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBCCCCACC958F0313982E296FC8C162500C53BF9CD3170F395FFBFC6CB0DC5CA)，打开AppAnalyzer页面。
2. 连接设备或启动模拟器，并对应用进行[签名](ide-signing.md)。
   * 真机：参考[使用本地真机运行应用](ide-run-device.md)连接真机。
   * 模拟器：在AppAnalyzer首页创建或启动模拟器，具体请参考[管理模拟器](ide-emulator-management.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。
4. 如果使用DevEco Studio 6.0.0 Beta2之前的版本，需要先编译生成HAP或HSP。使用Beta2及以上的版本，无需提前编译。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/2hNJs4kGQqCiW4uGtL2Osg/zh-cn_image_0000002779407002.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB4C3F8563B9EAD5909541F9EAE262F1D543943135B2BA34A70D6CC97A0827CE)图标选择Product、Target和构建模式，点击**Apply**后，在AppAnalyzer的首页中可查看对应的编译产物和构建模式。关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Ty0R6qycQFu-FrYdYvYQ3A/zh-cn_image_0000002779566978.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C36658A39E74FFB0617CFE876D71123AA0F86C676842B1B6BC02832679832260)
2. 在**AppAnalyzer**页面，选择**规则体检**，选择预置的体检卡片，或根据需要自定义卡片。
   * 点击预置的卡片开始体检，如需查看卡片包含的体检规则，请点击卡片右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/C7dDaovnSEaoJu0D9PpVXQ/zh-cn_image_0000002808766553.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=80FF5CE9CF0DDF00FDCDB6B9C6183F84973E7A54D3DEF11D2491DCF9274C310A)按钮，规则详情请参考[规则总览](ide-app-analyzer-all-rules.md)。
   * 如果需要自定义体检规则，点击**+**，选择自动/手动测试和体检规则，部分规则可修改单次录制时长，请根据界面提示进行修改。

     如果仅选择稳定性规则，从DevEco Studio 6.0.2 Beta1版本开始，支持录制回放遍历模式，开发者先手动录制在设备上的操作，录制结束后AppAnalyzer会自动保存录制文件，选择录制文件开始体检后，AppAnalyzer会按照设置的回放时长，自动循环执行录制的操作，体检结束后可[查看报告](ide-app-analyzer-rules.md#li22241112508)。

     **说明** 

     + 请确保录制过程可循环，例如从B页面开始录制，最后结束录制时要停留在B页面。
     + 录制回放功能仅支持直板机真机。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/yIvuFvx4TFu7s_pf173Cdg/zh-cn_image_0000002808886629.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=07E09FCA4B91A9160619FECF1112503B56F2321CB5E6F790D9CBCA333FE4C69C)

   **说明** 

   以下体检规则不支持在编译模式为release下运行，请把编译模式切换到debug再重新检测：组件树节点数目过大、执行函数耗时过长、渲染界面耗时过长、ForEach中item数量过大。
3. 开始体检后，请等待AppAnalyzer完成构建、签名、安装等操作。如果本次体检依赖Python三方库并且本地未安装，AppAnalyzer会同步下载安装三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。
   * 如果是自动测试，根据界面提示，登录应用账号后点击继续按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Tig4DgE1QMK_BJ-9rypmfw/zh-cn_image_0000002779566966.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=76DBA24E8A19178C716855FA70995949E0CFCE024F173DF8739F510F33B36753)，继续测试；或者无需登录账号，直接点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/g5re-eCbR0WM89MkSLugAg/zh-cn_image_0000002808766561.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=458D7121B3E8C7E60E2903CD0C54A2B49997CF2007CD1B0D48F5BC1E11837288)按钮继续测试。
   * 如果是手动测试，根据界面提示，点击开始按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/VmSjkyk2RXKkwkGn8F8DeA/zh-cn_image_0000002779566976.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3211F2C868D459ADF28E73F4532C47D9BDBB001E6A9F85EA1F21336860DEB459)开始录制，并手动遍历应用/元服务的功能。如果在录制时间范围内未遍历完成，可继续点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/y5_f2RM5SUuIpSoa0XuRwg/zh-cn_image_0000002808886643.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A419302DDFDF8E703D45AE1853BFB044993D209A2E473014E549F4FCC13E95C)按钮，进行多次遍历，遍历完成后点击结束按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/aRAY30eMSc2dxAwDo8vwiQ/zh-cn_image_0000002808766551.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A22D8D73C4984F2817FBB6FD75A41FB08A1A7823E8A4EDD50B18FDA2145C765)。
4. 查看测试报告，包含以下内容。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对检测出来的问题，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](ide-app-analyzer-history-reports.md#section78017171818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/iOflQOgYQ4KhUEohsy_P6Q/zh-cn_image_0000002779406998.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8819F3ECEB1763F2D9D940CCC3C9674CEEB70B2FDE767FE1497D0F4C2E3A9F8)

### DevEco Studio 6.0.1 Beta1以下版本

1. 如果使用DevEco Studio 6.0.0 Beta2及以上的版本，支持在体检过程中自动编译构建打包。点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/lTdDlsdmQ9OXaKh3v-abDQ/zh-cn_image_0000002779406990.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=40C140CEEE3E8442300D7B7A31ECE6168A0DA1F815C30EA24B70B34EBE48E08F)图标选择Product、Target和构建模式，关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
2. 在**AppAnalyzer**页面，选择**规则体检**，选择自动或手动方式，**模块**选择框选择HarmonyOS应用/元服务工程模块。
   * 自动方式：体检时无需手动遍历，AppAnalyzer会自动检测。
   * 手动方式：体检时需要根据提示手动遍历HarmonyOS应用/元服务的功能。

   **说明** 

   * 如果使用DevEco Studio 6.0.0 Beta2之前的版本，只有已经完成签名编译打包的模块才能被选中。
   * 支持同时添加多个模块，要求所有模块的bundleName相同，且只能包含一个entry。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/NlfH3szTSZKdqFfz46BEwA/zh-cn_image_0000002808886633.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A59B51AD2C75D499BA6CE9EC4D25180AC1B76E041498765A411CEEA267C3B55E)
3. 选择待测试的规则，规则详情请参考[规则总览](ide-app-analyzer-all-rules.md)，然后在**AppAnalyzer**页面底部单击**开始**按钮，开始测试。部分测试规则依赖Python，请根据AppAnalyzer的指引，下载Python及三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。

   **说明** 

   * 请勿在测试完成前点击结束，如果提前结束测试会导致测试结果不准确。
   * 支持Python 3.9~3.12版本，推荐使用Python 3.11.7版本。
   * 部分规则体检会进行投屏，如果测试过程中同时使用其他投屏工具，如DevEco Testing，可能会对UX测试的投屏造成干扰。如果投屏中断或不同步，可点击左上角刷新按钮重新投屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/1uiTMhI5Rjqd81fBAVzTfQ/zh-cn_image_0000002779406996.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF705312EFED70FF17214A20999700311C38051619CD5637FB17C3D68EF44328)
4. 如果是手动方式，在安装应用/元服务完成后，需要根据提示手动遍历HarmonyOS应用/元服务的功能。手动遍历完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。

   * 测试报告：检测结果的汇总信息，点击**详情链接**可跳转到对应的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/k1Y3lP8GRI-ut1pTA2D4XA/zh-cn_image_0000002779566974.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=25D5E407132D049F7C996D4F809F51AD96FF57D5F44FF4FA04DA13DECEBE0C39)
   * 详情报告：只包含检测失败的规则，给出详细的测试结果、相关的定位文件和对应的优化建议。
     + **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行优化。
     + **Code Linter**：在“最佳实践测试”项目中，可直接在拉起Code Linter的同时，传递有问题的代码文件名，自动执行代码检查。在“快速性能测试”和“性能测试”项目中，因无代码文件名等信息，部分检测规则不支持自动执行代码检查，仅支持拉起Code Linter。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/85k-39iuT4Gq4AuGjbgWXA/zh-cn_image_0000002808886635.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A415E6971687AEE34FD0F8E3051AD8D09F5DAED12BED41E88D0102E2206F1C75)
