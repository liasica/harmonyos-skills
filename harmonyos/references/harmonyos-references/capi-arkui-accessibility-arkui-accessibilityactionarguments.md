---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityactionarguments
title: ArkUI_AccessibilityActionArguments
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibilityActionArguments
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5a16320be14b73f88f0857f0510a3061a62c2436a0ab0f45c7ba299f8f8600df
---

```c
typedef struct ArkUI_AccessibilityActionArguments ArkUI_AccessibilityActionArguments
```

## 概述

用于设置无障碍操作的具体参数。在进行无障碍操作时，通过该结构体向无障碍服务传递操作所需的附加上下文信息。适用于开发者需要向无障碍服务精确描述无障碍操作细节的场景，例如自定义控件的无障碍读屏播报、辅助功能服务中的操作参数传递、语音助手触发的无障碍交互等应用功能。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)
