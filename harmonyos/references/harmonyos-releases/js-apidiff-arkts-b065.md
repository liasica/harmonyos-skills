---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b065
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2106a46807e5c6165485fd6a95c158a8b26d76315068225d922aa7e6e6b104e8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：LightWeightSet；  API声明：equal(obj: Object): boolean;  差异内容：NA | 类名：LightWeightSet；  API声明：equal(obj: Object): boolean;  差异内容：12 | api/@ohos.util.LightWeightSet.d.ts |
| 错误码变更 | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：10200003,10200006,10200025,10200051,401 | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：10200006,10200025,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool；  API声明：function execute(func: Function, ...args: Object[]): Promise<Object>;  差异内容：10200003,10200006,10200014,401 | 类名：taskpool；  API声明：function execute(func: Function, ...args: Object[]): Promise<Object>;  差异内容：10200006,10200014,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：10200003,10200006,10200014,10200051,401 | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：10200006,10200014,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool；  API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void;  差异内容：10200003,10200006,10200014,10200028,10200050,401 | 类名：taskpool；  API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void;  差异内容：10200006,10200014,10200028,10200050,401 | api/@ohos.taskpool.d.ts |
