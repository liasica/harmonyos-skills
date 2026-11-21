---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:54+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:ff806868ed9cf54f532283566958df3186a28bcbcf80359ded04c3d245dd53ac
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/QDRoQrL5Q-mxMDuYndtuAw/zh-cn_image_0000002792877542.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8F76A12C5C4297D98F7B3CAA38AB3366E59B7A429BA9421E774DEB85025123D)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/w7aIudORS_2RgWzAojIGgA/zh-cn_image_0000002821837449.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=591AC345E33480806162341A0862E9F3285B97EA409076F9F54AC06C56EAC5B5)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/KlVtYDYORnWnoVv4EieSRA/zh-cn_image_0000002821757451.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=B99F4F5A120920C917CB73CAAF9F8CEB29AFA87B9811C5944ECF13BFDB48E866)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```bash
  param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/HCM38LCVQbuDVNG5n6ScTw/zh-cn_image_0000002793037514.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=15D9DD8762E171C9582AC09AB2148D60C8840071C49EAD3D2D5215C83D42A9E8)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```bash
  param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/bC9pM_3PQ1ux3lPDDs8N0A/zh-cn_image_0000002792877544.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D93710E308D053EEB655B11EBC6DF53B9CF8D9F8B84A9D5C3FE61468DF51760)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```bash
  param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/i9o7SX9oSsS2o5QFUrfVcg/zh-cn_image_0000002821837451.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E3E2F23E8B637D7108A7573C4F5967EE074D0F6973F7F91D3E6122EF6D7577F)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```bash
  param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/uJjjkhkYSmKh8vetNzySjw/zh-cn_image_0000002821757453.png?HW-CC-KV=V1&HW-CC-Date=20261121T011027Z&HW-CC-Expire=31536000000&HW-CC-Sign=47075A54C41D207C452E0A77F6EA68A817F81256355964597544BE6EA542A085)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
