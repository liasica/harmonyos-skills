---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cppcrash-sigbus-fault-mode
title: SIGBUS非法内存访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > CppCrash故障模式说明 > SIGBUS非法内存访问故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:a7c8b9db54d5b1fe9db7752e58de17c3048bf94a3dc07d20d38039fda2d2c412
---

## BUS\_ADRALN内存地址对齐错误

### 根因描述

SIGBUS中BUS\_ADRALN表示内存地址对齐错误，该错误发生在尝试访问未对齐的内存地址时。例如访问一个4字节整数的非偶数地址。

### 问题分析思路

此类问题，通常情况下会有如下几种可能。

1. 结构体未对齐：使用#pragma pack或手动偏移导致成员未对齐。
2. 指针强制类型转换：将char\*转换为int\*等，导致访问地址不满足对齐要求。

问题分析的步骤如下。

1. 确认类型：确认信号为SIGBUS，错误码为BUS\_ADRALN。
2. 调用栈分析：参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)，使用llvm-addr2line工具定位具体访问未对齐地址的代码位置。
3. 代码分析：仔细检查指针类型转换、结构体定义、内存分配方式，确认是否存在未对齐访问。
4. 更多日志：查看完整崩溃日志文件（FatalLog），或在DevEco Studio中使用FatalLog查看功能，结合寄存器和内存映射进一步确认。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* SIGBUS
* BUS\_ADRALN

### 案例分析

**案例一：主动构造BUS\_ADRALN故障**

**问题现象**

触发业务代码调用后，应用崩溃退出，并生成CppCrash故障日志。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Reason:Signal:SIGBUS(BUS_ADRALN)@0x0000007f5158a251 
   Fault thread info:
   Tid:7875, Name:ppcrashanalysis
   #00 pc 0000000000028950 /data/storage/el1/bundle/libs/arm64/libentry.so(TestSigBusADRALN001(napi_env__*, napi_callback_info__*)+24)(9292a79a3a85a8e682ac2c774db1d42ff07d1ac4)
   #01 pc 0000000000062570 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(f017508e01b34e04b48d6447935ffa37)
   #02 pc 0000000000e86b98 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   ...
   ```

   说明1：在访问0x0000007f5158a251地址时，触发了SIGBUS(BUS\_ADRALN)异常，可以看到该地址不能被4整除。
2. 分析崩溃栈，第#00帧，即为触发内存访问错误的调用栈帧。

   证据2：查看CppCrash故障日志中，Fault thread info的栈信息。

   ```screen
   Fault thread info:
   Tid:7875, Name:ppcrashanalysis
   #00 pc 0000000000028950 /data/storage/el1/bundle/libs/arm64/libentry.so(TestSigBusADRALN001(napi_env__*, napi_callback_info__*)+24)(9292a79a3a85a8e682ac2c774db1d42ff07d1ac4)
   ...
   ```

   说明2：在第#00行代码处触发了BUS\_ADRALN异常。
3. 查找上下文，在DevEco Studio中，直接点击该帧，即可跳到崩溃的代码。代码分析需要检查指针类型转换、结构体定义、内存分配方式，确认是否存在未对齐访问。

   证据3：从上往下跳过C库的调用栈，找到调用abort函数的调用栈（#03层调用栈），从这里结合LastFatalMessage进行分析。

   ```cpp
   #if defined(__aarch64__)
       asm volatile(
           "mov x0, sp\n"
           "orr x0, x0, #0x1\n"
           "mov sp, x0\n"
           "str x0, [sp]\n"
           : : : "x0", "sp", "memory"
       );
   #endif
   ```

   说明3：

   **AArch64 ABI要求**：栈指针必须保持**16字节对齐**。这是硬件和ABI的强制要求。

   orr x0, x0, #0x1：人为破坏对齐，把最低位设为 1。

   mov sp, x0：设置了一个非法的栈指针。

   str x0, [sp]：尝试访问未对齐地址，直接触发SIGBUS(BUS\_ADRALN)。

**案例二：函数地址异常触发BUS\_ADRALN**

**问题现象**

触发业务代码调用后，应用崩溃退出，并生成CppCrash故障日志。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Reason:Signal:SIGBUS(BUS_ADRALN)@0x0000005ac3b0a96e 
   Fault thread info:
   Tid:8001, Name:ppcrashanalysis
   #00 pc 000000000000b96e /data/storage/el1/bundle/libs/arm64/libentry.so(9292a79a3a85a8e682ac2c774db1d42ff07d1ac4)
   #01 pc 000000000002898c /data/storage/el1/bundle/libs/arm64/libentry.so(TestSigBusADRALN002(napi_env__*, napi_callback_info__*)+32)(9292a79a3a85a8e682ac2c774db1d42ff07d1ac4)
   #02 pc 0000000000062570 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(f017508e01b34e04b48d6447935ffa37)
   #03 pc 0000000000e86b98 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   ...
   ```

   说明1：Reason:Signal:SIGBUS(BUS\_ADRALN)@0x0000005ac3b0a96e，可以看到地址未对齐。
2. 找到异常函数，#00栈帧未映射到有效的代码，继续分析#01栈帧。

   证据2：第9行为异常代码。

   ```cpp
   napi_value TestSigBusADRALN002(napi_env env, napi_callback_info info)
   {
       void *funcAddr = static_cast<void*>(GetName());
       reinterpret_cast<void(*)()>(funcAddr)();
       return {};
   }
   ```

   说明2：可以看到是funcAddr的低地址异常。
3. 继续分析funcAddr异常原因。

   证据3：

   ```cpp
   char* GetName()
   {
       return "testname";
   }
   ```

   结合崩溃地址上0x0000005ac3b0a96e附近的内存。

   ```screen
   x0(/data/storage/el1/bundle/libs/arm64/libentry.so):
       0000005ac3b0a958 3264003564007325   "%s\05d\0d2"
       0000005ac3b0a960 696c003832640034   "4\0d28\0li"
       0000005ac3b0a968 6574006f732e4262   "bB.so\0te"
       0000005ac3b0a970 5400656d616e7473   "stname\0T"
       0000005ac3b0a978 7341726567676972   "riggerAs"
   ```

   说明3：由于0x0000005ac3b0a96e上是普通字符，无法被当时可执行代码，GetName调用方式异常，触发了异常。

### 常见易错代码预防建议

针对BUS\_ADRALN导致的崩溃，可以参考[稳定性编码规范](bpta-stability-coding-standard.md)，通过标准化编码降低系统故障率。

## BUS\_OBJERR对象访问错误

### 根因描述

SIGBUS BUS\_OBJERR类型的Native崩溃，根本原因在于程序访问的内存区域所依赖的底层物理对象（如文件）出现了无法恢复的硬件或逻辑错误。

### 问题分析思路

对于SIGBUS BUS\_OBJERR类型的崩溃，通常情况下可能由以下原因导致：

1. 内存映射文件截断：文件被mmap映射后又被其他进程截断（ftruncate），导致访问映射区域中超出文件新大小的部分时触发此错误。因为进程的虚拟地址仍存在，但支撑它的文件内容已消失，操作系统需用BUS\_OBJERR来区分普通的无效内存访问。
2. 内存映射I/O（MMIO）错误：直接访问硬件寄存器时若方式不当（如读取未就绪的状态寄存器），硬件总线会拒绝访问并触发异常。
3. 系统资源限制：内核在处理缺页异常时，可能因资源限制而发送BUS\_OBJERR信号给进程。

问题分析的步骤如下：

1. **确认类型：**首先确认崩溃信号是否为SIGBUS，且si\_code是否为BUS\_OBJERR，这直接指明了问题的性质。重点关注**访问出错的地址** (fault addr) 和**导致崩溃的代码位置**（backtrace)，这是定位问题的物理出发点。
2. **调用栈分析：**找到异常内存访问的调用栈，根据栈帧崩溃文件名，转到业务代码栈帧去查看崩溃的函数。
3. **代码分析：**参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)，使用llvm-addr2line工具结合调用栈文件和地址偏移，找到具体业务代码行。根据代码上下文，分析其中可能存在的逻辑问题，从崩溃点出发逆向分析，数据从何而来，是否涉及mmap映射，对应的文件是否存在并发修改等问题。
4. **更多日志：**结合崩溃日志文件中的其他信息，以及hilog日志，还原更多故障现场信息，进行定位。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* SIGBUS
* BUS\_OBJERR

### 案例分析

**案例一：mmap映射访问越界**

**问题现象**

触发业务代码调用后，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR-AL00 6.1.0.120(C00E1R4P3log)
   DeviceDebuggable:Yes
   Fingerprint:b4b232eaa561c8dcc644e72822f5059204b73f62e1f01dd35b594da542634c8c
   Module name:com.huawei.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.1
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     16:37:54.932 /page_second/page_third_cppcrash/cppcrash_sigbus
     16:37:53.152 /pages/page_first/first_cppcrash_page
     16:37:43.967 :enters foreground
   Timestamp:2026-05-21 16:38:00.570
   Pid:46522
   Uid:20020208
   Process name:com.example.dfx_test
   Process life time:18s
   Process Memory(kB): 200232(Rss)
   Device Memory(kB): Total 15834760, Free 3808892, Available 8742912
   Reason:Signal:SIGBUS(BUS_OBJERR)@0x0000005a42159400 
   Fault thread info:
   Tid:46522, Name:ppcrashanalysis
   #00 pc 00000000000f2f5c /data/storage/el1/bundle/libs/arm64/libentry.so(AccessMmapOverFlow()+408)(abb4b46e70f623a009bd903f7972ff26d4d14792)
   #01 pc 00000000000f2fe4 /data/storage/el1/bundle/libs/arm64/libentry.so(AccessMmapOverFlow(napi_env__*, napi_callback_info__*)+36)(abb4b46e70f623a009bd903f7972ff26d4d14792)
   #02 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #03 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 000000000046b900 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+392)
   #05 at anonymous entry (entry/src/main/ets/pages/page_second/page_third_cppcrash/cppcrash_sigbus.ets:294:30)
   #06 pc 00000000002bee54 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaInterpreter::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+792)(f19df1a297a455d12a50e6564a6290c3)
   #07 pc 000000000020a994 /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+596)(f19df1a297a455d12a50e6564a6290c3)
   #08 pc 0000000000b4ae10 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*) const+404)(0f68c2705d33c62458011ef00d0c3567)
   #09 pc 0000000000aadeec /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunctionBase::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*)+456)(0f68c2705d33c62458011ef00d0c3567)
   #10 pc 0000000001259130 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsClickFunction::Execute(OHOS::Ace::GestureEvent&)+3988)(0f68c2705d33c62458011ef00d0c3567)
   Registers:
   x0:0000000000000000 x1:0000000000001000 x2:0000000000001000 x3:0000000000000001
   x4:0000000000000045 x5:0000000000000000 x6:000000000000000d x7:00000000000001bc
   x8:0000000000000058 x9:0000005a42159400 x10:0000000000000000 x11:0000007f01cffb60
   x12:0000007f01cffaf0 x13:0000007f01cffb20 x14:000000000000000a x15:00000000ffffffff
   x16:0000005a6e8a2958 x17:00000059ba569da4 x18:0000000000000001 x19:0000005a5a7ed000
   x20:0000005a5a797500 x21:0000007f01d00ec0 x22:0000005a6e7f2fc0 x23:0000000000000000
   x24:0000000000000122 x25:0000005a48a5e1b0 x26:0000007f01d00cb0 x27:00000059ba87df90
   x28:0000005a43f9f698 x29:0000007f01d00bb0
   lr:0000005a6e7f2f08 sp:0000007f01cffb60 pc:0000005a6e7f2f5c
   pstate:0000000060001000 esr:0000000092000047
   ```

   说明1：上图所示，Reason字段中的可以看到崩溃类型为Signal:SIGBUS(BUS\_OBJERR)@0x0000005a42159400。后面便为访问出错的地址。
2. 分析崩溃栈。

   证据2：

   ```screen
   Fault thread info:
   Tid:46522, Name:ppcrashanalysis
   #00 pc 00000000000f2f5c /data/storage/el1/bundle/libs/arm64/libentry.so(AccessMmapOverFlow()+408)(abb4b46e70f623a009bd903f7972ff26d4d14792) --> 业务栈帧，访问出错位置
   #01 pc 00000000000f2fe4 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerStackAlignObjerr(napi_env__*, napi_callback_info__*)+36)(abb4b46e70f623a009bd903f7972ff26d4d14792)
   #02 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #03 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 000000000046b900 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+392)
   #05 at anonymous entry (entry/src/main/ets/pages/page_second/page_third_cppcrash/cppcrash_sigbus.ets:294:30)
   ...
   ```

   说明2：通常认为标准库、系统so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号，通常用法为llvm-addr2line -Cfie libentry.so 00000000000f2f5c，即可定位到行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到内存访问出错的调用栈（#01层调用栈）。

   ```cpp
   napi_value AccessMmapOverFlow(napi_env env, napi_callback_info info)
   {
       const char* fileName = "/data/storage/el2/log/sigbustest";
       size_t mapSize = 4096 * 2;
       size_t truncateSize = 4096;
       
       // 1. Create and fill a file (O_SYNC reduces cache latency)
       int fd = open(fileName, O_RDWR | O_CREAT | O_TRUNC | O_SYNC, 0666); // 0666 : -rw-rw-rw-
       if (fd < 0) {
           perror("open failed.");
           return nullptr;
       }
       
       // Write real data to the file (ensure the file has content)
       char buf[4096] = { static_cast<char>(0xAA) };
       if (write(fd, buf, mapSize) != static_cast<ssize_t>(mapSize)) {
           perror("write failed.");
           close(fd);
           return nullptr;
       }
       
       // 2. Map the entire file.
       void* addr = mmap(nullptr, mapSize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
       if (addr == nullptr) {
           perror("mmap failed.");
           close(fd);
           return nullptr;
       }
       
       // 3. Truncate file (reduce)
       if (ftruncate(fd, truncateSize)) {
           perror("ftruncate failed.");
           munmap(addr, mapSize);
           close(fd);
           return nullptr;
       }
       
       // 4. Accessing the truncated area (offset 5120 > truncateSize = 4096)
       volatile char* fault = static_cast<volatile char *>(addr) + 5120;
       *fault = 'X';
       
       munmap(addr, mapSize);
       close(fd);
       return nullptr;
   }
   ```

   说明3：此处可以直接定位到具体访问的变量，排查其访问合法性。
4. 确认故障地址，然后计算访问偏移，最后检查文件状态三步进行检查。上述案例确认为文件被截断导致文件大小小于映射大小，实际访问超过文件大小的偏移时触发崩溃。

**问题结论与总结**

本案例为文件被截断导致文件大小小于映射大小，实际访问超过文件大小的偏移时触发崩溃。

**修复建议**

文件读写操作要确保访问的偏移地址合法。

**案例二：未判断内存读写合法性导致崩溃**

**问题现象**

一个多线程日志缓存服务使用内存映射文件作为底层存储。**线程****A（写入线程）**不断将日志记录追加写入映射文件的末尾区域；**线程****B（维护线程）**定期对文件进行“截断清理”，删除过期的旧日志（即缩小文件大小）。

触发业务代码调用后，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR-AL00 6.1.0.120(C00E1R4P3log)
   DeviceDebuggable:Yes
   Fingerprint:3f2b26e9e0955381b6b57d82f8ba6e1a403d4f59f85721f86b3ec6ef90ab9605
   Module name:com.huawei.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.1
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     20:03:47.177 /page_second/page_third_cppcrash/cppcrash_sigbus
     20:03:44.997 /pages/page_first/first_cppcrash_page
     20:03:42.708 :enters foreground
     20:03:41.019 :leaves foreground
     20:03:40.769 :enters foreground
   Timestamp:2026-05-21 20:03:49.322
   Pid:12877
   Uid:20020208
   Process name:com.example.dfx_test
   Process life time:10s
   Process Memory(kB): 196825(Rss)
   Device Memory(kB): Total 15834760, Free 3105120, Available 8151040
   Reason:Signal:SIGBUS(BUS_OBJERR)@0x0000005a420d3400 
   Fault thread info:
   Tid:13805, Name:ppcrashanalysis
   #00 pc 00000000001005f0 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #01 pc 0000000000100548 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #02 pc 0000000000100524 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #03 pc 00000000001002fc /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #04 pc 00000000001de794 /system/lib/ld-musl-aarch64.so.1(start+240)(6416fe50fbbb03147eb5a67ffee3f4e4)
   Registers:
   x0:0000000000000000 x1:0000000000000046 x2:0000000000000001 x3:00000059ba3abec3
   x4:0000000000000000 x5:0000000000000000 x6:0000000030383331 x7:3a6b636174735f6c
   x8:0000000000000042 x9:0000005a420d3400 x10:0000000000000000 x11:ffffffffffffffd8
   x12:0000005a6f768720 x13:00000059ba3b0453 x14:0000000000000000 x15:00000059ba3e8e58
   x16:0000005a6e423a20 x17:00000059ba4ebf90 x18:0000000000000001 x19:0000005a6f768910
   x20:0000005a6f768900 x21:00000059ba871000 x22:0000000000000000 x23:0000005a6f666000
   x24:0000005a6f768940 x25:0000005a6f768920 x26:0000005a6f768910 x27:0000005a6f768900
   x28:00000059ba592918 x29:0000005a6f768840
   lr:0000005a6e3805d4 sp:0000005a6f768810 pc:0000005a6e3805f0
   pstate:0000000000001000 esr:0000000092000047
   Other thread info:
   Tid:12877, Name:ppcrashanalysis
   #00 pc 00000000001df0c4 /system/lib/ld-musl-aarch64.so.1(pthread_join+136)(6416fe50fbbb03147eb5a67ffee3f4e4)
   #01 pc 00000000000d3d34 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::thread::join()+28)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #02 pc 00000000000f3804 /data/storage/el1/bundle/libs/arm64/libentry.so(AccessMemWithoutCheck(napi_env__*, napi_callback_info__*)+212)(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #04 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   ...
   ```

   说明1：上图所示，Reason字段中的可以看到崩溃类型为Signal:SIGBUS(BUS\_OBJERR)@0x0000005a420d3400。后面便为访问出错的地址。
2. 分析崩溃栈。

   证据2：

   ```screen
   Fault thread info:
   Tid:13805, Name:ppcrashanalysis
   #00 pc 00000000001005f0 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d) --> 业务栈帧，访问出错位置
   #01 pc 0000000000100548 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #02 pc 0000000000100524 /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #03 pc 00000000001002fc /data/storage/el1/bundle/libs/arm64/libentry.so(6d07e50b6b7cb781f587f7587a4b658b5fe2576d)
   #04 pc 00000000001de794 /system/lib/ld-musl-aarch64.so.1(start+240)(6416fe50fbbb03147eb5a67ffee3f4e4)
   ```

   说明3：通常认为标准库、系统侧so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号，通常用法为llvm-addr2line -Cfie libentry.so 000000000001005f0，即可定位到行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到内存访问出错的调用栈，对应#00层调用栈。

   ```cpp
   napi_value AccessMemWithoutCheck(napi_env env, napi_callback_info info)
   {
       const char* fileName = "/data/storage/el2/log/sigbustest";
       size_t mapSize = 4096 * 2;
       size_t truncateSize = 4096;
       
       // 1. Create and fill a file (O_SYNC reduces cache latency)
       int fd = open(fileName, O_RDWR | O_CREAT | O_TRUNC | O_SYNC, 0666); // 0666 : -rw-rw-rw-
       if (fd < 0) {
           perror("open failed.");
           return nullptr;
       }
       ftruncate(fd, mapSize);
       close(fd);
       
       // Thread A: simulate log writing thread.
       std::thread writer([=] () {
           int fd = open(fileName, O_RDWR);
           char* addr = (char *)mmap(nullptr, mapSize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
           close(fd);
           volatile char* logArea = addr;
           // Service meaning: Continuously write data to the position with the offset 5120
           // (simulating the addition of a new log).
           while (true) {
               logArea[5120] = 0x42; // 5120 : offset of writing log marker, where the crash occurs
           }
           munmap(addr, mapSize);
       });
       
       // Thread B: simulate the log clearing thread and continuously truncates the file to tuncated size.
       std::thread cleaner([=] () {
           while (true) {
               int fd = open(fileName, O_RDWR);
               ftruncate(fd, truncateSize);
               close(fd);
           }
       });
       
       writer.join();
       cleaner.join();
       return nullptr;
   }
   ```

   说明3：此处可以直接定位到具体访问的变量，排查其访问合法性。
4. 排查访问合法性。一般遵循先确认故障地址，然后计算访问偏移，最后检查文件状态三步进行检查。上述案例确认为文件被截断导致文件大小小于映射大小，实际访问超过文件大小的偏移时触发崩溃。

**问题结论与总结**

由于两个线程没有加任何同步，当写入线程在文件被截断后依然尝试写入原本有效但已被截断的地址时，就会触发SIGBUS BUS\_OBJERR崩溃。

**修复建议**

使用一个全局std::mutex保护：

* **写入线程**：在访问映射内存（尤其是靠近映射末尾的区域）之前加锁，访问完毕后解锁。
* **清理线程**：在执行ftruncate截断文件之前加锁，截断完成后解锁。

这样，当文件正在被截断时，写入线程会被阻塞，不会访问到已经失效的地址；反之，当写入线程正在使用映射区域时，截断操作无法执行，避免了文件大小在访问中途变化。

**注意**：由于mmap映射的大小是固定的，如果截断到比原映射更小，后续加锁访问时需要确保写入偏移不超过当前文件的实际大小（修复中也会加入边界检查，作为第二层防护）。

```cpp
std::mutex g_fileMutex;
std::atomic<bool> g_running(true);

napi_value AccessMemWithCheck(napi_env env, napi_callback_info info)
{
    const char* fileName = "/data/storage/el2/log/sigbustest";
    size_t mapSize = 4096 * 2;
    size_t truncateSize = 4096;
    size_t safeOffset = 5120;
    
    // 1. Create and fill a file (O_SYNC reduces cache latency)
    int fd = open(fileName, O_RDWR | O_CREAT | O_TRUNC | O_SYNC, 0666); // 0666 : -rw-rw-rw-
    if (fd < 0) {
        perror("open failed.");
        return nullptr;
    }
    ftruncate(fd, mapSize);
    close(fd);
    
    // Thread A: simulate log writing thread.
    std::thread writer([=] () {
        int fd = open(fileName, O_RDWR);
        char* addr = (char *)mmap(nullptr, mapSize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
        close(fd);
        volatile char* logArea = addr;
        // Service meaning: Continuously write data to the position with the offset 5120
        // (simulating the addition of a new log).
        while (g_running.load()) {
            // 1. lock
            std::lock_guard<std::mutex> lock(g_fileMutex);
            // 2. get file size
            struct stat st;
            fstat(fd, &st);
            if (safeOffset < truncateSize) {
                logArea[safeOffset] = 0x42;
            } else {
                std::cerr << "Offset out of range after truncation, skip write." << std::endl;
            }
        }
        munmap(addr, mapSize);
    });
    
    // Thread B: simulate the log clearing thread and continuously truncates the file to truncated size.
    std::thread cleaner([=] () {
        while (g_running.load()) {
            std::lock_guard<std::mutex> lock(g_fileMutex);
            int fd = open(fileName, O_RDWR);
            ftruncate(fd, truncateSize);
            close(fd);
        }
    });
    
    writer.join();
    cleaner.join();
    return nullptr;
}
```

### 常见易错代码预防建议

**文件访问和操作需要做长度校验**

1、检查文件大小并限制访问范围。

```cpp
int CorrectMmapUsage()
{
    const char* filePath = "/tmp/correct_mmap_test";
    int fd = open(filePath, O_RDWR | O_CREAT | O_TRUNC, 0644); // 0644 : -rw-r--r--
    if (fd < 0) {
        std::cout << "Open failed, errno: " << errno << std::endl;
        return -1;
    }
    
    // set file size
    size_t fileSize = 1024;
    if (ftruncate(fd, fileSize) != 0) {
        std::cout << "ftruncate failed, errno: " << errno << std::endl;
        close(fd);
        return -1;
    }
    
    // get file size actually (double check)
    struct stat st;
    if (fstat(fd, &st) != 0) {
        std::cout << "fstat failed, errno: " << errno << std::endl;
        close(fd);
        return -1;
    }
    fileSize = st.st_size;
    
    // The mapped area dose not exceed the file size.
    size_t mapSize = fileSize;
    void* mapped = mmap(nullptr, mapSize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    close(fd);
    
    if (mapped == MAP_FAILED) {
        std::cout << "mmap failed, errno: " << errno << std::endl;
        return -1;
    }
    
    // Checking whether the access offset is valid before the access.
    size_t accessOffset = 100;
    if (accessOffset < fileSize) {
        volatile char* ptr = static_cast<volatile char *>(mapped) + accessOffset;
        *ptr = 'x';
        std::cout << "write success at offset: " << accessOffset << std::endl;
    } else {
        std::cout << "Access offset " << accessOffset << " exceeds file size " << fileSize << std::endl;
    }
    
    munmap(mapped, mapSize);
    return 0;
}
```

2、封装安全的mmap访问。

```cpp
class SafeMmap {
public:
    SafeMmap() : mapped_(MAP_FAILED), size_(0), fd_(-1) {}
    ~SafeMmap()
    {
        if (mapped_ != MAP_FAILED) {
            munmap(mapped_, size_);
        }
        if (fd_ > 0) {
            close(fd_);
        }
    }
    
    bool Open(const char* filePath, size_t expectedSize = 0)
    {
        fd_ = open(filePath, O_RDWR | O_CREAT, 0644); // 0644 : -rw-r--r--
        if (fd_ < 0) {
            return false;
        }
        
        if (expectedSize > 0) {
            if (ftruncate(fd_, expectedSize) != 0) {
                close(fd_);
                fd_ = -1;
                return false;
            }
            size_ = expectedSize;
        } else {
            struct stat st;
            if (fstat(fd_, &st) != 0) {
                close(fd_);
                fd_ = -1;
                return false;
            }
            size_ = st.st_size;
        }
        
        mapped_ = mmap(nullptr, size_, PROT_READ | PROT_WRITE, MAP_SHARED, fd_, 0);
        if (mapped_ == MAP_FAILED) {
            close(fd_);
            fd_ = -1;
            size_ = 0;
            return false;
        }
        
        return true;
    }
    
    bool Write(size_t offset, const void* data, size_t len)
    {
        if (offset + len > size_) {
            return false;
        }
        
        if (memcpy_s(static_cast<char *>(mapped_) + offset, size_ - offset, data, len) != EOK) {
            return false;
        }
        
        return true;
    }
    
    bool Read(size_t offset, void* data, size_t len)
    {
        if (offset + len > size_) {
            return false;
        }
        
        if (memcpy_s(data, len, static_cast<char *>(mapped_) + offset, len) != EOK) {
            return false;
        }
        
        return true;
    }
    
private:
    void* mapped_;
    size_t size_;
    int fd_;
};
```

**并发场景操作文件需要加锁保护**

使用文件锁并发安全访问。

```cpp
int MmapWithFileLock()
{
    const char* filePath = "/tmp/locked_mmap_test";
    int fd = open(filePath, O_RDWR | O_CREAT, 0644); // 0644 : -rw-r--r--
    if (fd < 0) {
        return -1;
    }
    
    // Obtain file lock (write lock)
    struct flock fl;
    (void)memset_s(&fl, sizeof(flock), 0, sizeof(flock));
    fl.l_type = F_WRLCK;
    fl.l_whence = SEEK_SET;
    fl.l_start = 0;
    fl.l_len = 0;
    
    if (fcntl(fd, F_SETLK, &fl) == -1) {
        std::cout << "Failed to acquire file lock, errno : " << errno << std::endl;
        close(fd);
        return -1;
    }
    
    // set file size
    size_t fileSize = 4096;
    if (ftruncate(fd, fileSize) != 0) {
        std::cout << "ftruncate failed" << std::endl;
        close(fd);
        return -1;
    }
    
    // map file
    void* mapped = mmap(nullptr, fileSize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        std::cout << "mmap failed" << std::endl;
        close(fd);
        return -1;
    }
    
    // Using mapped memory
    volatile char* ptr = static_cast<volatile char*>(mapped);
    ptr[100] = 'x'; // 100 ：specific index
    
    std::cout << "File is locked, safe to use mmap" << std::endl;
    
    munmap(mapped, fileSize);
    
    // release flock
    fl.l_type = F_UNLCK;
    fcntl(fd, F_SETLK, &fl);
    
    close(fd);
    return 0;
}
```
