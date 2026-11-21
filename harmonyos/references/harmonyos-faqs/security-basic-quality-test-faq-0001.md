---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/security-basic-quality-test-faq-0001
title: DevEco Testing安全基础质量测试常见问题
breadcrumb: FAQ > DevEco Testing > 常见问题 > DevEco Testing安全基础质量测试常见问题
category: harmonyos-faqs
scraped_at: 2026-11-21T09:19:35+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:c8ae022daf39c61e60e2eaf9c232fc2ef9f8191797df372838c538b353025f68
---

**Q：安全基础质量测试如何测试？有什么注意点？测试报告如何查看分析？**

**A**：操作步骤如下：

1. 进入DevEco Testing客户端，左侧菜单栏点击专项测试-[安全基础质量测试](../harmonyos-guides/other-test.md#section2492910181110)，选择设备（连接单台设备默认展示设备SN号，连接多台设备时可根据SN号选择执行设备），上传应用包，点击创建任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/8H6sHX0oRG6yNyNN6xkIxw/zh-cn_image_0000002762452344.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B128993FC90C48C41EA7BDC7F83B66F44223009BB6A43FFC529419FECD21C76 "点击放大")

   注意点：

   * 支持多台设备同时执行，测试设备中根据SN号选择对应的设备，然后创建任务。
   * 安装包支持hap、app、zip类型，多个hap包的应用可以直接使用app包或者打包成zip来执行安全测试。
   * 系统版本支持HarmonyOS 5.0及以上版本。
2. 执行完成，如果有检测不通过项，详细日志列点击查看，问题列表-问题描述中可以查看到具体报错信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/nINedYleRkuaExxHxnJ6TA/zh-cn_image_0000002791971131.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=77F99DF2BF3694BC9B3CADB1B284F4E96DEC92E58AD0E0ECE86ADA02B3954499 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_PxV6IBkTS-rFnkjQK8MCg/zh-cn_image_0000002791850909.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F43BAC380A36088FC2E724EE6CFBEA69F1751FF5300E0844042FDC58576E214 "点击放大")
3. 问题列表中修复指南列点击查看，可以跳转到对应文档，参考文档进行修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/snZgdeQkR5ykzhwHTi5ReA/zh-cn_image_0000002762612278.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D968EC84AA7C57F9FF76D6A31E8CB27DE6BC496413EC10D7B2CFC6D483CE16 "点击放大")

**Q：DevEco Testing的安全基础质量测试为什么需要选择应用包，不能选择已安装应用？**

**A**：安全基础质量测试会对应用的组件安全、配置安全、通知、选择和同意、向第三方披露等规则进行测试，所以需要选择应用包。

**Q：测试报告中“应用权限申请遵循最小化原则”测试结果不通过如何定位？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/iWXf_mQqTP6RHErJFeUXJA/zh-cn_image_0000002791850911.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=6465BDA6C44E84EC6046C701A0C9D1652E88348C64A774F46BC254F2221E1268 "点击放大")

**A**：定位步骤如下：

1. 查看问题描述中所列的异常权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/qTXgw1hSQnGOrqUGgkCSVw/zh-cn_image_0000002762612280.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=619D8FC5586CAC2AEB176FBB2A484DCBC0F220FF80E470F8285EA337B603EE91 "点击放大")
2. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中requestPermissions字段下面找到问题描述所列的权限，在[应用权限列表](../harmonyos-guides/app-permissions.md)中查找权限名称：确认是否支持、权限是否废弃、权限拼写是否有误。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/yuiP4In7Tk-JDePNaAeYqg/zh-cn_image_0000002791850913.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D91C22DF581B78A717401D4D86D21DDB294C109CF6C5A551DAE96E9FB43A2FD "点击放大")

**Q：测试报告中“应用所需权限必须在应用的配置文件中严格按照权限开发指导逐个声明”测试结果不通过如何定位？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/-olcuRNJTeGy0OSJi2fe1A/zh-cn_image_0000002762452348.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=16D9C44F44ED07C4467B8602E7BD7D380E1ED564E824524ED1D75AA6369A462A "点击放大")

**A**：定位步骤如下：

1. 查看问题描述中报错原因（以下为举例）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/P8JkkxTOQ22v2nB0Lya_Fg/zh-cn_image_0000002762612282.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE6AE66D493F3709D31B21BB15AF26FF0B1DFA07A34DDAE8F48202209C63AF6E "点击放大")
2. 在module.json5配置文件中查找该权限，因为ohos.permission.ACCESS\_BLUETOOTH是UserGrant权限，所以usedScene是必填项，需要补充usedScene属性。参考文档[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/rzMXcX4rRTCreOJiKsNyUA/zh-cn_image_0000002791850915.png?HW-CC-KV=V1&HW-CC-Date=20261121T011934Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC3B48149811340CCA4CC68EADD5783BA132FA583F804B030EDDB91C2A10CA87 "点击放大")

   权限类型确认可查看[应用权限列表](../harmonyos-guides/app-permissions.md)。
