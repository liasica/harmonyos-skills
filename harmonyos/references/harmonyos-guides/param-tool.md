---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:d1eaa08f631ad63fd1881bc5d7740f4a1e6024fb3b4b7118a504420fad55bdf7
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/bY2MIg_XRBaKEfQedlgyAg/zh-cn_image_0000002786519756.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DF774B14CEC203A66C158EFD1456BAC7D6DDD68EBC53F754D0CFA73321DB430)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/lPaKp2U0R9SX6CGjHtTHKQ/zh-cn_image_0000002786359828.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=693AAD55942A138235E5CB6D5AA5E066432521570638E8BBF2CFAE814898E77F)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/00pgIr8iRDSUFcn0BrJ_tQ/zh-cn_image_0000002815559249.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=D402F7331E97048A54CF22103D7EE40A29AF94795894FB2CF078B45F409065C5)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```bash
  param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/pE5bqosZRf2gTHJ2_hKqHQ/zh-cn_image_0000002815399333.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D63285F8E2358E792FD79040D2A8AE45014C5287BAEC1F92F96EB23F4C6E1B2)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```bash
  param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/lJ32E2kGQL-ZVs3AuqYCQA/zh-cn_image_0000002786519758.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=25601B9D1ABF27BEEE9C84F918CB8106E9FBE193E4B9D720B8A30A64630C4C8D)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```bash
  param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/GiFkAq7ITXCtlEWj977E1A/zh-cn_image_0000002786359830.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A5BCFF6A44CECA962165A8E4BCF486DA93AC63BF085D258BA0FDFE78CEB81FD)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```bash
  param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/2W2325UrTxq56Y-gkeCdBw/zh-cn_image_0000002815559251.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DBE101B9644B3039C32EDEF0A2E016D0FC621C656641D5C8CF379615CC02725)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
