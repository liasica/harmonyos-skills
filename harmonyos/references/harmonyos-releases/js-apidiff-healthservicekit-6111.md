---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-healthservicekit-6111
title: Health Service Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Health Service Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:f9071eb8711ba96576190c010b5cca36329e51335b309b3a40c2e0556719011a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：workout；  API声明：interface SportInfo  差异内容：interface SportInfo | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportInfo；  API声明：sportType: number;  差异内容：sportType: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportInfo；  API声明：sportState: SportState;  差异内容：sportState: SportState; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function getCurrentSportInfo(): Promise<SportInfo>;  差异内容：function getCurrentSportInfo(): Promise<SportInfo>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：enum SportState  差异内容：enum SportState | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportState；  API声明：IDLE = 0  差异内容：IDLE = 0 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportState；  API声明：READY = 1  差异内容：READY = 1 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportState；  API声明：RUNNING = 2  差异内容：RUNNING = 2 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportState；  API声明：PAUSED = 3  差异内容：PAUSED = 3 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SportState；  API声明：STOPPED = 4  差异内容：STOPPED = 4 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：healthDataTypes；  API声明：const MENSTRUAL\_CYCLE: healthStore.DataType;  差异内容：const MENSTRUAL\_CYCLE: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：type MenstrualCycle = {  status: number;  remarks?: string;  };  差异内容：type MenstrualCycle = {  status: number;  remarks?: string;  }; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：type MenstrualCycleDetail = {  menstrualFlow?: MenstrualFlow[];  dysmenorrhea?: Dysmenorrhea[];  physicalSymptoms?: PhysicalSymptoms[];  mood?: Mood[];  skin?: Skin[];  sexuality?: Sexuality[];  ovulationTestPaper?: OvulationTestPaper[];  cervicalMucus?: CervicalMucus[];  };  差异内容：type MenstrualCycleDetail = {  menstrualFlow?: MenstrualFlow[];  dysmenorrhea?: Dysmenorrhea[];  physicalSymptoms?: PhysicalSymptoms[];  mood?: Mood[];  skin?: Skin[];  sexuality?: Sexuality[];  ovulationTestPaper?: OvulationTestPaper[];  cervicalMucus?: CervicalMucus[];  }; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface MenstrualFlow  差异内容：interface MenstrualFlow | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：MenstrualFlow；  API声明：volume: number;  差异内容：volume: number; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface Dysmenorrhea  差异内容：interface Dysmenorrhea | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：Dysmenorrhea；  API声明：level: number;  差异内容：level: number; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface PhysicalSymptoms  差异内容：interface PhysicalSymptoms | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：PhysicalSymptoms；  API声明：physicalSymptoms: string;  差异内容：physicalSymptoms: string; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface Mood  差异内容：interface Mood | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：Mood；  API声明：mood: string;  差异内容：mood: string; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface Skin  差异内容：interface Skin | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：Skin；  API声明：skinStatus: string;  差异内容：skinStatus: string; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface Sexuality  差异内容：interface Sexuality | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：Sexuality；  API声明：sexuality: number;  差异内容：sexuality: number; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface OvulationTestPaper  差异内容：interface OvulationTestPaper | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：OvulationTestPaper；  API声明：result: number;  差异内容：result: number; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：interface CervicalMucus  差异内容：interface CervicalMucus | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：CervicalMucus；  API声明：cervicalMucus: number;  差异内容：cervicalMucus: number; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthModels；  API声明：type MenstrualCycle = healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail>;  差异内容：type MenstrualCycle = healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail>; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthSequenceHelper；  API声明：namespace menstrualCycle  差异内容：namespace menstrualCycle | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：menstrualCycle；  API声明：const DATA\_TYPE: healthStore.DataType;  差异内容：const DATA\_TYPE: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：menstrualCycle；  API声明：type Model = healthModels.MenstrualCycle;  差异内容：type Model = healthModels.MenstrualCycle; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：menstrualCycle；  API声明：type Fields = healthFields.MenstrualCycle;  差异内容：type Fields = healthFields.MenstrualCycle; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：menstrualCycle；  API声明：type DetailFields = healthFields.MenstrualCycleDetail;  差异内容：type DetailFields = healthFields.MenstrualCycleDetail; | api/@hms.health.store.d.ts |
