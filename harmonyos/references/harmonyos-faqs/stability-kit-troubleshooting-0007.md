---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/stability-kit-troubleshooting-0007
title: 应用闪退与崩溃问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 故障排查 > 应用闪退与崩溃问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:52e82c1dfef6b3d6b41206b18f724087a1be6926eb4eafaf6fa7077c936fe067
---

## 应用闪退

### 问题现象

应用界面突然消失，直接返回桌面。

### 定位过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/I5qfGXa4TRuwrLID8T0xNA/zh-cn_image_0000002766022066.png "点击放大")

定位的核心逻辑遵循标准化路径：**“锁定时间点 → 识别退出原因 → 提取详细堆栈 → 针对性修复”**。

1. 锁定崩溃现场 (HiLog 分析)

   当问题复现时，通过系统实时日志找到“死亡 Reason”是定界的第一步。

   * **前置准备**：连接手机至电脑，确认应用包名。
   * **搜索指令**：在 Log 工具中开启**正则表达式**搜索：

     ```txt
     PROCESS_KILL.*你的包名
     ```

     *(注：.\* 用于匹配进程ID等中间字符，精准定位针对目标包名的杀进程动作)*
   * **关键信息提取**：找到形如 I ProcessManager: PROCESS\_KILL: ... reason: JsCrash 的日志，**记录下 reason 字段的值**。
2. 获取故障堆栈 (FaultLog 提取)

   根据上一步获取的 reason，导出系统生成的堆栈文件进行深度分析。

   * **存储路径**：/data/log/faultlog/faultlogger/
   * **导出工具**：使用终端执行 hdc file recv 命令将文件导出到本地。

### 分析结论

基于 PROCESS\_KILL 日志中的 reason 字段，可将问题快速定界为以下几类：

1. **代码错误类**：
   * **结论**：应用自身的 JS/ArkTS 或 C++ 代码存在逻辑缺陷或非法访问。
   * **方向**：需排查具体的代码行号和变量状态。
2. **主线程阻塞类**：
   * **结论**：主线程负载过重或被阻塞，导致无法及时响应用户输入或系统回调。
   * **方向**：需排查主线程中的耗时操作、死锁或死循环。
3. **系统管控类**：
   * **结论**：应用资源使用（内存、CPU）超标，或整机资源不足导致被动回收。
   * **方向**：需优化应用资源占用，治理内存泄漏和后台行为。

### 修改建议

根据导出的 FaultLog 文件及定界结果，针对典型场景的修复策略如下：

* 场景 1：Reason 为 JsCrash
  + **定性**：ArkTS/JS 层面的未捕获异常。
  + **分析方法**：打开 jscrash- 开头的日志，搜索 Stacktrace，查找指向项目源码的文件名和行号。
* 场景 2：Reason 为 CppCrash
  + **定性**：Native 层（NAPI/So库）的内存违规或段错误。
  + **分析方法**：打开 cppcrash- 开头的日志，查看 Tid（崩溃线程）下的堆栈（#00, #01...）。
    - 若栈顶是应用自带 .so，一般路径为/data开头：应用自身 C++ 代码问题。
    - 若栈顶是系统 .so，一般路径为/system开头（如 libark\_jsruntime.so）：通常为上层传参错误导致系统库崩溃。
* 场景 3：Reason 为 APP\_INPUT\_BLOCK / THREAD\_BLOCK\_6S
  + **定性**：主线程被耗时操作阻塞（ANR）。
  + **分析方法**：打开 appfreeze- 日志，搜索 Name:MainThread，查看其下方的调用栈，找出重复出现或明显耗时的函数调用。
* 场景 4：Reason 为 LIFECYCLE\_TIMEOUT
  + **定性**：UIAbility 生命周期回调执行超时。
  + **分析方法**：确认崩溃发生在应用启动（onCreate）或前后台切换（onForeground）阶段。

## 应用卡死

### 问题现象

应用界面画面静止，点击无反应，随后可能弹出“应用无响应”对话框或直接退出。

### 定位过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/E0BcAd4kTa2bDRRg1UYoTQ/zh-cn_image_0000002765863032.png "点击放大")

定位的核心逻辑遵循标准化路径：**“锁定时间点 → 识别退出原因 → 提取详细堆栈 → 针对性修复”**。

1. 锁定崩溃现场 (HiLog 分析)

   当问题复现时，通过系统实时日志找到“死亡 Reason”是定界的第一步。

   * **前置准备**：连接手机至电脑，确认应用包名。
   * **搜索指令**：在 Log 工具中开启**正则表达式**搜索：

     ```screen
     PROCESS_KILL.*你的包名
     ```

     *(注：.\* 用于匹配进程ID等中间字符，精准定位针对目标包名的杀进程动作)*
   * **关键信息提取**：找到形如 I ProcessManager: PROCESS\_KILL: ... reason: JsCrash 的日志，**记录下 reason 字段的值**。
2. 获取故障堆栈 (FaultLog 提取)

   根据上一步获取的 reason，导出系统生成的堆栈文件进行深度分析。

   * **存储路径**：/data/log/faultlog/faultlogger/
   * **导出工具**：使用终端执行 hdc file recv 命令将文件导出到本地。

### 分析结论

基于 PROCESS\_KILL 日志中的 reason 字段，可将问题快速定界为以下几类：

1. **代码错误类**：
   * **结论**：应用自身的 JS/ArkTS 或 C++ 代码存在逻辑缺陷或非法访问。
   * **方向**：需排查具体的代码行号和变量状态。
2. **主线程阻塞类**：
   * **结论**：主线程负载过重或被阻塞，导致无法及时响应用户输入或系统回调。
   * **方向**：需排查主线程中的耗时操作、死锁或死循环。
3. **系统管控类**：
   * **结论**：应用资源使用（内存、CPU）超标，或整机资源不足导致被动回收。
   * **方向**：需优化应用资源占用，治理内存泄漏和后台行为。

### 修改建议

根据导出的 FaultLog 文件及定界结果，针对典型场景的修复策略如下：

* 场景 1：Reason 为 JsCrash
  + **定性**：ArkTS/JS 层面的未捕获异常。
  + **分析方法**：打开 jscrash- 开头的日志，搜索 Stacktrace，查找指向项目源码的文件名和行号。
* 场景 2：Reason 为 CppCrash
  + **定性**：Native 层（NAPI/So库）的内存违规或段错误。
  + **分析方法**：打开 cppcrash- 开头的日志，查看 Tid（崩溃线程）下的堆栈（#00, #01...）。
    - 若栈顶是应用自带 .so，一般路径为/data开头：应用自身 C++ 代码问题。
    - 若栈顶是系统 .so，一般路径为/system开头（如 libark\_jsruntime.so）：通常为上层传参错误导致系统库崩溃。
* 场景 3：Reason 为 APP\_INPUT\_BLOCK / THREAD\_BLOCK\_6S
  + **定性**：主线程被耗时操作阻塞（ANR）。
  + **分析方法**：打开 appfreeze- 日志，搜索 Name:MainThread，查看其下方的调用栈，找出重复出现或明显耗时的函数调用。
* 场景 4：Reason 为 LIFECYCLE\_TIMEOUT
  + **定性**：UIAbility 生命周期回调执行超时。
  + **分析方法**：确认崩溃发生在应用启动（onCreate）或前后台切换（onForeground）阶段。

## 应用非预期推出

### 问题现象

应用在后台运行或前台切换时被系统强制关闭。

### 定位过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/bsYF_mXsR4S0KfvjqGAx3Q/zh-cn_image_0000002765863250.png "点击放大")

定位的核心逻辑遵循标准化路径：**“锁定时间点 → 识别退出原因 → 提取详细堆栈 → 针对性修复”**。

1. 锁定崩溃现场 (HiLog 分析)

   当问题复现时，通过系统实时日志找到“死亡 Reason”是定界的第一步。

   * **前置准备**：连接手机至电脑，确认应用包名。
   * **搜索指令**：在 Log 工具中开启**正则表达式**搜索：

     ```screen
     PROCESS_KILL.*你的包名
     ```

     *(注：.\* 用于匹配进程ID等中间字符，精准定位针对目标包名的杀进程动作)*
   * **关键信息提取**：找到形如 I ProcessManager: PROCESS\_KILL: ... reason: JsCrash 的日志，**记录下 reason 字段的值**。
2. 获取故障堆栈 (FaultLog 提取)

   根据上一步获取的 reason，导出系统生成的堆栈文件进行深度分析。

   * **存储路径**：/data/log/faultlog/faultlogger/
   * **导出工具**：使用终端执行 hdc file recv 命令将文件导出到本地。

### 分析结论

基于 PROCESS\_KILL 日志中的 reason 字段，可将问题快速定界为以下几类：

1. **代码错误类**：
   * **结论**：应用自身的 JS/ArkTS 或 C++ 代码存在逻辑缺陷或非法访问。
   * **方向**：需排查具体的代码行号和变量状态。
2. **主线程阻塞类**：
   * **结论**：主线程负载过重或被阻塞，导致无法及时响应用户输入或系统回调。
   * **方向**：需排查主线程中的耗时操作、死锁或死循环。
3. **系统管控类**：
   * **结论**：应用资源使用（内存、CPU）超标，或整机资源不足导致被动回收。
   * **方向**：需优化应用资源占用，治理内存泄漏和后台行为。

### 修改建议

根据导出的 FaultLog 文件及定界结果，针对典型场景的修复策略如下：

* 场景 1：Reason 为 JsCrash
  + **定性**：ArkTS/JS 层面的未捕获异常。
  + **分析方法**：打开 jscrash- 开头的日志，搜索 Stacktrace，查找指向项目源码的文件名和行号。
* 场景 2：Reason 为 CppCrash
  + **定性**：Native 层（NAPI/So库）的内存违规或段错误。
  + **分析方法**：打开 cppcrash- 开头的日志，查看 Tid（崩溃线程）下的堆栈（#00, #01...）。
    - 若栈顶是应用自带 .so，一般路径为/data开头：应用自身 C++ 代码问题。
    - 若栈顶是系统 .so，一般路径为/system开头（如 libark\_jsruntime.so）：通常为上层传参错误导致系统库崩溃。
* 场景 3：Reason 为 APP\_INPUT\_BLOCK / THREAD\_BLOCK\_6S
  + **定性**：主线程被耗时操作阻塞（ANR）。
  + **分析方法**：打开 appfreeze- 日志，搜索 Name:MainThread，查看其下方的调用栈，找出重复出现或明显耗时的函数调用。
* 场景 4：Reason 为 LIFECYCLE\_TIMEOUT
  + **定性**：UIAbility 生命周期回调执行超时。
  + **分析方法**：确认崩溃发生在应用启动（onCreate）或前后台切换（onForeground）阶段。

## 用户打开视频播放时，应用发生闪退

### 问题现象

应用播放视频时，无法播放直接闪退。

### 定位过程

1. 闪退问题首先排查是否出现JsCrash，CppCrash以及AppFreeze文件，查看faultlogger目录，是否生成了形如jscrash-应用包名/cppcrash-应用包名/appfreeze-应用包名的故障日志。如果存在则进入对应日志查看故障信息。
2. 在日志内查看对应信息：
   * 故障分类是CppCrash，故障根因是SIGSEGV。

     从故障日志可以看出，栈顶基础库ld-musl-aarch64的调用链sprintf->vfprintf->printf\_core->strnlen，这是在操作格式化字符串到缓冲区，下一个栈帧是libplay\_logic\_library.so，PlayerOption对象执行toString方法，当PlayerOption对象中的成员变量未正确初始化，调用toString方法时，就会在栈顶strnlen函数(计算字符串长度)出现空指针异常。

     ```txt
       Process name:com.hm.example
       Process life time:4832s
       Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000007e00000000
       Fault thread info:
       Tid:22654, Name:com.hm.example
       #00 pc 00000000000a4f10 /system/lib/ld-musl-aarch64.so.1(strnlen+16)(2af53e742fb0df4341adb4e9ae0f0054)
       #01 pc 00000000001a6830 /system/lib/ld-musl-aarch64.so.1(printf_core+2180)(2af53e742fb0df4341adb4e9ae0f0054)
       #02 pc 00000000001a5e24 /system/lib/ld-musl-aarch64.so.1(vfprintf+188)(2af53e742fb0df4341adb4e9ae0f0054)
       #03 pc 00000000001a4b84 /system/lib/ld-musl-aarch64.so.1(sprintf+212)(2af53e742fb0df4341adb4e9ae0f0054)
       #04 pc 000000000003f934 /data/storage/el1/bundle/libs/arm64/libplay_logic_library.so(PlayerOption::toString()+404)(2d78355f9595418980b6aace1ea3685860608a19)
     ```
   * 故障分类是JsCrash，故障原因是TypeError。异常信息是Error message：Cannot read property XXX of undefined。

     ```txt
       Reason:TypeError
       Error name:TypeError
       Error message:Cannot read property length of undefined
       Stacktrace:
       Cannot get SourceMap info, dump raw stack:
           at anonymous (entry|entry|1.0.0|src/main/ets/pages/MediaPlayer.ts:569:1)
     ```

     从异常信息可以看出，变量不是预期的类型。
   * 故障分类是AppFreeze。从日志中可以看出当前故障模块进程号是：47988，故障原因是THREAD\_BLOCK\_6S(应用主线程卡死)，故障发生的时间点是20240627092725。

     ```txt
       Pid:47988
       Uid:20020143
       Reason:THREAD_BLOCK_6S
       appfreeze: com.hm.example THREAD_BLOCK_6S at 20240627092725
       DisplayPowerInfo:powerState:AWAKE
     ```

     在日志中搜索关键字THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S，找到Tid:应用进程号,Name:应用包名下的堆栈信息。

     ```txt
       Tid:47988, Name:com.hm.example
       #00 pc 000000000056a540 /data/storage/el1/bundle/libs/arm64/libijkffmpeg.z.so(av_buffer_unref+60)(0e10837e2bdb99cbff68006c6e49e517)
       #01 pc 000000000026364c /data/storage/el1/bundle/libs/arm64/libijkffmpeg.z.so(av_packet_unref+88)(0e10837e2bdb99cbff68006c6e49e517)
       #02 pc 0000000000031524 /data/storage/el1/bundle/libs/arm64/libijkplayer.so(packet_queue_flush+80)(190419e211fa912da795fa2ee2cb02b1685dd3d6)
       #03 pc 000000000003ce60 /data/storage/el1/bundle/libs/arm64/libijkplayer.so(decoder_abort+72)(190419e211fa912da795fa2ee2cb02b1685dd3d6)
     ```

     两个堆栈信息完全一致，堆栈的栈顶为libijkffmpeg.z.so，需要结合代码对该so库进行后续的分析和排查。

### 分析结论

* 故障根因是SIGSEGV。

  调用so库时产生非法内存访问，导致出现闪退。
* 故障根因是JsCrash-TypeError。

  异常信息是Error message：Cannot read property XXX of undefined。变量不是预期的类型，不能调用对应的属性，导致JsCrash闪退。
* 故障根因是THREAD\_BLOCK\_6S。

  故障so库业务时间过长被判定为应用卡死，为了保证系统可恢复，用户能正常使用，系统会杀死应用。

### 修改建议

* 故障根因是SIGSEGV。

  故障so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
* 故障根因是JsCrash-TypeError。

  异常信息是Error message：Cannot read property XXX of undefined。

  在使用变量前进行校验，检查变量是否存在对应的属性。
* 故障根因是THREAD\_BLOCK\_6S。

  故障so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
