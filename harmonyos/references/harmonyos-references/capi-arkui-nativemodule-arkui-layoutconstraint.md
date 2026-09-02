---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-layoutconstraint
title: ArkUI_LayoutConstraint
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_LayoutConstraint
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c448a2868eeba55fedefbf9affdff60c537830c19219b71fa56c62718f5bc6ea
---

```c
typedef struct ArkUI_LayoutConstraint ArkUI_LayoutConstraint
```

## 概述

布局约束，用于组件布局时进行尺寸范围限制。支持设置最小尺寸和最大尺寸约束，约束值为非负浮点数，在组件布局时，系统会根据约束值限定组件的最终尺寸范围，确保布局结果符合约束条件。适用于自定义布局容器时控制子组件的尺寸范围，如瀑布流布局中限制图片卡片的高度、网格布局中限制单元格尺寸，以及需要限制组件尺寸上下限的场景，如图片展示组件限制最大宽度防止拉伸、响应式布局中限制最小尺寸保证可读性。防止组件尺寸超出预期范围，实现更精确的布局控制，提高布局的可预测性和稳定性，增强界面的可控性。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)
