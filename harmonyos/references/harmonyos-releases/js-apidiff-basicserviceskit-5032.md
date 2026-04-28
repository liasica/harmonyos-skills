---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-5032
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:34+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:23e5472a6193a8a3b4bfd2b9734a8ae9a9695844dc43e181f22a91ab5def8408
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_ENTER\_HIBERNATE = 'usual.event.ENTER\_HIBERNATE'  差异内容：COMMON\_EVENT\_ENTER\_HIBERNATE = 'usual.event.ENTER\_HIBERNATE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_EXIT\_HIBERNATE = 'usual.event.EXIT\_HIBERNATE'  差异内容：COMMON\_EVENT\_EXIT\_HIBERNATE = 'usual.event.EXIT\_HIBERNATE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED = 'usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED'  差异内容：COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED = 'usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const diskSN: string;  差异内容：const diskSN: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： enum FileConflictOptions  差异内容： enum FileConflictOptions | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：FileConflictOptions；  API声明：OVERWRITE  差异内容：OVERWRITE | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：FileConflictOptions；  API声明：SKIP  差异内容：SKIP | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： enum ProgressIndicator  差异内容： enum ProgressIndicator | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressIndicator；  API声明：NONE  差异内容：NONE | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressIndicator；  API声明：DEFAULT  差异内容：DEFAULT | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： interface ProgressInfo  差异内容： interface ProgressInfo | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：progress: number;  差异内容：progress: number; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明：type ProgressListener = (progress: ProgressInfo) => void;  差异内容：type ProgressListener = (progress: ProgressInfo) => void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： export class ProgressSignal  差异内容： export class ProgressSignal | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressSignal；  API声明：cancel(): void;  差异内容：cancel(): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： interface GetDataParams  差异内容： interface GetDataParams | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：destUri?: string;  差异内容：destUri?: string; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：fileConflictOptions?: FileConflictOptions;  差异内容：fileConflictOptions?: FileConflictOptions; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：progressIndicator: ProgressIndicator;  差异内容：progressIndicator: ProgressIndicator; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：progressListener?: ProgressListener;  差异内容：progressListener?: ProgressListener; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams；  API声明：progressSignal?: ProgressSignal;  差异内容：progressSignal?: ProgressSignal; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：getDataWithProgress(params: GetDataParams): Promise<PasteData>;  差异内容：getDataWithProgress(params: GetDataParams): Promise<PasteData>; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Config；  API声明：multipart?: boolean;  差异内容：multipart?: boolean; | api/@ohos.request.d.ts |
