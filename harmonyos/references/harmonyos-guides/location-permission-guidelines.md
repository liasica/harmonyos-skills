---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-permission-guidelines
title: 申请位置权限开发指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请位置权限开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8151f3ee625484c472b96cf0ca990f01acf0b99c984b2c87a291f71d5b9e072f
---

## 场景概述

应用在使用Location Kit系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限。

系统提供的定位权限有：

* ohos.permission.LOCATION：用于获取精准位置，精准度在米级别。
* ohos.permission.APPROXIMATELY\_LOCATION：用于获取模糊位置，精确度为5公里。
* ohos.permission.LOCATION\_IN\_BACKGROUND：用于应用切换到后台仍然需要获取定位信息的场景。

Location Kit接口对权限的要求参见API参考：[@ohos.geoLocationManager (位置服务)](../harmonyos-references/js-apis-geolocationmanager.md)。

## 开发步骤

1. 开发者可以在应用配置文件中声明所需要的权限并向用户申请授权，具体可参考[向用户申请授权](request-user-authorization.md)。
2. 当APP运行在前台，且访问设备位置信息时，申请位置权限的方式如下：

| 申请位置权限的方式 | 是否允许申请 | 申请成功后获取的位置的精确度 |
| --- | --- | --- |
| 申请ohos.permission.APPROXIMATELY\_LOCATION | 是 | 获取到模糊位置，精确度为5公里。 |
| 同时申请ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION | 是 | 获取到精准位置，精准度在米级别。 |

1. 当APP运行在后台时，申请位置权限的方式如下：

如果应用在后台运行时也需要访问设备位置，除了按照步骤2申请权限外，还需要申请LOCATION类型的长时任务。

长时任务申请可参考：[长时任务介绍](continuous-task.md)。

## 示例代码

* [位置信息](https://gitcode.com/harmonyos_samples/location-service)
