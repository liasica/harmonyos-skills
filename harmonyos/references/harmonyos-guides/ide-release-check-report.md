---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-release-check-report
title: 导入上架检测报告进行诊断
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 导入上架检测报告进行诊断
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:28b561f783b558812ddd34e0099066f5d61e465978493799c6661c7a142fe962
---

应用在AppGallery申请上架会对UX、稳定性、功耗、性能和兼容性等专项进行审核。从26.0.0版本开始，AppAnalyzer支持导入上架审核不通过的报告并进行诊断分析，帮助定位可能的故障原因并生成体检报告。

## 使用约束

* AppAnalyzer支持导入UX、功耗、性能专项报告进行诊断分析。
* AppAnalyzer仅支持对手机的报告进行诊断分析。

## 操作步骤

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**History**打开历史报告页面，点击右上角的**Import** **> Release Check Report**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Omp_TRrGS7WLTjbSUpbpOw/zh-cn_image_0000002779406784.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E900ACE01AE970070E44AD8EBD72D2976AF132C0C4D2C61DFECA9F4E5F0D4057 "点击放大")
2. 确认需要导入的上架检测报告，点击**Import**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/c1zJs1stTz2iaVb3s9bYtg/zh-cn_image_0000002779406786.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4175A09FD0BD71EEC513ED325C286E81C75AC3B37E5541E68C156EA4C581BF91)
3. 根据界面提示，确保即将导入的上架报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/vhlQm6fZTVCnbbzogOuB-A/zh-cn_image_0000002779566764.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB117751E002DFFBF1886FAF7D130C83EFFA03D133B2CB629492955DF323E9B2)

   选择是否授权AppAnalyzer获取应用上架驳回问题关联的hiperf数据，用于诊断问题的可能故障原因。在**AppAnalyzer**首页，点击底部**Settings**也支持进行堆栈授权**。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/mGfUTQHpTPSt2LncB2p5-w/zh-cn_image_0000002808766347.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F644AE6C418DE0504903AB818DDE3196D71B5D261A70B7D76E111F37DE2EE3E9)
4. 诊断完成后，会提示生成的体检报告的数量，请在当前的历史报告页面中查看对应的报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/TX1-A6sURrqez3bPrgZkMw/zh-cn_image_0000002808886431.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C33F5FB4952A6B3C3428E361491D22B6964F5FC9CAFCA55D21AFB6DBA02D8FA)
5. 查看体检报告。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

   如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/hj3PsqE_TaSTM68cAK_Z4A/zh-cn_image_0000002808766349.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C70BB7EFA656C0A7D90B889608DB2D4FD3ED3A4676C04F1557C8DFAA4B80734A)
