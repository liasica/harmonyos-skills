---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo
title: ohpm-repo export_userinfo
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo export_userinfo
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:abe9bb458febbf891ca83c748de2ea8575bcd31b54ca6620278c35e3ad415341
---

导出用户的DB数据。

## 命令格式

```screen
ohpm-repo export_userinfo
```

## 功能描述

在当前工作目录导出export\_userInfo\_xxx.zip文件，该文件记录了DB数据，包含加密组件和以下10张数据表。

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

```screen
ohpm-repo export_userinfo
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/1Iy23l7tRG-2tAxVyaQoLQ/zh-cn_image_0000002731541409.png "点击放大")

```screen
PS D:\> ohpm-repo export_userinfo
[2025-08-09T19:14:16.721] [INFO] default - initialize "file database" successfully.
[2025-08-09T19:14:16.724] [INFO] default - export the "user" table done.
[2025-08-09T19:14:16.726] [INFO] default - export the "group_member" table done.
[2025-08-09T19:14:16.728] [INFO] default - export the "access_token" table done.
[2025-08-09T19:14:16.728] [INFO] default - export the "public_key" table done.
[2025-08-09T19:14:16.730] [INFO] default - export the "repo" table done.
[2025-08-09T19:14:16.730] [INFO] default - export the "repo_permission" table done.
[2025-08-09T19:14:16.731] [INFO] default - export the "uplink" table done.
[2025-08-09T19:14:16.732] [INFO] default - export the "uplink_proxy" table done.
[2025-08-09T19:14:16.733] [INFO] default - export the "validation_config" table done.
[2025-08-09T19:14:16.734] [INFO] default - export the "system_security" table done.
[2025-08-09T19:14:16.761] [INFO] default - userinfo exported completed, save the .zip file to : "D:\export_userInfo_1754738056722.zip".
```

```screen
export_userInfo_1754738056722.zip文件结构

|   access_token.json
|   group_member.json
|   public_key.json
|   repo.json
|   repo_permission.json
|   system_security.json
|   uplink.json
|   uplink_proxy.json
|   user.json
|   validation_config.json
\---meta
    |   version.txt
    +---ac
    +---ce
    \---fd
```
