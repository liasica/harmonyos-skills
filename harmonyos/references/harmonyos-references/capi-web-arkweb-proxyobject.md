---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobject
title: ArkWeb_ProxyObject
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ProxyObject
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8f50ba86d946a263fa809e5011230743972dcb5a25cec2ee9c2d05398be2546
---

```c
typedef struct {...} ArkWeb_ProxyObject
```

## 概述

ArkWeb\_ProxyObject是注入到Web页面的JavaScript代理对象结构体，用于将一组相关的ArkWeb\_ProxyMethod方法组织成对象整体暴露给Web前端。该结构体指定了对象在JavaScript中的名称（objName）、方法数组（methodList）和方法数量（size），使得Native应用可以向Web页面暴露结构化的API集合。代理对象通过方法映射机制将Native侧的ArkWeb\_ProxyMethod与JavaScript侧的方法调用进行关联，支持方法参数和返回值的自动转换。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* objName | 注入的对象名，命名应遵循JavaScript标识符规则，不支持特殊字符。 |
| const [ArkWeb\_ProxyMethod](capi-web-arkweb-proxymethod.md)\* methodList | 注入的对象携带的方法结构体数组。 |
| size\_t size | 方法结构体数组的长度，必须与methodList数组的实际元素个数一致。 |
