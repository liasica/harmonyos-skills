---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-dbprocess
title: 开发流程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 开发流程
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c0e93dc96d298ff3acc03468f945ebd0b1f2bba9ac63bcc58280e81936465a06
---

|  |  |
| --- | --- |
| 云数据库是一款端云协同的数据库产品，提供端云数据的协同管理、统一的数据模型和丰富的数据管理API接口等能力。云数据库采用基于对象模型的数据存储结构。   * 数据以对象（Object）的形式存储在不同的存储区中，每一个对象，都是一条完整的数据记录。 * 对象类型（ObjectType）用于定义存储对象的集合，不同的对象类型对应的不同数据结构。 * 存储区（Zone）是一个独立的数据存储区域，每个存储区拥有完全相同的对象类型定义。 |  |

您可以使用DevEco Studio在端云一体化云侧工程下开发云数据库，总体流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/xBqpuHObRwuA-rpBwZMPrw/zh-cn_image_0000002314347097.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=CF4C3B34CD2714C593ACD5C8A06692B5111DFC0BDA5052A39A6E91DAEFE47654 "点击放大")

1. [创建对象类型](agc-harmonyos-clouddev-objecttype.md)：创建一个用于存储数据条目的对象类型。
2. [添加数据条目](agc-harmonyos-clouddev-dataentry.md)：在刚刚创建的对象类型内添加一条条数据，并配置数据所在的存储区。
3. [部署云数据库](agc-harmonyos-clouddev-deploydatabase.md)：数据成功添加后，您可以直接将该数据部署至AGC云端。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到AGC云端。
