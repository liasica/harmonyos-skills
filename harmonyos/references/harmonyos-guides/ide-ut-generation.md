---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:377d8cd4b8b81b9ad0a676c27f6ca9c31cd094ab37c4d57f25e98acb16acc1ab
---

根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/9j6hT4n2SmSEaS3BTxEvbg/zh-cn_image_0000002731381925.png)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/Q0q7UZXKR-qYOyvGRnPRTA/zh-cn_image_0000002731381921.png)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Gishj61DQ9KP6OpCqAtAgw/zh-cn_image_0000002701662706.png)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Aqt4vt-eSH-wKIkFL90p7A/zh-cn_image_0000002731381915.png)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/9gxJcwXyRNKcaIzN2lEWcQ/zh-cn_image_0000002731381919.png "点击放大")
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/cPe6DZs6SyOdPcIBxaNzyw/zh-cn_image_0000002701822624.png)
4. 运行单元测试用例，具体请参考[运行测试用例](ide-instrument-test.md#section14415226122419)。
