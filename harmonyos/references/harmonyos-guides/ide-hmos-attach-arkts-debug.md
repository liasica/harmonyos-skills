---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-attach-arkts-debug
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ebc9789aef02de8c92feded55f5ccb257513a37ddee927536e1f7d9856637077
---

开发者也可以通过将调试程序附加到已运行的应用进行调试。

附加调试和调试的区别在于，附加调试可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而调试是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被附加调试的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

附加调试不支持的场景：

* 本地无源码。
* 应用包名不匹配，将出现提示“**所选进程与当前项目的包名不匹配！**”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/MCS2Z_jSTBKZhu_guD9C4Q/zh-cn_image_0000002792001174.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E287FB5493368F834D11D8C11B5DCA61CDE9DAC5A1C84EBA1C6B15E7E42B689)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Z2jtBXgaSWSHvMpuTsY2HQ/zh-cn_image_0000002791841202.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=68EC51C9C75615F14A5BD0626969C5CDB65DABC46E8D90DADACB3AE3F390AC9A)
2. 选择要调试的应用进程，若应用包名与当前工程不一致，则需勾选**显示所有进程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/uqE8hdyVQ7qqw56a6sjfvg/zh-cn_image_0000002791841204.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB1ADF3BCD43BCEBA5FEB2DB8CFE608AB1034E3D4AEDBFE4D87AB9B3EE1A7E00)
3. 选择需要使用的调试配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/c9u6kVSvS2mUrhgK499B9w/zh-cn_image_0000002792001176.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C43283E8CBBFCCF0BA261B75435520FB98BB385275215595629A4052B0FD0422)
4. 选择好调试配置进行附加调试后，**调试类型**不可改变，只可在**运行/调试配置**界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/w8E-MtipRkKPAcx3id6YOQ/zh-cn_image_0000002820721143.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F7D3C49F452EE033813FE5714C6F97EB1E051A73C20489A4835A2A958675753)
5. 点击**确定**开始附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/PXPj9OXmRle1h4_7UWGeUQ/zh-cn_image_0000002820681139.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4A8DE1DE57768017F4E0AD4296BDAAC92795ADCB2D9405090A5081B2126B162)
