---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/publish-testing
title: 上架预检
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 上架预检
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:987cb7397d50be0dd44473b005a9b90548e22d2c6927b0e73cc0940f5956db85
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ClqIYcAVQfG1DxbQJiyIaA/zh-cn_image_0000002524623381.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=95D58CA96539E1D55D65C59EB9F1E7F784F835841EB8F83A8EE779704FCB3ADA "点击放大")

## 应用上架预检（本地）

**应用上架预检（本地）：**基于鸿蒙应用上架质量标准构建的一键式自动化测试服务，提供兼容性、性能、稳定性、UX、功耗专项基础质量的专业检测报告，帮助用户识别应用的基础质量问题。

**创建任务**

步骤1：打开DevEco Testing客户端，左边菜单栏选择“上架预检”，点击“应用上架预检（本地）”卡片，进入任务创建界面。

步骤2**：**进入任务创建界面后，配置任务参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/aG0OTv9iQ-KQKao9zI4oOw/zh-cn_image_0000002569034623.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=D227DB7FF1E161781ADB8627B248C6A74875425914A6BF08548F3A063FF115DE)

* 任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
* 备注信息：填写任务备注信息，便于快速筛选报告。
* 测试设备：选择待测设备，最多可选择3台相同类型的设备并发执行，提高测试效率；支持 HarmonyOS 5.0及以上版本。

说明

任务模式分为“自定义预检”与“综合预检”。“自定义预检”可自定义选择执行的专项及参数；“综合预检”执行全部专项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/pbzhdW-QRnq6RYVFJC5DRQ/zh-cn_image_0000002492343708.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=2761FE34FE002A4106FF7B9E9E582DE9C20DDAFC7F3268960D62BAB082DBC092 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/cotzLrQrSAmdabgNt0swrQ/zh-cn_image_0000002492343688.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=D2D06CC33F2F94015FAC8AC0AE52593DFF952A9A667BF4001FD4341E403CAE03 "点击放大")

**综合预检**

* 应用包名：选择设备中已安装的应用包名。
* 应用类型：选择应用所属的分类。
* 选择应用包：选择与待测应用相同的应用包文件用于测试静态检查项，可选.hap、.zip文件。

步骤3**：**配置完成后，点击创建任务按钮开始测试。

**测试执行**

创建任务后，将会跳转到执行页，执行测试环境初始化操作。初始化完成后，开始检测应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/o6qP1Zx0T3STCB057d6_iQ/zh-cn_image_0000002492343714.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=DC65205FEEB2FF7F4A8226A37640E5541D72123EBFB3D2CFD9E013B5DB4C3A81 "点击放大")

测试页面支持查看各测试项以及测试状态。每个专项测试完成后，点击查看按钮可以查看各测试项详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/0u-6iISERDG1Pml5u_N4HQ/zh-cn_image_0000002492503654.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=FA29CB3A74BABAC9AEC41C7DDB7F7DA49175835542DBE34B476BC0BE1179A569 "点击放大")

**测试报告**

测试报告：任务信息包含：任务名称、任务类型、测试时间等。点击打开目录按钮可导出报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/tA3C7oJfQr-I_AlYO6W0EA/zh-cn_image_0000002492343704.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=0512F37DD252635DA54DFAA4A38FA54DBC9181EA3D41F3D60F2A6D34350443AD "点击放大")

应用信息：包含应用名称、版本等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Vn1gCv29TNCri9utveRH7A/zh-cn_image_0000002524503407.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=687EEA18EB3B2866E9232CA54DD0E59D1BB3A5AD722CB0D38DD86CC4531095E4 "点击放大")

测试总览：专项测试的基础质量满足度与总体测试结论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/CuuaQ3n2TvmvForxGwh6yA/zh-cn_image_0000002524623379.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=655CD2452FC122537C2FDB7345F0C0A125EC1460C4D4C015D4C4ABE6FA125E28 "点击放大")

测试详情：专项测试结果详情。

**兼容性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/a1LveCtCQFKqp3_Jo4mYoA/zh-cn_image_0000002524623371.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=19446D82D3590FA9CE8A94867C789567A2588BA0D91F2DAEE9D079A53A11EE37 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/YcWh7A_OSmqXcFm1vWw3Fw/zh-cn_image_0000002492503660.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=A99CE5F1185B917E048D075912615477D21EAE08AD052964CD2EF9C9D9076D99 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/sWoo2ZM7Qr-eE74s9KetOw/zh-cn_image_0000002524623361.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=2383D2FF79E080B6B06F2AA5ABF61039B9708BB5FB1533EC0AE70A0BDD676908 "点击放大")

**功耗测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/wp4IEiNVTHOnrHR2TPuKVA/zh-cn_image_0000002492503682.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=1A681B6CDBA73ED3FDD4ADA0BABB42CE2D41871D263CE9FE99801AB6388D004E "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Emm8Xi9vRV6QIadNTbPUsA/zh-cn_image_0000002524503395.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=F872B488439BEE2EC729C6D1B9B6374C6D58CE39083556DFA77BEC310C4572B4 "点击放大")

**性能测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/aRX0jMpJTuWKSc1jloXoSA/zh-cn_image_0000002524503417.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=EACAB9DF9E1E92A4FED9BD768DE72FFC0B96F0A62EB75DC71453361CAF369BC5 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/yWkjNI00R7ehBV-79pTLfQ/zh-cn_image_0000002524623369.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=04A2804607007596D3E2EE8013C4485840A2F808F2DF7C62C3FE181F21BFAE80 "点击放大")

**UX测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/SgMMErm6Tvy_IyA3Y_JZcw/zh-cn_image_0000002492343690.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=D9D03BE8BE4619EE57D0150E8581DAC56718F7A5B1CEC42EB3F5B70A88F6E9EF "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fV8S2xj9Tg6nA0B4bbcq3g/zh-cn_image_0000002524503389.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=1F97FFD59CED1607ECA43D5DDE0FA9825646CD7B1B63E978A7DCB38A72FD98D1 "点击放大")

**稳定性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/6Hs7YdjCSdqmPyyLXNpo_Q/zh-cn_image_0000002524623367.png?HW-CC-KV=V1&HW-CC-Date=20260427T235754Z&HW-CC-Expire=86400&HW-CC-Sign=DC03230138B4CA966EECC15F3CFE05FA820C257A2BA708867132748575334B9D "点击放大")

说明

更多测试服务详情，请前往DevEco Testing客户端->上架预检->应用上架预检（本地）->任务创建页->测试指南中查询。
