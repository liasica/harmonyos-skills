---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-5032
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:33+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ea3578ebd522dedfbdfc2df6c9b51534ea25eeecbb3d636cd8c659ffd7fa61bb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace intelligence  差异内容： declare namespace intelligence | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>;  差异内容：function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>;  差异内容：function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明： interface ModelConfig  差异内容： interface ModelConfig | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig；  API声明：version: ModelVersion;  差异内容：version: ModelVersion; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig；  API声明：isNpuAvailable: boolean;  差异内容：isNpuAvailable: boolean; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig；  API声明：cachePath?: string;  差异内容：cachePath?: string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明： enum ModelVersion  差异内容： enum ModelVersion | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelVersion；  API声明：BASIC\_MODEL = 0  差异内容：BASIC\_MODEL = 0 | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明： interface TextEmbedding  差异内容： interface TextEmbedding | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：TextEmbedding；  API声明：loadModel(): Promise<void>;  差异内容：loadModel(): Promise<void>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：TextEmbedding；  API声明：releaseModel(): Promise<void>;  差异内容：releaseModel(): Promise<void>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：TextEmbedding；  API声明：getEmbedding(text: string): Promise<Array<number>>;  差异内容：getEmbedding(text: string): Promise<Array<number>>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：TextEmbedding；  API声明：getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>;  差异内容：getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明： interface ImageEmbedding  差异内容： interface ImageEmbedding | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ImageEmbedding；  API声明：loadModel(): Promise<void>;  差异内容：loadModel(): Promise<void>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ImageEmbedding；  API声明：releaseModel(): Promise<void>;  差异内容：releaseModel(): Promise<void>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ImageEmbedding；  API声明：getEmbedding(image: Image): Promise<Array<number>>;  差异内容：getEmbedding(image: Image): Promise<Array<number>>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：type Image = string;  差异内容：type Image = string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：function splitText(text: string, config: SplitConfig): Promise<Array<string>>;  差异内容：function splitText(text: string, config: SplitConfig): Promise<Array<string>>; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明： interface SplitConfig  差异内容： interface SplitConfig | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：SplitConfig；  API声明：size: number;  差异内容：size: number; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：SplitConfig；  API声明：overlapRatio: number;  差异内容：overlapRatio: number; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： enum FileConflictOptions  差异内容： enum FileConflictOptions | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：FileConflictOptions；  API声明：OVERWRITE  差异内容：OVERWRITE | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：FileConflictOptions；  API声明：SKIP  差异内容：SKIP | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： enum ProgressIndicator  差异内容： enum ProgressIndicator | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ProgressIndicator；  API声明：NONE  差异内容：NONE | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ProgressIndicator；  API声明：DEFAULT  差异内容：DEFAULT | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： enum ListenerStatus  差异内容： enum ListenerStatus | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：FINISHED = 0  差异内容：FINISHED = 0 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：PROCESSING  差异内容：PROCESSING | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：CANCELED  差异内容：CANCELED | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：INNER\_ERROR = 200  差异内容：INNER\_ERROR = 200 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：INVALID\_PARAMETERS  差异内容：INVALID\_PARAMETERS | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：DATA\_NOT\_FOUND  差异内容：DATA\_NOT\_FOUND | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：SYNC\_FAILED  差异内容：SYNC\_FAILED | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ListenerStatus；  API声明：COPY\_FILE\_FAILED  差异内容：COPY\_FILE\_FAILED | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： interface ProgressInfo  差异内容： interface ProgressInfo | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：progress: number;  差异内容：progress: number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：status: ListenerStatus;  差异内容：status: ListenerStatus; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void;  差异内容：type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： interface GetDataParams  差异内容： interface GetDataParams | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：progressIndicator: ProgressIndicator;  差异内容：progressIndicator: ProgressIndicator; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：dataProgressListener: DataProgressListener;  差异内容：dataProgressListener: DataProgressListener; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：destUri?: string;  差异内容：destUri?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：fileConflictOptions?: FileConflictOptions;  差异内容：fileConflictOptions?: FileConflictOptions; | api/@ohos.data.unifiedDataChannel.d.ts |
| kit变更 | NA | ArkData | api/@ohos.data.intelligence.d.ts |
