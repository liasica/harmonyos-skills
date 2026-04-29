---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo
title: ohpm-repo export_userinfo
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo export_userinfo
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:42+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3e234a8b6010e50400a44a846c8bfe820c032f709a10cf83a06f875ec3516f91
---

导出用户必要的DB数据。

## 命令格式

```
1. ohpm-repo export_userinfo
```

## 功能描述

在当前的工作目录导出记录了DB数据的export\_userInfo\_xxx.zip文件，其中包含加密组件和下面的10张数据表。

* user
* group\_member
* public\_key
* access\_token
* uplink
* uplink\_proxy
* repo
* repo\_permission
* validation\_config
* system\_security

## 示例

执行以下命令：

```
1. ohpm-repo export_userinfo
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/8_TJEKsrSzWnpc_P3NfbKw/zh-cn_image_0000002530751298.png?HW-CC-KV=V1&HW-CC-Date=20260429T054441Z&HW-CC-Expire=86400&HW-CC-Sign=91584D4F42EE82E606568B535A401DC968A5FC2C022564F9A2D321E94B8B0984)

```
1. PS D:\> ohpm-repo export_userinfo
2. [2025-08-09T19:14:16.721] [INFO] default - initialize "file database" successfully.
3. [2025-08-09T19:14:16.724] [INFO] default - export the "user" table done.
4. [2025-08-09T19:14:16.726] [INFO] default - export the "group_member" table done.
5. [2025-08-09T19:14:16.728] [INFO] default - export the "access_token" table done.
6. [2025-08-09T19:14:16.728] [INFO] default - export the "public_key" table done.
7. [2025-08-09T19:14:16.730] [INFO] default - export the "repo" table done.
8. [2025-08-09T19:14:16.730] [INFO] default - export the "repo_permission" table done.
9. [2025-08-09T19:14:16.731] [INFO] default - export the "uplink" table done.
10. [2025-08-09T19:14:16.732] [INFO] default - export the "uplink_proxy" table done.
11. [2025-08-09T19:14:16.733] [INFO] default - export the "validation_config" table done.
12. [2025-08-09T19:14:16.734] [INFO] default - export the "system_security" table done.
13. [2025-08-09T19:14:16.761] [INFO] default - userinfo exported completed, save the .zip file to : "D:\export_userInfo_1754738056722.zip".
```

```
1. export_userInfo_1754738056722.zip文件结构

3. |   access_token.json
4. |   group_member.json
5. |   public_key.json
6. |   repo.json
7. |   repo_permission.json
8. |   system_security.json
9. |   uplink.json
10. |   uplink_proxy.json
11. |   user.json
12. |   validation_config.json
13. \---meta
14. |   version.txt
15. +---ac
16. +---ce
17. \---fd
```
