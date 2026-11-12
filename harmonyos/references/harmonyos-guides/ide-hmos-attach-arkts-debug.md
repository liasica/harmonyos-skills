---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-attach-arkts-debug
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5c6e2856c9c63886b39d9d51817596798f4e23be9ddcd599c40c68c7ab5a3f25
---

开发者也可以通过将调试程序附加到已运行的应用进行调试。

附加调试和调试的区别在于，附加调试可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而调试是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被附加调试的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

附加调试不支持的场景：

* 本地无源码。
* 应用包名不匹配，将出现提示“**所选进程与当前项目的包名不匹配！**”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_FslSxDPQOmakJRDkLnigQ/zh-cn_image_0000002781311070.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1510CCBE8E4A693DAC024D9900D2884B9412D5365F830CD8E90C400E1144068)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ORGREzyBT969X_kDj6B6Fg/zh-cn_image_0000002810750669.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=406635EB5F63DAD4DC9DCCBCD0F0558579753F52FB7BBB6B3CD60FDBCDA1D3F9)
2. 选择要调试的应用进程，若应用包名与当前工程不一致，则需勾选**显示所有进程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/_qzF9wEkTWu0Iqdebj38hg/zh-cn_image_0000002810750685.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD1005C8B576C83E32F134000BB6360F38B195EECDC93DB70FB23864961BF81B)
3. 选择需要使用的调试配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/AnUThritRZSZULQgeD3fAA/zh-cn_image_0000002781471006.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F72A8185FD2ACE5954665C7B39225DE05B46D70C5BC022599BFE3B7A18EF6D9)
4. 选择好调试配置进行附加调试后，**调试类型**不可改变，只可在**运行/调试配置**界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/y7f3pTyjRL6znftNvhx8GA/zh-cn_image_0000002781311076.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=50058B4B344598EDC8A64623AE7D357E317A876AD053105B10AAC3DF2063453F)
5. 点击**确定**开始附加调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/kVWEFconQUen3Nx_m8jwzg/zh-cn_image_0000002810630559.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DAAC7600C7CC6D934C2877E7B2D3B20503DD69CD46190522F21965A1015CE8C)
