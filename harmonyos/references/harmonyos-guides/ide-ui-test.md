---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test
title: 黑盒覆盖率测试
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 黑盒覆盖率测试
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f695b4c6c0edf4e5f69e35bf477794923e4aafe740e5f8ab52c58966c660096
---

DevEco Studio支持黑盒覆盖率测试，不需要开发测试用例，将编译插桩的HAP包推到设备上，然后对该应用/元服务模拟用户操作，测试完成后可生成覆盖率报告，当前仅支持Stage模型。

## 使用约束

* DevEco Studio 6.0.1 Beta1版本前，仅支持对UIAbility进行覆盖率测试。
* 从DevEco Studio 6.0.1 Beta1版本开始，当继承的ExtensionAbility中存在onDump或onDestroy方法时，支持获取覆盖率数据。如果两个方法都不存在，则无法进行覆盖率测试。
* 覆盖率测试不支持开启混淆。

## 前置操作

将设备与电脑进行连接，并对应用/元服务签名，具体请参考[使用本地真机运行应用](ide-run-device.md)和[应用/元服务签名](ide-signing.md)。

## 配置覆盖率过滤文件

如果开发者希望只针对部分文件进行覆盖率测试，可在工程目录下创建coverage-filter.json5文件，在文件中配置参与或不参与覆盖率统计的文件/文件夹。DevEco Studio编译插桩时将按照coverage-filter.json5文件中的配置进行过滤。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/8jSaf12gQoiAJXNgWSeMIw/zh-cn_image_0000002530752874.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=B88D6F1322D07AB9CBF81363B153FCACD8DEC6E8B7EDCAC50B669F6C376B89F0)

coverage-filter.json5文件包含以下参数。

**表1**

| 参数 | 是否必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| include | 否 | 字符串数组 | 配置参与覆盖率统计的文件或文件夹路径，仅支持模块名开头的绝对路径，暂不支持通配符。include的优先级比exclude高。 |
| exclude | 否 | 字符串数组 | 配置不参与覆盖率统计的文件或文件夹路径，仅支持模块名开头的绝对路径，暂不支持通配符。 |

示例如下：

```
1. {
2. "include":[    // 配置参与覆盖率统计的文件或文件夹路径，仅支持模块名开头的绝对路径，暂不支持通配符
3. "entry/src/main/ets/pages/aaa.ets"
4. ],
5. "exclude":[    // 配置不参与覆盖率统计的文件或文件夹路径，仅支持模块名开头的绝对路径，暂不支持通配符
6. "entry/src/main/ets/pages"
7. ]
8. }
```

说明

修改配置文件后不会触发增量编译，需要重新编译插桩再测试。

## 执行覆盖率测试

### 编译与安装

有两种方式进行编译与安装，DevEco Studio方式和命令行方式，具体步骤如下。

* **方式一：通过DevEco Studio进行编译与安装，从DevEco Studio 6.0.2 Beta1版本开始支持。**
  1. 点击菜单栏**Run** > **Edit Configurations** **>** **Diagnostics**，勾选**Black Coverage**，开启黑盒覆盖率测试。

     说明

     + 调试场景下，该配置不生效，运行的是未插桩的应用。
     + attach调试和等待调试场景下，该配置会导致断点不准确，建议取消该配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/WfmUkJdlTMaKAk6ehEeJuA/zh-cn_image_0000002530752878.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=BD03C5235981F1E6CDBF4670316D0C98D111E34DD195C9CEE10F24DC7D026A4B)
  2. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/slysgH1eQTSAq1sc38PAkg/zh-cn_image_0000002561752825.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=6330485E9245C62F8361BADC52C015B3C1FB8B233165D1824FDB7A2E4CE04D0A)，DevEco Studio会启动编译插桩，并推包安装到设备上。
* **方式二：通过命令行进行编译与安装**
  1. 执行hvigor插桩编译命令，编译后在{projectPath}/{moduleName}/.test/default/intermediates/ohosTest路径下会生成init\_coverage.json文件，供后续生成覆盖率报告使用。

     ```
     1. hvigorw --mode module -p module={moduleName@targetName} -p product={productName} -p buildMode=test -p ohos-test-coverage=true -p coverage-mode=black assembleHap --parallel --incremental --daemon
     ```

     + moduleName：执行测试的模块。
     + targetName/productName：当前生效的target/product，可以通过点击DevEco Studio右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/LlaY8oiAT9qE7a886r4edg/zh-cn_image_0000002561752809.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=CEE03C745C7477ACFF0A469333FEECFA9532B68ED0B27CA6FB6578DA19F4D187)图标进行查看。

     说明

     如果HAP依赖HSP，需要单独编译HSP，将以上命令的assembleHap替换为assembleHsp即可。
  2. 如果设备上已存在待测试的应用，先卸载应用，不存在则跳过此步骤，关于hdc工具的使用指导请参考[hdc](hdc.md)。

     ```
     1. hdc uninstall {bundleName}
     ```

     + bundleName：设备上已安装的应用包名。
  3. 将插桩编译生成的HAP包安装到设备上，如果依赖HSP，需要同时安装HSP。

     ```
     1. hdc install {SignedHapPath}
     ```

     + SignedHapPath：已签名的HAP包路径，默认在模块的build\{productName}\outputs\{targetName}目录下。

### 进行测试

在设备上模拟用户操作，进行黑盒测试，测试完毕后，通过以下方式，生成覆盖率数据。

* 针对UIAbility和存在onDump方法的ExtensionAbility，执行命令生成覆盖率数据。UIAbility从DevEco Studio 5.1.0 Release版本开始支持，ExtensionAbility从DevEco Studio 6.0.1 Beta1版本开始支持。

  ```
  1. hdc shell aa dump -c -l
  ```
* 针对UIAbility，退出应用，触发[onDestroy()回调](uiability-lifecycle.md#ondestroy)，生成覆盖率数据。
* 针对存在onDestroy方法的ExtensionAbility，Ability销毁时，触发onDestroy()回调，生成覆盖率数据。从DevEco Studio 6.0.1 Beta1版本开始支持。
* 针对UIAbility，支持通过[EventHub接口](../harmonyos-references/js-apis-inner-application-eventhub.md)通知UIAbility生成覆盖率数据。从DevEco Studio 6.0.2 Beta1版本开始支持。

  ```
  1. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  2. context.eventHub.emit('coverage');
  ```

说明

从API 13开始，如果用户使用最近任务列表一键清理来关闭应用，将不会执行onDestroy()回调，导致获取不到覆盖率数据。

### 生成覆盖率报告

1. 从设备上取出覆盖率数据json文件存放到电脑本地，该命令会将cache目录下的所有文件都保存到LocalPath目录下。

   ```
   1. // 如果是应用则执行该命令，其中LocalPath非必填，如果不填写，默认存放在当前执行命令的目录
   2. hdc file recv data/app/el2/100/base/{bundleName}/haps/{moduleName}/cache {LocalPath}
   3. // 如果是元服务则执行该命令，其中LocalPath必填
   4. hdc file recv -b {bundleName} ls ./data/storage/el2/base/haps/{moduleName}/cache {LocalPath}
   ```

   1. LocalPath：数据在电脑本地存放的路径。

   说明

   在多模块相互跳转的场景下，只需要取最后退出的模块下生成的覆盖率数据json文件，但特殊场景下如多模块无跳转关系，则需要取每个独立模块下生成的覆盖率数据json文件。
2. 生成覆盖率报告：

   ```
   1. hvigorw collectCoverage -p projectPath={projectPath} -p reportPath={reportPath} -p coverageFile={projectPath}/{moduleName}/.test/default/intermediates/ohosTest/init_coverage.json#{LocalPath/bjc_cov_yyyyMMdd_HHmmss_SSS.json}
   ```

   1. projectPath：工程路径。
   2. reportPath：指定的覆盖率报告文件生成路径。
   3. bjc\_cov\_yyyyMMdd\_HHmmss\_SSS.json：指定上一个步骤LocalPath目录下的一份最新的json文件，格式以bjc\_cov开头，yyyyMMdd\_HHmmss\_SSS表示年月日\_时分秒\_毫秒。

   说明

   在多模块相互跳转的场景下，需要取各模块的init\_coverage.json文件路径，与bjc\_cov\_yyyyMMdd\_HHmmss\_SSS.json文件通过#拼接生成coverageFile参数。
3. 在本地找到报告文件路径并在浏览器中打开，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/oWiS-uMfQ-uzDKjE_sB93A/zh-cn_image_0000002530752880.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=10CB1245ABB1E88A243C0BFD8069C1998D0DA31AE84E518276D9E5AB64092CF5)

## 查看覆盖率报告

执行覆盖率测试后，会生成两份报告，一份是html格式，用于可视化查看报告，一份是json格式，即coverageReport.json文件，记录了详细的覆盖率数据，文件中各字段的含义请参考[覆盖率coverageReport.json文件](ide-ui-test.md#section175644610218)。

### 覆盖率报告解读

测试覆盖率报告有三个测量维度，分别是：

* 函数覆盖率（Functions）：每个函数是否都已调用。
* 分支覆盖率（Branches）：每个流程控制的各个分支是否都已执行。

* 行覆盖率（Lines）：每个可执行代码行是否都已执行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/DoOD2_C-TBq-JlOzABrDqA/zh-cn_image_0000002530912884.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=A3EFBF365D38ADC17895E7EAF02D0B06E7E4E24C5C605CB41DBE5999FA6A7F02)

以下是关于三个测量维度的细节说明：

* **流程控制**

  常见的流程控制语句有if、while、do...while、switch、for等等，以及三目运算符（condition ? exprIfTrue : exprIfFalse），需要确保流程控制的每个边界情况（即分支）都被执行。
* **行（Lines of Source Code） vs 可执行代码行（Lines of Executable Code）**
  + “行覆盖率”中的行是指可执行代码行（Lines of Executable Code），而不是源文件中所有的行（含空行）（Lines of Source Code）。一般来说，包含语句的每一行都应被视为可执行行。
  + 对于DevEco Studio的覆盖率测试引擎来说，只会统计方法内的语句，方法外的语句都不会被统计覆盖率。
    - 方法内，如果某行存在可执行代码，则这一整行会被视为可执行代码行（+1）。
    - 方法内，如果某行只包含标点符号**{**，会被视为可执行行（+1）。
    - 方法内，如果某行只包含标点符号**}**、**})** 或**});** ，会被视为非可执行行（+0）。

    说明

    箭头函数在方法内时，可以正常统计覆盖率，如果作为参数声明，则无法统计该行覆盖率。

    示例如下：

    ```
    1. import { window } from '@kit.ArkUI';  // +0  方法外不统计
    2. let filePath :string;               // +0  方法外不统计
    3. const fileName = 'a.txt';          // +0  方法外不统计

    5. export function doTheThing ()  // +1
    6. {                              // +1
    7. let s1: string;              // +1
    8. const str = 'aaa';           // +1
    9. console.log(str);            // +1
    10. }                              // +0

    12. export class Person {         // +0  方法外不统计
    13. name: string = ''           // +0  方法外不统计
    14. constructor (n:string) {    // +1 构造函数
    15. this.name = n;            // +1
    16. }                           // +0

    18. static sayHello () {        // +1  类静态方法
    19. console.log('hello');     // +1
    20. }                           // +0

    22. walk () {                   // +1  类实例方法
    23. for (                     // +1
    24. let i=0;                // +1
    25. i < 10;                 // +1
    26. i++)                    // +1
    27. {                         // +1
    28. }                         // +0
    29. }                           // +0
    30. }                             // +0

    32. function func ():object {    // +1
    33. return Object({        // +1      一个语句被拆分为多行
    34. a: 1,                // +1
    35. b: 2,                // +1
    36. })                     // +0
    37. }                        // +0

    39. func();                  // +0  方法外不统计

    41. function foo(n:number, m:number){}   // +1

    43. function bar():number {              // +1
    44. return 1;                          // +1
    45. }

    47. foo(1, bar());                       // +0  方法外不统计
    ```
* 测试覆盖率报告左侧的标识：
  + 灰色：不统计覆盖率。
  + 粉色：语句/函数未覆盖。
  + 绿色：语句/函数覆盖。
  + Nx：表示当前可执行代码行被执行了N次。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/QdAOlp4oRSyoOD1Q2NRrQg/zh-cn_image_0000002561832805.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=3C75F8E8726E94AF60D2E91E3B16E8B34DF0C63C2F50E12C79BEDE1AA450C927)
* **通过注释语法忽略指定代码**

  代码中的某些分支可能很难、甚至无法测试，DevEco Studio提供了instrument ignore \* 语法来进行忽略，使得某些代码不计入覆盖率。

  说明

  使用时需先清除缓存，点击菜单栏**Build -> Clean Project**。

  + **忽略文件：**在源文件中加入注释 // instrument ignore file或者 /\* instrument ignore file \*/，加入注释后，该文件不再插桩，覆盖率报告也不会有该文件。
  + **忽略代码块、class、function等：**在代码块前加入/\* instrument ignore next \*/或者// instrument ignore next即可忽略。
  + **忽略if/else分支：**在条件表达式前加上// instrument ignore if或者/\* instrument ignore if\*/（忽略if），// instrument ignore else或者/\* instrument ignore else\*/（忽略else）。

  ```
  1. import {testA} from './Index'
  2. // instrument ignore file       忽略整个文件

  4. // instrument ignore next       忽略代码块
  5. export function sum(a:number,b:number){
  6. return a+b;
  7. }
  8. sum(1,2);

  10. let a = 1;
  11. // instrument ignore else       忽略else分支
  12. if (a!=1) {
  13. // do something
  14. console.log('BBB');
  15. }else {
  16. console.log('AAA');
  17. }

  19. // instrument ignore if         忽略if分支
  20. if (a==1) {
  21. // do something
  22. console.log('BBB');
  23. }else {
  24. console.log('AAA');
  25. }
  ```

### 覆盖率coverageReport.json文件

覆盖率coverageReport.json文件记录了详细的覆盖率数据，文件中各字段的含义如下。

在阅读本文前，请先查看[覆盖率报告解读](ide-ui-test.md#section1485213972114)，了解行覆盖率、分支覆盖率和函数覆盖率的相关概念和统计方式。

1. summary字段记录了本次测试的覆盖率，包括行覆盖率、函数覆盖率和分支覆盖率，示例如下。

   ```
   1. {
   2. "summary": {
   3. "lines": {         // 行数总览
   4. "total": 43,     // 可执行行代码行数
   5. "covered": 12,   // 覆盖数量
   6. "pct": 27.91     // 行覆盖率
   7. },
   8. "functions": {     // 函数总览
   9. "total": 17,     // 函数数量
   10. "covered": 4,    // 覆盖数量
   11. "pct": 23.53     // 函数覆盖率
   12. },
   13. "branches": {      // 分支总览
   14. "total": 2,      // 分支数量
   15. "covered": 0,    // 覆盖数量
   16. "pct": 0         // 分支覆盖率
   17. }
   18. },
   19. }
   ```
2. files是个数组，记录了所有文件的详细覆盖率数据，数组中的每个元素对应一个文件。

   以一个文件为例，各字段含义如下。

   ```
   1. {
   2. "files": [
   3. {
   4. "version": "bjc v1.0.0",   // 覆盖率算法版本
   5. "versionCode": 10000,      // 覆盖率算法版本代码
   6. "path": "D:/DevEcoStudioProjects/MyApplication36/application/src/main/ets/applicationability/ApplicationAbility.ets",  // 文件路径
   7. "hash": "6828362e96a78934b93db4b980fa5ad83af85a111bf187e74da89ae0c0ec613a",  // 文件内容hash值
   8. "lineCnt": 44,     // 当前文件总行数
   9. "count": 0,        // 执行次数
   10. "projectPath": "D:/DevEcoStudioProjects/MyApplication36",     // 工程路径
   11. "functions": [],   // 函数集合
   12. "exeLine": {},     // 可执行代码行
   13. "summary": {}      // 单个文件的覆盖率详情
   14. },
   15. ...
   16. ]
   17. }
   ```

* **functions**

  functions是个数组，记录了文件中所有函数的详细覆盖率数据，数组中的每个元素对应一个函数。

  ```
  1. "functions": [
  2. {
  3. "name": "ApplicationAbility.onCreate",    // 函数名称，如果是匿名函数，name是anonymous_N
  4. "count": 0,         // 函数执行次数
  5. "regions": [],      // 对应代码区域
  6. "branches": [],     // 分支
  7. "ignored": 0,       // 函数忽略次数
  8. "index": 0          // 函数在整个文件中的位置，从0开始排序
  9. },
  10. ...
  11. ]
  ```

  + **regions**

    regions是一个可执行行数组，数组可能有一个元素、两个元素或多个元素。

    第一个元素是该方法对应的代码区域，如果不止一个元素，后面的元素是方法内的可执行代码区域。元素中每个字段的含义如下。

    ```
    1. "regions": [
    2. {
    3. "startLoc": {   // 开始代码位置
    4. "line": 8,    // 起始行号
    5. "col": 3      // 起始列号
    6. },
    7. "endLoc": {     // 结束代码位置
    8. "line": 10,   // 结束行号
    9. "col": 4      // 结束列号
    10. },
    11. "count": 0,     // 执行次数
    12. "ignored": 0    // 忽略次数
    13. }
    14. ]
    ```

    - 如果方法内没有任何实现，是个空方法，则regions数组只有一个元素，即方法对应的代码区域，示例如下。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/z9MVRJahQpOWtpn2dKERTQ/zh-cn_image_0000002530912892.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=B650B6AAC6C49C1526EE2DFCEFA2B40312B1FE8F06DB9A33E3FEC3D415B6BCD0)

      ```
      1. {
      2. "name": "dddd",
      3. "count": 1,
      4. "regions": [
      5. {
      6. "startLoc": {
      7. "line": 31,
      8. "col": 1
      9. },
      10. "endLoc": {
      11. "line": 33,
      12. "col": 2
      13. },
      14. "count": 1,
      15. "ignored": 0
      16. }
      17. ],
      18. },
      ```
    - 如果方法内只有一个代码区域，则regions数组有两个元素，示例如下。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/DjXzyOHdTIOuBfyuNg3LQw/zh-cn_image_0000002530752892.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=D71EA958A728F114DAFE53E89D532F1B462675C708531625D6144406EBCEFD66)

      ```
      1. {
      2. "name": "aaaaa",
      3. "count": 2,
      4. "regions": [
      5. {    // 方法对应的代码区域
      6. "startLoc": {
      7. "line": 2,
      8. "col": 1
      9. },
      10. "endLoc": {
      11. "line": 9,
      12. "col": 2
      13. },
      14. "count": 2,
      15. "ignored": 0
      16. },
      17. {    // 可执行代码区域
      18. "startLoc": {
      19. "line": 4,
      20. "col": 3
      21. },
      22. "endLoc": {
      23. "line": 9,
      24. "col": 2
      25. },
      26. "count": 2,
      27. "ignored": 0
      28. }
      29. ],
      30. }
      ```
    - 如果方法内存在多个代码区域，则每新增一个代码区域，regions数组就增加一个元素，示例如下。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/2BEE0kF0RcmWY4-SCngOHg/zh-cn_image_0000002561832813.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=76C589F82222FC0A9AE2ADC7829BE18C8CBA2E8C796243D78CE83E208BCC2155)

      ```
      1. {
      2. "name": "bbb",
      3. "count": 1,
      4. "regions": [
      5. {    // 方法对应的代码区域11-18行
      6. "startLoc": {
      7. "line": 11,
      8. "col": 1
      9. },
      10. "endLoc": {
      11. "line": 18,
      12. "col": 2
      13. },
      14. "count": 1,
      15. "ignored": 0
      16. },
      17. {    // 第一个可执行代码区域13-15行
      18. "startLoc": {
      19. "line": 13,
      20. "col": 13
      21. },
      22. "endLoc": {
      23. "line": 15,
      24. "col": 4
      25. },
      26. "count": 0,    // 由于flag是false，代码未执行
      27. "ignored": 0
      28. },
      29. {    // 第二个可执行代码区域15-17行
      30. "startLoc": {
      31. "line": 15,
      32. "col": 10
      33. },
      34. "endLoc": {
      35. "line": 17,
      36. "col": 4
      37. },
      38. "count": 1,    // 代码被执行
      39. "ignored": 0
      40. }
      41. ],
      42. }
      ```
  + **branches**

    branches是个分支数组，会将if和switch case这种条件判断语句相关的代码块放入数组中，数组中每个元素的字段含义如下。

    ```
    1. "branches": [
    2. {
    3. "startLoc": {      // 开始代码位置
    4. "line": 46,      // 起始行号
    5. "col": 10        // 起始列号
    6. },
    7. "endLoc": {        // 结束代码位置
    8. "line": 46,      // 结束行号
    9. "col": 11        // 结束列号
    10. },
    11. "trueCount": 0,    // 该行满足条件的已执行次数，0表示未执行
    12. "falseCount": 1,   // 该行不满足条件的已执行次数，0表示未执行
    13. "group": [         // 分组，if语句不涉及分组，switch case涉及分组
    14. 0,               // group:[0,1]，表示branches数组的0号和1号元素属于一个switch case
    15. 1
    16. ],
    17. "ignored": 0       // 忽略次数
    18. }
    19. ]
    ```

    **示例一：**调用eeee(2)。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/2a6px50pT4eJGpaOgrgxhQ/zh-cn_image_0000002530752884.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=CD01F3F163EA807DBEFE95118C7C796B1FA2E3F50F57A4A0C20B86C70E8DF578)

    ```
    1. {
    2. "name": "eeee",
    3. "count": 1,
    4. "regions": [
    5. ...
    6. ],
    7. "branches": [
    8. {
    9. "startLoc": {
    10. "line": 46,
    11. "col": 10
    12. },
    13. "endLoc": {
    14. "line": 46,
    15. "col": 11
    16. },
    17. "trueCount": 0,     // 该行条件未执行
    18. "falseCount": 1,    // 该行已执行，但不满足条件
    19. "group": [          // 0和1号元素属于1个switch case，2和3号元素属于另一个switch case
    20. 0,
    21. 1
    22. ],
    23. "ignored": 0
    24. },
    25. {
    26. "startLoc": {
    27. "line": 49,
    28. "col": 10
    29. },
    30. "endLoc": {
    31. "line": 49,
    32. "col": 11
    33. },
    34. "trueCount": 1,
    35. "falseCount": 0,
    36. "group": [
    37. 0,
    38. 1
    39. ],
    40. "ignored": 0
    41. },
    42. {
    43. "startLoc": {
    44. "line": 55,
    45. "col": 10
    46. },
    47. "endLoc": {
    48. "line": 55,
    49. "col": 13
    50. },
    51. "trueCount": 0,
    52. "falseCount": 1,
    53. "group": [
    54. 2,
    55. 3
    56. ],
    57. "ignored": 0
    58. },
    59. {
    60. "startLoc": {
    61. "line": 58,
    62. "col": 10
    63. },
    64. "endLoc": {
    65. "line": 58,
    66. "col": 13
    67. },
    68. "trueCount": 1,
    69. "falseCount": 0,
    70. "group": [
    71. 2,
    72. 3
    73. ],
    74. "ignored": 0
    75. }
    76. ],
    77. }
    ```

    **示例二：**调用bbb(2)和bbb(-1)，该方法触发两次。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/p4LEVgcfRka3TsvdlqPLwQ/zh-cn_image_0000002530912866.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=89249545379A5E82E6178F2F5905E80774449F952B3DBF0834419FE8E0E4D287)

    branches的0号元素，对应12行，trueCount和falseCount都为1，表示该行触发了两次，一次满足条件，一次不满条件。

    ```
    1. {
    2. "name": "bbb",
    3. "count": 2,
    4. "regions": [
    5. ...
    6. ],
    7. "branches": [
    8. {
    9. "startLoc": {
    10. "line": 12,
    11. "col": 7
    12. },
    13. "endLoc": {
    14. "line": 12,
    15. "col": 12
    16. },
    17. "trueCount": 1,
    18. "falseCount": 1,
    19. "group": [],
    20. "ignored": 0
    21. },
    22. {
    23. "startLoc": {
    24. "line": 14,
    25. "col": 14
    26. },
    27. "endLoc": {
    28. "line": 14,
    29. "col": 20
    30. },
    31. "trueCount": 0,
    32. "falseCount": 1,
    33. "group": [],
    34. "ignored": 0
    35. },
    36. {
    37. "startLoc": {
    38. "line": 22,
    39. "col": 7
    40. },
    41. "endLoc": {
    42. "line": 22,
    43. "col": 13
    44. },
    45. "trueCount": 1,
    46. "falseCount": 1,
    47. "group": [],
    48. "ignored": 0
    49. }
    50. ]
    51. }
    ```
* **exeLine**

  exeLine记录了所有可执行行的行号，示例如下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/X-HCnADaTOicd0ud_ZbgfA/zh-cn_image_0000002530752896.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=A22CD8953E7824361713C0351C76816D9E5EB891A004D8CA0E7D56D2E3DFCA58)

  生成的exeLine为：

  ```
  1. "exeLine": {
  2. "0": 2,
  3. "1": 3,
  4. "2": 4,
  5. "3": 6,
  6. "4": 7,
  7. "5": 8,
  8. }
  ```
* **summary**

  summary记录了单个文件的覆盖率详情。

  ```
  1. "summary": {
  2. "lines": {           // 行数总览
  3. "total": 10,       // 可执行代码行数
  4. "covered": 5,      // 覆盖数量
  5. "pct": 50,         // 行覆盖率
  6. "executedLineCount": [     // 代码行执行次数，-1表示该行不被统计，0表示未执行，1-N表示执行1-N次
  7. -1,
  8. -1,
  9. -1,
  10. 0,
  11. -1,
  12. 1,
  13. 0,
  14. 2,
  15. 2,
  16. -1,
  17. 1,
  18. 1,
  19. 0,
  20. 0,
  21. 0,
  22. -1
  23. ]
  24. },
  25. "functions": {    // 函数总览
  26. "total": 6,     // 函数数量
  27. "covered": 5,   // 覆盖数量
  28. "pct": 83.33    // 函数覆盖率
  29. },
  30. "branches": {     // 分支总览
  31. "total": 2,     // 分支数量
  32. "covered": 1,   // 覆盖数量
  33. "pct": 50       // 分支覆盖率
  34. }
  35. }
  ```
