---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing
title: 模块描述
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > 模块描述
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6917fa33d5c2a949b1260fc6cc746d86aef91af2ea9892a30c7fc13354a18ffd
---

开发者在绘制界面元素时，若ArkUI组件无法满足自定义图形需求，可使用Drawing模块实现灵活的自定义绘制效果。Drawing模块提供基础的图形绘制能力，包括绘制矩形、圆形、点、直线、自定义Path和字体等。

**说明** 

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

```ts
import { drawing } from '@kit.ArkGraphics2D';
```
