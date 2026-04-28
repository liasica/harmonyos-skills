---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/actions-entities
title: 常见action与entities（不推荐使用）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 信息传递载体Want > 常见action与entities（不推荐使用）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b3b6940e603c5d98c5a84f876c34e040ce5df3b693d6612506898fcf28fcbddf
---

说明

由于action/entity被泛化使用，系统对应用声明action/entity的行为缺少管控，恶意应用虚假声明，抢占流量，导致跳转后功能不可用。后续系统会逐步废弃非必要action/entity，建议通过[指定类型的方式拉起应用](start-intent-panel.md)。

**action**：表示调用方要执行的通用操作（如查看、分享、应用详情）。在隐式[Want](../harmonyos-references/js-apis-app-ability-want.md)中，您可定义该字段，配合uri或parameters来表示对数据要执行的操作。如打开，查看该uri数据。例如，当uri为一段网址，action为ACTION\_VIEW\_DATA则表示匹配可访问该网址的应用组件。在Want内声明action字段表示希望被调用方应用支持声明的操作。在被调用方应用配置文件的[skills字段](module-configuration-file.md#skills标签)内声明actions表示该应用支持声明操作。常见的action如下，具体的action取值请见[action常数说明](../harmonyos-references/js-apis-ability-wantconstant.md#action)。

**常见action**

* ACTION\_HOME：启动应用入口组件的动作，需要和ENTITY\_HOME配合使用；系统桌面应用图标就是显式的入口组件，点击也是启动入口组件；入口组件可以配置多个。
* ACTION\_CHOOSE：选择本地资源数据，例如联系人、相册等；系统一般对不同类型的数据有对应的Picker应用，例如联系人和图库。
* ACTION\_VIEW\_DATA：查看数据，当使用网址uri时，则表示显示该网址对应的内容。具体操作流程请见[通过startAbility拉起文件处理类应用](file-processing-apps-startup.md)。
* ACTION\_VIEW\_MULTIPLE\_DATA：发送多个数据记录的操作。

**entities**：表示目标应用组件的类别信息（如浏览器、视频播放器），在隐式[Want](../harmonyos-references/js-apis-app-ability-want.md)中是对action的补充。在隐式Want中，开发者可定义该字段，来过滤匹配应用的类别，例如必须是浏览器。在Want内声明entities字段表示希望被调用方应用属于声明的类别。在被调用方应用配置文件的[skills字段](module-configuration-file.md#skills标签)内声明entities表示该应用支持的类别。常见的entities如下，具体的entity取值及说明请见[entity常数说明](../harmonyos-references/js-apis-ability-wantconstant.md#entity)。

**常见entities**

* ENTITY\_DEFAULT：默认类别无实际意义。
* ENTITY\_HOME：主屏幕有图标点击入口类别。
* ENTITY\_BROWSABLE：指示浏览器类别。
