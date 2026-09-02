---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-content
title: Content
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > Content
category: harmonyos-references
scraped_at: 2026-09-02T15:00:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4b36d3df4e1fd8e2da4e06ade54db5fe57708f6b95351ed8f95078d52750bfb
---

定义ComponentContent和NodeContent的基类，为ArkUI内容承载结构提供统一的内容管理能力，适用于需要动态创建和挂载自定义内容节点的场景。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { Content } from '@kit.ArkUI';
```

## Content

Content是ArkUI内容承载结构的基类，为[ComponentContent](js-apis-arkui-componentcontent.md)和[NodeContent](js-apis-arkui-nodecontent.md)提供统一的内容管理能力，适用于需要动态创建和挂载自定义内容节点的场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
