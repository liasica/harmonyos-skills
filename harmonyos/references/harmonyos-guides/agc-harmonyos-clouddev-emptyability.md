---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-emptyability
title: 通用云开发模板
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 附录：云开发工程模板 > 通用云开发模板
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:06+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:86abab565ef496907451afd7506ea8c8d6c246be7d922d685d2eb116bf33af19
---

## 适用范围

|  |  |
| --- | --- |
| 模板名称 | 通用云开发模板（[CloudDev]Empty Ability） |
| 模板说明 | DevEco Studio内预置的端云一体化开发模板。当前使用Cloud Foundation Kit（云开发服务，包括云函数、云数据库和云存储）搭建了基础的演示项目，不含业务属性。您可参考模板学习如何进行基础的端云工程开发，后续开发时可删除预置的页面代码。 |
| 支持的应用类型 | * HarmonyOS应用 * 元服务 |

## 效果图

以下为通用云开发模板主要功能模块的效果图。

| 功能模块 | 效果图 | 功能说明 |
| --- | --- | --- |
| 云函数 |  | 点击“Generate Global Unique ID”时，调用云函数SDK执行部署在AGC云端的云对象“id-generator”，生成UUID。 |
| 云数据库 |  | 点击“New”创建数据，可在AGC云端查看到创建的数据。 |
| 云存储 |  | 点击“Upload Image”上传本地图片，成功后可获取图片链接。 |

## 体验模板

如您希望在设备上亲自体验该模板的功能和页面效果，可按如下流程操作：

1. [使用模板创建端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)。
2. [将云侧工程一键部署至AGC云端](agc-harmonyos-clouddev-deploy.md)。
3. 配置云存储安全策略。

   由于端云一体化开发工程的初始化代码未[配置AccessToken](../harmonyos-references/cloudfoundation-cloudcommon.md#getaccesstoken)，因此您还需配置云存储的安全策略为始终可读写，否则会导致云存储无法上传文件。具体操作如下：

   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
   2. 在项目列表中点击您的项目。
   3. 在左侧导航栏选择“云开发（Serverless） > 云存储”，进入云存储页面。
   4. 选择“安全”页签，在“配置策略”页面修改默认安全策略为始终可读写后，点击“发布”。

      ```
      1. agc.cloud.storage[
      2. match: /{bucket}/{path=**} {
      3. allow read, write: if true;
      4. }
      5. ]
      ```

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/iyj7C-pcTDaxPomMZPXBvg/zh-cn_image_0000002492564672.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=B6EBA9DD68E883FCBB3FC78155485ED2008F5EA55448E0A993AC3B403ECAFAA7)
4. 将模板工程推包到手机上，在手机上开通应用访问数据权限，即可开始体验模板。

   注意

   当前自动签名仅支持“[关联注册应用进行签名](ide-signing.md#section20943184413328)”方式。

   如使用模拟器体验，请参考[使用模拟器调试](cloudfoundation-emulator.md)操作。
