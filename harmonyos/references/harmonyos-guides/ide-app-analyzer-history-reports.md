---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-history-reports
title: 管理体检报告
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 管理体检报告
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee1b427864bc576d3ebe8944f78e7797c3fbf99566d5c6008be9cdecf442a23d
---

AppAnalyzer支持查看、导出、导入体检报告，具体如下。

## 查看报告

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**体检历史**按钮，可查看最近15次的体检报告卡片，点击卡片可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/cBHvw9qaTGSLhmLUo8V_5Q/zh-cn_image_0000002530753246.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=002A30D489A6787D938B680E69B638C310A478725BA88E4C9745B92131A075BA)

### DevEco Studio 6.0.1 Beta1以下版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**历史记录**按钮，可查看最近15次的体检报告记录，点击时间戳可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/qr0p6uCoT62wT61CdgkusQ/zh-cn_image_0000002561753185.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=E2EF1E246F732DE6187CE4F481A7E525C26C82581CE73702E109E655088A6692)

## 导出报告

从DevEco Studio 6.1.0 Release版本开始，AppAnalyzer支持导出体检报告，以实现报告的共享。使用该功能，需要满足以下条件。

* 支持导出场景化体检、规则体检、上架前体检这三种体检方式的报告。
* 历史版本生成的体检报告不支持导出，仅DevEco Studio 6.1.0 Release及以上版本生成的体检报告才支持导出。

操作步骤如下：

1. 点击AppAnalyzer底部的**体检历史**按钮，选择符合条件的报告卡片进入报告页面，点击右上角的**导出报告**按钮，选择需要保存的路径，点击**确定**后，等待报告导出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/0RPryDRFQIeo085HSrF8AQ/zh-cn_image_0000002561753183.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=B7AF8B872CAB16ABDD58EEA0B47C754734DB1E8717B5E4F2D85E1DBDA9A98AE4)
2. 报告导出成功后，在DevEco Studio右下角会弹框提示，点击**查看报告**可打开报告保存的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/stKUX-HyQY2sYBrWHifucA/zh-cn_image_0000002530913242.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=C6407E9DDF32D28B04C8918556177E7E61E47E3633029DF8555A768C189BA702)

## 导入报告

从DevEco Studio 6.1.0 Release版本开始，如需查看他人的体检报告，可使用导入报告功能，需要满足以下条件。

* 支持导入场景化体检、规则体检、上架前体检这三种体检方式的报告。如需导入DevEco Testing的报告，请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 导入报告使用的DevEco Studio版本，要求不低于导出报告时使用的版本，仅校验版本号前两位，例如6.1.x.x导出的报告，可以在6.1.x.x及以上版本中导入。

操作步骤如下：

1. 点击AppAnalyzer底部的**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/hLrUTx_wR3mg62sp2VNaSg/zh-cn_image_0000002561833161.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=7E9913A2329E352157B211A33700EAF395AFF772BD8BF60FCD424ABED501C4CD)
2. 选择本地的体检报告zip文件，点击**确定**后，等待报告导入。导入成功后，AppAnalyzer会自动打开报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/quwDCp45Qi2fIu1IJqhTFg/zh-cn_image_0000002561833169.png?HW-CC-KV=V1&HW-CC-Date=20260427T235702Z&HW-CC-Expire=86400&HW-CC-Sign=5DD584D32E1BAFC0DF819E2E9CBB1527AA1F9053631D91AA557D0020E44809BC)
