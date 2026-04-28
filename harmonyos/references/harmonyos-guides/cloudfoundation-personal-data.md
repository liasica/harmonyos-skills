---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-personal-data
title: 个人数据处理说明
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10a325028df17c339d1333b7260b1f7ad7bd485bc7e76abf22a7098e5b2593fa
---

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单
* 指导开发者如何帮助最终用户实现对数据的控制

## 华为处理的个人数据清单

最后修改时间：2025/02/27

| 个人数据清单 | 使用目的 | 存留期 |
| --- | --- | --- |
| （可选）华为账号信息 | 如果开发者在初始化Cloud Foundation Kit时携带了华为账号信息，Cloud Foundation Kit在访问云侧接口时会携带该账号信息用于资源的访问权限控制。 | 端侧不保存信息，云侧信息将保存至如下时刻：  - 最终用户或开发者主动删除上传的数据  - 开发者主动删除整个项目 |
| （可选）用户凭证信息 | Cloud Foundation Kit的预加载能力是一种数据传输通道，开发者可以通过该通道传递用户凭证信息给自己的服务器，以对预加载资源进行访问权限控制。 | 直接透传给开发者服务器，由开发者自行处理，华为不保存该信息。 |

## 指导开发者如何帮助最终用户实现对数据的控制

* 如何清除最终用户的数据

  + 最终用户或开发者主动删除上传的数据
    - 清除云存储中的用户数据：可通过[StorageBucket.deleteFile](../harmonyos-references/cloudfoundation-cloudstorage.md#deletefile)接口删除通过云存储上传的用户数据。
    - 清除云数据库中的用户数据：可通过[DatabaseZone.delete](../harmonyos-references/cloudfoundation-clouddatabase.md#delete)接口删除写入云数据库的用户数据。
  + 开发者主动删除整个项目
* 如何导出最终用户的数据

  不涉及
