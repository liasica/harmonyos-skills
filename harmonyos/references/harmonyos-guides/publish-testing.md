---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/publish-testing
title: 上架预检
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 上架预检
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:4e00157a01dd32dfcbb39ce3e81ea371dcfb60efd899eb3e9a519c7afa1c3612
---

## 应用上架预检（本地）

**应用上架预检（本地）：**基于鸿蒙应用上架质量标准构建的一键式自动化测试服务，提供兼容性、性能、稳定性、UX、功耗专项基础质量的专业检测报告，帮助用户识别应用的基础质量问题。

**创建任务**

步骤1：打开DevEco Testing客户端，左边菜单栏选择“测试服务”找到“上架预检”，点击“应用上架预检（本地）”卡片，进入任务创建界面。

步骤2**：**进入任务创建界面后，配置任务参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/j6tx_onKTt-5c8DLAAagSA/zh-cn_image_0000002663932313.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=D23CF5DD4950106541FB6BF151FE22524F8C6BC978D6B2373821415A31BF3F4D)

* 任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
* 备注信息：填写任务备注信息，便于快速筛选报告。
* 测试设备：选择待测设备，最多可选择3台相同类型的设备并发执行，提高测试效率；支持 HarmonyOS 5.0及以上版本。

**说明** 

任务模式分为“自定义预检”与“综合预检”。“自定义预检”可自定义选择执行的专项及参数；“综合预检”执行全部专项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ynEtFvnARfyL8ACe73alDg/zh-cn_image_0000002663932311.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=71B81BCCBD68ED90D9602890A10BE8E78EB1C50D3F8416F78D980C57AA1BBE87 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/o-Z7d_3FQGeiuDl4kMdb8Q/zh-cn_image_0000002664012369.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=132A29044F29DA9077C604AA7544C72010A8816ACE5E5FE4A59B8BB250A88C74 "点击放大")

**综合预检**

* 应用包名：选择设备中已安装的应用包名。
* 应用类型：选择应用所属的分类。
* 选择应用包：选择与待测应用相同的应用包文件用于测试静态检查项，可选.hap、.zip文件。

步骤3**：**配置完成后，点击创建任务按钮开始测试。

**测试执行**

创建任务后，将会跳转到执行页，执行测试环境初始化操作。初始化完成后，开始检测应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/i237dz7VTv2IS2NM8eqS5Q/zh-cn_image_0000002633533234.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDDFE783353B777D29D5C1F7A89EF0386B8EA0BF9F5F0B6EA2CD84B539D81E0C "点击放大")

测试页面支持查看各测试项以及测试状态。每个测试完成后，点击查看按钮可以查看各测试项详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/VCZqvY4ZQ7y4ab-R8oYgsA/zh-cn_image_0000002633533236.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=23A29A0CD04715D8A3BF79B7A3ED1CF3945B24FBB7E304E2ED3FEB077363A816 "点击放大")

**测试报告**

测试报告：任务信息包含：任务名称、任务类型、测试时间等。点击打开目录按钮可导出报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3kzbVSVRRU6LYURja8AlIA/zh-cn_image_0000002664012361.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C068FC2E5D166C0E440D9E09B4BCAF0782798516DF87DB688E0C44ACBC766FB "点击放大")

应用信息：包含应用名称、版本等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/UbsAlMMOT7WzCALLdKWc6g/zh-cn_image_0000002633693146.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=932CF7C991FCCE82F71D9AC7819BF0DEBF3131EDE5BBE71840212613A5D9DBFC "点击放大")

测试总览：专项测试的基础质量满足度与总体测试结论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/vjYTsqH5RJG6frd-wT4ZfQ/zh-cn_image_0000002633693152.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECCCF67941A22D7B2DA537EB718C9D58B199D6EFA5B41C034EFE58CF632D2F25 "点击放大")

测试详情：专项测试结果详情。

**兼容性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8HI2dLFxScOjSyJsyaTRHw/zh-cn_image_0000002664012365.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C5EDCC6C505317B2590A088992C36EEE06D3E77075CF20EBC3C63EA5DDEA17B "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/PyVqQoO_S9GKwLrwOtHR2A/zh-cn_image_0000002633693144.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=59DC0FE74C917AF80E21CF0748E27AF5EFCEBF363DF2270540A9B29A04B8BE11 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/KDHRc6o5RG-Yejj6uTw8FQ/zh-cn_image_0000002663932309.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DDE0F90FCECC538536927CFD5892F2A17D447393A134F2F1AB49AB5CB1F8700 "点击放大")

**功耗测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/G4ZKO1jrT0uuUhrNuii-Ig/zh-cn_image_0000002664012367.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=318E6081605118DBC15A0E92974E53206ADCD50573CAE982F70A8C796A72FD4D "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/vtizDevfRA6pay0vxI3HXA/zh-cn_image_0000002633533228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=361C6BA29D3168CD0A6C4F06F3FE8FCFB77188A931C77C462F8CF157C70FB359 "点击放大")

**性能测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/WfqFW2BSRNWzsIL7touslA/zh-cn_image_0000002633533232.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=C302BB2201113786DA574198C4704425FF889D445D2ECB3B83683C9DBB163970 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Al9agZnrTxmuW2wiyOHjrw/zh-cn_image_0000002633693142.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=799F6BD7EC7AB4A118017158FB23DB394DDF14F9E00F99E6EB5CD0ACDA1B7648 "点击放大")

**UX测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5llPPsErQeyfasgSFCVg_A/zh-cn_image_0000002664012363.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F845FE985DAE3FB38097515DE578D0DAC8716973A029AF5D012AB586303C53D "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ORygYx_dRAq5t7TRqWHN5w/zh-cn_image_0000002663932307.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=58E0735B79E2E0FD8BFAB8E717683385BDD8B8A8CFB03E47AF4825E3E3DD901A "点击放大")

**稳定性测试：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/FJ9YFfWDT7ukIBp53KvTsQ/zh-cn_image_0000002633693148.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7ED54865894D0C696FE964832F57193EE0E6AAF2187E342821004590BEC4BD7 "点击放大")

**说明** 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->上架预检->应用上架预检（本地）->任务创建页->测试指南中查询。
