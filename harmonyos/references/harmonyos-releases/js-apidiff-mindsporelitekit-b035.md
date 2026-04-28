---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mindsporelitekit-b035
title: MindSpore Lite Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > MindSpore Lite Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:31+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9c0bdbd289c4243eb7c33208cd05fb58ec49239342c6ac6323af6a9dceb47fed
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：Context；  API声明：target?: string[];  差异内容：NA | 类名：Context；  API声明：target?: string[];  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Context；  API声明：cpu?: CpuDevice;  差异内容：NA | 类名：Context；  API声明：cpu?: CpuDevice;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Context；  API声明：nnrt?: NNRTDevice;  差异内容：NA | 类名：Context；  API声明：nnrt?: NNRTDevice;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice；  API声明：threadNum?: number;  差异内容：NA | 类名：CpuDevice；  API声明：threadNum?: number;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice；  API声明：threadAffinityMode?: ThreadAffinityMode;  差异内容：NA | 类名：CpuDevice；  API声明：threadAffinityMode?: ThreadAffinityMode;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice；  API声明：threadAffinityCoreList?: number[];  差异内容：NA | 类名：CpuDevice；  API声明：threadAffinityCoreList?: number[];  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice；  API声明：precisionMode?: string;  差异内容：NA | 类名：CpuDevice；  API声明：precisionMode?: string;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode；  API声明：NO\_AFFINITIES = 0  差异内容：NA | 类名：ThreadAffinityMode；  API声明：NO\_AFFINITIES = 0  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode；  API声明：BIG\_CORES\_FIRST = 1  差异内容：NA | 类名：ThreadAffinityMode；  API声明：BIG\_CORES\_FIRST = 1  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode；  API声明：LITTLE\_CORES\_FIRST = 2  差异内容：NA | 类名：ThreadAffinityMode；  API声明：LITTLE\_CORES\_FIRST = 2  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：name: string;  差异内容：NA | 类名：MSTensor；  API声明：name: string;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：shape: number[];  差异内容：NA | 类名：MSTensor；  API声明：shape: number[];  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：elementNum: number;  差异内容：NA | 类名：MSTensor；  API声明：elementNum: number;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：dataSize: number;  差异内容：NA | 类名：MSTensor；  API声明：dataSize: number;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：dtype: DataType;  差异内容：NA | 类名：MSTensor；  API声明：dtype: DataType;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor；  API声明：format: Format;  差异内容：NA | 类名：MSTensor；  API声明：format: Format;  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：TYPE\_UNKNOWN = 0  差异内容：NA | 类名：DataType；  API声明：TYPE\_UNKNOWN = 0  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_INT8 = 32  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_INT8 = 32  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_INT16 = 33  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_INT16 = 33  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_INT32 = 34  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_INT32 = 34  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_INT64 = 35  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_INT64 = 35  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT8 = 37  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT8 = 37  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT16 = 38  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT16 = 38  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT32 = 39  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT32 = 39  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT64 = 40  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_UINT64 = 40  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT16 = 42  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT16 = 42  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT32 = 43  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT32 = 43  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT64 = 44  差异内容：NA | 类名：DataType；  API声明：NUMBER\_TYPE\_FLOAT64 = 44  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：DEFAULT\_FORMAT = -1  差异内容：NA | 类名：Format；  API声明：DEFAULT\_FORMAT = -1  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：NCHW = 0  差异内容：NA | 类名：Format；  API声明：NCHW = 0  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：NHWC = 1  差异内容：NA | 类名：Format；  API声明：NHWC = 1  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：NHWC4 = 2  差异内容：NA | 类名：Format；  API声明：NHWC4 = 2  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：HWKC = 3  差异内容：NA | 类名：Format；  API声明：HWKC = 3  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：HWCK = 4  差异内容：NA | 类名：Format；  API声明：HWCK = 4  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format；  API声明：KCHW = 5  差异内容：NA | 类名：Format；  API声明：KCHW = 5  差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
