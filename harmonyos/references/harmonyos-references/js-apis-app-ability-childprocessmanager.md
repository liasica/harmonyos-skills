---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager
title: @ohos.app.ability.childProcessManager (子进程管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.childProcessManager (子进程管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2bb954b6ddac9454a37d1b80ad2b526e89b7ff1f6686a46d4aee9e9d64b06163
---

childProcessManager模块提供子进程管理能力，支持子进程创建和启动操作。

创建的子进程会随着父进程的退出而退出，无法脱离父进程独立运行。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 约束限制

PhonePC/2in1TabletTVWearable

* 通过本模块中接口创建的子进程有如下限制:

  + 创建的子进程不支持创建UI界面。
  + 创建的子进程不支持依赖Context的API调用（包括Context模块自身API及将Context实例作为入参的API）。
  + 创建的子进程内不支持再次创建子进程。
* 通过本模块中定义的创建子进程的接口和[native\_child\_process.h](capi-native-child-process-h.md)中定义的创建子进程的接口启动的子进程总数最大为512个（系统资源充足情况下），其中[startChildProcess](js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartchildprocess)接口在SELF\_FORK模式下启动的子进程不计入总数内。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { childProcessManager } from '@kit.AbilityKit';
```

## StartMode

PhonePC/2in1TabletTVWearable

子进程启动模式枚举。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELF\_FORK | 0 | 从App自身进程Fork子进程。以该模式启动的子进程会继承父进程资源，不能使用Binder IPC和其他进程通信，否则会导致子进程崩溃退出。 |
| APP\_SPAWN\_FORK | 1 | 从AppSpawn Fork子进程。以该模式启动的子进程不会继承父进程资源，可以使用Binder IPC和其他进程通信。 |

## childProcessManager.startChildProcess

PhonePC/2in1TabletTVWearable

startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>

启动[ArkTS子进程](../harmonyos-guides/ability-terminology.md#arkts子进程)。使用Promise异步回调。

说明

调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数，[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数执行完后子进程会自动销毁。

调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcEntry | string | 是 | 子进程源文件路径，只支持源文件放在entry类型的模块中，以src/main为根目录。例如子进程文件在entry模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"./ets/process/DemoProcess.ets"。  另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码） |
| startMode | [StartMode](js-apis-app-ability-childprocessmanager.md#startmode) | 是 | 子进程启动模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回子进程pid。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000062 | The number of child processes exceeds the upper limit. |

**示例：**

```
1. // 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
2. // entry/src/main/ets/process/DemoProcess.ets
3. import { ChildProcess } from '@kit.AbilityKit';

5. export default class DemoProcess extends ChildProcess {
6. onStart() {
7. console.info('DemoProcess OnStart() called');
8. }
9. }
```

```
1. // 使用childProcessManager.startChildProcess方法启动子进程:
2. // entry/src/main/ets/tool/Tool.ets
3. import { childProcessManager } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import DemoProcess from '../process/DemoProcess';

7. try {
8. DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
9. childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK)
10. .then((data) => {
11. console.info(`startChildProcess success, pid: ${data}`);
12. }, (err: BusinessError) => {
13. console.error(`startChildProcess error, errorCode: ${err.code}`);
14. })
15. } catch (err) {
16. console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
17. }
```

## childProcessManager.startChildProcess

PhonePC/2in1TabletTVWearable

startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void

启动[ArkTS子进程](../harmonyos-guides/ability-terminology.md#arkts子进程)。使用callback异步回调。

说明

调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数，[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数执行完后子进程会自动销毁。

调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcEntry | string | 是 | 子进程源文件路径，只支持源文件放在entry类型的模块中，以src/main为根目录。例如子进程文件在entry模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"./ets/process/DemoProcess.ets"。  另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码） |
| startMode | [StartMode](js-apis-app-ability-childprocessmanager.md#startmode) | 是 | 子进程启动模式。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当子进程启动成功，err为undefined，data为获取到的子进程pid；否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000062 | The number of child processes exceeds the upper limit. |

**示例：**

```
1. // 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
2. // entry/src/main/ets/process/DemoProcess.ets
3. import { ChildProcess } from '@kit.AbilityKit';

5. export default class DemoProcess extends ChildProcess {
6. onStart() {
7. console.info('DemoProcess OnStart() called');
8. }
9. }
```

```
1. // 使用childProcessManager.startChildProcess方法启动子进程:
2. // entry/src/main/ets/tool/Tool.ets
3. import { childProcessManager } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import DemoProcess from '../process/DemoProcess';

7. try {
8. DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
9. childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK, (err, data) => {
10. if (data) {
11. console.info(`startChildProcess success, pid: ${data}`);
12. } else {
13. console.error(`startChildProcess error, errorCode: ${err.code}`);
14. }
15. });
16. } catch (err) {
17. console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
18. }
```

## childProcessManager.startArkChildProcess12+

PhonePC/2in1TabletTVWearable

startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>

启动[ArkTS子进程](../harmonyos-guides/ability-terminology.md#arkts子进程)。使用Promise异步回调。

说明

调用该接口创建的子进程不会继承父进程资源，子进程创建成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数。[ChildProcess.onStart](js-apis-app-ability-childprocess.md#childprocessonstart)函数执行完后子进程不会自动销毁，需要子进程调用[process.abort](js-apis-process.md#processabort)销毁。调用该接口的进程销毁后，所创建的子进程也会一并销毁。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcEntry | string | 是 | 子进程源文件路径，不支持源文件放在HAR类型的模块中。由“模块名” + “/” + “文件路径”组成，文件路径以src/main为根目录。例如子进程文件在module1模块下src/main/ets/process/DemoProcess.ets，则srcEntry为"module1/ets/process/DemoProcess.ets"。  另外，需要确保子进程源文件被其它文件引用到，防止被构建工具优化掉。（详见下方示例代码） |
| args | [ChildProcessArgs](js-apis-app-ability-childprocessargs.md) | 是 | 传递到子进程的参数。 |
| options | [ChildProcessOptions](js-apis-app-ability-childprocessoptions.md) | 否 | 子进程的启动配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回子进程pid。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000062 | The number of child processes exceeds the upper limit. |

**示例：**

子进程部分：

```
1. // 在module1模块的src/main/ets/process下创建DemoProcess.ets子进程类:
2. // module1/src/main/ets/process/DemoProcess.ets
3. import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

5. export default class DemoProcess extends ChildProcess {

7. onStart(args?: ChildProcessArgs) {
8. let entryParams = args?.entryParams;
9. let fd = args?.fds?.key1;
10. // ..
11. }
12. }
```

主进程部分，示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)：

```
1. // 使用childProcessManager.startArkChildProcess方法启动子进程:
2. // module1/src/main/ets/tool/Tool.ets
3. import { common, ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import DemoProcess from '../process/DemoProcess';

8. @Entry
9. @Component
10. struct Index {
11. build() {
12. Row() {
13. Column() {
14. Text('Click')
15. .fontSize(30)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. try {
19. DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
20. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
21. let path = context.filesDir + "/test.txt";
22. let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
23. let args: ChildProcessArgs = {
24. entryParams: "testParam",
25. fds: {
26. "key1": file.fd
27. }
28. };
29. let options: ChildProcessOptions = {
30. isolationMode: false
31. };
32. childProcessManager.startArkChildProcess("module1/ets/process/DemoProcess.ets", args, options)
33. .then((pid) => {
34. console.info(`startChildProcess success, pid: ${pid}`);
35. })
36. .catch((err: BusinessError) => {
37. console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
38. })
39. } catch (err) {
40. console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
41. }
42. });
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }
48. }
```

## childProcessManager.startNativeChildProcess13+

PhonePC/2in1TabletTVWearable

startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>

启动[Native子进程](../harmonyos-guides/ability-terminology.md#native子进程)。使用Promise异步回调。

说明

调用该接口创建的子进程不会继承父进程资源，子进程创建成功会返回子进程pid，然后加载参数中指定的动态链接库文件并执行子进程的入口函数，入口函数执行完后子进程会自动销毁。调用该接口的进程销毁后，所创建的子进程也会一并销毁。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entryPoint | string | 是 | 子进程中调用动态库的符号和入口函数，中间用“:”隔开（例如“libentry.so:Main”)。 |
| args | [ChildProcessArgs](js-apis-app-ability-childprocessargs.md) | 是 | 传递到子进程的参数。 |
| options | [ChildProcessOptions](js-apis-app-ability-childprocessoptions.md) | 否 | 子进程的启动配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回子进程pid。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000062 | The number of child processes exceeds the upper limit. |

**示例：**

子进程部分，详见[Native子进程开发指导（C/C++）- 创建支持参数传递的Native子进程](../harmonyos-guides/capi-nativechildprocess-development-guideline.md#创建支持参数传递的native子进程)：

```
1. #include <AbilityKit/native_child_process.h>

3. extern "C" {

5. /**
6. * 子进程的入口函数，实现子进程的业务逻辑
7. * 函数名称可以自定义，在主进程调用OH_Ability_StartNativeChildProcess方法时指定，此示例中为Main
8. * 函数返回后子进程退出
9. */
10. void Main(NativeChildProcess_Args args)
11. {
12. // 获取传入的entryPrams
13. char *entryParams = args.entryParams;
14. // 获取传入的fd列表，对应ChildProcessArgs中的args.fds
15. NativeChildProcess_Fd *current = args.fdList.head;
16. while (current != nullptr) {
17. char *fdName = current->fdName;
18. int32_t fd = current->fd;
19. current = current->next;
20. // 业务逻辑..
21. }
22. }
23. } // extern "C"
```

主进程部分，示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)：

```
1. // 主进程：
2. // 使用childProcessManager.startNativeChildProcess方法启动子进程:
3. import { common, ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

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
18. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
19. let path = context.filesDir + "/test.txt";
20. let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
21. let args: ChildProcessArgs = {
22. entryParams: "testParam",
23. fds: {
24. "key1": file.fd
25. }
26. };
27. let options: ChildProcessOptions = {
28. isolationMode: false
29. };
30. childProcessManager.startNativeChildProcess("libentry.so:Main", args, options)
31. .then((pid) => {
32. console.info(`startChildProcess success, pid: ${pid}`);
33. })
34. .catch((err: BusinessError) => {
35. console.error(`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}`);
36. })
37. } catch (err) {
38. console.error(`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}`);
39. }
40. });
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```
