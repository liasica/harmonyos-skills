---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6002
title: Performance Analysis Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:39d4c7678b98ea4308ab0842f79b008d65b9359bb164829a8ab367d6b8af2d07
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：event；  API声明：const APP\_KILLED: string;  差异内容：const APP\_KILLED: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function addProcessorFromConfig(processorName: string, configName?: string): Promise<number>;  差异内容：function addProcessorFromConfig(processorName: string, configName?: string): Promise<number>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Processor；  API声明：configName?: string;  差异内容：configName?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
