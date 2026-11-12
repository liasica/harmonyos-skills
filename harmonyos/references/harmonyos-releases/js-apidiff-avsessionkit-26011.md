---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-26011
title: AVSession Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5dfc2335239b0c56bcde332f49ab3c50862be53897759d2b3d0f75c43d437e9d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：avMusicTemplate；  API声明：type CustomCommandEvent = (command: string, args: string) => Promise<OperResult>;  差异内容：type CustomCommandEvent = (command: string, args: string) => Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：onCustomCommand(callback: CustomCommandEvent): void;  差异内容：onCustomCommand(callback: CustomCommandEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplate；  API声明：offCustomCommand(callback?: CustomCommandEvent): void;  差异内容：offCustomCommand(callback?: CustomCommandEvent): void; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVMusicTemplateController；  API声明：sendCustomCommand(command: string, args: string): Promise<OperResult>;  差异内容：sendCustomCommand(command: string, args: string): Promise<OperResult>; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayMusicInfo；  API声明：extras?: string;  差异内容：extras?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayKaraokeItem  差异内容：interface SearchPlayKaraokeItem | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeItem；  API声明：entityId: string;  差异内容：entityId: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeItem；  API声明：entityName?: string;  差异内容：entityName?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：avMusicTemplate；  API声明：interface SearchPlayKaraokeInfo  差异内容：interface SearchPlayKaraokeInfo | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：items?: SearchPlayKaraokeItem[];  差异内容：items?: SearchPlayKaraokeItem[]; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：songName?: string;  差异内容：songName?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：artist?: string;  差异内容：artist?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：albumName?: string;  差异内容：albumName?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：billBoard?: string;  差异内容：billBoard?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：scene?: string;  差异内容：scene?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：genre?: string;  差异内容：genre?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：instrument?: string;  差异内容：instrument?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：language?: string;  差异内容：language?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：decade?: string;  差异内容：decade?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：mood?: string;  差异内容：mood?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：gender?: string;  差异内容：gender?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：queryKeyWords?: string;  差异内容：queryKeyWords?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayKaraokeInfo；  API声明：extra?: string;  差异内容：extra?: string; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfo；  API声明：karaokeInfo?: SearchPlayKaraokeInfo;  差异内容：karaokeInfo?: SearchPlayKaraokeInfo; | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_MUSIC\_LIST = 'playMusicList'  差异内容：PLAY\_MUSIC\_LIST = 'playMusicList' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_VIDEO\_LIST = 'playVideoList'  差异内容：PLAY\_VIDEO\_LIST = 'playVideoList' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_KARAOKE = 'playKaraoke'  差异内容：PLAY\_KARAOKE = 'playKaraoke' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：SearchPlayInfoType；  API声明：PLAY\_KARAOKE\_LIST = 'playKaraokeList'  差异内容：PLAY\_KARAOKE\_LIST = 'playKaraokeList' | api/@ohos.multimedia.avMusicTemplate.d.ts |
| 新增API | NA | 类名：AVSessionErrorCode；  API声明：ERR\_CODE\_SERVICE\_NOT\_RUNNING = 6700101  差异内容：ERR\_CODE\_SERVICE\_NOT\_RUNNING = 6700101 | api/@ohos.multimedia.avsession.d.ts |
