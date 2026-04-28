---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-scenes
title: 场景化体检
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 场景化体检
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51ae96dd66a0299198d422a40d30eb4d7ff9e3d7087e73ef1359a25a0853d130
---

场景化体检支持页面滑动、页面间转场、冷启动等多种测试场景，开发者可以基于实际的应用场景进行测试。

## 前置操作

1. 通过以下任意一种方式，打开AppAnalyzer。
   * 单击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/DeTty2wISpexMNNis4KsNg/zh-cn_image_0000002561752861.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=C020C0A677776609F60592DEFE721788A445729EC52A9CD2F4ADCE8160A5EE37)，打开AppAnalyzer页面。
2. 连接设备或启动模拟器，并对应用进行[签名](ide-signing.md)。
   * 真机：参考[使用本地真机运行应用](ide-run-device.md)连接真机。
   * 模拟器：在AppAnalyzer首页创建或启动模拟器，具体请参考[管理模拟器](ide-emulator-management.md)。
3. 如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部**Python 配置**按钮进行配置。
4. 如果使用DevEco Studio 6.0.0 Beta2之前的版本，需要先编译生成HAP或HSP。使用Beta2及以上的版本，无需提前编译。

## 进行体检

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/l_CyCNiSQb2rDqZU2iO_cA/zh-cn_image_0000002530752924.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=84D439DA477A4F07367FCB89159AC63D742E08BCFACD76681DFDA556604A4F45)图标选择Product、Target和构建模式，点击**Apply**后，在AppAnalyzer的首页中可查看对应的编译产物和构建模式。关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/uyDO3zRSSMODs-vHIZYSHA/zh-cn_image_0000002561752865.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=2C5AB37E2BE3CD2E8BC3574426079436C2443B7E54E772085C1B7142F77C39FB)
2. 在**AppAnalyzer**页面，选择**场景化体检**，选择预置的体检卡片，或根据需要自定义卡片。
   * 点击预置的体检卡片开始体检，如需查看卡片包含的体检场景，请点击卡片右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/jvAhej0iRjiceNP0QbQ07A/zh-cn_image_0000002561832847.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=7E5E7F24E02B8016C57B8D21961E17B9F5788CBEDAFAC0E6B97A34D78DF3B99B)按钮，不同场景对应的检测指标请参考[体检场景](ide-app-analyzer-scenes.md#section578981218613)。
   * 如果需要自定义体检场景，点击**+**，选择自动/手动测试和体检场景，部分场景可修改单次录制时长/测试总时长，请根据界面提示进行修改。
3. 开始体检后，请等待AppAnalyzer完成构建、签名、安装等操作。如果本次体检依赖Python三方库并且本地未安装，AppAnalyzer会同步下载安装三方库。在测试过程中，请保持连接的设备为解锁亮屏状态。
   * 如果是自动测试，根据界面提示，登录应用账号后点击继续按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/89MpNLLARQeEST-wp_hNrQ/zh-cn_image_0000002561832841.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=01C184BD2D991DF9C97CC6E9FAE9D779C3551240B7155259C7D3F1D19E14BE0F)，继续测试；或者无需登录账号，直接点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/DMNbAHHMRxGKBnqP4ULrCQ/zh-cn_image_0000002561752859.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=C3F8C8B5C63916FE8367CAE9D6231D815867D60B831777C1B4909626279079A5)按钮继续测试。
   * 如果是手动测试，根据界面提示，点击开始按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/n1Kcc5XYSQCf5okNDAp8Gg/zh-cn_image_0000002561752867.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=1B18F28141B236CEBD542C975497D2066BAABD3376A449829DCCDC785F550B05)开始录制，并手动遍历应用/元服务的功能。如果在录制时间范围内未遍历完成，可继续点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/DSVuvj4-QnOKNsJoysP47Q/zh-cn_image_0000002530752930.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=059B72014A64EFFDB90DC9451D79B46755D37F8AAB4ECD876F5A8EC6640AB955)按钮，进行多次遍历，遍历完成后点击结束按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/59HZMZz6SqGbfY5BoN43Mg/zh-cn_image_0000002530912914.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=9FA235EDC33C44C02DEA27D4EAE9E84D828616253CEA67B11FA2943A2C6231EF)。
4. 查看测试报告，包含以下内容。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**用户反馈**向我们反馈。

   从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看[导出报告](ide-app-analyzer-history-reports.md#section78017171818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/9GYiKZ4fRCSmsjM4prfR_A/zh-cn_image_0000002530752926.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=C2AEB633706A87D85496C4631AE2B1EDA190F74EE1DDF8CE3159A98B52741848)

### DevEco Studio 6.0.1 Beta1以下版本

1. 如果使用DevEco Studio 6.0.0 Beta2及以上的版本，支持在体检过程中自动编译构建打包。点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/v-yVm82eSDikAVXJQFWr8Q/zh-cn_image_0000002561832837.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=DFFD61AE3108062F7D5674D1303EE910732B4536E4B6876CB0F343D984497688)图标选择Product、Target和构建模式，关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。
2. 在**AppAnalyzer**页面，选择**场景化体检**，选择**自动**或**手动**方式，**模块**选择框选择HarmonyOS应用/元服务工程模块。
   * 自动方式：体检时无需手动遍历，AppAnalyzer会自动检测。自动方式下还需要选择具体的运行时长。
   * 手动方式：体检时需要根据提示手动遍历HarmonyOS应用/元服务的功能。

   说明

   * 如果使用DevEco Studio 6.0.0 Beta2之前的版本，只有已经完成签名编译打包的模块才能被选中。
   * 支持同时添加多个模块，要求所有模块的“bundleName”相同，且多个模块中只能包含一个entry。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/AyNApk2-SBKrAlO6cryyEA/zh-cn_image_0000002530752916.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=CE8D9E838F962A8730633A2AD4F5A4F56F4888077F94D0E3C9E6906C3DEB378A)
3. 勾选体检场景，不同场景对应的检测指标请参考[体检场景](ide-app-analyzer-scenes.md#section578981218613)，然后在**AppAnalyzer**页面底部单击**开始**按钮，开始测试。首次测试时，请根据AppAnalyzer的指引，下载Python及三方库，或者登录开发者账号并自动签名音频辅助检测APP。在测试过程中，请保持连接的设备为解锁亮屏状态。

   说明

   * 请勿在测试完成前点击结束，如果提前结束测试会导致测试结果不准确。
   * 支持Python 3.9~3.12版本，推荐使用Python 3.11.7版本。
4. 如果是手动方式，在安装应用/元服务完成后，需要根据提示手动遍历HarmonyOS应用/元服务的功能。手动遍历完成后点击**结束**按钮停止测试任务，等待数据解析完成后，查看测试结果如下。
   * 测试报告：检测结果的汇总信息，默认展示告警和失败的检测结果，点击**详情链接**可跳转到对应场景的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/9YwUkNJGQ5m4WyGepLXQ4g/zh-cn_image_0000002561752869.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=230B56B5CD2BF10D15E28B3A00E1F114E5B9C1F146FD80DFB164308419F66CAF)
   * 详情报告：给出详细的测试结果、相关的定位文件和对应的优化建议。
     + **开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等**：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/zp07wDxsQqieGo6zro5hJQ/zh-cn_image_0000002530752920.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=5F4E9C829D26D6BD48306614D58362AF9C758D9695EB247DB5066F513B2410FB)

## 体检场景

### 性能

| 场景 | 子场景 | 检测指标/检测项 | 应用或元服务场景 | 自动或手动方式 |
| --- | --- | --- | --- | --- |
| 页面间转场 | router或者navigation页面跳转 | [点击响应时延](performance-delay.md#section118706211961) | 应用，元服务 | 自动，手动 |
| [点击完成时延](performance-delay.md#section2406192820717) |
| [转场卡顿率](performance-frame-rate.md#section1591383182619) |
| [起播时延](performance-delay.md#section1140562816186) |
| 页面滑动 | 页面滑动（仅支持List、Grid、WaterFlow这三个组件实现的页面滑动） | [滑动响应时延](performance-delay.md#section1767913186810) | 应用，元服务 | 自动，手动 |
| [滑动卡顿率](performance-frame-rate.md#section159268494256) |
| 冷启动 | 冷启动 | [完成时延](performance-delay.md#section58771582411) | 应用，元服务 | 自动，手动 |
| 页面内转场 | swiper滑动转场 | [滑动响应时延](performance-delay.md#section1767913186810) | 应用，元服务 | 自动，手动 |
| [滑动卡顿率](performance-frame-rate.md#section159268494256) |
| [起播时延](performance-delay.md#section1140562816186) |
| tabs点击转场 | [点击响应时延](performance-delay.md#section118706211961) |
| [点击完成时延](performance-delay.md#section2406192820717) |
| [转场卡顿率](performance-frame-rate.md#section1591383182619) |
| tabs滑动转场 | [滑动响应时延](performance-delay.md#section1767913186810) |
| [滑动卡顿率](performance-frame-rate.md#section159268494256) |
| [起播时延](performance-delay.md#section1140562816186) |
| swiper点击转场  （从DevEco Studio 6.0.2 Beta1版本开始支持） | [点击响应时延](performance-delay.md#section118706211961) |
| [点击完成时延](performance-delay.md#section2406192820717) |
| [转场卡顿率](performance-frame-rate.md#section1591383182619) |
| web场景  （从DevEco Studio 6.0.0 Beta2版本开始支持） | web页面跳转 | [点击响应时延](performance-delay.md#section118706211961) | 应用，元服务 | 自动，手动 |
| [点击完成时延](performance-delay.md#section2406192820717) |
| web页面滑动 | [滑动响应时延](performance-delay.md#section1767913186810) |
| [滑动卡顿率](performance-frame-rate.md#section159268494256) |

### 功能兼容性

| 场景 | 子场景 | 检测指标/检测项 | 应用或元服务场景 | 自动或手动方式 |
| --- | --- | --- | --- | --- |
| 音频播控服务  （从DevEco Studio 5.1.0 Release版本开始支持） | 播控中心音频控制场景 | [播控中心控制音频播放检测](audio-specification.md#section12303131815311) | 应用 | 手动 |
| [播控中心控制音频暂停检测](audio-specification.md#section12303131815311) |
| [播控中心控制歌曲切换上一首检测](audio-specification.md#section12303131815311) |
| [播控中心控制歌曲切换下一首检测](audio-specification.md#section12303131815311) |
| [播控中心控制歌曲播放进度条拖动检测](audio-specification.md#section12303131815311) |
| [播控中心控制歌曲循环播放检测](audio-specification.md#section12303131815311) |
| [播控中心控制歌曲收藏检测](audio-specification.md#section12303131815311) |
| 音频焦点切换  （从DevEco Studio 5.1.0 Release版本开始支持） | 来电接听场景 | [音频焦点变化事件响应检测](audio-specification.md#section256142914530) | 应用 | 手动 |
| VoIP通话场景 |
| 闹钟场景 |
| 导航场景 |
| 语音助手播报场景 |
| 静音播放场景 |
| 非静音播放场景 |
| 普通录音场景 |
| 音频设备控制  （从DevEco Studio 5.1.0 Release版本开始支持） | 耳机控制音频场景 | [耳机控制音频播放检测](audio-specification.md#section12303131815311) | 应用 | 手动 |
| [耳机控制音频暂停检测](audio-specification.md#section12303131815311) |
| [耳机控制歌曲切换上一首检测](audio-specification.md#section12303131815311) |
| [耳机控制歌曲切换下一首检测](audio-specification.md#section12303131815311) |
| 耳机断开场景 | [耳机断开事件响应检测](audio-specification.md#section256142914530) |
| 运行异常  （从DevEco Studio 6.1.0 Beta1版本开始支持） | 运行异常 | [运行无兼容性问题](ide-app-analyzer-all-rules.md#section202813103565) | 应用，元服务 | 自动 |
| [API兼容性问题](ide-api-compatibility-check.md) |

### 多设备

多设备测试支持以下设备：

* API 20及以上的双折叠、三折叠手机和模拟器。
* API 20及以上的Pura X Max手机和模拟器。

| 场景 | 检测指标/检测项 | 应用或元服务场景 | 自动或手动方式 |
| --- | --- | --- | --- |
| 折叠开合  （从DevEco Studio 6.0.2 Beta1版本开始支持） | 参考[UX规则](ide-app-analyzer-all-rules.md#section68461625141414) | 应用，元服务 | 手动 |

### 功耗

| 场景 | 子场景 | 检测指标/检测项 | 应用或元服务场景 | 自动或手动方式 |
| --- | --- | --- | --- | --- |
| 前台静置  （从DevEco Studio 6.1.0 Beta1版本开始支持） | 前台静置 | [前台不可见动效](standard-foreground-render.md#section12791152171) | 应用 | 自动，手动 |
| [UI空跑](standard-foreground-resource.md#section169882223810) |
| [未使用硬件合成](standard-foreground-render.md#section18911148816) |
| [CPU负载异常](standard-foreground-resource.md#section177973203218) |
