---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-26011
title: Wear Engine Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Wear Engine Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:76c7e4b8a2a95fe00e129fcfc6e53df9d652f25a22ad0de4ef0c14aac7391e3a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace watchFace  差异内容：declare namespace watchFace | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：function isWatchFaceSupport(): Promise<boolean>;  差异内容：function isWatchFaceSupport(): Promise<boolean>; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：function getWatchFaceManager(context: common.UIAbilityContext): WatchFaceManager;  差异内容：function getWatchFaceManager(context: common.UIAbilityContext): WatchFaceManager; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface WatchFaceManager  差异内容：interface WatchFaceManager | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：WatchFaceManager；  API声明：addWatchFace(config: WatchFaceConfigUnion): Promise<void>;  差异内容：addWatchFace(config: WatchFaceConfigUnion): Promise<void>; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：WatchFaceManager；  API声明：generatePreviews(configs: WatchFaceConfigUnion[]): Promise<image.PixelMap[]>;  差异内容：generatePreviews(configs: WatchFaceConfigUnion[]): Promise<image.PixelMap[]>; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：type WatchFaceConfigUnion = VibrantWatchFaceConfig | ClassicWatchFaceConfig;  差异内容：type WatchFaceConfigUnion = VibrantWatchFaceConfig | ClassicWatchFaceConfig; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface VibrantWatchFaceConfig  差异内容：interface VibrantWatchFaceConfig | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantWatchFaceConfig；  API声明：defaultStyle: Style.VIBRANT;  差异内容：defaultStyle: Style.VIBRANT; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantWatchFaceConfig；  API声明：containers?: VibrantContainersConfig;  差异内容：containers?: VibrantContainersConfig; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantWatchFaceConfig；  API声明：isCurrentAppFormsOnly?: boolean;  差异内容：isCurrentAppFormsOnly?: boolean; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface ClassicWatchFaceConfig  差异内容：interface ClassicWatchFaceConfig | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicWatchFaceConfig；  API声明：defaultStyle: Style.CLASSIC;  差异内容：defaultStyle: Style.CLASSIC; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicWatchFaceConfig；  API声明：containers?: ClassicContainersConfig;  差异内容：containers?: ClassicContainersConfig; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicWatchFaceConfig；  API声明：isCurrentAppFormsOnly?: boolean;  差异内容：isCurrentAppFormsOnly?: boolean; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：enum Style  差异内容：enum Style | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Style；  API声明：VIBRANT = 2  差异内容：VIBRANT = 2 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Style；  API声明：CLASSIC = 3  差异内容：CLASSIC = 3 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：enum Position  差异内容：enum Position | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：TOP\_LEFT = 'top\_left'  差异内容：TOP\_LEFT = 'top\_left' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：TOP\_CENTER = 'top\_center'  差异内容：TOP\_CENTER = 'top\_center' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：TOP\_RIGHT = 'top\_right'  差异内容：TOP\_RIGHT = 'top\_right' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：MIDDLE\_LEFT = 'middle\_left'  差异内容：MIDDLE\_LEFT = 'middle\_left' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：MIDDLE\_CENTER = 'middle\_center'  差异内容：MIDDLE\_CENTER = 'middle\_center' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：MIDDLE\_RIGHT = 'middle\_right'  差异内容：MIDDLE\_RIGHT = 'middle\_right' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：BOTTOM\_LEFT = 'bottom\_left'  差异内容：BOTTOM\_LEFT = 'bottom\_left' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：BOTTOM\_CENTER = 'bottom\_center'  差异内容：BOTTOM\_CENTER = 'bottom\_center' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：Position；  API声明：BOTTOM\_RIGHT = 'bottom\_right'  差异内容：BOTTOM\_RIGHT = 'bottom\_right' | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface VibrantContainersConfig  差异内容：interface VibrantContainersConfig | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantContainersConfig；  API声明：[Position.TOP\_LEFT]?: ContainerConfig1x1;  差异内容：[Position.TOP\_LEFT]?: ContainerConfig1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantContainersConfig；  API声明：[Position.BOTTOM\_LEFT]?: ContainerConfig2x2;  差异内容：[Position.BOTTOM\_LEFT]?: ContainerConfig2x2; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantContainersConfig；  API声明：[Position.MIDDLE\_RIGHT]?: ContainerConfig1x1;  差异内容：[Position.MIDDLE\_RIGHT]?: ContainerConfig1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：VibrantContainersConfig；  API声明：[Position.BOTTOM\_RIGHT]?: ContainerConfig1x1;  差异内容：[Position.BOTTOM\_RIGHT]?: ContainerConfig1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface ClassicContainersConfig  差异内容：interface ClassicContainersConfig | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicContainersConfig；  API声明：[Position.BOTTOM\_LEFT]?: ContainerConfig2x2;  差异内容：[Position.BOTTOM\_LEFT]?: ContainerConfig2x2; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicContainersConfig；  API声明：[Position.MIDDLE\_RIGHT]?: ContainerConfig1x1;  差异内容：[Position.MIDDLE\_RIGHT]?: ContainerConfig1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ClassicContainersConfig；  API声明：[Position.BOTTOM\_RIGHT]?: ContainerConfig1x1;  差异内容：[Position.BOTTOM\_RIGHT]?: ContainerConfig1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface ContainerConfig1x1  差异内容：interface ContainerConfig1x1 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerConfig1x1；  API声明：defaultOptions?: ContainerOption1x1;  差异内容：defaultOptions?: ContainerOption1x1; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerConfig1x1；  API声明：options?: ContainerOption1x1[];  差异内容：options?: ContainerOption1x1[]; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface ContainerConfig2x2  差异内容：interface ContainerConfig2x2 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerConfig2x2；  API声明：defaultForm?: FormInfo;  差异内容：defaultForm?: FormInfo; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerConfig2x2；  API声明：defaultOptions?: ContainerOption2x2;  差异内容：defaultOptions?: ContainerOption2x2; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerConfig2x2；  API声明：options?: ContainerOption2x2[];  差异内容：options?: ContainerOption2x2[]; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：interface FormInfo  差异内容：interface FormInfo | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：name: string;  差异内容：name: string; | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：enum ContainerOption1x1  差异内容：enum ContainerOption1x1 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：WORKOUT = 7  差异内容：WORKOUT = 7 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：WORKOUT\_RECORDS = 8  差异内容：WORKOUT\_RECORDS = 8 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：VO2MAX = 9  差异内容：VO2MAX = 9 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：ACTIVITY\_RECORDS = 10  差异内容：ACTIVITY\_RECORDS = 10 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：MOVEMENT = 11  差异内容：MOVEMENT = 11 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：EXERCISE = 12  差异内容：EXERCISE = 12 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：STAND = 13  差异内容：STAND = 13 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：STEPS = 14  差异内容：STEPS = 14 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：EMOTIONS = 15  差异内容：EMOTIONS = 15 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：STRESS\_VALUE = 16  差异内容：STRESS\_VALUE = 16 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：HEART\_RATE\_VALUE = 17  差异内容：HEART\_RATE\_VALUE = 17 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：SPO2 = 18  差异内容：SPO2 = 18 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：SLEEP\_DURATION = 19  差异内容：SLEEP\_DURATION = 19 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：WECHAT = 20  差异内容：WECHAT = 20 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：ALIPAY = 21  差异内容：ALIPAY = 21 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：TEMP = 22  差异内容：TEMP = 22 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：AQI = 23  差异内容：AQI = 23 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：UV\_INDEX = 24  差异内容：UV\_INDEX = 24 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：SUNRISE\_SUNSET = 25  差异内容：SUNRISE\_SUNSET = 25 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：MOONRISE\_MOONSET = 26  差异内容：MOONRISE\_MOONSET = 26 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：MOON\_PHASE = 27  差异内容：MOON\_PHASE = 27 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：ALTITUDE = 28  差异内容：ALTITUDE = 28 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：AIR\_PRESSURE = 29  差异内容：AIR\_PRESSURE = 29 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：DATE = 30  差异内容：DATE = 30 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：LUNAR\_DATE = 32  差异内容：LUNAR\_DATE = 32 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：WORLD\_CLOCK = 33  差异内容：WORLD\_CLOCK = 33 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：STOPWATCH = 34  差异内容：STOPWATCH = 34 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：TIMER = 35  差异内容：TIMER = 35 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：ALARM = 36  差异内容：ALARM = 36 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：COMPASS = 37  差异内容：COMPASS = 37 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：BATTERY = 38  差异内容：BATTERY = 38 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption1x1；  API声明：WECHAT\_PAY = 76  差异内容：WECHAT\_PAY = 76 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：watchFace；  API声明：enum ContainerOption2x2  差异内容：enum ContainerOption2x2 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：WORKOUT = 59  差异内容：WORKOUT = 59 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：RECOVERY = 60  差异内容：RECOVERY = 60 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：ACTIVITY\_RECORDS = 61  差异内容：ACTIVITY\_RECORDS = 61 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：ACTIVITY\_DATA = 62  差异内容：ACTIVITY\_DATA = 62 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：EMOTIONS = 63  差异内容：EMOTIONS = 63 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：STRESS\_LEVEL = 64  差异内容：STRESS\_LEVEL = 64 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：HEART\_RATE\_VALUE = 65  差异内容：HEART\_RATE\_VALUE = 65 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：SPO2 = 66  差异内容：SPO2 = 66 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：RECENT\_SLEEP = 67  差异内容：RECENT\_SLEEP = 67 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：MEDIA\_PLAYER = 68  差异内容：MEDIA\_PLAYER = 68 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：TODAY\_WEATHER = 69  差异内容：TODAY\_WEATHER = 69 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：MOON\_PHASE = 70  差异内容：MOON\_PHASE = 70 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：WEATHER\_COMBO = 71  差异内容：WEATHER\_COMBO = 71 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：UPCOMING\_EVENTS = 72  差异内容：UPCOMING\_EVENTS = 72 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：BATTERY = 73  差异内容：BATTERY = 73 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：CUTE\_PET\_MYSTERY\_BOX = 74  差异内容：CUTE\_PET\_MYSTERY\_BOX = 74 | api/@hms.health.watchFace.d.ts |
| 新增API | NA | 类名：ContainerOption2x2；  API声明：EMOTIONAL\_PET = 75  差异内容：EMOTIONAL\_PET = 75 | api/@hms.health.watchFace.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.health.watchFace.d.ts  差异内容：WearEngine | api/@hms.health.watchFace.d.ts |
