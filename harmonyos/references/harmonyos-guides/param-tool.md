---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:76e2fd9654e292c8e953cb55b0fe70c7a427e22530e0bfb960ebaffb7f3cc222
---

param是为开发人员提供用于操作系统参数的工具，该工具只支持标准系统。

## 环境要求

* 获取hdc工具，执行hdc shell。
* 正常连接设备。

## param工具命令列表

| 选项 | 说明 |
| --- | --- |
| -h | 获取param支持的命令。 |
| ls [-r] [name] | 显示匹配name的系统参数信息。带"-r"则根据参数权限获取信息，不带"-r"则直接获取参数信息。 |
| get [name] | 获取指定name系统参数的值；若不指定任何name，则返回所有系统参数。 |
| set name value | 设置指定name系统参数的值为value。 |
| wait name [value] [timeout] | 同步等待指定name系统参数与指定值value匹配。value支持模糊匹配，如"\*"表示任何值，"val\*"表示只匹配前三个val字符。timeout为等待时间（单位：s），不设置则默认为30s。 |
| save | 保存persist参数到工作空间。 |

## 获取param支持的命令

* 获取param支持的命令，命令格式如下：

  ```
  1. param -h
  ```

## 获取系统参数信息

* 显示匹配name的系统参数信息，命令格式如下：

  ```
  1. param ls [-r] [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/kBe-XraDRDeZWX8gwabC_A/zh-cn_image_0000002583478523.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=4CA8959FE2985CFD62CCE90F3657AF0DCDD3230395FF8831024FD264F8E69AF5)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/n9bidQu3QQaAdbJYFzATTw/zh-cn_image_0000002552798874.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=213750BE882FB6D7ABD68EA243FC29C37C776488AEFEBDC19A6E12B673EECC89)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/6duhSP9tR2KphtptFj5KOQ/zh-cn_image_0000002583438569.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=E1B52812C4D256E780EF15A6F167E56C25D0D0C1231605FCFBCFBFA4074B91FE)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```
  1. param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/L3qrdlkSTSmQ9E6axCbo7A/zh-cn_image_0000002552958524.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=DE450A21752167D32C3D226B44E91948FBE4F0D66B5CA939F69F07F0B7EB7A86)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```
  1. param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/2PSFnQSTTwCdQeZ8soznIQ/zh-cn_image_0000002583478525.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=83C1182DB578002D4A8AD12719AE209B3DBFC07D87C6CF3391133CB4E986D143)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```
  1. param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/9UYrrKF7SxC5Rop5v_9t4g/zh-cn_image_0000002552798876.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=27F04A68019F113736D8BECC5B87D8FBE852704A8038BD0EA02255FC52D3FD36)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```
  1. param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/xlTsOhk0RcS68r7UxxlCTg/zh-cn_image_0000002583438571.png?HW-CC-KV=V1&HW-CC-Date=20260427T234525Z&HW-CC-Expire=86400&HW-CC-Sign=EBCE5C18E46DA61391F50C9FD953723B869B65C68AC8EC975B2180D8E8EE8102)
