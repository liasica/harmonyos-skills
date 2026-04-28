---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-6021
title: AVSession Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a08d656792a7237dcaa1c986d54d3e70c31fe46135ce139e84466bfea3e796ef
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：avSession；  API声明：type AVSessionType = 'audio' | 'video' | 'voice\_call' | 'video\_call';  差异内容：'audio' | 'video' | 'voice\_call' | 'video\_call' | 类名：avSession；  API声明：type AVSessionType = 'audio' | 'video' | 'voice\_call' | 'video\_call' | 'photo';  差异内容：'audio' | 'video' | 'voice\_call' | 'video\_call' | 'photo' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：function getAVSession(context: Context): Promise<AVSession>;  差异内容：function getAVSession(context: Context): Promise<AVSession>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：type NoParamCallback = () => void;  差异内容：type NoParamCallback = () => void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：type TwoParamCallback<T, G> = (data1: T, data2: G) => void;  差异内容：type TwoParamCallback<T, G> = (data1: T, data2: G) => void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：readonly sessionTag: string;  差异内容：readonly sessionTag: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onPlay(callback: Callback<CommandInfo>): void;  差异内容：onPlay(callback: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onPlayNext(callback: Callback<CommandInfo>): void;  差异内容：onPlayNext(callback: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onPlayPrevious(callback: Callback<CommandInfo>): void;  差异内容：onPlayPrevious(callback: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onFastForward(callback: TwoParamCallback<number, CommandInfo>): void;  差异内容：onFastForward(callback: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：onRewind(callback: TwoParamCallback<number, CommandInfo>): void;  差异内容：onRewind(callback: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offPlay(callback?: Callback<CommandInfo>): void;  差异内容：offPlay(callback?: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offPlayNext(callback?: Callback<CommandInfo>): void;  差异内容：offPlayNext(callback?: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offPlayPrevious(callback?: Callback<CommandInfo>): void;  差异内容：offPlayPrevious(callback?: Callback<CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void;  差异内容：offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：offRewind(callback?: TwoParamCallback<number, CommandInfo>): void;  差异内容：offRewind(callback?: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：interface MenuPosition  差异内容：interface MenuPosition | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition；  API声明：x: number;  差异内容：x: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition；  API声明：y: number;  差异内容：y: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition；  API声明：width: number;  差异内容：width: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition；  API声明：height: number;  差异内容：height: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVCastPickerOptions；  API声明：pickerStyle?: AVCastPickerStyle;  差异内容：pickerStyle?: AVCastPickerStyle; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVCastPickerOptions；  API声明：menuPosition?: MenuPosition;  差异内容：menuPosition?: MenuPosition; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVControlCommand；  API声明：commandInfo?: CommandInfo;  差异内容：commandInfo?: CommandInfo; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：interface CommandInfo  差异内容：interface CommandInfo | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo；  API声明：callerBundleName?: string;  差异内容：callerBundleName?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo；  API声明：callerModuleName?: string;  差异内容：callerModuleName?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo；  API声明：callerDeviceId?: string;  差异内容：callerDeviceId?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo；  API声明：callerType?: CallerType;  差异内容：callerType?: CallerType; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：enum CallerType  差异内容：enum CallerType | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType；  API声明：TYPE\_CAST = 'cast'  差异内容：TYPE\_CAST = 'cast' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType；  API声明：TYPE\_BLUETOOTH = 'bluetooth'  差异内容：TYPE\_BLUETOOTH = 'bluetooth' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType；  API声明：TYPE\_NEARLINK = 'nearlink'  差异内容：TYPE\_NEARLINK = 'nearlink' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType；  API声明：TYPE\_APP = 'app'  差异内容：TYPE\_APP = 'app' | api/@ohos.multimedia.avsession.d.ts |
