---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-b031
title: Media Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5fbd09557691fb8901d4e9b9d41308aff62c139d4ac52aaa35060155b8e66e60
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AVPlayer；  API声明：addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>;  差异内容：addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：addSubtitleFromUrl(url: string): Promise<void>;  差异内容：addSubtitleFromUrl(url: string): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void;  差异内容：on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void;  差异内容：off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明： interface SubtitleInfo  差异内容： interface SubtitleInfo | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo；  API声明：startTime?: number;  差异内容：startTime?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo；  API声明：text?: string;  差异内容：text?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaType；  API声明：MEDIA\_TYPE\_SUBTITLE = 2  差异内容：MEDIA\_TYPE\_SUBTITLE = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey；  API声明：MD\_KEY\_LANGUAGE = 'language'  差异内容：MD\_KEY\_LANGUAGE = 'language' | api/@ohos.multimedia.media.d.ts |
