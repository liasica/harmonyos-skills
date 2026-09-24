---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-enable-storage
title: 开通云存储服务
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 开发准备 > 开通云存储服务
category: harmonyos-guides
scraped_at: 2026-09-25T07:07:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2ccbe250e7cd8e795a710ddac9a21517732311ee675bffb4207901f104b1234
---

首次使用云存储服务前，需要先开通此服务。如果已经开通，可跳过本步骤。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要开通云存储的项目。
3. 选择“云开发（Serverless） > 云存储”，进入云存储页面，点击“立即开通”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/_SjohJRwSiK_fRrqFaOO0A/zh-cn_image_0000002743379736.png)
4. 在引导界面输入存储实例名称并设置默认数据处理位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/bVmoceXQTmyuY8VzH3OkEA/zh-cn_image_0000002743219850.png)

   | 参数 | 说明 |
   | --- | --- |
   | 存储实例 | 存储实例名称必须符合以下条件：  - 只能包含英文小写字母、数字、中划线（-）。  - 只能以数字或字母开头和结尾。  - 要求不少于3个字符，并且不能超过57个字符。  - 不能为IP地址。  - 不能包含连续两个及以上中划线（-）。  - 名称全局唯一，创建后，不能修改。 |
   | 默认数据处理位置 | 云存储支持启用多个数据处理位置，具体请参见[设置数据处理位置](../app/agc-help-data-location-0000002277923065.md#section154810363471)。如当前项目已设置数据处理位置，则此处无需再设置。 |
5. 点击“下一步”，进入默认安全策略展示界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/FoZuk156TMCrwiQjBD-MzQ/zh-cn_image_0000002772739103.png)

   **说明** 

   默认安全策略将允许经过身份验证的用户执行所有读写操作，开通服务时无法修改安全策略。服务开通后，开发者可制定更合适的安全策略来保护其用户数据。关于如何修改安全策略，请参见[安全规则](../AppGallery-connect-Guides/agc-cloudstorage-securityrules-overview-0000001054966859.md)。
6. 点击“完成”，开通云存储成功。

   服务开通成功后，AGC将为开发者创建一个默认存储实例，默认存储实例的名称即为步骤4中配置的存储实例名称+“-五位随机数字字母”的组合，如“bucket001-2wezr”。
7. 如果开发者已启用多个数据处理位置，当需要在不同的数据处理位置管理云存储时，可在云存储页面选择“数据处理位置”下拉选项进行切换。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/bo3AwBOsStmYtya-mhUPqg/zh-cn_image_0000002772898987.png)
