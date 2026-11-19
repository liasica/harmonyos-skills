---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:28+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:1e26d8493afb96cd5af2cf2b5a9442940f6d30ad796f6aad5033805c9e6604d2
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ntgkY5xSRnenCTEN6yMHgw/zh-cn_image_0000002820405841.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAE0E231C976409E76075C7F058A6E247B4A63946D30F69A818E93AFA2D395B6)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/HKxXrS5IRcuGuLUFzKjVCA/zh-cn_image_0000002791725862.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CEFE1950003B78F4D1CD479B874EC7C6DCCB1B89B95C59DB0631EBE80F7C41A)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q6qBNcJpR7uHDPUZpAJaQA/zh-cn_image_0000002791565890.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F8C11574E2F46CABE6646EFA220D60C4C36CF6290FC30F3898BCAAF6FCC0E1D)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```bash
  param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/zEXKKQDrSMu9lenb_XpMEQ/zh-cn_image_0000002820525843.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=53C82F920EB27B8448FADFE486719CB7AA51733D8C82EEB087A2E1BC365E6A9C)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```bash
  param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/pRVX9BF2SBCbL2kt1pK3mw/zh-cn_image_0000002820405843.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE36806DAE190E908585F5E108ED1CB98ADBD41E22313B17A6743DE75F99A3E2)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```bash
  param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/AyHIsL6RQByr9rOcnkhejg/zh-cn_image_0000002791725864.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F33CB471AC373230D83197CDD0FE2C3DEACFD5F4A10474BCC667651C30A94D1)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```bash
  param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/i4kxstRKSM2PicDklsNV7Q/zh-cn_image_0000002791565892.png?HW-CC-KV=V1&HW-CC-Date=20261119T014828Z&HW-CC-Expire=31536000000&HW-CC-Sign=28E852C6D38F903585387F7C1E7178CF5C8FD866F3EA66501FFAA51F7BE53507)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
