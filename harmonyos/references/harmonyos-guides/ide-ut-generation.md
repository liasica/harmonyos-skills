---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bf9a434150decc2716fdd01cae107f3a9bb774070e64d386b797698bcff846c7
---

根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/Uh7FSfDuSeWQn7DgKKVhOA/zh-cn_image_0000002561752715.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=694E6CBD64A06C04B24455ED93B16A6871F03590F15F6445A87E7C6678AB4261)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hnGgw8g0Tjqcqrj6JUEu3Q/zh-cn_image_0000002530912774.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=79AEB9DFCCA4DD7FD13C64C1A4F09E4ED47A6AEC3F8066CD0331E70CFCCA17A4)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Al-aIhzNRnmSGJSzh1rHxA/zh-cn_image_0000002530752776.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=A8E2120AAC8FDBDE798D31C97B81B2D4DBBBD7C4AC0BD55F8956E6D8AFD838EB)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/0LVlH3QUTce3RrajvYu9hw/zh-cn_image_0000002530912778.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=0C0041BD2AB8ECF5122163CAE8CA888442F2A941653AD6F0703B9D9959EC1133)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/xFyQbpPLT-yvLsn2ZYW87A/zh-cn_image_0000002561752719.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=2C59F0FEF97EBD5F41D9F20B374C799CD09E3821ADCB9BA9D7A0446151C3E754)
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/WPj1NKNfRm2Zv6JIOqkKUw/zh-cn_image_0000002561832699.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=994372C3B6943FC37646C5BC10273893D3B066984FA04CF9F0695A09378D49C5)
4. 运行单元测试用例，具体请参考[运行测试用例](ide-instrument-test.md#section14415226122419)。
