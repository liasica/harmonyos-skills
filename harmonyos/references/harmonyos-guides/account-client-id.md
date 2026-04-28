---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46f5583d85cf25a8b780164e70cc0837c63e263b81bfae04d05a0c5078b9f53e
---

## 获取Client ID和APP ID

在 AppGallery Connect（简称AGC）的[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中，选择对应的项目和对应的应用，在“常规 > 应用 ”下，找到**应用**的Client ID和APP ID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/cy93AM6gSd2Ili6VYzhveA/zh-cn_image_0000002552799096.png?HW-CC-KV=V1&HW-CC-Date=20260427T234756Z&HW-CC-Expire=86400&HW-CC-Sign=01A109EE155897862E757FB52ABFFB81CEC8367A075920EE093B716C33D606E3)

## 确认是否需要配置Client ID

如果上一步获取到的Client ID和APP ID相同，则无需配置Client ID，否则需要按下一步配置Client ID。

## 配置Client ID

在工程中**entry**模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

说明

1.若工程中存在多个模块，需要在"type"为"entry"模块中的module.json5文件配置应用的Client ID。

2.请确认获取的Client ID是**应用**Client ID，错配成项目Client ID将导致接口调用报错。

```
1. "module": {
2. "name": "<name>",
3. "type": "entry",
4. "description": "<description>",
5. "mainElement": "<mainElement>",
6. "deviceTypes": [],
7. "pages": "<pages>",
8. "abilities": [],
9. "metadata": [ // 配置信息如下
10. {
11. "name": "client_id",
12. "value": "xxxxx" // 将上一步获取到的Client ID赋值给value，请注意不要使用其他方式设置value值
13. }
14. ]
15. }
```
