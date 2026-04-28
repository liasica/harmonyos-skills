---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wukong-guidelines
title: wukong稳定性工具使用指导
breadcrumb: 指南 > 应用测试 > 专项测试 > 命令行工具 > wukong稳定性工具使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:54+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:ae9ca32de8ba5b8cea797bee4317d02c498291dda09c86a8f24969d107a02c3b
---

## 功能介绍

wukong是系统自带的一种命令行工具，支持Ability的随机事件注入、控件注入、异常捕获、报告生成和对Ability数据遍历截图等特性。通过模拟用户行为，对系统或应用进行稳定性压力测试。wukong分为随机测试、专项测试和专注测试。

随机测试是指随机测试界面内容，支持的能力包括：shell启动、拉起整机应用、多种注入方式、设置随机种子、打印运行日志和生成报告。

专项测试主要提供对指定应用控件进行测试，支持的能力包括：shell启动、顺序遍历及截图、测试休眠唤醒、录制回放、打印运行日志和生成报告。

专注测试主要提供对指定控件的注入测试，支持的能力包括：shell启动、拉起整机应用、多种注入方式、设置随机种子、设置专注控件类型、设置注入控件次数、打印运行日志和生成报告。

## 实现原理

wukong部件架构图以及部件内子模块职责如下所述。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/6byQDmmaQ7KnZZGOxnvMLw/zh-cn_image_0000002550617950.png?HW-CC-KV=V1&HW-CC-Date=20260427T235753Z&HW-CC-Expire=86400&HW-CC-Sign=6609D5B7FFC033E95C3E0C11D1DAAA83DD97B491E7FB3817DA7F285D91B4EF19)

* 命令行解析：支持命令行获取参数并解析。
* 运行环境管理：根据命令行初始化wukong整体运行环境。
* 系统接口管理：检查并获取指定的mgr，注册controller和dfx的faultlog的回调函数。
* 随机事件生成：通过random函数生成指定种子数的随机序列，生成事件。
* 事件注入：根据支持的事件类型向系统注入事件，依赖窗口、多模、安全等子系统。
* 异常捕获处理/报告生成：通过DFX子系统获取运行中的异常信息并记录log，生成报告。

## 约束与限制

1. wukong测试工具在API 9版本开始预置使用。
2. 所有命令执行前需完成[hdc环境配置](hdc.md)，并进入shell模式。

## 功能特性及命令说明

| 命令 | 说明 |
| --- | --- |
| -v/--version | 获取wukong版本信息。 |
| help | 获取wukong帮助信息。 |
| appinfo | 查询支持拉起应用bundleName和对应的mainAbility名。 |
| special | wukong专项测试。 |
| exec | wukong随机测试。 |
| focus | wukong专注测试。 |

### 执行命令

* 进入shell模式

  ```
  1. #若连接单个设备，则直接输入如下命令进入shell模式
  2. C:\Users>hdc shell
  3. $
  4. #若同时连接多个设备，则需先获取sn号，先输入hdc list targets获取sn号，然后进入shell模式
  5. C:\Users>hdc list targets
  6. 15xxx424axxxx345209d94xxxx8fxx900
  7. C:\Users>hdc -t 15xxx424axxxx345209d94xxxx8fxx900 shell
  8. $
  ```
* 获取应用的bundle name和ability name

  ```
  1. $ wukong appinfo
  2. BundleName:  com.ohos.adminprovisioning
  3. AbilityName:  com.ohos.adminprovisioning.MainAbility
  4. BundleName:  com.ohos.callui
  5. AbilityName:  com.ohos.callui.MainAbility
  ```
* 执行查看帮助命令

  ```
  1. C:\Users>hdc shell
  2. $ wukong help        #wukong帮助菜单
  3. usage: wukong <command> [<arguments>]
  4. These are common wukong command list:
  5. help                       wukong help information
  6. -v/--version               wukong version
  7. exec                       run random test
  8. special                    run special test
  9. focus                      run focus test
  10. appinfo                    show all app information
  11. $ wukong exec -help   #wukong随机测试帮助菜单
  12. usage: wukong exec [<arguments>]
  13. These are wukong exec arguments list:
  14. -h, --help                 random test help
  15. -a, --appswitch            appswitch event percent
  16. -b, --bundle               the bundle name of allowlist
  17. -p, --prohibit             the bundle name of blocklist
  18. -d, --page                 block page list
  19. -t, --touch                touch event percent
  20. -c, --count                test count
  21. -i, --interval             interval
  22. -s, --seed                 random seed
  23. -m, --mouse                mouse event percent
  24. -k, --keyboard             keyboard event percent
  25. -H, --hardkey              hardkey event percent
  26. -S, --swap                 swap event percent
  27. -T, --time                 test time
  28. -C, --component            component event percent
  29. -r, --rotate               rotate event percent
  30. -e, --allow ability        the ability name of allowlist
  31. -E, --block ability        the ability name of blocklist
  32. -Y, --blockCompId          the id list of block component
  33. -y, --blockCompType        the type list of block component
  34. -I, --screenshot           get screenshot(only in random input)
  35. -B, --checkBWScreen        black and white screen detection
  36. -U, --Uri                  set Uri pages
  37. -x, --Uri-type             set Uri-type
  38. -K, --knuckle              set percent of knuckle event
  39. -f, --finger               set the number of fingers and proportions for tests such as swipe and knuckle gesture
  40. -P, --pinch                set percent of pinch-to-zoom event
  41. -D, --direction            set the swipe directions and proportions
  42. -o, --pause                pause swiping for 1 second
  43. -w, --crown                set percent of watch crown rotation event
  44. -g, --gestures             set percent of watch gesture recognition events
  45. -l, --idle                 set percent of watch idle event
  46. -j, --keypress             set percent of watch physical button press event
  47. -F, --float                set percent of float and split event
  48. -W, --browser              set percent of browser operation event
  49. $ wukong special -help    #wukong专项测试帮助菜单
  50. usage: wukong special [<arguments>]
  51. These are wukong special arguments list:
  52. -h, --help                 special test help
  53. -t, --touch[x,y]           touch event
  54. -c, --count                total count of test
  55. -i, --interval             interval
  56. -S, --swap[option]         swap event
  57. option is -s| -e| -b
  58. -s, --start: the start point of swap
  59. -e, --end: the end point of swap
  60. -b, --bilateral: swap go and back
  61. -k, --spec_insomnia        power on/off event
  62. -T, --time                 total time of test
  63. -C, --component            component event
  64. -p, --screenshot           get screenshot(only in componment input)
  65. -r, --record               record user operation
  66. -R, --replay               replay user operation
  67. -u, --uitest               uitest dumpLayout
  ```

## 随机测试

### 命令参数

| 命令 | 功能 | 必选 | 说明 |
| --- | --- | --- | --- |
| -h,--help | 获取当前测试的帮助信息。 | 否 | - |
| -c,--count | 设置执行次数，与测试总时间-T冲突。二者取其一。 | 否 | 单位次数，默认值为10次。 |
| -i,--interval | 设置执行间隔。 | 否 | 单位ms，默认值为1500ms。 |
| -s,--seed | 设置随机种子。 | 否 | 配置相同随机种子，会生成相同随机事件序列。 |
| -b,--bundle[bundlename,……,bundlename] | 设置本次测试的允许应用名单，与-p冲突。 | 否 | 默认测试当前设备所有应用（应用名称用英文逗号隔开）。 |
| -p,--prohibit[bundlename,……,bundlename] | 设置本次测试的禁止应用名单，与-b冲突。 | 否 | 默认不禁止任何应用（应用名称用英文逗号隔开）。 |
| -d,--page[page,……,page] | 设置本次测试的禁止页面名单。 | 否 | 系统默认禁止pages/system页面（页面名称用逗号隔开）。 |
| -a,--appswitch | 设置应用随机拉起测试比例。 | 否 | 取值范围0到1，默认值为10%。 |
| -t,--touch | 设置屏幕随机触摸测试比例。 | 否 | 取值范围0到1，默认值为10%。 |
| -S,--swap | 设置屏幕随机移动测试比例。 | 否 | 取值范围0到1，默认值为3%。 |
| -m,--mouse | 设置屏幕随机鼠标测试比例。 | 否 | 取值范围0到1，默认值为1%。 |
| -k,--keyboard | 设置屏幕随机键盘操作测试比例。 | 否 | 取值范围0到1，默认值为2%。 |
| -H,--hardkey | 设置随机物理按键测试比例。 | 否 | 取值范围0到1，默认值为2%。 |
| -r,--rotate | 设置随机屏幕旋转测试比例。 | 否 | 取值范围0到1，默认值为2%。 |
| -C, --component | 设置随机控件测试比例。 | 否 | 取值范围0到1，默认值为70%。 |
| -I, --screenshot | 控件测试截图。 | 否 | - |
| -T,--time | 设置测试总时间，与设置执行次数-c冲突。二者取其一。 | 否 | 单位分钟，默认值为10分钟。 |
| -e, --allow ability | 设置允许测试的ability。 | 否 | - |
| -E, --block ability | 设置禁止测试的ability。 | 否 | - |
| -Y, --blockCompId | 设置不进行注入的CompId。 | 否 | - |
| -y, --blockCompType | 设置不进行注入的CompType。 | 否 | - |
| -B, --checkBWScreen | 设置启用黑白屏检测。 | 否 | - |
| -U, --Uri | 设置应用拉起页面的URI。 | 否 | - |
| -x, --UriType | 设置应用拉起页面的URIType（统一资源标识符类型）。 | 否 | - |
| -K, --knuckle | 设置指关节敲击测试比例。 | 否 | 取值范围0到1，默认值为0。 |
| -f, --finger | 设置滑动和指关节敲击测试的参与手指数量及比例。 | 否 | 支持配置1-4个手指，格式：-f <手指数1,比例>,<手指数2,比例>,<手指数3,比例>,<手指数4,比例>，例如:-f 1,0.25,2,0.25,3,0.25,4,0.25。 |
| -P, --pinch | 设置双指捏合测试比例。 | 否 | 取值范围0到1，默认值为0。 |
| -D, --direction | 设置滑动方向及比例。 | 否 | 支持配置上(u)、下(d)、左(l)、右(r)四个方向，格式：-D <方向1,比例>,<方向2,比例>,<方向3,比例>,<方向4,比例>，例如:u,0.25,r,0.25,d,0.25,l,0.25。 |
| -o, --pause | 设置滑动过程中支持暂停。 | 否 | 该参数缺省则不支持暂停。 |
| -w, --crown | 设置表冠操作测试比例。 | 否 | 仅Wearable设备支持，取值范围0到1，默认值为0。 |
| -g, --gestures | 设置手势（如上滑、下滑、左滑、右滑等）操作测试比例。 | 否 | 仅Wearable设备支持，取值范围0到1，默认值为0。 |
| -l, --idle | 设置待机状态下的操作测试比例。 | 否 | 仅Wearable设备支持，取值范围0到1，默认值为0。 |
| -j, --keypress | 设置按键（电源键、智感窗按键）操作测试比例。 | 否 | 仅Wearable设备支持，取值范围0到1，默认值为0。 |
| -F, --float | 设置应用分屏模式和悬浮窗模式的测试比例。 | 否 | 取值范围0到1，默认值为0。 |
| -W, --browser | 设置浏览器操作测试比例。 | 否 | 取值范围0到1，默认值为0。 |

说明

* 上述参数的测试比例表示在当前测试中的操作，所有参数的测试比例之和需小于等于1。
* -K，-f，-P，-D，-o，-w，-g，-l，-j，-F，-W参数从API version 23开始支持。

### 使用示例

* 设置100次事件注入

  ```
  1. $ wukong exec -s 10 -i 1000 -a 0.28 -t 0.72 -c 100
  ```

  命令中各参数含义：

  | 命令 | 参数值 | 说明 |
  | --- | --- | --- |
  | wukong exec | - | 主命令。 |
  | -s | 10 | 参数设置随机种子，10为种子值。 |
  | -i | 1000 | 参数设置应用拉起间隔为1000ms。 |
  | -a | 0.28 | 参数设置应用随机拉起测试比例28%。 |
  | -t | 0.72 | 参数设置屏幕随机touch测试比例为72%。 |
  | -c | 100 | 参数设置执行次数为100次。 |
* 指定页面压测

  ```
  1. > 显示启动
  2. > hdc_std shell
  3. $ wukong exec -b bundlename -e abilityname -U uri

  5. > 隐式启动
  6. > hdc_std shell
  7. $ wukong exec -b bundlename -U uri -x uriType
  ```
* 设置允许测试和禁止测试的ability

  ```
  1. $ wukong exec -b com.ohos.settings -e com.ohos.settings.MainAbility -E com.ohos.settings.AppInfoAbility
  ```

  说明

  若配置-e、-E则须配置-b来指定应用。

## 专项测试

### 命令参数

| 命令 | 功能 | 必选 | 说明 |
| --- | --- | --- | --- |
| -h, --help | 获取当前专项测试的帮助信息。 | 否 | - |
| -k, --spec\_insomnia | 休眠唤醒专项测试。 | 否 | - |
| -c, --count | 设置执行次数。 | 否 | 单位次数，默认值为10次。 |
| -i, --interval | 设置执行间隔。 | 否 | 单位ms，默认值为1500ms。 |
| -S, --swap | 滑动测试。 | 否 | - |
| -s, --start[x,y] | 设置滑动测试起点坐标。 | 否 | 坐标均为正值。 |
| -e, --end[x,y] | 设置滑动测试终点坐标。 | 否 | 坐标均为正值。 |
| -b, --bilateral | 设置往返滑动。 | 否 | 默认不往返滑动。 |
| -t, --touch[x,y] | 点击测试。 | 否 | - |
| -T, --time | 设置测试总时间。 | 否 | 单位分钟，默认值为10分钟。 |
| -C, --component | 控件顺序遍历测试。 | 否 | 需要设置测试应用名称。 |
| -r, --record | 录制。 | 否 | 需要指定录制文件。 |
| -R, --replay | 回放。 | 否 | 需要指定回放文件。 |
| -p, --screenshot | 控件测试截图。 | 否 | - |

### 测试命令

```
1. $ wukong special -C [bundlename] -p
```

## 专注测试

### 命令参数

| 命令 | 功能 | 必选 | 说明 |
| --- | --- | --- | --- |
| -n,--numberfocus | 设置每个控件注入的次数。 | 否 | 单位次数。 |
| -f, --focustypes | 设置需要专注的控件类型。 | 否 | 以英文逗号隔开。 |
| -h,--help | 获取当前测试的帮助信息。 | 否 | - |
| -c,--count | 设置执行次数，与设置执行时间-T冲突。二者取其一。 | 否 | 单位次数，默认值为10次。 |
| -i,--interval | 设置执行间隔。 | 否 | 单位ms，默认值为1500ms。 |
| -s,--seed | 设置随机种子。 | 否 | 配置相同随机种子，会生成相同随机事件序列。 |
| -b,--bundle[bundlename,……,bundlename] | 设置本次测试的允许应用名单，与-p冲突。 | 否 | 默认测试当前设备所有应用（应用名称用英文逗号隔开）。 |
| -p,--prohibit[bundlename,……,bundlename] | 设置本次测试的禁止应用名单，与-b冲突。 | 否 | 默认不禁止任何应用（应用名称用英文逗号隔开）。 |
| -d,--page[page,……,page] | 设置本次测试的禁止页面名单。 | 否 | 系统默认禁止pages/system页面（页面名称用逗号隔开）。 |
| -a,--appswitch | 设置应用随机拉起测试比例。 | 否 | 默认值为10%。 |
| -t,--touch | 设置屏幕随机触摸测试比例。 | 否 | 默认值为10%。 |
| -S,--swap | 设置屏幕随机移动测试比例。 | 否 | 默认值为3%。 |
| -m,--mouse | 设置屏幕随机鼠标测试比例。 | 否 | 默认值为1%。 |
| -k,--keyboard | 设置屏幕随机键盘操作测试比例。 | 否 | 默认值为2%。 |
| -H,--hardkey | 设置随机物理按键测试比例。 | 否 | 默认值为2%。 |
| -r,--rotate | 设置随机屏幕旋转测试比例。 | 否 | 默认值为2%。 |
| -C, --component | 设置随机控件测试比例。 | 否 | 默认值为70%。 |
| -I, --screenshot | 控件测试截图。 | 否 | - |
| -T,--time | 设置测试总时间，与设置执行次数-c冲突。二者取其一。 | 否 | 单位分钟，默认值为10分钟。 |
| -e, --allow ability | 设置允许测试的ability。 | 否 | - |
| -E, --block ability | 设置禁止测试的ability。 | 否 | - |
| -Y, --blockCompId | 设置不进行注入的CompId。 | 否 | - |
| -y, --blockCompType | 设置不进行注入的CompType。 | 否 | - |
| -B, --checkBWScreen | 设置启用黑白屏检测。 | 否 | - |

### 使用示例

```
1. $ wukong focus -s 10 -i 1000 -a 0.28 -t 0.72 -c 100
```

命令中各参数含义：

| 命令 | 参数值 | 说明 |
| --- | --- | --- |
| wukong focus | - | 主命令。 |
| -s | 10 | 参数设置随机种子，10为种子值。 |
| -i | 1000 | 参数设置应用拉起间隔为1000ms。 |
| -a | 0.28 | 参数设置应用随机拉起测试比例28%。 |
| -t | 0.72 | 参数设置屏幕随机touch测试比例为72%。 |
| -c | 100 | 参数设置执行次数为100次。 |

## 查看测试结果

### 测试结果输出路径

执行完测试指令后，会自动生成测试结果，测试结果输出根路径如下：

* 2022/9/22之前的DevEco Studio版本，结果存放路径为：/data/local/wukong/report/xxxxxxxx\_xxxxxx/
* 2022/9/22之后的DevEco Studio版本，结果存放路径为：/data/local/tmp/wukong/report/xxxxxxxx\_xxxxxx/

### 测试报告文件目录

| 类型 | 描述 |
| --- | --- |
| exception/ | 存放本次测试产生的异常文件。 |
| screenshot/ | 存放测试遍历的截图。 |
| wukong\_report.csv | 测试报告统计汇总。 |
| wukong.log | 测试操作历程。 |

### 查看操作日志

wukong支持通过hdc命令将日志获取到本地，查看操作历程。

```
1. # wukong.log文件对应路径如下
2. /data/local/tmp/wukong/report/xxxxxxxx_xxxxxx/wukong.log

4. # 查看wukong测试报告文件目录操作如下
5. $ cd /data/local/tmp/wukong/report/20170805_170053
6. $ ls
7. data.js  exception  wukong.log  wukong_report.csv

9. # 开启shell窗口，用hdc file recv获取wukong日志
10. C:\Users\xxx>hdc file recv /data/local/tmp/wukong/report/20170805_170053/wukong.log C:\Users\xxx\Desktop\log
11. [I][2024-01-03 20:08:02] HdcFile::TransferSummary success
12. FileTransfer finish, Size:76492, File count = 1, time:16ms rate:4780.75kB/s
```

### 测试报告解析

包含基本信息、事件注入统计、Ability统计、故障统计。

1. 基本信息（Base Info）

   | 字段 | 描述 |
   | --- | --- |
   | task status | 任务状态。success表示成功，fail表示失败。 |
   | task time | 任务执行时间。单位：秒。 |
   | seed | 随机种子。 |
   | task count | 事件注入总次数。 |
2. 故障注入统计（Input Message Statistics）

   | 类型 | 描述 |
   | --- | --- |
   | type | 事件或控件注入的类型，事件注入类型范围请参考[随机测试命令参数](wukong-guidelines.md#随机测试)，控件注入类型范围请参考[ArkTS组件](../harmonyos-references/arkui-declarative-comp.md)。 |
   | execTimes | 事件或者控件注入执行次数。 |
   | proportion | 当前事件操作在事件注入执行总次数里的占比。 |
   | inputedTimes | 遍历的控件类型个数。 |
   | expectInputTimes | 应用控件类型总数。 |
   | coverage | 控件遍历覆盖率。 |
3. Ability统计（ability Statistics）

   | 字段 | 描述 |
   | --- | --- |
   | bundleName | 应用的bundleName。 |
   | inputedAbilityCount | 遍历的Ability数量。 |
   | abilitiesCount | 应用的Ability总数。 |
   | coverage | Ability遍历覆盖率。 |
4. 故障统计（Exception Message Statistics）

   说明

   故障日志路径：/data/log/faultlog/faultlogger/

   | 字段 | 描述 |
   | --- | --- |
   | type | 故障类型，故障类型包含：CPP\_CRASH、JS\_CRASH、SYS\_FREEZE、APP\_FREEZE等。 |
   | times | 故障次数。 |
   | proportion | 当前故障在故障总数里的占比。 |

## 常见问题

### failed to connect to AAMS

**错误描述**

failed to connect to AAMS.

**可能原因**

AAMS被hypium或者dev testing的UIViewer占用了，AAMS同一时间只能被一个程序连接。

**解决方案**

结束占用AAMS的进程，或直接重启设备。

### Errorcode:(4005)

**错误描述**

Errorcode:(4005).

**可能原因**

因屏幕显示区域大小变化，导致无障碍获取页面信息失败。

**解决方案**

该错误不影响测试流程，无需处理。

### Errorcode:(4007)

**错误描述**

Errorcode:(4007).

**可能原因**

因屏幕显示区域大小变化，导致无障碍获取页面信息失败。

**解决方案**

该错误不影响测试流程，无需处理。
