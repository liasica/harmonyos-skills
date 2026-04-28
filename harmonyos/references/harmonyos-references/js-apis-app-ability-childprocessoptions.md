---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessoptions
title: @ohos.app.ability.ChildProcessOptions (子进程启动选项)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ChildProcessOptions (子进程启动选项)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eecec587972c71857a2bf0a792d652a1e636b4f40aef88c9993e3824feb4bcbc
---

子进程的启动配置选项。通过[childProcessManager](js-apis-app-ability-childprocessmanager.md)启动子进程时，可以通过ChildProcessOptions配置子进程启动选项。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ChildProcessOptions } from '@kit.AbilityKit';
```

## ChildProcessOptions

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isolationMode | boolean | 否 | 是 | 控制子进程的沙箱隔离级别及网络访问权限。true表示子进程运行在独立沙箱环境中，且无法访问网络；false表示子进程与主进程共享沙箱和网络环境。默认为false。 |
| isolationUid21+ | boolean | 否 | 是 | 控制子进程是否使用独立的uid。true表示子进程运行拥有独立的uid；false表示子进程与主进程拥有相同uid。默认为false。仅在isolationMode为true时生效。 |

**示例：**

子进程部分：

```
1. // 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
2. // entry/src/main/ets/process/DemoProcess.ets
3. import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

5. export default class DemoProcess extends ChildProcess {
6. onStart(args?: ChildProcessArgs) {
7. let entryParams = args?.entryParams;
8. let fd = args?.fds?.key1;
9. // 子进程代码逻辑
10. }
11. }
```

主进程部分：

```
1. // 使用childProcessManager.startArkChildProcess方法启动子进程:
2. // entry/src/main/ets/pages/Index.ets
3. import { ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import DemoProcess from '../process/DemoProcess';

7. @Entry
8. @Component
9. struct Index {
10. build() {
11. Row() {
12. Column() {
13. Text('Click')
14. .fontSize(30)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. try {
18. DemoProcess.toString(); // 这里调用DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
19. let options: ChildProcessOptions = {
20. isolationMode: false,
21. isolationUid: false
22. };
23. let args: ChildProcessArgs = {
24. entryParams: "testParam",
25. };
26. childProcessManager.startArkChildProcess("entry/ets/process/DemoProcess.ets", args, options)
27. .then((pid) => {
28. console.info(`startChildProcess success, pid: ${pid}`);
29. })
30. .catch((err: BusinessError) => {
31. console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
32. });
33. } catch (err) {
34. console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
35. }
36. });
37. }
38. .width('100%')
39. }
40. .height('100%')
41. }
42. }
```
