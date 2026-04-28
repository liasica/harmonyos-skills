---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-6002
title: ArkData
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d772b93f3bba8f650f8f65126ae502892af1641a03b643dc9f6c048ded41c136
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：enum Visibility  差异内容：enum Visibility | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Visibility；  API声明：ALL  差异内容：ALL | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Visibility；  API声明：OWN\_PROCESS  差异内容：OWN\_PROCESS | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：interface DataLoadInfo  差异内容：interface DataLoadInfo | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：DataLoadInfo；  API声明：types?: Set<string>;  差异内容：types?: Set<string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：DataLoadInfo；  API声明：recordCount?: number;  差异内容：recordCount?: number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null;  差异内容：type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：interface DataLoadParams  差异内容：interface DataLoadParams | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：DataLoadParams；  API声明：loadHandler: DataLoadHandler;  差异内容：loadHandler: DataLoadHandler; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：DataLoadParams；  API声明：dataLoadInfo: DataLoadInfo;  差异内容：dataLoadInfo: DataLoadInfo; | api/@ohos.data.unifiedDataChannel.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResultSet；  API声明：getValueForFlutter(columnIndex: number): ValueType;  差异内容：getValueForFlutter(columnIndex: number): ValueType; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResultSet；  API声明：getRowForFlutter(): ValuesBucket;  差异内容：getRowForFlutter(): ValuesBucket; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：intention?: Intention;  差异内容：intention?: Intention; | api/@ohos.data.unifiedDataChannel.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：key?: string;  差异内容：key?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：visibility?: Visibility;  差异内容：visibility?: Visibility; | api/@ohos.data.unifiedDataChannel.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GetDataParams；  API声明：acceptableInfo?: DataLoadInfo;  差异内容：acceptableInfo?: DataLoadInfo; | api/@ohos.data.unifiedDataChannel.d.ts |
