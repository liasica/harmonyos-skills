---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4b08929eb482ac1c8d6ab532b3ffea594db6b02086bd470c465b45104fbc3143
---

根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/4vVAd_6-Sg6pQMJ3oA-AOQ/zh-cn_image_0000002808886177.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB5B28D074C9B2E551D1E011E07B6EEB35FD30D6AEBDC4F4DA83BCCE1E68A55B)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/usfmhvXVS-a4-efjZArYBA/zh-cn_image_0000002808886173.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D3458D638B3677A0A64BD55B5DF9E56DEB9F08D40A648C9782F4CB654D6DE69)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/fT10HPiESY2auDtr7drdGA/zh-cn_image_0000002779566516.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F9E2B2D0FD8354BE470778EECB757E1C7F1677D5A2C0F5B1FA7D2A747F90DEE)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/rKuu2rmqTVi-NEbC79W-pQ/zh-cn_image_0000002808886171.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EBDBA2001C753FD57259A1B338793F79E9E74A4823B5E335D719007354A4B19)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/A3o1yXORQDqjqsxhlIh5FQ/zh-cn_image_0000002808766091.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=60C679710F034959A3355C211FB2E8E31016F17DD3CAF4559DDD0FC500FA38DD "点击放大")
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/HWaJSHylSey8cklgvFV25A/zh-cn_image_0000002808766093.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=69F68E8A9C1D1FF3570BB87151422B4479ED38912C1E58529C534848300D13C8)
4. 运行单元测试用例，具体请参考[运行测试用例](ide-instrument-test.md#section14415226122419)。
