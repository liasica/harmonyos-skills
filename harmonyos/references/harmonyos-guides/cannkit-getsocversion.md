---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsocversion
title: GetSocVersion
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetSocVersion
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80b73838c7dcfab373d2f7f1a87e305f02022c972725c0de8b14ee549e6d09f2
---

## 函数功能

获取当前硬件平台版本型号。

## 函数原型

```cpp
SocVersion GetSocVersion(void) const;
```

## 参数说明

无

## 返回值

当前硬件平台版本型号的枚举类。该枚举类和AI处理器型号的对应关系请通过CANN DDK包里的ddk/ai\_ddk\_lib/include/tiling/platform/platform\_ascendc.h头文件获取。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    auto socVersion = ascendcPlatform.GetSocVersion();
    // 根据所获得的版本型号自行设计Tiling策略
    if (socVersion == platform_ascendc::SocVersion::KIRIN9020) {
        // ...
    }
    return ret;
}
```
