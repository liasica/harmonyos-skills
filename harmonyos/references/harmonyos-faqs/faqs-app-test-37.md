---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-37
title: 如何整合多个module模块的单元测试
breadcrumb: FAQ > DevEco Studio > 应用测试 > 如何整合多个module模块的单元测试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:e50db57d31c8b948c63f7143ea301a1a6f321507a417cedc3372e2bfaa5ae367
---

## 问题现象

在开发多module模块项目时，如果多个模块均开发单元测试，如何将不同模块的单元测试进行汇总执行，达到快速验证的效果。

## 背景知识

[Local Test](../harmonyos-guides/ide-local-test.md)：测试用例存放在Test测试目录下，不需要运行在设备或模拟器上。Local Test支持ArkTS语言，仅支持Stage模型，不支持测试C/C++方法及系统API。

## 解决方案

如果要联合多个Local Test进行集中测试验证，需要创建Compound并关联上所有的Local Test测试用例，直接运行Compound即可对所有的Local Test进行测试验证：

1. 在工具栏主菜单点击Run->Edit Configurations。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/HqVwuxxfSZS2ZF_e48mVnQ/zh-cn_image_0000002675023655.png "点击放大")
2. 点击Add New Configuration，即左上角的+，选择Local Test，给所有要测试的模块创建LocalTest。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/Xcuu6xZwSaCwO4mzMcwPlA/zh-cn_image_0000002644943828.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/jCPywBpxT5inbXo8Jfa3Nw/zh-cn_image_0000002675103535.png "点击放大")
3. 点击Add New Configuration，即左上角的+，选择Compound，创建Compound复合类型将多个子SDK的所有单元测试都加进去，之后再点击应用，点击确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Nzk_ALVjS8CI1iVpgftImQ/zh-cn_image_0000002675103933.png "点击放大")
4. 选中刚才编辑好的复合类型名称，点击运行即可执行整合的单元测试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fQ2NEUl5SjOoZ93I-PCrrw/zh-cn_image_0000002645104202.png)

## 常见FAQ

Q：单元测试报告，是否支持输出lcov.info格式文件，或者可以转化为lcov.info格式？

A：单元测试报告目前只有html+json格式。

Q：多个module如何进行单元测试，测试代码希望能够复用？

A：多个module按照正常用例编写，测试代码如果不涉及mock，按照正常重构方法进行提取。
