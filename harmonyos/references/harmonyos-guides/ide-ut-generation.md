---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ut-generation
title: 单元测试用例生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 单元测试用例生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b6952db32007148039624cb14756af392f51faa4115e5e9af50521088e6044ee
---

根据选中的ArkTS方法名称，CodeGenie支持自动生成对应单元测试用例，提升测试覆盖率。

## 使用约束

* 该功能最多支持解读30000字符以内的代码片段。
* ArkUI代码、生命周期函数、@Extend/@Styles/@Builder修饰的函数、private修饰的私有函数不支持生成单元测试用例。
* 单元测试用例生成时使用HarmonyOS Ask智能体。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后，在ArkTS文档中，光标放置于方法名称上或框选完整的待测试方法代码块，右键选择**CodeGenie > Generate UT**，开始生成单元测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/75IajWLsSxCeepuVCdtkaA/zh-cn_image_0000002561752715.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=E654DA02B44DD467530CDA63DA04CCB62D9444263035CB76A32E8FDF65DE9844)
2. 在问答对话区生成单元测试用例后，点击Code Genie问答区中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/3BCcA2NmRWGPYkMsZPXHwg/zh-cn_image_0000002530912774.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=F0567CF168773064E52FE69138945B8C21D0750713A10075451C2F677830EAB2)可复制生成的代码，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/yqN6OYGPSFmIMUEzqRHFbw/zh-cn_image_0000002530752776.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=418302ACF34F00D095D719DF5C7173266AD7F1A4812AB45C90EA8FA1DE2B5F85)将生成的代码插入到代码文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/5jxvW1CISl6eZs7aiQyvYw/zh-cn_image_0000002530912778.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=4C03DE2432D457A1380A3B76B09D2D26C056C4B3FC8FB2DA36DA1AE49C1D9524)弹出文件另存为框，填写文件名称后点击**OK**按钮保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/-d9-qwEgT42XZO4Woeqovw/zh-cn_image_0000002561752719.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=AC1FE43EF0125584CC8DF8A5D497C51743E5D9FFC8A9CB2B4EA183D246E6D8A9)
3. 生成的单元测试用例文件被保存在待测函数所在模块下的**ohosTest/ets/test**目录，目录结构和待测函数保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/BwnEs3atQb-7nU_omPSZyw/zh-cn_image_0000002561832699.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=989340B5928803344B0EC80206DE89E7798B5EAC3E4F14FB50455AB0FDEEC720)
4. 运行单元测试用例，具体请参考[运行测试用例](ide-instrument-test.md#section14415226122419)。
