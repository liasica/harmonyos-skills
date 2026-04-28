---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-speechkit-b031
title: Speech Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Speech Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4d616d184970aa8787eecf3f4652cbfa4317e097f47f9c4e0848698de4bb0ce6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：TextReader；  API声明：function init(context: common.BaseContext, readParams: ReaderParam): Promise<void>;  差异内容：1010600011,401 | 类名：TextReader；  API声明：function init(context: common.BaseContext, readParams: ReaderParam): Promise<void>;  差异内容：1010600011,201,401 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface AudioInfo  差异内容： export declare interface AudioInfo | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：audioType: string;  差异内容：audioType: string; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：sampleRate: audio.AudioSamplingRate;  差异内容：sampleRate: audio.AudioSamplingRate; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：soundChannel: audio.AudioChannel;  差异内容：soundChannel: audio.AudioChannel; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AudioInfo；  API声明：sampleBit: number;  差异内容：sampleBit: number; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface AudioData  差异内容： export declare interface AudioData | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AudioData；  API声明：data: Uint8Array;  差异内容：data: Uint8Array; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class AICaptionController  差异内容： export declare class AICaptionController | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionController；  API声明：getAudioInfo(): AudioInfo;  差异内容：getAudioInfo(): AudioInfo; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionController；  API声明：writeAudio(audioData: AudioData): void;  差异内容：writeAudio(audioData: AudioData): void; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface AICaptionOptions  差异内容： export declare interface AICaptionOptions | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：onPrepared: Callback<void>;  差异内容：onPrepared: Callback<void>; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：onError: ErrorCallback;  差异内容：onError: ErrorCallback; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：initialOpacity?: number;  差异内容：initialOpacity?: number; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct AICaptionComponent  差异内容： export declare struct AICaptionComponent | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionComponent；  API声明：@Link  isShown: boolean;  差异内容：@Link  isShown: boolean; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionComponent；  API声明：controller: AICaptionController;  差异内容：controller: AICaptionController; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionComponent；  API声明：options: AICaptionOptions;  差异内容：options: AICaptionOptions; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionComponent；  API声明：build(): void;  差异内容：build(): void; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function playPrev(): void;  差异内容：function playPrev(): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function playNext(): void;  差异内容：function playNext(): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReader；  API声明：function setArticle(readInfo: ReadInfo): void;  差异内容：function setArticle(readInfo: ReadInfo): void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：ReaderParam；  API声明：keepBackgroundRunning?: boolean;  差异内容：keepBackgroundRunning?: boolean; | api/@hms.ai.textReader.d.ets |
