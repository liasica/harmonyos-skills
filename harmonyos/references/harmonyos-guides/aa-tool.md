---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool
title: aa工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > aa工具
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:17+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d234112c5ed3a002722a37c4913b564e94aa587dde27dbf267e1d10a1a27a71e
---

Ability assistant（Ability助手，简称为aa），是用于启动应用和启动测试用例的工具，为开发者提供基本的应用调试和测试能力，例如启动应用组件、强制停止进程、打印应用组件相关信息等。

## 环境要求

在使用本工具前，开发者需要先获取[hdc工具](hdc.md#环境准备)，执行hdc shell。

本文中命令介绍均基于交互式命令环境。如果直接执行hdc shell [aa命令]，则需要采用""来包裹aa命令，确保命令中的传参能被正确识别。示例如下：

```
1. # 启动命令
2. hdc shell "aa start -A ohos.want.action.viewData -U 'https://www.example.com'"

4. # 应用调试/调优命令
5. hdc shell "aa process -b com.example.myapplication -a EntryAbility -p perf-cmd"
```

## aa工具命令列表

| 命令 | 描述 |
| --- | --- |
| -h/help | 帮助命令。用于查询aa支持的命令信息。 |
| start | 启动命令。用于启动一个应用组件，目标组件可以是FA模型的PageAbility和ServiceAbility组件，也可以是Stage模型的UIAbility和ServiceExtensionAbility组件，且目标组件相应配置文件中的exported标签不能配置为false。 |
| stop-service | 停止命令。用于停止一个应用组件，目标组件可以是FA模型的ServiceAbility组件，也可以是Stage模型的ExtensionAbility组件。 |
| dump(deprecated) | 打印命令。用于打印应用组件的相关信息。 |
| force-stop | 强制停止进程命令。通过bundleName强制停止一个进程。 |
| test | 启动测试框架命令。根据所携带的参数启动测试框架。 |
| attach | 进入调试模式命令。通过bundleName使指定应用进入调试模式。 |
| detach | 退出调试模式命令。通过bundleName使指定应用退出调试模式。 |
| appdebug | 等待调试命令。用于设置、取消设置应用等待调试状态，以及获取处于等待调试状态的应用包名和持久化信息。等待调试状态只对debug类型应用生效。appdebug的设置命令只对单个应用生效，当重复设置时，应用包名与持久化状态会替换成最新设置内容。 |
| process | 应用调试/调优命令。对应用进行调试或调优，IDE用该命令集成调试和调优工具。 |
| send-memory-level | onMemoryLevel回调命令。指定进程的pid和内存使用级别来触发该进程的onMemoryLevel生命周期回调。 |

## 帮助命令（help）

```
1. # 显示帮助信息
2. aa help
```

## 启动命令（start）

启动一个应用组件，目标组件可以是FA模型的PageAbility和ServiceAbility组件，也可以是Stage模型的UIAbility和ServiceExtensionAbility组件，且目标组件相应配置文件中的exported标签不能配置为false。

```
1. # 显示启动Ability。
2. # 如果需要启动分身应用，可以使用[--pi ohos.extra.param.key.appCloneIndex <unsigned integer-value>]来指定分身应用的索引。
3. aa start [-d <deviceId>] [-a <abilityName> -b <bundleName>] [-m <moduleName>] [-c] [-E] [-D] [-R] [-S] [-W] [--pi <key> <unsigned integer-value>] [--pb <key> <bool-value: true/false/t/f大小写不敏感] [--ps <key> <value>] [--psn <key>] [--wl <windowLeft>] [--wt <windowTop>] [--wh <windowHeight>] [--ww <windowWidth>] [-p <perf-cmd>]

5. # 隐式启动Ability。如果命令中的参数都不填，会导致启动失败。
6. aa start [-d <deviceId>] [-U <URI>] [-t <type>] [-A <action>] [-e <entity>] [-c] [-D] [-E] [-R] [--pi <key> <unsigned integer-value>] [--pb <key> <bool-value: true/false/t/f大小写不敏感] [--ps <key> <value>] [--psn <key>] [--wl <windowLeft>] [--wt <windowTop>] [--wh <windowHeight>] [--ww <windowWidth>] [-p <perf-cmd>]
```

**启动命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -d | 可选参数，deviceId。 |
| -a | 可选参数，abilityName。 |
| -b | 可选参数，bundleName。 |
| -m | 可选参数，moduleName。 |
| -U | 可选参数，URI。  **说明：** 仅支持传递字符串。 |
| -A | 可选参数，action。 |
| -e | 可选参数，entity。 |
| -t | 可选参数，type。 |
| --pi | 可选参数，整型类型键值对。  **说明：** 仅支持无符号整型值。 |
| --pb | 可选参数，布尔类型键值对。 |
| --ps | 可选参数，字符串类型键值对。  **说明：** 字符串值不能以中划线“-”开头。 |
| --psn | 可选参数，空字符串关键字。 |
| --wl | 可选参数，windowLeft，窗口左边距，单位px。  **约束：**  仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。 |
| --wt | 可选参数，windowTop，窗口上边距，单位px。  **约束：**  仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。 |
| --wh | 可选参数，windowHeight，窗口高度，单位px。  **约束：**  仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。 |
| --ww | 可选参数，windowWidth，窗口宽度，单位px。  **约束：**  仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。 |
| -c | 可选参数，调试时是否通过跨端迁移启动Ability。携带该参数代表跨端迁移场景，不携带代表非跨端迁移场景。 |
| -E | 可选参数，调试时是否显示详细的异常信息。携带该参数代表显示，不携带代表不显示。  **说明：** 从API version 14开始，支持该参数。 |
| -R | 可选参数，调试时是否开启多线程错误检测。携带该参数代表开启，不携带代表关闭。  **说明：** 从API version 14开始，支持该参数。 |
| -S | 可选参数，调试时是否进入应用沙箱。携带该参数代表进入，不携带代表不进入。 |
| -D | 可选参数，调试模式。 |
| -N | 可选参数，使能启动阶段调试。 |
| -C | 可选参数，使能ASan调试。 |
| -p | 可选参数，调优命令。命令由调用方自定义。 |
| -W | 可选参数，调优命令。用于测量UIAbility从启动到切换至前台状态耗时。  **说明：**  - 从API version 20开始支持，支持该参数。  - 仅当显式启动UIAbility（必须携带-b和-a参数）时，该参数生效。  **正常情况的返回信息如下：**  - StartMode：UIAbility启动模式，值：Cold（冷启动）/Hot（热启动）。  - BundleName：目标应用bundleName。  - AbilityName：目标应用abilityName。  - ModuleName：目标应用moduleName，命令中带有"-m"参数时会打印moduleName，否则不打印。  - TotalTime：  冷启动场景下，系统侧接收到aa启动UIAbility请求到该UIAbility完成首帧绘制的耗时，单位毫秒（ms）。  热启动场景下，系统侧接收到aa启动UIAbility请求到该UIAbility状态切换至前台的耗时，单位毫秒（ms）。  - WaitTime：命令启动到命令执行结束的耗时，单位毫秒（ms）。  **异常情况的返回信息如下：**  - "The wait option does not support starting implicit" ：不支持隐式启动。  - "The wait option does not support starting non-uiability" ：不支持启动非UIAbility组件。 |

**返回值**：

当启动成功时，返回"start ability successfully."；当启动失败时，返回"error: failed to start ability."，同时会包含相应的失败信息。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10103001 | Failed to verify the visibility of the target ability. |
| 10104001 | The specified ability does not exist. |
| 10105001 | Failed to connect to the ability service. |
| 10105002 | Failed to obtain ability information. |
| 10106002 | The aa start command's window option or the aa test command does not support app with release signature. |
| 10100101 | Failed to obtain application information. |
| 10100102 | The aa start command cannot be used to launch a UIExtensionAbility. |
| 10103101 | Failed to find a matching application for implicit launch. |
| 10103102 | The passed appCloneIndex is invalid. |
| 10106101 | The current ability will be placed in the queue to wait for the previous ability to finish launching. |
| 10106102 | The device screen is locked during the application launch. |
| 10106103 | The target application is an expired crowdtesting application. |
| 10106105 | The target application is under control. |
| 10106106 | The target application is managed by EDM. |
| 10106107 | The current device does not support using window options. |
| 10107102 | Permission verification failed for the specified process. |
| 10108101 | An internal error occurs while attempting to launch the ability. |

**示例**：

以隐式启动Ability为例。

说明

本例中仅介绍了部分字段的使用。关于Ability匹配的详细规则参考[显式Want与隐式Want匹配规则](explicit-implicit-want-mappings.md)。

* **目标应用**：修改module.json5配置，为目标Ability配置uris。

  ```
  1. {
  2. "name": "TargetAbility",
  3. // ......
  4. "exported": true,
  5. "skills": [
  6. {
  7. "actions":[
  8. "ohos.want.action.viewData"
  9. ],
  10. "uris":[
  11. {
  12. "scheme": "myscheme",
  13. "host": "www.test.com",
  14. "port": "8080",
  15. "path": "path"
  16. }
  17. ]
  18. }
  19. ]
  20. }
  ```
* **拉起方应用**：隐式启动Ability。

  + 如果需要拉起应用的页面，可以使用-U命令，示例如下：

    ```
    1. aa start -U myscheme://www.test.com:8080/path
    ```
  + 在上述基础上，如果需要携带参数，可以使用如下命令：

    ```
    1. aa start -U myscheme://www.test.com:8080/path --pi paramNumber 1 --pb paramBoolean true --ps paramString teststring  --psn paramNullString
    ```

    UIAbility获取传入参数示例如下：

    ```
    1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
    2. import { hilog } from '@kit.PerformanceAnalysisKit';

    4. export default class TargetAbility extends UIAbility {
    5. onCreate(want:Want, launchParam: AbilityConstant.LaunchParam) {
    6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    7. let paramNumber = want.parameters?.paramNumber;
    8. let paramBoolean = want.parameters?.paramBoolean;
    9. let paramString = want.parameters?.paramString;
    10. let paramNullString = want.parameters?.paramNullString;
    11. }
    12. }
    ```
  + 如果需要拉起浏览器并跳转指定页面，可以使用-A -U命令，示例如下：

    本例中以https://www.example.com为例，请根据实际情况替换为真实的网址。

    ```
    1. aa start -A ohos.want.action.viewData -U https://www.example.com
    ```

## 停止命令（stop-service）

停止命令。用于停止一个应用组件，目标组件可以是FA模型的ServiceAbility组件，也可以是Stage模型的ExtensionAbility组件。

```
1. aa stop-service [-d <deviceId>] -a <abilityName> -b <bundleName> [-m <moduleName>]
```

**停止命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -d | 可选参数，deviceId。 |
| -a | 必选参数，abilityName。 |
| -b | 必选参数，bundleName。 |
| -m | 可选参数，moduleName。 |

**返回值**：

当成功停止ServiceAbility或ExtensionAbility时，返回"stop service ability successfully."；当停止失败时，返回"error: failed to stop service ability."。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10103001 | Failed to verify the visibility of the target ability. |
| 10103201 | The target ability is not of the ServiceAbility type. |
| 10104001 | The specified ability does not exist. |
| 10105001 | Failed to connect to the ability service. |
| 10105002 | Failed to obtain ability information. |

**示例**：

```
1. # 停止一个ServiceAbility
2. aa stop-service -a EntryAbility -b com.example.myapplication -m entry
```

## 打印命令（dump(deprecated)）

用于打印应用组件的相关信息。

```
1. aa dump -a
```

说明

aa dump命令从API version 7开始支持，从API version 9废弃，替换命令为[hidumper](hidumper.md) -s AbilityManagerService。

**打印命令参数列表**

| 参数 | 二级参数 | 参数说明 |
| --- | --- | --- |
| -h/--help | - | 帮助信息。 |
| -a/--all | - | 打印所有mission内的应用组件信息。 |
| -l/--mission-list | type（缺省打印全部） | 服务侧为了方便管理任务链，内部维护了4种类型的任务链。  可取值：  - NORMAL：正常启动的任务链(比如A拉起B拉起C, 则对应的任务链是A->B->C)  - DEFAULT\_STANDARD：已经被破坏的任务链中的任务, 启动模式为multiton的任务被放到该任务链中, 这里面的任务之间没有关联关系  - DEFAULT\_SINGLE：已经被破坏的任务链中的任务, 启动模式为singleton的任务被放到该任务链中, 这里面的任务之间没有关联关系  - LAUNCHER：launcher的任务链 |
| -e/--extension | elementName | 打印扩展组件信息。 |
| -u/--userId | UserId | 打印指定UserId的栈信息，需要和其他参数组合使用，例如aa dump -a -u 100、aa dump -d -u 100。 |
| -d/--data | - | 打印DataAbility相关信息。 |
| -i/--ability | AbilityRecord ID | 打印指定应用组件详细信息。 |
| -c/--client | - | 打印应用组件详细信息，需要和其他参数组合使用，例如aa dump -a -c、aa dump -i 21 -c。 |
| -p/--pending | - | 打印pendingWant信息，需要和其他参数组合使用，例如aa dump -a -p。 |
| -r/--process | - | 打印应用进程信息，需要和其他参数组合使用，例如aa dump -a -r。 |

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10105001 | Failed to connect to the ability service. |

**示例**：

```
1. # 打印所有mission内的应用组件信息
2. aa dump -a
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/hNDVlDQqTmSzeff2_Go7YA/zh-cn_image_0000002558605356.png?HW-CC-KV=V1&HW-CC-Date=20260429T053415Z&HW-CC-Expire=86400&HW-CC-Sign=F42189CE337AA4A00FA691EAA0637B92AF2F889597E692E89381723532D9DC7F)

```
1. # 打印所有任务链
2. aa dump -l
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Udc-vyBGShS75JKkCZ6q_g/zh-cn_image_0000002589324883.png?HW-CC-KV=V1&HW-CC-Date=20260429T053415Z&HW-CC-Expire=86400&HW-CC-Sign=5B68CE8D2C7E37CD94ACC8895A29D25FBA499EDCBAA51C70174671FC56EDCC77)

```
1. # 打印指定应用组件详细信息
2. aa dump -i 105
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Xzgm9zT-RjePBoyp36Fmag/zh-cn_image_0000002589244819.png?HW-CC-KV=V1&HW-CC-Date=20260429T053415Z&HW-CC-Expire=86400&HW-CC-Sign=E965A1B0E1F0085D7D5B727086D48439127B66BD5CAB275576E71D2CC2D06B7F)

## 强制停止进程命令（force-stop）

通过bundleName强制停止一个进程。

```
1. aa force-stop <bundle-name> [-p pid] [-r kill-reason]
```

**强制停止进程命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -p | 指定pid，需要与-r配合使用，两者共同设置指定pid的进程退出原因。 |
| -r | 指定进程退出原因，需要与-p配合使用，两者共同设置指定pid的进程退出原因。 |

**返回值**：

当成功强制停止该进程时，返回"force stop process successfully."；当强制停止失败时，返回"error: failed to force stop process."。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10105001 | Failed to connect to the ability service. |
| 10104002 | Failed to retrieve specified package information. |
| 10106401 | Failed to terminate the process. |
| 10106402 | Persistent processes cannot be terminated. |

**示例**：

```
1. # 通过bundleName强制停止一个进程
2. aa force-stop com.example.myapplication
```

## 启动测试框架命令（test）

根据所携带的参数启动测试框架。

```
1. aa test -b <bundleName> [-m <module-name>] [-p <package-name>] [-s class <test-class>] [-s level <test-level>] [-s size <test-size>] [-s testType <test-testType>] [-s timeout <test-timeout>] [-s <any-key> <any-value>] [-w <wait-time>] -s unittest <testRunner>
```

说明

关于class、level、size、testType等参数的详细说明请参见[命令行执行测试脚本](unittest-guidelines.md#命令行执行测试脚本)。

**启动测试框架命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |
| -s unittest | 必选参数，testRunner。 |
| -p | 可选参数，testRunner的packageName。  **说明**：该可选参数仅可在FA模型下使用。 |
| -m | 可选参数，testRunner的moduleName。  **说明**：该可选参数仅可在Stage模型下使用。 |
| -s class | 可选参数，指定要执行的测试套或测试用例。 |
| -s level | 可选参数，指定要执行用例的用例级别。 |
| -s size | 可选参数，指定要执行用例的用例规模。 |
| -s testType | 可选参数，指定要执行用例的用例类型。 |
| -s timeout | 可选参数，测试用例执行的超时时间（单位ms），默认为5000。 |
| -s <any-key> | 可选参数，任意键值对。 |
| -w | 可选参数，指定测试运行时间（单位ms）。 |
| -D | 可选参数，调试模式。 |

**返回值**：

当成功启动测试框架时，返回"user test started."；当启动失败时，返回"error: failed to start user test."和对应的错误信息。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10104002 | Failed to retrieve specified package information. |
| 10105001 | Failed to connect to the ability service. |
| 10106002 | The aa start command's window option or the aa test command does not support app with release signature. |
| 10108501 | An internal error occurs during the execution of the aa test command. |

**示例**：

```
1. # 启动测试框架
2. aa test -b com.example.myapplication -s unittest ActsAbilityTest
3. # 启动测试框架并设置moduleName
4. aa test -b com.example.myapplication -m entry_test -s unittest ActsAbilityTest
5. # 启动测试框架并指定超时时间
6. aa test -b com.example.myapplication -m entry_test -s timeout 10000 -s unittest ActsAbilityTest
```

## 进入调试模式命令（attach）

通过bundleName使指定应用进入调试模式。

```
1. aa attach -b <bundleName>
```

**进入调试模式命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |

**返回值**：

当应用成功进入调试模式时，返回"attach app debug successfully."；当给定参数不合法时，返回"fail: unknown option."并打印帮助信息。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10105001 | Failed to connect to the ability service. |
| 10106001 | The current device is not in developer mode. |
| 10106002 | The aa start command's window option or the aa test command does not support app with release signature. |
| 10103601 | The specified bundleName does not exist. |
| 10108601 | An internal error occurs while attempting to enter/exit debug mode. |

**示例**：

```
1. # 通过bundleName使指定应用进入调试模式
2. aa attach -b com.example.myapplication
```

## 退出调试模式命令（detach）

通过bundleName使指定应用退出调试模式。

```
1. aa detach -b <bundleName>
```

**退出调试模式命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |

**返回值**：

当应用成功退出调试模式时，返回"detach app debug successfully."；当给定参数不合法时，返回"fail: unknown option."并打印帮助信息。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10105001 | Failed to connect to the ability service. |
| 10106001 | The current device is not in developer mode. |
| 10106002 | The aa start command's window option or the aa test command does not support app with release signature. |
| 10103601 | The specified bundleName does not exist. |
| 10108601 | An internal error occurs while attempting to enter/exit debug mode. |

**示例**：

```
1. # 通过bundleName使指定应用退出调试模式
2. aa detach -b com.example.myapplication
```

## 等待调试命令（appdebug）

用于设置、取消设置应用等待调试状态，以及获取处于等待调试状态的应用包名和持久化信息。等待调试状态只对debug类型应用生效。appdebug的设置命令只对单个应用生效，当重复设置时，应用包名与持久化状态会替换成最新设置内容。

```
1. aa appdebug -b <bundleName> [-p]
```

**等待调试命令参数列表**

| 参数 | 二级参数 | 参数说明 |
| --- | --- | --- |
| -h/--help | - | 帮助信息。 |
| -b/--bundlename | bundleName | 为指定应用设置等待调试状态。设置时，不会进行包名合法化的校验。 |
| -p/--persist | - | 可选参数；持久化标志位，加入该参数，代表持续设置应用为等待调试状态，无论重启设备、重装应用都可以持续生效；不加入该参数，代表等待调试状态仅可以在重启设备前生效一次。需要和-b参数组合使用，例如：aa appdebug -b <bundleName> -p。 |
| -c/--cancel | - | 取消等待调试状态。 |
| -g/--get | - | 获取等待调试状态的应用包名和持久化信息。 |

**返回值**：

当执行成功时，返回"app debug successfully."；当执行失败时，返回"error: failed to app debug."；当失败原因为非开发者模式时，返回"error: not developer mode."。

**错误码**：

| 错误码ID | 错误信息 |
| --- | --- |
| 10105003 | Failed to connect to the app service. |
| 10106001 | The current device is not in developer mode. |
| 10106701 | Cannot debug applications using a release certificate. |

**示例**：

```
1. # 显示帮助信息
2. aa appdebug -h

4. # 为指定应用设置等待调试状态
5. aa appdebug -b com.example.myapplication [-p]

7. # 取消等待调试状态
8. aa appdebug -c

10. # 获取等待调试状态的应用包名和持久化信息
11. # 获取信息例： bundle name : com.example.publishsystem, persist : false
12. aa appdebug -g
```

## 应用调试/调优命令（process）

对应用进行调试或调优，IDE用该命令集成调试和调优工具。

```
1. # 调试应用
2. aa process -b <bundleName> -a <abilityName> [-m <moduleName>] [-D <debug-cmd>] [-S]

4. # 调优应用
5. aa process -b <bundleName> -a <abilityName> [-m <moduleName>] [-p <perf-cmd>] [-S]
```

**应用调试/调优命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |
| -a | 必选参数，abilityName。 |
| -m | 可选参数，moduleName。 |
| -p | 可选参数，调优命令，与-D必须二选一。命令由调用方自定义。 |
| -D | 可选参数，调试命令，与-p必须二选一。命令由调用方自定义。 |
| -S | 可选参数，进入应用沙箱。 |

**返回值**：

当执行成功时，返回"start native process successfully."；当执行失败时，返回"error: failed to start native process."；当给定参数不合法时，返回"error: option requires a value."并打印帮助信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 10105002 | Failed to obtain ability information. |
| 10105003 | Failed to connect to the app service. |
| 10106002 | The aa start command's window option or the aa test command does not support app with release signature. |

**示例**：

```
1. # 调试应用
2. aa process -b com.example.myapplication -a EntryAbility -D debug_cmd [-S]

4. # 调优应用
5. aa process -b com.example.myapplication -a EntryAbility -p perf-cmd [-S]
```

## onMemoryLevel回调命令（send-memory-level）

从API version 13开始，开发者可以通过该命令来调试应用的[onMemoryLevel](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)生命周期。通过在参数中指定进程的pid和内存使用级别来触发该进程的onMemoryLevel生命周期回调。该命令只提供基本的应用调试能力，不能完全模拟真实的内存加压测试场景。

```
1. # 触发onMemoryLevel回调
2. aa send-memory-level -p <processId> -l <memoryLevel>
```

**参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h/--help | 帮助信息。 |
| -p | 必选参数，进程pid。 |
| -l | 必选参数，内存使用级别，具体值参考[AbilityConstant.MemoryLevel](../harmonyos-references/js-apis-app-ability-abilityconstant.md#memorylevel)。 |

**返回值**：

当执行成功时，返回"send memory level successfully."；当执行失败时，返回"error: failed to send memory level."；当给定参数值缺失时，返回"fail: unknown option."并打印帮助信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 10104003 | The specified pid does not exist. |
| 10104004 | The specified level does not exist. |

**示例**：

```
1. # 触发进程号为6066应用的onMemoryLevel回调，此时回调的level为0
2. aa send-memory-level -p 6066 -l 0
```

## aa工具错误码

### 10103001 目标Ability可见性校验失败

**错误信息**

Failed to verify the visibility of the target ability.

**错误描述**

目标Ability可见性校验失败时，aa工具将返回该错误码。

**可能原因**

当目标应用在module.json5配置文件中的[abilities标签](module-configuration-file.md#abilities标签)/[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)中的exported字段配置为false时，表示对应UIAbility组件/ExtensionAbility组件不可以被其他应用调用，也无法被aa工具命令拉起。

**处理步骤**

需要检查目标应用module.json5中对应Ability字段的exported配置是否为true，如果不为true，改为true重试即可。

### 10104001 指定的Ability不存在

**错误信息**

The specified ability does not exist.

**错误描述**

当指定的Ability名称不存在时，aa工具将返回该错误码。

**可能原因**

指定的Ability未安装。

**处理步骤**

1. 检查aa命令的-a的参数abilityName和-b的参数bundleName是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

   ```
   1. hdc shell bm dump -a
   ```
3. 多HAP应用需确认Ability所属的HAP是否已被安装。可使用如下命令查询应用的包信息，若安装的应用中没有对应的HAP和Ability，说明Ability所属的HAP未被安装。

   ```
   1. hdc shell bm dump -n 包名
   ```

### 10104003 指定的pid不存在

**错误信息**

The specified pid does not exist.

**错误描述**

当指定的pid不存在时，aa工具将返回该错误码。

**可能原因**

指定的pid不存在。

**处理步骤**

检查-p参数指定的进程号在设备上是否存在。

### 10104004 指定的内存使用级别不存在

**错误信息**

The specified level does not exist.

**错误描述**

当指定的内存使用级别不存在时，aa工具将返回该错误码。

**可能原因**

指定的内存使用级别不存在。

**处理步骤**

检查-l参数指定的内存使用级别是否为[0, 2]区间内的整数值。

### 10105001 Ability服务连接失败

**错误信息**

Failed to connect to the ability service.

**错误描述**

连接Ability服务失败。

**可能原因**

调用接口时Ability服务断开。

**处理步骤**

尝试重启设备重新执行。

### 10105002 获取Ability信息失败

**错误信息**

Failed to obtain ability information.

**错误描述**

获取Ability信息失败。

**可能原因**

生成Ability请求时通过BMS获取AbilityInfo为空。

**处理步骤**

检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

```
1. hdc shell bm dump -a
```

### 10105003 App服务连接失败

**错误信息**

Failed to connect to the app service.

**错误描述**

App服务连接失败。

**可能原因**

调用接口时App服务断开。

**处理步骤**

尝试重启设备。

### 10106001 当前设备不是开发者模式

**错误信息**

The current device is not in developer mode.

**错误描述**

当前设备不是开发者模式。

**可能原因**

当前设备不是开发者模式。

**处理步骤**

在设置中打开开发者模式。操作如下：

查看设备的“设置 > 系统”中是否有“开发者选项”。如果不存在，可在“设置 > 关于本机”连续七次单击“版本号”，直到提示“开启开发者模式”，点击“确认开启”后输入PIN码（如果已设置），设备将自动重启。请等待设备完成重启后，可以在“设置 > 系统”中查看。

### 10106002 不支持release签名的应用程序

**错误信息**

The aa start command's window option or the aa test command does not support app with release signature.

**错误描述**

aa start命令的参数wl、wt、wh、ww或aa test命令不支持release签名的应用程序。

**可能原因**

目标应用为release签名。

**处理步骤**

使用Debug签名证书重新签名，安装新签名出的HAP后，再尝试执行该命令。

### 10100101 获取应用信息失败

**错误信息**

Failed to obtain application information.

**错误描述**

从BMS查询到的App信息异常。

**可能原因**

从BMS查询到的App信息中应用名或包名异常。

**处理步骤**

1. 检查aa命令的-a的参数abilityName和-b的参数bundleName是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

   ```
   1. hdc shell bm dump -a
   ```
3. 多HAP应用需确认Ability所属的HAP是否已被安装。可使用如下命令查询应用的包信息，若安装的应用中没有对应的HAP和Ability，说明Ability所属的HAP未被安装。

   ```
   1. hdc shell bm dump -n 包名
   ```

### 10100102 aa start命令无法拉起UIExtensionAbility

**错误信息**

The aa start command cannot be used to launch a UIExtensionAbility.

**错误描述**

aa工具无法拉起UIExtensionAbility。

**可能原因**

aa start命令不支持启动UIExtensionAbility。

**处理步骤**

确认目标Ability是否为UIExtensionAbility，aa start命令无法拉起UIExtensionAbility。

### 10103101 隐式启动未查找到匹配应用

**错误信息**

Failed to find a matching application for implicit launch.

**错误描述**

隐式启动无法查找到匹配的Ability。

**可能原因**

* 如果为隐式启动，可能是启动参数配置有误或指定的HAP包未安装。
* 如果为显式启动，可能是命令中指定了bundleName、却未指定abilityName。

**处理步骤**

* 如果为隐式启动，需要确保启动参数配置正确，且指定的HAP包已安装。
* 如果为显式启动，需要确保abilityName传参正确。

### 10103102 传入的AppCloneIndex是一个无效值

**错误信息**

The passed appCloneIndex is invalid.

**错误描述**

传入一个无效的AppCloneIndex，返回该错误码。

**可能原因**

aa start命令的参数中携带的AppCloneIndex是一个无效值，则返回该错误码。

**处理步骤**

确认AppCloneIndex是否合法。

### 10106101 上一个Ability未启动完成，先缓存在队列中等待后续启动

**错误信息**

The current ability will be placed in the queue to wait for the previous ability to finish launching.

**错误描述**

需要启动的Ability过多，由于系统处理能力有限，会先将请求缓存在队列中，按照顺序依次处理。

**可能原因**

系统并发大。

**处理步骤**

无需处理，等待启动即可。

### 10106102 启动应用时，设备处于锁屏状态

**错误信息**

The device screen is locked during the application launch.

**错误描述**

启动应用时，设备处于锁屏状态。

**可能原因**

启动应用时无法解锁屏幕。

**处理步骤**

解锁屏幕后重新尝试即可。

### 10106103 目标应用为到期众测应用

**错误信息**

The target application is an expired crowdtesting application.

**错误描述**

当目标应用为众测应用并且到达测试期限时，方法将返回该错误码。

**可能原因**

众测应用到期，无法打开。

**处理步骤**

请检查应用是否众测到期，已过有效期的众测应用无法启动。

### 10106105 目标应用被管控

**错误信息**

The target application is under control.

**错误描述**

当目标应用受到应用市场管控时，方法将返回该错误码。

**可能原因**

* 目标应用疑似存在恶意行为，受到应用市场管控不允许启动。
* 目标应用是系统预装应用，并且使用本地编译的版本进行覆盖安装。
* 目标应用开发证书过期，拉起时被系统管控拦截，此时会有系统弹框提示“应用已过期”。
* 目标应用刚完成应用克隆，处于数据恢复中，此时会有系统弹框提示“数据恢复中，请稍后再试”。
* [创建试用调试Profile](../app/agc-help-apply-acl-0000002394212138.md#section1443958124819)的5天有效期已过期，导致应用拉起时被系统管控拦截。

**处理步骤**

* 针对可能原因1，建议卸载该应用。
* 针对可能原因2，需要先卸载该应用，再使用本地编译的版本进行安装。
* 针对可能原因3，需要[更换证书](../app/agc-help-cert-faq-0000002329508280.md#section11365113515519)。
* 针对可能原因4，需要等待数据恢复完成后再尝试启动。
* 针对可能原因5，需要重新[创建试用调试Profile](../app/agc-help-apply-acl-0000002394212138.md#section1443958124819)。

### 10106106 目标应用被EDM管控

**错误信息**

The target application is managed by EDM.

**错误描述**

当目标应用受到企业设备管理管控时，方法将返回该错误码。

**可能原因**

目标应用被企业管理服务设置为禁止启动。

**处理步骤**

该设备是一个企业设备，目标应用被设置为禁止启动，开发者无法处理。

### 10106107 当前设备不支持使用窗口选项

**错误信息**

The current device does not support using window options.

**错误描述**

尝试使用窗口选项但设备不支持。

**可能原因**

用户使用aa start命令指定了WindowOptions，但设备不支持。

**处理步骤**

删除aa start命令中代表WindowOptions的参数wl、wt、wh、ww后重试。

### 10107102 指定的进程权限校验失败

**错误信息**

Permission verification failed for the specified process.

**错误描述**

当指定的进程权限校验失败时，方法将返回该错误码。

**可能原因**

指定的进程权限校验失败。

**处理步骤**

确认指定进程的权限是否正确。

### 10108101 拉起Ability时内部错误

**错误信息**

An internal error occurs while attempting to launch the ability.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、包管理获取应用信息失败、系统服务获取失败、启动的Ability实例已达到上限等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10103201 目标Ability不是ServiceAbility类型

**错误信息**

The target ability is not of the ServiceAbility type.

**错误描述**

操作的目标Ability不是ServiceAbility类型。

**可能原因**

aa stop命令停止ServiceAbility时，-a的参数abilityName对应的Ability不是Service类型。

**处理步骤**

检查aa -a的参数abilityName对应的Ability是否为ServiceAbility类型。

### 10104002 获取指定包信息失败

**错误信息**

Failed to retrieve specified package information.

**错误描述**

获取指定包信息失败。

**可能原因**

指定的包名对应的应用没有安装。

**处理步骤**

1. 检查指定的包名是否正确。
2. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

   ```
   1. hdc shell bm dump -a
   ```

### 10106401 杀死进程失败

**错误信息**

Failed to terminate the process.

**错误描述**

杀死进程失败。

**可能原因**

1. aa force-stop命令指定的应用不存在。
2. 未成功连接到AppManagerService。

**处理步骤**

1. 检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

   ```
   1. hdc shell bm dump -a
   ```
2. 尝试重启设备。

### 10106402 常驻进程无法被杀死

**错误信息**

Persistent processes cannot be terminated.

**错误描述**

常驻进程无法被杀死。

**可能原因**

aa force-stop命令指定的bundleName是常驻进程。

**处理步骤**

检查目标应用是否为常驻进程，常驻进程无法通过命令杀死。

**处理步骤**

关闭目标应用的多实例之后重新尝试。

### 10108501 aa test命令内部错误

**错误信息**

An internal error occurs during the execution of the aa test command.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、系统服务获取失败等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10108601 进入/退出调试模式时内部错误

**错误信息**

An internal error occurs while attempting to enter/exit debug mode.

**错误描述**

当内存申请、多线程处理异常等内部处理错误时，方法将返回该错误码。

**可能原因**

内存申请、多线程处理等内核通用错误。具体原因可能包括：内部对象为空、处理超时、系统服务获取失败等原因。

**处理步骤**

内部错误是系统运行过程中出现的内部错误，开发者无法处理。

### 10103601 指定的包名不存在

**错误信息**

The specified bundleName does not exist.

**错误描述**

用户指定的包名未找到时返回该错误码。

**可能原因**

aa attach/detach命令指定的包名不存在。

**处理步骤**

检查指定的bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若该bundleName不在查询结果中，说明应用未安装成功。

```
1. hdc shell bm dump -a
```

### 10106701 目标应用不是Debug应用

**错误信息**

Cannot debug applications using a release certificate.

**错误描述**

目标应用不是Debug应用。

**可能原因**

当前使用签名工具中“type”参数不为“debug”。

**处理步骤**

使用Debug签名证书重新签名，安装新签名出的HAP后，再尝试执行该命令。

签名工具及签名证书的生成方式可以参考：[签名工具指导](ide-signing.md)。
