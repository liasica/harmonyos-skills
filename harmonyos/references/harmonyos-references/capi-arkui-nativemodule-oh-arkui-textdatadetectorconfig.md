---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig
title: OH_ArkUI_TextDataDetectorConfig
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextDataDetectorConfig
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3d08211a3d1e7c4959ff672bc662813838b30d4f9c92ea15a6a9763dbd1af3c0
---

```c
typedef struct OH_ArkUI_TextDataDetectorConfig OH_ArkUI_TextDataDetectorConfig
```

## 概述

定义文本实体识别的配置，通过设置需要识别的实体类型（如电话号码、网址、邮箱、地址、日期等），在文本组件中启用对应的实体检测功能，检测到的实体将以可交互形式呈现。适用于聊天消息中自动识别联系方式、文档中提取链接等场景。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [text.h](capi-text-h.md)
