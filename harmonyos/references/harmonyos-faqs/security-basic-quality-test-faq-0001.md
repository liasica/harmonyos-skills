---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/security-basic-quality-test-faq-0001
title: DevEco Testing安全基础质量测试常见问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 安全基础质量测试 > 常见问题 > DevEco Testing安全基础质量测试常见问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:12a3c9941ba43158f15230d22dbf3120e62d0258b8df26fb1aaf2da85e47fd0c
---

**Q：安全基础质量测试如何测试？有什么注意点？测试报告如何查看分析？**

**A**：操作步骤如下：

1. 进入DevEco Testing客户端，左侧菜单栏点击专项测试-[安全基础质量测试](../harmonyos-guides/other-test.md#section2492910181110)，选择设备（连接单台设备默认展示设备SN号，连接多台设备时可根据SN号选择执行设备），上传应用包，点击创建任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/8a3AdR7nT5CpsntSmAwJZg/zh-cn_image_0000002762452344.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD64C644CBB1CF50B1B95FC55B834A9890B9AC8617573F56DA25100853F9D3F9 "点击放大")

   注意点：

   * 支持多台设备同时执行，测试设备中根据SN号选择对应的设备，然后创建任务。
   * 安装包支持hap、app、zip类型，多个hap包的应用可以直接使用app包或者打包成zip来执行安全测试。
   * 系统版本支持HarmonyOS 5.0及以上版本。
2. 执行完成，如果有检测不通过项，详细日志列点击查看，问题列表-问题描述中可以查看到具体报错信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/htToojQ_T_ODBly4uEaDDA/zh-cn_image_0000002791971131.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C01FDA226A8FEB8C43689E2B33F5903C477C0966ED3EE965BFB844ABFAE5224 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/SU9t2on8RECyBfKLHYu2qw/zh-cn_image_0000002791850909.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F976F31468E4FF574D4C728083C23AAC3827C87248EE53FCA9033844EFDACCE "点击放大")
3. 问题列表中修复指南列点击查看，可以跳转到对应文档，参考文档进行修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/52ZGtdiRTjWxMKIBFVBtJA/zh-cn_image_0000002762612278.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C9537F905B9B2A89613B4810CEBD0AD295FCC51979E83DA7A3C6EC8FE5CC480 "点击放大")

**Q：DevEco Testing的安全基础质量测试为什么需要选择应用包，不能选择已安装应用？**

**A**：安全基础质量测试会对应用的组件安全、配置安全、通知、选择和同意、向第三方披露等规则进行测试，所以需要选择应用包。

**Q：测试报告中“应用权限申请遵循最小化原则”测试结果不通过如何定位？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/lQJFeN2BQEubWs_nVYhtkA/zh-cn_image_0000002791850911.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD76B2948A9B297FA079A768434AC049A7F07224D48C3D9FD0D262EE50F77238 "点击放大")

**A**：定位步骤如下：

1. 查看问题描述中所列的异常权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/_66nPsEHTKm2JKoLyrQUlQ/zh-cn_image_0000002762612280.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0E21FD020192C579C8B4259A711A54E62D7D1BEC70EAEDE6895F1F43F852574 "点击放大")
2. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中requestPermissions字段下面找到问题描述所列的权限，在[应用权限列表](../harmonyos-guides/app-permissions.md)中查找权限名称：确认是否支持、权限是否废弃、权限拼写是否有误。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/JDbkuwv4SR-E5otk2qL3Wg/zh-cn_image_0000002791850913.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6A21F4B2EACBA6B026BC58D2DB5497FD4BFC6A0257FF458926A08A9F332E647 "点击放大")

**Q：测试报告中“应用所需权限必须在应用的配置文件中严格按照权限开发指导逐个声明”测试结果不通过如何定位？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/rL7fJJlCR5yz55dTk5gq_g/zh-cn_image_0000002762452348.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBE7FCDBBF780D384B7E5248C95400BA3D5D0CE478E3EE6FA4057E45AFCCEB94 "点击放大")

**A**：定位步骤如下：

1. 查看问题描述中报错原因（以下为举例）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/27B1o-7OQI-M9nLwUmwBxQ/zh-cn_image_0000002762612282.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF6F6E96FA37C1263A67655A41D3D570545F525528219D1D5CE88A7AB7E52429 "点击放大")
2. 在module.json5配置文件中查找该权限，因为ohos.permission.ACCESS\_BLUETOOTH是UserGrant权限，所以usedScene是必填项，需要补充usedScene属性。参考文档[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4_PmWZIvRXCaGVU-Gn6LQA/zh-cn_image_0000002791850915.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF6A151935BBA9ED03E42491EB1866AF6E075B151265457786F947AFFA25F72C "点击放大")

   权限类型确认可查看[应用权限列表](../harmonyos-guides/app-permissions.md)。
