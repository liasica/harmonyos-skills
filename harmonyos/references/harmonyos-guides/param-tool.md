---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:49+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:fefe10ac37f04c998e3e27de920849c95e3bf526b92e954da52f5e57aebc0a99
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

  ```bash
  param -h
  ```

## 获取系统参数信息

* 显示匹配name的系统参数信息，命令格式如下：

  ```bash
  param ls [-r] [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/kVePYLXSSE6A76OPz8R0SA/zh-cn_image_0000002788307560.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A583726659AFA98FC9099E7912D55B07591A868EEBAB083B6C1CEB48C3F4E7D)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/eOP2eFPfTPeFOBF5z_IQMQ/zh-cn_image_0000002817426923.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=48213A7811B2088182492FD04D11475B3F9B641A1131C46035B80F66E29D7885)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/n4B6eQ9EQ3CFBtpDx6sr3Q/zh-cn_image_0000002788467504.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=68B945B7FC4CB044861CCBD270437108A4279EA8A4C09319318EE3348AD8A2EF)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```bash
  param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/VVTnimdJRl6TI4StM4owxw/zh-cn_image_0000002817506993.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DBADB0D7DDBC27C09ABC8EAB21AC8FEDA480B0F08A6398093F413FCAB5C4571)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```bash
  param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/7MPsAz8gQnWNixfCD8WDtQ/zh-cn_image_0000002788307562.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC7BBF02EAB885A0F077A94BBB1B5D83715E4047A4A1E36C05360EED14803BFC)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```bash
  param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/gdO_0x1TSLa4HEfnTuzwoQ/zh-cn_image_0000002817426925.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BEF64E98B5C8AA39026BF5515ED46060DD16178BD88C4D3A402E9EF5EDE6A2E)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```bash
  param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/0xQOquJqRw-Q47JP4oQkqw/zh-cn_image_0000002788467506.png?HW-CC-KV=V1&HW-CC-Date=20261114T004749Z&HW-CC-Expire=31536000000&HW-CC-Sign=008A92073A99968609CA5D66DC0BD759EF0F256985FFA9842B47A92A290D1FA2)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
