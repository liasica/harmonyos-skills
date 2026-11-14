---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-ag-policy
title: 上架合规体检
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 上架合规体检
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7dd33df3212277847af7d7fde979f6f0b88e4bd9538759860802ec87b0a8ac03
---

从DevEco Studio 6.1.0 Beta1版本开始，AppAnalyzer新增上架合规体检，针对AppGallery应用的上架合规要求进行检测，提前发现需要重点关注的合规事项，了解应做和不应做的事项，避免常见误区。

## 进行体检

1. 确保[DevEco Studio与真机设备已连接](ide-run-device.md)，并对应用进行[签名](ide-signing.md)。
2. 通过以下任意一种方式，打开AppAnalyzer。
   * 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面。
   * 在编辑窗口右侧的工具栏，点击**AppAnalyzer**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Zp6FKTL8QM6ka1TdFvCtHA/zh-cn_image_0000002808886563.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=10948E1E20E81E4E69768F5ED3B5B6E691A68FE1DAC7958C17CBBA86A1F537DC)，打开AppAnalyzer页面。
3. 点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/RF0KyWHQRZWD_BlMC8p5dg/zh-cn_image_0000002808766477.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=436927E884DD24C2DB35A8B9007C2BB316F5FE5B2F9104A2F2C14D06AF1E986D)图标选择Product、Target和构建模式，点击**Apply**后，在AppAnalyzer的首页中可查看对应的编译产物和构建模式。关于Product、Target、构建模式的介绍请参考[配置多目标产物](ide-customized-multi-targets-and-products-guides.md)和[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/1jAEYw0TSB6lSzsXuqJnrA/zh-cn_image_0000002779406916.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF28D846B7A7A6D428037EE038D53AF7FBA2FD740FE740D4E160170367A5732F)
4. 在**AppAnalyzer**页面，选择**上架合规体检**，选择预置的体检卡片，或根据需要自定义卡片。
   * 点击预置的体检卡片开始体检，如需查看卡片包含的体检规则，请点击卡片右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/IsY6A6EsTS-KUYp51iG1QA/zh-cn_image_0000002808886555.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=F01A04BD1894B7F2CEEB7FE43C8FAD26518BC9CD5F41402E9F4862ADD97B7ADF)按钮，规则详情请参考[体检规则](ide-app-analyzer-ag-policy.md#section63875091019)。
   * 如果需要自定义体检规则，点击**+**，选择体检规则。
5. 开始体检后，请等待AppAnalyzer完成构建、签名、安装等操作，并根据界面提示，登录应用账号后点击继续按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/2WW27U5ySAGKCPL-oKqD0A/zh-cn_image_0000002779406924.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=40EF268F20522DFAB3607EBA71AA73E77FF290AD989B454AAFBF9354282BB383)，继续测试；或者无需登录账号，直接点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/gu70OmqFSOyp7odvHRLARg/zh-cn_image_0000002808766479.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=7701BCD0E7535CCBC71BBE9933A55EE12CE896FA8AFFA79920A86784AB5E0A5C)按钮继续测试。在测试过程中，请保持连接的设备为解锁亮屏状态。
6. 测试完成后，查看测试报告，针对测试不通过的规则，AppAnalyzer会给出应该做和不应该做的事项，以及对应的优化建议。

   如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/bwZEo7aBQYSRhLiP4QWEIw/zh-cn_image_0000002779566898.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9710B71625D1D5B3B080720C1BA3692B12BE0131DD5BD0772A6CDF52786B230)

## 体检规则

### 质量体验

**表1**

| 规则名称 | 应该做 | 不应该做 | 应用或元服务规则 |
| --- | --- | --- | --- |
| 深色模式 | 应用需支持深色模式显示，确保系统切换到深色模式后，界面以深色风格呈现，并且界面内没有因未适配导致的识别性问题。 | 避免文字与背景对比度小于1.9。 | 应用，元服务 |
| 色彩对比度 | 应用使用的色彩需满足最小对比度要求：  (1)图标或标题文字与背景对比度大于3:1。  (2)正文文字与背景对比度大于4.5:1。  (3)智慧屏深色模式推荐文字与背景对比度范围5:1~15.1:1 ，其中正文文字与背景对比度范围：11:1~15.1:1。 | 避免文字与背景对比度小于1.9。 | 应用，元服务 |
| 字体大小 | 应用的文字大小需满足最小字号要求：  (1)手机/折叠/平板文本字号不小于12vp（推荐），最小不得小于8vp（必须）。  (2)电脑文本字号不小于14vp（推荐），最小不小于10vp（必须）。  (3)智慧屏字号范围 - 所有文本字号不小于16vp（推荐），最小不得小于14vp（必须），其中正文字号建议22～26vp。 | 应用的文字过小，不满足最小字号要求。 | 应用，元服务 |
| 状态栏 | (1)应用需要对状态栏进行适配显示。  (2)采用沉浸一体化的背景设计，保证效果的整体性。  (3)根据页面内状态栏区域的背景色选择合适的状态栏颜色（黑/白），保证状态栏信息的易读性。 | (1)避免系统状态栏区域被单独切割。  (2)避免系统状态栏信息文本与背景色对比度小于3。  (3)避免在状态栏背景区域内采用左右半区对比差异过大的颜色，导致部分系统状态栏信息无法阅读。  (4)避免应用信息和系统状态栏信息互相遮挡。 | 应用，元服务 |
| 应用图标 | 应用图标资源需分层，尺寸需满足规范要求：  (1)应用图标资源必须分为前景图和背景图两层，尺寸要求必须为1024 px \* 1024 px。  (2)应用图标显示正常，图标显示完整。 | (1)图标资源不允许自行裁切圆角，不允许在资源内添加内间距。  (2)图标存在明显的模糊、拉伸、压缩、锯齿等情况。 | 应用，元服务 |

### 隐私合规

**表2**

| 体检规则 | 应该做 | 不应该做 | 应用或元服务规则 |
| --- | --- | --- | --- |
| 权限获取 | (1)清晰、明确地在字段reason（申请权限的原因）声明您申请权限的目的，而不仅仅是说明需要该权限。  (2)权限使用理由应准确告知用户获取权限后用于什么场景/功能。  (3)字串应为直白、具体、易理解的完整短句， 用于向用户说明应用使用敏感权限的理由。句子避免使用被动语态，并以句号结尾。  (4)用途描述的字串建议小于72个字符（即36个中文字符，UI界面显示大约为两行）。不能超过256个字符，以保证多语言适配的体验。  (5)不能为空白字符串，即不能不填，也不能只填空格符。  (6)如果应用申请的权限用于多个场景，需要确保字串的完整性，让用户了解应用使用此权限的所有场景；多个HAP包内如果申请同一个权限，各个权限Reason字段需要保持场景的完整性和一致性。 | (1)应用向用户索取敏感权限时，未同步告知用户申请该权限的目的。  (2)应用向用户索取敏感权限时，描述的使用目的与使用的功能模块不符或描述不明确。  (3)应用向用户申请敏感权限时，点击不同模块均申请同一权限，其中部分权限申请时未符合要求，应排查应用内所有权限申请行为均同步告知使用目的。 | 应用，元服务 |
| 定向推送功能或者精准广告营销 | (1)若APP的业务功能存在定向推送功能，应以个人信息处理规则（隐私政策）弹窗等形式向用户明示，将收集的用户个人信息用于定向推送、精准营销。若APP定向推送功能使用了第三方的个人信息来源，还需向用户明示第三方的个人信息来源。  (2)APP以个人信息处理规则（隐私政策）弹窗等形式明示存在定向推送功能，页面中应显著区分定向推送服务，显著方式包括但不限于：标明“个性化推荐”、“定推”、“猜你喜欢”等其他能显著区分的字样，或通过不同的栏目、版块、页面分别展示等。  (3)APP以个人信息处理规则（隐私政策）弹窗等形式明示存在定向推送功能，应提供退出或关闭个性化展示模式的选项，如拒绝接受定向推送信息，或停止、退出、关闭相应功能的机制。  (4)关闭按钮需真实有效：用户拒绝接受定向推送信息，或停止、退出、关闭相应功能的机制后，应用不再将收集的用户个人信息用于定向推送、精准营销。 | (1)隐私政策中对定向推送的描述含糊，未明示将收集的用户个人信息用于定向推送、精准营销。  (2)未在应用内显著标识定向推送。  (3)APP存在定向推送功能，定推关闭按钮“推送通知”无法显著关联定推功能，建议定推关闭按钮也使用显著区分的字样命名，如“定向推送、个性化推荐”等。  (4)APP的定向推送功能提供的关闭按钮无效。  (5)不得以定向推送信息为由，强制要求用户同意超范围或者与服务场景无关的个人信息处理行为。 | 应用，元服务 |

### 生态

**表3**

| 体检规则 | 应该做 | 不应该做 | 应用或元服务规则 |
| --- | --- | --- | --- |
| 体现适配HarmonyOS操作系统 | 您的应用内容，需补充HarmonyOS操作系统的介绍/选项等相关信息。 | 您的应用内容，未说明HarmonyOS操作系统相关信息。 | 应用，元服务 |
