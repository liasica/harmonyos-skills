---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/publish-testing
title: 上架预检
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 上架预检
category: harmonyos-guides
scraped_at: 2026-04-29T13:48:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b3c1302333faa27f9f62770cb7a7325d00592871a0761814862932f71824bcd
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ClqIYcAVQfG1DxbQJiyIaA/zh-cn_image_0000002524623381.png "点击放大")

## 应用上架预检（本地）

**应用上架预检（本地）：**基于鸿蒙应用上架质量标准构建的一键式自动化测试服务，提供兼容性、性能、稳定性、UX、功耗专项基础质量的专业检测报告，帮助用户识别应用的基础质量问题。

**创建任务**

步骤1：打开DevEco Testing客户端，左边菜单栏选择“上架预检”，点击“应用上架预检（本地）”卡片，进入任务创建界面。

步骤2**：**进入任务创建界面后，配置任务参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/aG0OTv9iQ-KQKao9zI4oOw/zh-cn_image_0000002569034623.png)

* 任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
* 备注信息：填写任务备注信息，便于快速筛选报告。
* 测试设备：选择待测设备，最多可选择3台相同类型的设备并发执行，提高测试效率；支持 HarmonyOS 5.0及以上版本。

说明

任务模式分为“自定义预检”与“综合预检”。“自定义预检”可自定义选择执行的专项及参数；“综合预检”执行全部专项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/pbzhdW-QRnq6RYVFJC5DRQ/zh-cn_image_0000002492343708.png "点击放大")

**自定义预检：**

自定义策略：选择本次测试的专项和对应的参数。

* 兼容性：选择是否测试安装卸载场景。
* 功耗：无特殊参数。
* 性能：选择启动测试次数（对应用进行启动测试）、遍历时长。
* UX：选择遍历时长。
* 稳定性：选择测试时长。
* 应用包名：选择设备中已安装的应用包名。
* 应用类别：选择应用所属的分类。
* 选择应用包：选择与待测应用相同的应用包文件用于测试静态检查项，仅支持.hap或.zip文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/cotzLrQrSAmdabgNt0swrQ/zh-cn_image_0000002492343688.png "点击放大")

**综合预检**

* 应用包名：选择设备中已安装的应用包名。
* 应用类型：选择应用所属的分类。
* 选择应用包：选择与待测应用相同的应用包文件用于测试静态检查项，可选.hap、.zip文件。

步骤3**：**配置完成后，点击创建任务按钮开始测试。

**测试执行**

创建任务后，将会跳转到执行页，执行测试环境初始化操作。初始化完成后，开始检测应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/o6qP1Zx0T3STCB057d6_iQ/zh-cn_image_0000002492343714.png "点击放大")

测试页面支持查看各测试项以及测试状态。每个专项测试完成后，点击查看按钮可以查看各测试项详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/0u-6iISERDG1Pml5u_N4HQ/zh-cn_image_0000002492503654.png "点击放大")

**测试报告**

测试报告：任务信息包含：任务名称、任务类型、测试时间等。点击打开目录按钮可导出报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/tA3C7oJfQr-I_AlYO6W0EA/zh-cn_image_0000002492343704.png "点击放大")

应用信息：包含应用名称、版本等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Vn1gCv29TNCri9utveRH7A/zh-cn_image_0000002524503407.png "点击放大")

测试总览：专项测试的基础质量满足度与总体测试结论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/CuuaQ3n2TvmvForxGwh6yA/zh-cn_image_0000002524623379.png "点击放大")

测试详情：专项测试结果详情。

**兼容性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/a1LveCtCQFKqp3_Jo4mYoA/zh-cn_image_0000002524623371.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/YcWh7A_OSmqXcFm1vWw3Fw/zh-cn_image_0000002492503660.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/sWoo2ZM7Qr-eE74s9KetOw/zh-cn_image_0000002524623361.png "点击放大")

**功耗测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/wp4IEiNVTHOnrHR2TPuKVA/zh-cn_image_0000002492503682.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Emm8Xi9vRV6QIadNTbPUsA/zh-cn_image_0000002524503395.png "点击放大")

**性能测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/aRX0jMpJTuWKSc1jloXoSA/zh-cn_image_0000002524503417.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/yWkjNI00R7ehBV-79pTLfQ/zh-cn_image_0000002524623369.png "点击放大")

**UX测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/SgMMErm6Tvy_IyA3Y_JZcw/zh-cn_image_0000002492343690.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fV8S2xj9Tg6nA0B4bbcq3g/zh-cn_image_0000002524503389.png "点击放大")

**稳定性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/6Hs7YdjCSdqmPyyLXNpo_Q/zh-cn_image_0000002524623367.png "点击放大")

说明

更多测试服务详情，请前往DevEco Testing客户端->上架预检->应用上架预检（本地）->任务创建页->测试指南中查询。
