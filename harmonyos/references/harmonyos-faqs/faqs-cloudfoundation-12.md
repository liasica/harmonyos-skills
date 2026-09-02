---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-12
title: 云数据库端云同步方案
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 云数据库端云同步方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:2cf24fc7357911e7db6af1df8eb135678bb045b7dfc5975a932297b5613d67e6
---

## 问题现象

接入[Cloud Foundation Kit](../harmonyos-guides/cloudfoundation-introduction.md)后应用客户端如何监听云数据库的数据变化？

## 背景知识

[Cloud Foundation Kit简介](../harmonyos-guides/cloudfoundation-introduction.md)：Cloud Foundation Kit（云开发服务）可以按需为应用提供云函数、云数据库、云存储、预加载等云端服务。应用运行所需的服务器和环境可以皆由云端平台提供，开发者只需关注应用的业务逻辑，而无需关心基础设施（例如：服务器、操作系统、容器等）。

* 云函数[业务介绍](../AppGallery-connect-Guides/agc-cloud-function-introduction-0000001059279544.md)：云函数是一项Serverless计算服务，提供FaaS（Function as a Service）能力。
* 云数据库[业务介绍](../AppGallery-connect-Guides/agc-clouddb-introduction-0000001054212760.md)：云数据库是一款端云协同的数据库产品，提供端云数据的协同管理、统一的数据模型和丰富的数据管理API接口等能力。在保证数据的可用性、可靠性、一致性，以及安全等特性基础上，能够实现数据在客户端和云端之间的无缝同步，并为应用提供离线支持，以帮助开发者快速构建端云、多端协同的应用。

[云数据库触发器](../AppGallery-connect-Guides/agc-cloudfunction-clouddbtrigger-0000001658558540.md)：支持通过云数据库相关事件来触发云函数。

* AGC云数据库服务为开发者提供了基于云函数服务的扩展机制，开发者可以为云函数配置云数据库触发器，当云数据库发生插入或者更新数据、删除数据、清空数据等变更操作时将触发云函数，并在云函数中扩展业务处理逻辑。
* 使用场景：云数据库有数据变更时可以自动触发函数进行逻辑处理。

## 解决方案

Cloud Foundation Kit的云数据库如果要实现监听云侧数据变化，需要结合云函数的云数据库触发器一起使用。

1. 创建云数据库，按照以下步骤完成接入云数据库的准备工作：[新增对象类型](../harmonyos-guides/cloudfoundation-database-add-object.md)、[新增存储区](../harmonyos-guides/cloudfoundation-database-add-zone.md)、[引入对象类型文件](../harmonyos-guides/cloudfoundation-database-add-file.md)、[初始化数据库访问](../harmonyos-guides/cloudfoundation-database-initialize.md)。
2. [创建函数](../harmonyos-guides/cloudfoundation-create-and-config-function.md#创建函数-1)，在进入到创建触发器页面时，"触发器类型"选择"云数据库触发器"，"存储区"和"对象类型"选择上一步创建云数据库所新增的选项。由于需要监听云数据库数据的所有变化，所以"事件类型"选择"onWrite"。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/pVCFTBE5TZir5I4yGrk1LA/zh-cn_image_0000002719018075.png "点击放大")
3. 根据实际业务，完成接收到云数据库触发器事件后的云函数代码，调用函数时，入口方法的入参event对象中包含了云数据库触发器传递的信息，具体event对象的字段要求请参见event对象说明中的[云数据库触发器](../AppGallery-connect-Guides/agc-cloudfunction-trigger-event-0000001620581529.md#section207831182811)示例。[入口方法](../harmonyos-guides/cloudfoundation-develop-function-nodejs.md#入口方法)的开发参见[开发函数](../harmonyos-guides/cloudfoundation-develop-function.md)官方文档。

## 常见FAQ

Q：初始化数据库访问时，cloudDatabase.zone()方法传入的名称是否需要与AGC平台上创建的存储区名称一致？

A：必须一致。cloudDatabase.zone()方法传入的名称必须与AGC平台上新增的存储区名称完全一致，否则会访问失败。新增存储区的具体操作请参见[新增存储区](../harmonyos-guides/cloudfoundation-database-add-zone.md)。
