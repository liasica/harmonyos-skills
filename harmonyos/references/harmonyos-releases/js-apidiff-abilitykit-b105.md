---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-b105
title: Ability Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:18a8b5843e41e17d46e7f204de4452d0d5bda6cd4a28cd5803df48bdf3d59dd1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：childProcessManager；  API声明：function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;  差异内容：16000050,16000061,401,801 | 类名：childProcessManager；  API声明：function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;  差异内容：16000050,16000061,16000062,401,801 | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：childProcessManager；  API声明：function startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;  差异内容：function startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>; | api/@ohos.app.ability.childProcessManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getLaunchWant(): Want;  差异内容：function getLaunchWant(): Want; | api/@ohos.bundle.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationContext；  API声明：setFontSizeScale(fontSizeScale: number): void;  差异内容：setFontSizeScale(fontSizeScale: number): void; | api/application/ApplicationContext.d.ts |
| 删除API | 类名：bundleManager；  API声明：function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void;  差异内容：function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void; | NA | api/@ohos.bundle.bundleManager.d.ts |
| 删除API | 类名：bundleManager；  API声明：function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>;  差异内容：function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>; | NA | api/@ohos.bundle.bundleManager.d.ts |
| 删除API | 类名：bundleManager；  API声明：function deleteAbc(abcPath: string): Promise<void>;  差异内容：function deleteAbc(abcPath: string): Promise<void>; | NA | api/@ohos.bundle.bundleManager.d.ts |
