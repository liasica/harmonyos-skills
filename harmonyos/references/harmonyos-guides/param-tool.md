---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-10-22T07:05:22+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:31e79a161a64f1fff6d7b054a3750fc90afd63bfe5e4eab01897604dc830c67b
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zYvCS2rJQ1yz8pBdKppUoA/zh-cn_image_0000002797180917.png)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Mx5RnFQUQT2MpiCHXwz09A/zh-cn_image_0000002768020940.png)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/R4DHLr_iRpywioMIlsbqwQ/zh-cn_image_0000002797300887.png)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```bash
  param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/KVW4hJIERTmcIgpE4uVESw/zh-cn_image_0000002767860956.png)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```bash
  param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/UOboPqkbRJG5RSmdJvxoGg/zh-cn_image_0000002797180919.png)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```bash
  param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/1y-qv_ooSEKf3zd7myi8jg/zh-cn_image_0000002768020942.png)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```bash
  param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/a5EtNh2vSs6c92AEPV9kNQ/zh-cn_image_0000002797300889.png)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
