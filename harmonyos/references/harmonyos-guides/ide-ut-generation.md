---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c93bb09818ca8f7e2cfab8ba1c4f226bc14e14747d1beb292a1a19e0caa514d0
---

根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wVPMO8luRri2aBubLs9sRw/zh-cn_image_0000002808886177.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D62DE859A0B1CFBA9AFB0B039E5BA54515133003261D3EF0FDC1CD08005C433)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/eb3XiDI3SKGBspRqj_Q-zw/zh-cn_image_0000002808886173.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1514126C037FC1E3A731522ECC859D544FAD0C6E257CC699EA0AA67491B4B5A)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/DUU-LRbnQBOXl00B-v6dvg/zh-cn_image_0000002779566516.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C2A55595056CB468D5C76B60E802CED0257F0CA88FE4D667E45C35B903D5E6F)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/fsmeEnz3TtSzFMMNAe7xCQ/zh-cn_image_0000002808886171.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=745B9EE5806C8F12F46CA874AA60E0BDF1AE41FE89FF5C36D20E7FED5AA45DFB)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/w2yrLxHlRMqJPNqSLUATAw/zh-cn_image_0000002808766091.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF4B0FDE7EA620631CC3FC242BBC6592764E234100B68D2C24757B2A3033FF7E "点击放大")
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/fIKAyAWxQDWVxB28uRKasA/zh-cn_image_0000002808766093.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4849814FF9156B9E05C9C5F9AD675DA290F7F8F0BA439CC59426900D9D65BF6)
4. 运行单元测试用例，具体请参考[运行测试用例](ide-instrument-test.md#section14415226122419)。
