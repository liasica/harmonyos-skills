---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsocversion
title: GetSocVersion
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetSocVersion
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1fc149dbe21134ad4182c9d4c6d4f0e35be30463ae372f1e198c5c08df24056
---

## 函数功能

获取当前硬件平台版本型号。

## 函数原型

```
1. SocVersion GetSocVersion(void) const;
```

## 参数说明

无

## 返回值

当前硬件平台版本型号的枚举类。该枚举类和AI处理器型号的对应关系请通过CANN DDK包里的ddk/ai\_ddk\_lib/include/tiling/platform/platform\_ascendc.h头文件获取。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. auto socVersion = ascendcPlatform.GetSocVersion();
4. // 根据所获得的版本型号自行设计Tiling策略
5. if (socVersion == platform_ascendc::SocVersion::KIRIN9020) {
6. // ...
7. }
8. return ret;
9. }
```
