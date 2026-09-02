---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-paragraphstyle
title: OH_ArkUI_ParagraphStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_ParagraphStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c52684b87e8eeafa019cdb4d7af2104bfbd4ef50898ca2d5f9f39ea034cf648
---

```c
typedef struct OH_ArkUI_ParagraphStyle OH_ArkUI_ParagraphStyle
```

## 概述

定义段落样式，用于在构建富文本段落时统一设置文本对齐、换行、截断等排版行为，适用于需要对段落进行精细化排版控制的场景，例如在富文本编辑器中设置段落对齐方式、在新闻阅读应用中控制长文本的换行与截断显示等。

调用[OH\_ArkUI\_ParagraphStyle\_Create](capi-styled-string-h.md#oh_arkui_paragraphstyle_create)接口创建对应的段落样式对象。

调用[OH\_ArkUI\_ParagraphStyle\_Destroy](capi-styled-string-h.md#oh_arkui_paragraphstyle_destroy)接口销毁段落样式对象。

对象创建后，调用OH\_ArkUI\_ParagraphStyle\_SetXXX系列接口设置具体样式。例如，调用[OH\_ArkUI\_ParagraphStyle\_SetTextAlign](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextalign)设置文本对齐方式。若创建对象失败（返回空指针）或对象已销毁，调用SetXXX系列接口将不会生效。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
