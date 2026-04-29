---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-configuration
title: DataAbility组件配置
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > DataAbility组件配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28842bb714c5551992d7dd7ec2d1336921efdc94f8eaee86fd87c30badb469c2
---

## URI介绍

DataAbility的提供方和使用方都通过URI（Uniform Resource Identifier）来标识一个具体的数据，例如数据库中的某个表或磁盘上的某个文件。此处的URI仍基于URI通用标准，格式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/DyaI41ziSFeltBx8ZgwXvg/zh-cn_image_0000002558764004.png?HW-CC-KV=V1&HW-CC-Date=20260429T052602Z&HW-CC-Expire=86400&HW-CC-Sign=99153F88A658945567AD56554731381FF301E70FD49D0080FFBF6D318E77FF72)

* scheme：协议方案名，固定为"dataability"，代表Data Ability所使用的协议类型。
* authority：设备ID。如果为跨设备场景，则为目标设备的ID；如果为本地设备场景，则不需要填写。
* path：资源的路径信息，代表特定资源的位置信息。
* query：查询参数。
* fragment：可以用于指示要访问的子资源。

URI示例：

* 跨设备场景：dataability://device\_id/com.domainname.dataability.persondata/person/10
* 本地设备：dataability:///com.domainname.dataability.persondata/person/1

说明

本地设备的"device\_id"字段为空，因此在"dataability:"后面有三个"/"。

## 部分配置项介绍

与PageAbility类似，DataAbility的相关配置在config.json配置文件的"module"对象的"abilities"对象中，与PageAbility的区别在于"type"属性及"uri"属性。

**表1** DataAbility的部分配置项说明

| Json重要字段 | 备注说明 |
| --- | --- |
| "name" | Ability名称。 |
| "type" | UIAbility类型，DataAbility的类型为"data"。 |
| "uri" | 通信使用的URI。 |
| "visible" | 对其他应用是否可见，设置为true时，DataAbility才能与其他应用进行通信传输数据。 |

config.json配置样例

```
1. "abilities": [
2. ...
3. {
4. "name": ".DataAbility",
5. "srcLanguage": "ets",
6. "srcPath": "DataAbility",
7. "icon": "$media:icon",
8. "description": "$string:DataAbility_desc",
9. "type": "data",
10. "visible": true,
11. "uri": "dataability://com.samples.famodelabilitydevelop.DataAbility",
12. "readPermission": "ohos.permission.READ_CONTACTS",
13. "writePermission": "ohos.permission.WRITE_CONTACTS"
14. },
15. ...
16. ]
```

DataAbility支持的配置项及详细说明详见[module对象内部结构](module-structure.md)。
