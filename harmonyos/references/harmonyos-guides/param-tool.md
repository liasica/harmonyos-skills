---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c1100e79be93c1692aa7728cbca78cc0fcb26a0fcc10a3db15de7f50dca3a37a
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Jeex3UgZSVGjS3qJloNQvQ/zh-cn_image_0000002558605366.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=931A31D735145A3CF089175E08114B0C279011979EDF4FD0CDE28FE62E95D305)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/pIZcCG3cSDOrvn1mVQ_fdw/zh-cn_image_0000002589324893.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=B9FB4DCB56C2AEB6BAC1CD7B10FC5B84ECEAA8769762046AF55648681CD65D2F)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/fbWkgSr2TjmP9HKaq-2yJA/zh-cn_image_0000002589244829.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=9C7B074AAD8867709E8EBCB3EC335EDAF60ED6E9D654B195C16B395181B04C84)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```
  1. param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Eu8AgwhQTOC_KFD6ywSlpA/zh-cn_image_0000002558765024.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=A7953AF4F3ACC697A32E7CCDF7751AB541628F85419E605F04F7744A55D3ACCB)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```
  1. param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/eybH7lSCT3GRxIdWj2A4wg/zh-cn_image_0000002558605368.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=8C377BB1D6307D367EAF3E485F1699F3CA0A59419442B63736F3F81ECFD4E6CD)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```
  1. param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/iaZLT2gkTrSfyolL2JFErA/zh-cn_image_0000002589324895.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=32E7738D655B4937170D35D8BF5555C1D8AC7A616AA22A6A5C146F22AE4706A0)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```
  1. param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/9yLnyUM1SluqvQiXMMVLDA/zh-cn_image_0000002589244831.png?HW-CC-KV=V1&HW-CC-Date=20260429T053419Z&HW-CC-Expire=86400&HW-CC-Sign=F812A913423331FACA62B429B766D6D8065EFFE753142AB1668089A018D23143)
