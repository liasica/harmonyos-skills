---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-testing
title: 导入DevEco Testing的检测报告进行诊断
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 导入DevEco Testing的检测报告进行诊断
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:958b186fb1e1dfb2c7fbc25dc9902f08a9634ea27dacd7dbdae85ed2cecd5b40
---

从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行性能相关测试生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告。

## 前置操作

体检前，请先在DevEco Testing中测试并导出检测报告，具体操作方式请参考[性能基础质量测试](specialized-testing.md#section12324184817324)或[场景化性能测试](specialized-testing.md#section8642101711299)。

## 进行体检

说明

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的检测报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/wao5k8OrSXyeTudh0ESPeA/zh-cn_image_0000002561752875.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=68D6E2F9100C26C193CD2C6F758590B9DBF119B4E1F081852ADADE9DA2959C63)
2. 选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](ide-app-analyzer-testing.md#section16156317171913)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/gEFwPGHwTHiBTrLORyMhVw/zh-cn_image_0000002530752944.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=02A7A22F0CC1004D0F756632C1619BE4CD3287FA0FFEDAD3B522694946B91C46)
3. 诊断完成后，查看测试报告如下。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**用户反馈**向我们反馈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/H3kJfo81Rt2sslUMDPfpBQ/zh-cn_image_0000002561832869.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=93383C0F581DD538CD02D2CA73EFF054564466AB669D9909684629A08A578A75)

### DevEco Studio 6.0.1 Beta1以下版本

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**历史记录**按钮，进入历史记录页面。
2. 点击右上角的**检测报告导入**按钮，首次测试时，请根据AppAnalyzer的指引，下载Python及三方库，并根据界面提示，确保即将导入的检测报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/RDJtwGnuT9CHWzd3I2HFTQ/zh-cn_image_0000002561752877.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=F45903FCD6DDB1CD2BF74A3C443F8C2DCD993F82CEEF47973343BF123320DC7F)
3. 选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](ide-app-analyzer-testing.md#section16156317171913)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/ltXM-E7kTYqn4339KxwNDw/zh-cn_image_0000002530912948.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=1B949A4CFE5F6E5878F1C318BBA96D1DDEECAFC8D589C2E2726E30F5DBCFDAAB)
4. 诊断完成后，查看测试结果如下。
   * 测试报告：测试结果的汇总信息，点击**详情链接**可跳转到对应场景的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/34fUXE1XSDi2cyJYCupJrQ/zh-cn_image_0000002561752889.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=7E148A9E30DF38A219463C8903899212A9ADBBF19245CA6C973B01908DE3883D)
   * 详情报告：给出详细的测试结果、可能的故障原因和对应的优化建议。
     + **开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等**：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/iatYzCm-QEuQhwrjZ33kxQ/zh-cn_image_0000002530752936.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=3B3F001970897C77CA092E5C8C56121C107EF84F67F1036546D593FE7AB51121)

   说明

   由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

## 检测指标

AppAnalyzer会将DevEco Testing测试用例的操作归类为以下场景，仅支持对部分指标进行诊断，具体如下。

| 场景 | 检测指标 |
| --- | --- |
| 页面间转场 | 点击响应时延 |
| 点击完成时延 |
| 转场卡顿率 |
| 页面滑动 | 滑动响应时延 |
| 滑动卡顿率 |
| 冷启动 | 完成时延 |
| 页面内转场 | 滑动响应时延 |
| 点击响应时延 |
| 点击完成时延 |
| 滑动卡顿率 |
| 起播时延 |
