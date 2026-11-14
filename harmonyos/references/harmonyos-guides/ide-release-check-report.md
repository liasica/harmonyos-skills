---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-release-check-report
title: 导入上架检测报告进行诊断
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 导入上架检测报告进行诊断
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:05ab71872d569fad96739d23e02220c0ab6b8dedb5ccdea52588e711bc9d7572
---

应用在AppGallery申请上架会对UX、稳定性、功耗、性能和兼容性等专项进行审核。从26.0.0版本开始，AppAnalyzer支持导入上架审核不通过的报告并进行诊断分析，帮助定位可能的故障原因并生成体检报告。

## 使用约束

* AppAnalyzer支持导入UX、功耗、性能专项报告进行诊断分析。
* AppAnalyzer仅支持对手机的报告进行诊断分析。

## 操作步骤

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**History**打开历史报告页面，点击右上角的**Import** **> Release Check Report**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/-u5BVp80QySH_0R2VXyQIQ/zh-cn_image_0000002779406784.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=535BCB6A51CB79EEFC4AEAF1880897CDC73E2581101759ED86236BC2AC543AD4 "点击放大")
2. 确认需要导入的上架检测报告，点击**Import**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/_uviSXoaS7SJ1ysnZH2t_A/zh-cn_image_0000002779406786.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=9506F37DE545CAE4B0DCCDF41772FF5EA8CD6B1719E29DE02DA43ED7C60337B5)
3. 根据界面提示，确保即将导入的上架报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/7tKkroLTTUSa-cRT9_PnOw/zh-cn_image_0000002779566764.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=69063C7F3DE045C7C5A453790A4D29F36CD2EFA32E28E9C67B6D6A43FCE06D5C)

   选择是否授权AppAnalyzer获取应用上架驳回问题关联的hiperf数据，用于诊断问题的可能故障原因。在**AppAnalyzer**首页，点击底部**Settings**也支持进行堆栈授权**。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HtsFnzIRQgGCyl3DUImH8w/zh-cn_image_0000002808766347.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF9487956818093C594F2B047A01E751DBF25D2C3CB3118C2D4F600238D4C01B)
4. 诊断完成后，会提示生成的体检报告的数量，请在当前的历史报告页面中查看对应的报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/kT8gqwX_RZS2KtbjhjCQiw/zh-cn_image_0000002808886431.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=A62DD76EBD27322C7F9013912CF8D269B6B84570CF2D9BA4A1DA30FD9EA6667E)
5. 查看体检报告。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

   如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/poiZ_lJ5QUCXNQY0Z3KW0Q/zh-cn_image_0000002808766349.png?HW-CC-KV=V1&HW-CC-Date=20261114T004714Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F870CC11CD301D382F88D3D13D892D9C7791168B1FFCB9AF2DF9DB2EA72A445)
