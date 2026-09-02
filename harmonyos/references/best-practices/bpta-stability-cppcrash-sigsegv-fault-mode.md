---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cppcrash-sigsegv-fault-mode
title: SIGSEGV无效内存访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > CppCrash故障模式说明 > SIGSEGV无效内存访问故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:024468cb3c7d0043e750f531ecb55b395e3240d8bc59549cb4c77c0907d145fc
---

## SEGV\_MAPERR不存在的内存地址

### 根因描述

SEGV\_MAPERR是SIGSEGV（Segmentation Fault，段错误）信号中的一种具体错误代码，全称为Segmentation Violation - Map Error。

SEGV\_MAPERR表示程序试图访问一个未映射到物理内存或虚拟内存空间的地址。程序试图读写某个内存地址，但操作系统检测到该地址不属于当前进程合法的内存范围。

### 问题分析思路

问题分析的步骤如下：

1. **确认类型：**根据Reason字段等信息初步确认故障的具体类型。
2. **调用栈分析：** 根据调用栈、寄存器等信息进一步确认问题原因，缩小分析范围。
3. **代码分析：** 查找对应调用栈的具体代码行，结合代码上下文，查找代码中的异常原因，并据此进行防范修改。
4. **更多日志：** 可以结合更多的流水日志等进行辅助定位，还原故障场景等。

常见的几种问题类型如下：

1. **空指针解引用（Null Pointer Dereference）**。

   这是最常见的原因。当指针值为NULL(0x0)或接近0的小地址时，尝试读取或写入该地址会触发此错误。

   **示例：** 详情参见下文案例一。

   ```cpp
   int *ptr = nullptr;
   int value = *ptr; // crash: SEGV_MAPERR, fault addr 0x0
   ```

   **特征：** 在故障日志Reason字段中的故障地址通常为0x0、0x4、0x8等极小的值， 同时也会提示probably caused by NULL pointer dereference的字样。
2. **踩内存问题**。

   当发生踩内存问题，并且踩踏了指针指向的地址，当被踩踏后的指针指向了一个完全未映射（不存在）的内存区域，就会报SEGV\_MAPERR；如果指向的是一个已存在但权限不足或数据损坏的区域，可能会报其他错误（如SEGV\_ACCERR）或导致逻辑错误而非立即崩溃。

   1. **野指针或使用已释放的内存（Use-After-Free）**。

      指针指向的内存已经被free或delete释放，或者对象已被销毁，但指针未被置空，后续再次访问该地址。

      **示例：** 详情参见下文案例二。

      ```cpp
       int tmp = 1;
       int **p = new int*[10];
       *p = &tmp;
       delete [] p;
       **p = 2;
      ```

      **特征：**最后访问的指针地址通常以6b开头。例如：x1:6b6b1e7f9352c001/x9:6b6b1e7f9352c001。
   2. **数组越界（Out-of-Bounds Access）**。

      访问数组时索引超出分配的范围，且越界后的地址落在了未分配的内存页中。

      **示例：**详情参见下文案例四。

      ```cpp
       char buff[1] = {0};
       buff[1] = 'a';  // Array out-of-bounds access,may not cause a crash.
       buff[100000000] = 'a';  // Accessing an array with an out-of-bounds index and an excessively large index will cause a crash.
      ```

      **注意：**如果越界地址仍在合法堆栈或堆内存范围内，可能不会立即崩溃，或者表现为数据错误，此场景建议使用ASan检测内存错误；但如果越界极大，触及未映射页面，则报SEGV\_MAPERR。
   3. **动态库被提前释放问题**。

      动态库提前被dlclose释放，释放后调用动态库内的函数，会导致函数指针指向无效地址，调用时触发SEGV\_MAPERR。这也是一类特殊的UAF（Use-After-Free）问题。

      **示例：**详情参见下文案例六。

      ```cpp
        void *handle = dlopen(path, RTLD_LAZY); // Loading dynamic libraries
        Add func = (Add)dlsym(handle, "add"); // Find the symbol
        dlclose(handle); // Release dynamic library
        func(); // Calling a Function in a Dynamic Library After the Library Is Released
      ```

      **特征：**栈顶为Not mapped。栈顶指针不落在任何动态库的可执行段。
3. **栈溢出**。

   递归过深或局部变量过大导致栈空间耗尽，访问了栈边界之外的未映射内存。

   **示例：**详情参见下文案例五。

   ```cpp
   static void RecursiveFunction(int depth)
   {
       char buffer[1024];
       memset(buffer, 0, sizeof(buffer));
       if (depth < 10000) {
           RecursiveFunction(depth + 1);
       }
   }
   ```

   **特征：**故障时操作的地址不在栈空间范围内，一般Reason字段中会有current thread stack low address = 0x000000xxxxxxxx, probably caused by stack-buffer-overflow的字样。递归调用导致的问题调用栈同样最多显示255层栈。
4. **虚拟机多线程**。

   由于JavaScript本身是单线程的，对JS对象的任何操作都必须在创建该JS线程的原始线程上进行。如果违反了这一规则，就会导致多线程安全问题。

   **示例：**详情参见下文案例七。

   ```cpp
       callNativeFunc(); // Saving the JS object on the native side.
       ...
       destroyJsobj(); // The JS object has been destroyed.
       ...
       callNativeFunc(); // The saved JS object is used by other threads.
   ```

   **特征：**栈顶是libark\_jsruntime.so、stub.an、libace\_napi.z.so等会操作JS对象的库。
5. **STL库是非线程安全**。

   在多线程操作STL容器（如vector、map、set等）的场景中，由于STL容器是非线程安全的，当出现竞争时也会产生异常。

   **示例：**详情参见下文案例三。

   ```cpp
   std::vector<int> sharedVector = std::vector<int>();

   auto task = [&] {
       int counter = 0;
       while (true) {
           sharedVector.push_back(counter++);
       }
   };

   std::thread writerThread1(task);
   std::thread writerThread2(task);
   ```

   **特征：**栈顶是在进行容器操作。
6. **栈不可信。**

   当栈上的LR寄存器被踩之后，当前函数退出，需要回到该函数被调用的位置继续向后执行时，读取栈上保存的LR寄存器，进行跳转。此时地址已经非法，触发崩溃。在此场景下，故障日志中的栈帧00和01之后的是不可信。00和01由于是读取的当前寄存器中PC和LR所以是可信的。

   **示例：**详情参见下文案例八。

   ```cpp
   void Func()
   {
       char buff[16];
       memset(buff, 0x41, 64); // Write cache, stack stepping
       return; // crash
   }
   ```

   **特征**：在LastFatalMessage中会有Failed to unwind stack, try to get unreliable call stack from #03 by reparsing thread stack的字样。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* probably caused by NULL pointer dereference：空指针解引用，需要注意的是其他场景也可能会出现该字样，例如：虚拟机多线程等。
* 6b：UAF，访问的寄存器值以6b开头。
* current thread stack low address = 0x000000xxx, probably caused by：栈溢出，访问栈外内存。
* Not mapped：动态库被卸载，需要执行的地址不在有效的可执行段内存地址上。
* Failed to unwind stack, try to get unreliable call stack from #03 by reparsing thread stack：堆栈不可信。

### 案例分析

**案例一：空指针解引用**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
napi_value TriggerInvalidMemoryMAPERR(napi_env env, napi_callback_info info)
{
    char *p = nullptr;
    p[1] = 1;
    return nullptr;
}
```

上述函数生成的故障日志节选如下。

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000000000000001  probably caused by NULL pointer dereference
Fault thread info:
Tid:64855, Name:ppcrashanalysis
#00 pc 00000000000f3484 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerInvalidMemoryMAPERR(napi_env__*, napi_callback_info__*)+28)(0a973579a606828fd6f3e99787bb7e4c444f8464)
#01 pc 000000000005f7b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(7fd796b76701cf17dca125280fa3cefd)
...
Registers:
x0:0000000000000000 x1:0000007e2ec711c0 x2:00000059e1c9f6c0 x3:0001000000000000
x4:00000013fffc1b50 x5:0000007e2ec711d0 x6:000000000000000d x7:000000000000000a
x8:0000000000000001 x9:0000000000000000 x10:0000000000000000 x11:0000000000010000
x12:0000000000000008 x13:0000000000000018 x14:00000000ffffffff x15:00000000000001e6
x16:00000059e1ce2b68 x17:00000059d8dd0504 x18:00000000000001d0 x19:00000059f3a4c000
x20:00000059eefaa100 x21:0000005b5e1b3468 x22:0000007e2ec711c0 x23:0000000000000000
x24:0000000000000122 x25:00000059e1ce5738 x26:0000007e2ec70fb0 x27:00000059d333e340
x28:0000000000000000 x29:0000007e2ec71140
lr:00000059e1c9f7b4 sp:0000007e2ec70ef0 pc:0000005b5e1b3484
pstate:0000000080001000 esr:0000000000000001
```

**故障分析**

1. 确认类型。

   查看Reason，故障地址为极小值0x1；且有probably caused by NULL pointer dereference的字样，判定为空指针解引用问题。
2. 调用栈分析。

   根据调用栈，对00帧进行反编译（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取没有去符号化的二进制文件）。

   ```screen
   .text:00000000000F347C                 ADRP            X8, #qword_1A0B50@PAGE
   .text:00000000000F3480                 LDR             X8, [X8,#qword_1A0B50@PAGEOFF]
   .text:00000000000F3484                 LDR             X8, [X8]
   .text:00000000000F3488                 STUR            X8, [X29,#-8]
   ```

   通过汇编代码可以看到问题点在LDR X8, [X8]，访问X8寄存器的值，此时X8寄存器的值为01，属于一个空指针的解引用。**当代码行中有多个指针时，可以通过阅读汇编代码的方式确认访问异常的指针**。
3. 代码分析。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具对00000000000f3484偏移地址进行解析（本例中也可以使用DevEco Studio故障日志的直接跳转功能）可知，指向示例中的p[1] = 1；这也是印证了调用栈分析的结论。在实际问题中不会如同示例中如此明显，需要开发者对指针的生命周期进行检查。
4. 更多日志。

   当前示例无需更多日志辅助分析。实际问题分析时可结合流水日志对指针进行生命周期的分析。

分析结论：该问题为对空指针进行解引用导致的崩溃。

**开发建议**

* 问题排查建议
  + 通过串联业务，查找指针的生命周期是否合理。
  + 查找是否有多个变量持有同一个裸指针，此场景可以使用shared\_ptr。
  + 排查是否会有多线程同时访问的风险，此场景需要对共享资源进行合理的加锁保护。
  + 上述手段无法排查时，可以使用ASan版本进行问题复现。
* 编码建议
  + 指针在使用前进行有效性判断。
  + 避免使用裸指针。使用C++的RAII机制进行生命周期管理。
  + 裸指针禁止多个位置拷贝保存。
  + 手动管理的指针在内存释放后将指针手动赋值为nullptr。

**案例二：UAF问题分析示例**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
napi_value TriggerInvalidMemoryMAPERRUAF(napi_env env, napi_callback_info info)
{
    int tmp = 1;
    int **p = new int* [10];
    *p = &tmp;
    delete [] p;
    **p = 2; // 2 : value
    return nullptr;
}
```

上述函数生成的故障日志节选如下。

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x006b1e7f9352c001 
Fault thread info:
Tid:54719, Name:ppcrashanalysis
#00 pc 00000000000f36a8 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerInvalidMemoryMAPERRUAF(napi_env__*, napi_callback_info__*)+108)(61595c468ddd8bf122407e3c291e4d1b07fbcacf)
#01 pc 000000000005f7b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(7fd796b76701cf17dca125280fa3cefd)
...
Registers:
x0:00000059d3a02400 x1:6b6b1e7f9352c001 x2:00000059e1c9f6c0 x3:0001000000000000
x4:00000013fffc1b50 x5:0000007e2ec711c0 x6:000000000000000d x7:000000000000000a
x8:0000000000000002 x9:6b6b1e7f9352c001 x10:6b6b000000000000 x11:00000059f47e87a0
x12:0000000000000008 x13:0000000000000018 x14:00000000ffffffff x15:0000000000000000
x16:0000005a062f4b20 x17:00000059d31baa04 x18:00000000000001d0 x19:00000059f3a4c000
x20:00000059eefaa100 x21:0000005b5c93363c x22:0000007e2ec711b0 x23:0000000000000000
x24:0000000000000172 x25:00000059e1ce5738 x26:0000007e2ec70fa0 x27:00000059d333e340
x28:1000000200000000 x29:0000007e2ec70ef0
lr:0000005b5c933698 sp:0000007e2ec70ec0 pc:0000005b5c9336a8
pstate:0000000020001000 esr:006b1e7f9352c001
```

**故障分析**

1. 确认类型。

   查看Reason只有故障地址，没有其他的提示信息。将故障地址0x006b1e7f9352c001在寄存器中进行查看，寄存器中为x1:6b6b1e7f9352c001/x9:6b6b1e7f9352c001，均以6b开头，判断为UAF问题。
2. 调用栈分析。

   根据调用栈，对00帧进行反编译。（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取带符号的二进制文件）

   ```screen
   .text:00000000000F369C                 LDR             X8, [SP,#0x40+var_30]
   .text:00000000000F36A0                 LDR             X9, [X8]
   .text:00000000000F36A4                 MOV             W8, #2
   .text:00000000000F36A8                 STR             W8, [X9]
   .text:00000000000F36AC                 BRK             #1
   ```

   通过查看汇编代码可以看到问题点在STR W8, [X9]，这里可以得出结论需要访问x9寄存器的指向的值。X9寄存器的值以6b开头，表明该内存已经被释放过。可以参考[内存问题引发的Crash故障](../harmonyos-guides/cppcrash-guidelines.md#内存问题引发的crash故障)对6b的解释。
3. 代码分析。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具对00000000000f36a8偏移地址进行解析（本例中也可以使用DevEco Studio故障日志的直接跳转功能）可知，指向示例中的\*\*p = 2; 这也是印证了分析结论。
4. 更多日志。

   实际问题分析中，可以通过hilog日志串联业务流程，辅助分析指针的生命周期，查找不当释放的位置。

分析结论：该问题为访问一片已经释放的内存时触发崩溃。需要对相关的指针进行排查，保证有效的生命周期，防止出现UAF问题。

**开发建议**

* 问题排查建议
  + 通过串联业务，查找指针的生命周期是否合理。
  + 排查是否有时序问题，指针已经被提前释放。
  + 查找是否有多个变量持有同一个裸指针。
  + 排查是否会有多线程同时访问的风险，此场景需要对共享资源进行合理的加锁保护。
  + 上述手段无法排查时，可以使用ASan版本进行问题复现。
* 编码建议
  + 使C++的RAII机制进行生命周期的管理。
  + 手动管理的指针在内存释放后将指针手动赋值为nullptr。
  + 使用智能指针进行内存管理。

**案例三：STL容器非线程安全**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
napi_value TriggerStlContainerRace(napi_env env, napi_callback_info info)
{
    volatile bool stopThreads = false;
    std::vector<int> sharedVector = std::vector<int>();
    
    std::thread writerThread1([&] {
        int counter = 0;
        while (!stopThreads) {
            sharedVector.push_back(counter++);
        }
    });
    
    std::thread writerThread2([&] {
        int counter = 0;
        while (!stopThreads) {
            sharedVector.push_back(counter++);
        }
    });
    
    sleep(5); // 5 : wait time
    
    stopThreads = true;
    writerThread2.join();
    writerThread1.join();
    return nullptr;
}
```

上述的示例代码不能稳定生成SIGSEGV(SEGV\_MAPERR)，由于多线程并发的随机性，还有概率生成SIGSEGV(SEGV\_ACCERR)等其他类型的故障。

上述代码生成的SIGSEGV(SEGV\_MAPERR)故障日志节选如下。

```screen
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0xfffffffffffff9d0 
Fault thread info:
Tid:11840, Name:ppcrashanalysis
#00 pc 0000000000145170 /system/lib/ld-musl-aarch64.so.1(memcpy+432)(b542f5b9ca34c1f117b06c04e67f8604)
#01 pc 0000000000013a00 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#02 pc 0000000000013794 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#03 pc 0000000000013618 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#04 pc 00000000000134fc /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#05 pc 00000000000132c0 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#06 pc 0000000000012a2c /data/storage/el1/bundle/libs/arm64/libentry.so(std::__n1::vector<int, std::__n1::allocator<int>>::__swap_out_circular_buffer(std::__n1::__split_buffer<int, std::__n1::allocator<int>&>&)+136)(75af9681c85ad20a8b6b2c7088a4428784459547)
#07 pc 00000000000125c4 /data/storage/el1/bundle/libs/arm64/libentry.so(void std::__n1::vector<int, std::__n1::allocator<int>>::__push_back_slow_path<int>(int&&)+172)(75af9681c85ad20a8b6b2c7088a4428784459547)
#08 pc 0000000000012418 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#09 pc 0000000000012388 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547) // sharedVector->push_back(counter++);
#10 pc 00000000000122ec /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#11 pc 00000000000122c8 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#12 pc 00000000000120a0 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#13 pc 00000000001e02cc /system/lib/ld-musl-aarch64.so.1(start+240)(b542f5b9ca34c1f117b06c04e67f8604)
Registers:
x0:0000005bc0e00f60 x1:0000000000000000 x2:fffffffffffff9e0 x3:0000000000000000
x4:fffffffffffff9e0 x5:0000005bc0e00940 x6:0000005bc0e00940 x7:000032c17916f69b
x8:fffffffffffffe78 x9:0000000000000004 x10:fffffffffffffe78 x11:0000005bc0d7e610
x12:0000000000000000 x13:0000005b0cb4f000 x14:0000005bc0e00f60 x15:0000000000000000
x16:0000005d1dd1d000 x17:0000005b0c874fc0 x18:00000000000001d0 x19:0000005bbfa06908
x20:0000005bbfa068f8 x21:0000005b0cc23000 x22:0000000000000000 x23:0000005bbf904000
x24:0000005bbfa06938 x25:0000005bbfa06918 x26:0000005bbfa06908 x27:0000005bbfa068f8
x28:0000005b0c944518 x29:0000005bbfa06340
lr:0000005d1dd13a04 sp:0000005bbfa062e0 pc:0000005b0c875170
pstate:0000000000001000 esr:0000000092000004
Other thread info:
...
Tid:11841, Name:ppcrashanalysis
#00 pc 0000000000012890 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#01 pc 00000000000145a8 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#02 pc 000000000001456c /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#03 pc 000000000001453c /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)  // sharedVector.push_back();
#04 pc 00000000000144c4 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#05 pc 00000000000144a0 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#06 pc 0000000000014278 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#07 pc 00000000001e02cc /system/lib/ld-musl-aarch64.so.1(start+240)(b542f5b9ca34c1f117b06c04e67f8604)
```

**故障分析**

1. 确认类型。

   通过Reason字段分析，故障地址0xfffffffffffff9d0不是一个有效的内存地址。查看栈顶为memcpy，可以得出结论是给memcpy传入了一个异常的指针导致的问题。
2. 调用栈分析。

   分析故障线程调用栈，分析传递异常指针的原因。参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具解析偏移地址（这里也可以使用DevEco Studio栈帧跳转）可看到09帧是在对vector做push\_back操作。鉴于此，出现访问问题的原因考虑是vector内存被踩。由于STL容器是非并发安全，查找其他线程调用栈，11841号线程也在进行vector的访问，推断是并发访问导致的。
3. 代码分析。

   通过对代码进行分析，故障线程和步骤2中是对同一个vector进行访问。到这里可以确认是由于并发访问vector导致的内存问题。
4. 更多日志。

   实际业务中，可以结合流水日志梳理业务流程辅助分析问题。

分析结论：该问题为非线程安全的STL vector容器并发操作导致的崩溃。

**开发建议**

* 问题排查建议
  + 在实际问题分析中，由于触发问题时已经不是问题的第一现场，大概率抓不到另外一个线程也在操作vector的堆栈。此时使用ASan版本进行问题复现，依赖ASan版本抓栈进行问题定位。
  + 当栈顶是在操作STL容器时，对代码进行排查，看是否是由于并发访问导致。
* 编码建议
  + STL容器都是非线程安全的，需要并发访问时，需要加锁保护，防止并发。

**案例四：数组越界**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
napi_value TriggerArrayOverflow(napi_env env, napi_callback_info info)
{
    constexpr size_t size = 10;
    int *arr = new int[size];
    const uint32_t bigSize = 100000000;
    arr[bigSize] = 42; // 42 : value
    delete[] arr;
    return nullptr;
}
```

上述函数生成的故障日志节选如下。

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000005b7ab10b50 
Fault thread info:
Tid:38172, Name:ppcrashanalysis
#00 pc 00000000000f34a8 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerArrayOverflow(napi_env__*, napi_callback_info__*)+56)(cfc15fd6462d53ec7e8602acf4618f454b5475bc)
#01 pc 000000000005f7b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(7fd796b76701cf17dca125280fa3cefd)
...
Registers:
x0:0000005b62d98750 x1:6b6b1e7d05f5c0f1 x2:00000059e1c9f6c0 x3:0001000000000000
x4:00000013fffc1b50 x5:0000007e2ec711d0 x6:000000000000000d x7:000000000000000a
x8:000000000000002a x9:0000005b62d98750 x10:0000000017d78400 x11:0000005b62d98750
x12:0000000000000008 x13:0000000000000018 x14:00000000ffffffff x15:0000000000000000
x16:0000005a07034b18 x17:00000059d31ba800 x18:00000000000001d0 x19:00000059f3a4c000
x20:00000059eefaa100 x21:0000005b5e473470 x22:0000007e2ec711c0 x23:0000000000000000
x24:0000000000000122 x25:00000059e1ce5738 x26:0000007e2ec70fb0 x27:00000059d333e340
x28:0000000000000000 x29:0000007e2ec70f00
lr:0000005b5e473494 sp:0000007e2ec70ed0 pc:0000005b5e4734a8
pstate:0000000060001000 esr:0000005b7ab10b50
...
Maps:
...
5b62521000-5b63321000 rw-p 00000000 [anon:native_heap:jemalloc]
5b63321000-5b646cb000 r--p 00000000 /system/fonts/HarmonyOS_Sans_SC.ttf
5b646cb000-5b656cb000 rw-p 00000000 [anon:native_heap:jemalloc]
7e2e47d000-7e2e47f000 ---p 00000000 [guard]
7e2e47f000-7e2ec7d000 rw-p 00000000 [stack]
```

**故障分析**

1. 确认类型。

   查看Reason字段中的故障地址0x0000005b7ab10b50在寄存器中除去esr寄存器以外无相关记录，查找Maps也无直接关联的内存段，暂时不直接确定故障类型。
2. 调用栈分析。

   根据调用栈，对00帧llvm-objdump.exe -C -S -l -d libentry.so | c++filt.exe > obj.asm进行反编译。（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取带符号的二进制文件）

   ```screen
   00000000000f3470 <TriggerArrayOverflow(napi_env__*, napi_callback_info__*)>:
   ; TriggerArrayOverflow(napi_env__*, napi_callback_info__*)():
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:81
   ; napi_value TriggerArrayOverflow(napi_env env, napi_callback_info info) {
   f3470: d10103ff     	sub	sp, sp, #64
   f3474: a9037bfd     	stp	x29, x30, [sp, #48]
   f3478: 9100c3fd     	add	x29, sp, #48
   f347c: f81f83a0     	stur	x0, [x29, #-8]
   f3480: f81f03a1     	stur	x1, [x29, #-16]
   f3484: d2800148     	mov	x8, #10
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:83
   ;     constexpr size_t size = 10;
   f3488: f9000fe8     	str	x8, [sp, #24]
   f348c: d2800500     	mov	x0, #40
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:84
   ;     int *arr = new int[size];
   f3490: 940274f4     	bl	0x190860 <_Znam@plt>
   f3494: f9000be0     	str	x0, [sp, #16]
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:86
   ;     arr[100000000] = 42;
   f3498: f9400be9     	ldr	x9, [sp, #16]
   f349c: d290800a     	mov	x10, #33792
   f34a0: f2a2faea     	movk	x10, #6103, lsl #16
   f34a4: 52800548     	mov	w8, #42
   f34a8: b82a6928     	str	w8, [x9, x10]
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:87
   ;     delete[] arr;
   f34ac: f9400be8     	ldr	x8, [sp, #16]
   f34b0: f90007e8     	str	x8, [sp, #8]
   f34b4: f1000108     	subs	x8, x8, #0
   f34b8: 1a9f17e8     	cset	w8, eq
   f34bc: 370000a8         tbnz	w8, #0, 0xf34d0 <TTriggerArrayOverflow(napi_env__*, napi_callback_info__*)+0x60>
   f34c0: 14000001          b	0xf34c4 <TTriggerArrayOverflow(napi_env__*, napi_callback_info__*)+0x54>
   f34c4: f94007e0     	ldr	x0, [sp, #8]
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:87
   ;     delete[] arr;
   f34c8: 940274fa     	bl	0x1908b0 <_ZdaPv@plt>
   f34cc: 14000001         b	0xf34d0 <TTriggerArrayOverflow(napi_env__*, napi_callback_info__*)+0x60>
   f34d0: aa1f03e0     	mov	x0, xzr
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:88
   ;     return nullptr;
   f34d4: a9437bfd     	ldp	x29, x30, [sp, #48]
   f34d8: 910103ff     	add	sp, sp, #64
   f34dc: d65f03c0     	ret
   ```

   故障指令为str w8, [x9, x10]，将w8的值拷贝到[x9, x10]所在的内存地址，x9 + x10 = 0x5B7AB10B50，查看Maps内容，该地址不落在任何地址段中，最靠近的地址是native\_heap段。分析汇编代码，x9是new出来的栈内存，x9寄存器指向的段，落在5b62521000-5b63321000 rw-p 00000000 [anon:native\_heap:jemalloc]段，这是符合预期的。而访问x9 + x10即为访问以x9为基地址的一段内存，最后需要访问的地址是非法地址导致的崩溃。在本例中x10超大，显而易见的是一个超大的非法索引。
3. 代码分析。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具对00000000000f34a8偏移地址进行解析（本例中也可以使用DevEco Studio故障日志的直接跳转功能）可知，指向示例中的arr[bigSize] = 42代码行，这里是进行数组访问，结合前后的代码可以发现这里是对数组越界的访问，这也符合步骤2中分析的结果。至此可以判定当前问题是数组越界访问。
4. 更多日志。

   实际业务中，如果是变长数组需要结合日志来判断是否发生了越界。

分析结论：由于数组越界访问导致的崩溃。

**开发建议**

* 问题排查建议
  + 排查索引是否发生越界访问
* 编码建议
  + 在进行数组访问前需要进行边界检查
  + 使用C++的for循环时，需要特别注意删除等会操作迭代的操作。

    ```cpp
        void Func()
        {
            std::vector<int> c{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            // Positive example
            for (std::vector<int>::iterator it = c.begin(); it != c.end();)
            {
                if (*it % 2 == 0) {
                    it = c.erase(it);
                } else {
                    ++it;
                }
            }
            // counter example
            for (std::vector<int>::iterator it = c.begin(); it != c.end(); ++it)
            {
                if (*it % 2 == 0) {
                    it = c.erase(it);
                }
            }
        }
    ```

**案例五：栈溢出**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
static void RecursiveFunction(int depth)
{
    char buffer[1024];
    memset_s(buffer, sizeof(buffer), 0, sizeof(buffer));
    if (depth < 10000) { // 10000 : depth
        RecursiveFunction(depth + 1);
    }
}

napi_value TriggerStackOverflow(napi_env env, napi_callback_info info)
{
    RecursiveFunction(0);
    return 0;
}
```

上述函数生成的故障日志节选如下。

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000007e6f57afb4  current thread stack low address = 0x0000007e6f57b000, probably caused by stack-buffer-overflow
Fault thread info:
Tid:13753, Name:ppcrashanalysis
#00 pc 000000000000c50c /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
#01 pc 000000000000c540 /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
#02 pc 000000000000c540 /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
#03 pc 000000000000c540 /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
...
#254 pc 000000000000c540 /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
#255 pc 000000000000c540 /data/storage/el1/bundle/libs/arm64/libentry.so(4077e1c7e7f6d108a2601e77d5e88f16386c1416)
...
Registers:
x0:0000000000001e5a x1:0000000000000000 x2:ffffffffffffffe8 x3:0000007e6f57b780
x4:0000007e6f57b7e8 x5:0000000000000004 x6:0000000080000000 x7:7f7f7f7f7f7f7f7f
x8:83777015dae2003f x9:0000000000002710 x10:6b6b000000000000 x11:0000005c8fd7d100
x12:0000000000000000 x13:aaaaaaaa00000000 x14:000000003b9ac9ff x15:0000000000000000
x16:0000005b356d45c8 x17:0000005a842d01c0 x18:00000000000001d0 x19:0000005b2615c000
x20:0000005b21692c00 x21:0000007e6fd6cfa0 x22:0000005b356ca250 x23:0000000000000000
x24:0000000000000122 x25:0000005b105d9d88 x26:0000007e6fd6cd90 x27:0000005a8468a5d0
x28:0000005b0d99f2d8 x29:0000007e6f57b3c0
lr:0000005b356cc544 sp:0000007e6f57afb0 pc:0000005b356cc50c
pstate:0000000080001000 esr:0000000092000047
...
FaultStack:
...
    0000007e6f57afa0 ffffffffffffffff
    0000007e6f57afa8 ffffffffffffffff
sp0:0000007e6f57afb0 ffffffffffffffff
    0000007e6f57afb8 ffffffffffffffff
    0000007e6f57afc0 ffffffffffffffff
    0000007e6f57afc8 ffffffffffffffff
    0000007e6f57afd0 ffffffffffffffff
    0000007e6f57afd8 ffffffffffffffff
    0000007e6f57afe0 ffffffffffffffff
    0000007e6f57afe8 ffffffffffffffff
    0000007e6f57aff0 ffffffffffffffff
    0000007e6f57aff8 ffffffffffffffff
    0000007e6f57b000 0000000000000000
    0000007e6f57b008 0000000000000000
    0000007e6f57b010 0000000000000000
    0000007e6f57b018 0000000000000000
    0000007e6f57b020 0000000000000000
    0000007e6f57b028 0000000000000000
    0000007e6f57b030 0000000000000000
    0000007e6f57b038 0000000000000000
    0000007e6f57b040 0000000000000000
...
Maps:
...
5c9688f000-5c9708f000 rw-p 00000000 [anon:ffrt_coroutine_stack]
7e6f579000-7e6f57b000 ---p 00000000 [guard]
7e6f57b000-7e6fd79000 rw-p 00000000 [stack]
```

**故障分析**

1. 确认类型。

   通过查看Reason字段可知，当前问题可能为栈溢出。进一步查看故障地址0x0000007e6f57afb4已经不在栈7e6f57b000-7e6fd79000 rw-p 00000000 [stack]范围内，可以明确为栈溢出的问题。通过调用栈可以看出，出现了递归调用，这也往往是栈溢出的一个原因。至此，可以确认当前问题为栈溢出问题。
2. 调用栈分析。

   根据调用栈，对00帧进行反编译（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取带符号的二进制文件）。

   ```screen
   .text:000000000000C4EC _ZL17RecursiveFunctioni                 ; CODE XREF: StackOverflow(napi_env__ *,napi_callback_info__ *)+48�p
   .text:000000000000C4EC                                         ; RecursiveFunction(int)+54
   .text:000000000000C4EC
   .text:000000000000C4EC var_41C         = -0x41C
   .text:000000000000C4EC var_418         = -0x418
   .text:000000000000C4EC var_10          = -0x10
   .text:000000000000C4EC var_8           = -8
   .text:000000000000C4EC var_s0          =  0
   .text:000000000000C4EC
   .text:000000000000C4EC                 STP             X29, X30, [SP,#-0x10+var_10]! ; Alternative name is '$x.181'
   .text:000000000000C4F0                 STR             X28, [SP,#0x10+var_s0]
   .text:000000000000C4F4                 MOV             X29, SP
   .text:000000000000C4F8                 SUB             SP, SP, #0x410
   .text:000000000000C4FC                 ADRP            X8, #qword_14350@PAGE
   .text:000000000000C500                 LDR             X8, [X8,#qword_14350@PAGEOFF]
   .text:000000000000C504                 LDR             X8, [X8]
   .text:000000000000C508                 STUR            X8, [X29,#var_8]
   .text:000000000000C50C                 STR             W0, [SP,#0x420+var_41C]
   .text:000000000000C510                 ADD             X0, SP, #0x420+var_418
   .text:000000000000C514                 MOV             W1, WZR
   ```

   故障指令为STR W0, [SP, #0x420+var\_41C]，其操作是将W8寄存器的值进行压栈，而故障地址为0x0000007e6f57afb4，其地址不在栈空间7e6f57b000-7e6fd79000的范围内，属于栈溢出问题。
3. 代码分析。

   查看栈顶代码发现，RecursiveFunction函数出现了递归调用，而且函数中有一个局部变量，大小为1024，当出现递归调用时，进行压栈会快速消耗栈空间，导致栈溢出。
4. 更多日志。

   实际业务中，需要结合流水日志分析导致递归的原因。为什么没有终止递归，如果经过分析，确实是需要一直递归，那么需要修改递归函数，禁止一直分配栈内存，而改用堆内存。

分析结论：由于递归调用快速消耗栈内存导致的栈溢出问题。

**开发建议**

* 问题排查建议
  + 排查业务进行递归调用是否合理。
  + 排查业务，一直进行大块的栈内存分配是否合理。
* 编码建议
  + 避免不当的递归调用，设置合理的终止递归的条件。
  + 避免在函数中进行大块的栈内存分配，确实需要大内存可以使用堆内存。针对可复用的内存可以使用参数的引用传递进行共享。
  + 在信号处理函数中，栈空间比较小（典型值为24KB）。禁止在信号处理函数中使用超大栈内存；不建议代码实现过于复杂，避免函数层次嵌套过深。

**案例六：动态库被提前释放**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
using Add = int (*)(int, int);
napi_value CallMathAdd(napi_env env, napi_callback_info info)
{
    size_t argc = 3;
    napi_value args[3] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    int value0;
    napi_get_value_int32(env, args[0], &value0);
    int value1;
    napi_get_value_int32(env, args[1], &value1);
    size_t length = 0;
    napi_status status = napi_get_value_string_utf8(env, args[2], nullptr, 0, &length);
    if (status != napi_ok) {
        return nullptr;
    }
    char *path = new char[length + 1];
    memset_s(path, length + 1, 0, length + 1);
    napi_get_value_string_utf8(env, args[2], path, length + 1, &length); // 2 : argv
    void *handle = dlopen(path, RTLD_LAZY);
    if (handle == nullptr) {
        OH_LOG_ERROR(LOG_APP, "[%s@%d] dlopen failed:%s", __func__, __LINE__, dlerror());
        return nullptr;
    }
    napi_value result = nullptr;
    Add addFunc = reinterpret_cast<Add>(dlsym(handle, "add")); // Get function address from dynamic library
    if (addFunc == nullptr) {
        OH_LOG_ERROR(LOG_APP, "[%s@%d] dlsym failed:%s", __func__, __LINE__, dlerror());
        return nullptr;
    }
    dlclose(handle); // Release dynamic library
    int ret = addFunc(value0, value1); // Call function after dynamic library is released
    status = napi_create_int32(env, ret, &result);
    delete[] path;
    if (status != napi_ok) {
        return nullptr;
    }
    return result;
}
```

另外还需要动态库依赖，动态库路径等，导入动态库的过程参考[通过调用dlopen的方式引用](../harmonyos-guides/integrate-third-party-dlls.md#通过调用dlopen的方式引用)动态库。

上述函数生成的故障日志节选如下。

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000007adc3817ac 
Fault thread info:
Tid:27689, Name:ppcrashanalysis
#00 pc 0000007adc3817ac Not mapped
#01 pc 000000000000eef0 /data/storage/el1/bundle/libs/arm64/libentry.so(6648c6a709ee9454c89f7a4f24629f08350ffcad)
#02 pc 000000000005f820 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(3469b98d825ff0165844454647e06a37)
#03 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
#04 pc 000000000047e868 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis3Imm8V8V8V8V8StwCopy+460)
...
Registers:
x0:0000000000000001 x1:0000000000000002 x2:0000000000000000 x3:ffffffffffffffff
x4:0000000000000000 x5:0000000000000000 x6:725e6865625e7368 x7:7f7f7f7f7f7f7f7f
x8:0000007adc3817ac x9:0000007fa6c883d0 x10:0000000000000000 x11:00000059b44eab30
x12:00000059b44eab30 x13:0000000000000000 x14:0000000000000000 x15:0000000000000000
x16:0000007adc382a80 x17:00000059b444af6c x18:00000000000001d0 x19:0000007fa6c88420
x20:0000006db7186080 x21:0000007adeb4e81c x22:0000007fa6c888b0 x23:0000000000000000
x24:0000000000000002 x25:00000079bc065838 x26:0000007fa6c886a0 x27:00000059b44ea340
x28:0000002f4f6c70d0 x29:0000007fa6c885e0
lr:0000007adeb4eef4 sp:0000007fa6c88340 pc:0000007adc3817ac
pstate:0000000020001800 esr:0000000082000007
...
Maps:
...
7adaea0000-7adc24a000 r--p 00000000 /system/fonts/HarmonyOS_Sans_SC.ttf
7adc24a000-7adc24c000 ---p 00000000 [anon:guard:27776]
7adc24c000-7adc34d000 rw-p 00000000 [anon:stack:27776]
7adc450000-7adcc50000 rw-p 00000000 [anon:ffrt_coroutine_stack]
7adcc50000-7adcc52000 ---p 00000000 [anon:guard:27778]
7adcc52000-7adcd53000 rw-p 00000000 [anon:stack:27778]
...
```

**故障分析**

1. 确认类型。

   从Reason字段中只能获取故障地址0x0000007adc3817ac，往下看，该地址为00帧的函数地址，且00帧显示为Not mapped，至此初步判断该问题是由于动态库被卸载导致的。
2. 调用栈分析。

   根据调用栈，对01帧进行反编译（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取带符号的二进制文件）。

   ```screen
   .text:000000000000EEE0
   .text:000000000000EEE0 loc_EEE0                                ; CODE XREF: NAPI_Global_CallMathAdd(napi_env__ *,napi_callback_info__ *)+688
   .text:000000000000EEE0                                         ; NAPI_Global_CallMathAdd(napi_env__ *,napi_callback_info__ *):loc_EED
   .text:000000000000EEE0                 LDR             X8, [X19,#0x48]
   .text:000000000000EEE4                 LDR             W0, [X19,#0x34]
   .text:000000000000EEE8                 LDR             X9, [X19,#0xF0]
   .text:000000000000EEEC                 LDR             W1, [X9]
   .text:000000000000EEF0                 BLR             X8
   .text:000000000000EEF4                 STR             W0, [X19,#0x164]
   .text:000000000000EEF8                 LDR             W7, [X19,#0x164]
   .text:000000000000EEFC                 MOV             W0, WZR
   ```

   通过上述的汇编代码可以找到触发故障的语句为BLR X8，将代码跳转到X8寄存器的地址。这是一个函数调用，直接查看代码。
3. 代码分析。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具对000000000000eef0偏移地址进行解析（本例中也可以使用DevEco Studio故障日志的直接跳转功能），指向示例中的int ret = addFunc(value0, value1)，结合步骤2中的汇编代码可知，当前操作是调用动态库的函数指针时发生异常。结合代码前后文可知，函数所在的动态库已经被dlclose。
4. 更多日志。

   实际问题分析可以结合流水日志分析动态库的生命周期。

分析结论：由于动态库被提前释放，在进行动态库中的函数调用时发生崩溃。

**开发建议**

* 问题排查建议
  + 排查业务对动态库的生命周期管理，禁止在动态库释放后调用库内的函数。
  + 排查是否有多线程在操作使用同一个动态库，并且有不当的动态库管理。
* 编码建议
  + 注意动态库的生命周期管理，防止不当的释放，尤其需要注意多线程并发问题。
  + 可以考虑使用单例对动态库进行统一的管理和释放。
  + 动态库被打开后，不要对函数指针进行保存传递，如果需要保存、传递，一定需要保证动态库有效。

**案例七：虚拟机多线程问题**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

在NAPI侧提供JS对象的保存和使用的代码：

```cpp
static napi_env global_env = nullptr;
napi_value SaveEnv(napi_env env, napi_callback_info info)
{
    global_env = env; // Save JS environment
    return nullptr;
}

napi_value UseEnv(napi_env env, napi_callback_info info)
{
    // Use saved JS environment
    size_t parameterCount = 1;
    napi_value parameters[1] = {0};
    napi_value thisVar = nullptr;
    void *data = nullptr;
    if (napi_get_cb_info(global_env, info, &parameterCount, parameters, &thisVar, &data) != napi_ok) {
        return nullptr;
    }
    
    napi_ref callbackRef = nullptr;
    if (napi_create_reference(global_env, parameters[0], 1, &callbackRef) != napi_ok) {
        return nullptr;
    }
    napi_value callbackFunc = nullptr;
    if (napi_get_reference_value(global_env, callbackRef, &callbackFunc) != napi_ok) {
        return nullptr;
    }
    napi_value recv = nullptr;
    if (napi_get_undefined(global_env, &recv) != napi_ok) {
        return nullptr;
    }
    napi_value result = nullptr;
    napi_value callbackValues[] = { nullptr };
    if (napi_call_function(global_env, recv, callbackFunc, sizeof(callbackValues) / sizeof(napi_value), callbackValues,
                           &result) != napi_ok) {
        return nullptr;
    }
    if (napi_delete_reference(global_env, callbackRef) != napi_ok) {
        return nullptr;
    }
    return nullptr;
}
```

在ETS侧提供worker线程，调用NAPI接口对JS对象进行保存：

```typescript
import dfxNapi from 'libentry.so';

import type { MessageEvents, ErrorEvent } from '@kit.ArkTS';
import { worker } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const ARRAY_FILL_VALUE: number = 3;
const LOG_DOMAIN: number = 0x0000;
const LOG_TAG: string = 'WorkerManager';

// Creates a worker thread object for communicating with the sink main thread.
const workerPort = worker.workerPort;

// Information received by the worker thread from the host main thread.
workerPort.onmessage = (e: MessageEvents): void => {
  dfxNapi.SaveEnv();

  // The worker thread sends information to the host main thread.
  const view = new Int8Array().fill(ARRAY_FILL_VALUE);
  workerPort.postMessage(view);
};

// Callback function for the error occurred in the worker thread.
workerPort.onerror = (err: ErrorEvent): void => {
  hilog.error(LOG_DOMAIN, LOG_TAG, 'worker.ets onerror' + err.message);
};
```

提供在worker线程销毁后，使用NAPI侧保存的JS对象：

```typescript
private MultiThread(): void {
  // Create a Worker object in the host thread.
  const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets');
  // The host thread passes information to the worker thread.
  const buffer = new ArrayBuffer(BUFFER_SIZE);
  workerInstance.postMessage(buffer);
  // The sink main thread receives information from the worker thread.
  workerInstance.onmessage = (e: MessageEvents): void => {
    // Destroy the Worker object.
    workerInstance.terminate();

    dfxNapi.UseEnv(() => {
      hilog.info(LOG_DOMAIN, 'DFX', `create_object callback`);
    });
  };
  // After calling terminate, execute onexit.
  workerInstance.onexit = (): void => {
    hilog.error(LOG_DOMAIN, LOG_TAG, 'main thread terminate');
  };

  workerInstance.onAllErrors = (err: ErrorEvent): void => {
    hilog.error(LOG_DOMAIN, LOG_TAG, 'main error message ' + err.message);
  };
}
```

worker的配置声明：

```screen
// entry\build-profile.json5
{
  "buildOption": {
    "sourceOption": {
      "workers": [
        "./src/main/ets/workers/save_env_worker.ets",
      ]
    },
  }
}
```

上述代码生成的故障日志节选如下：

```screen
...
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x00000000000001f0  probably caused by NULL pointer dereference
Fault thread info:
Tid:28546, Name:ppcrashanalysis
#00 pc 000000000021ac18 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ConstantPool::GetStringFromCache(panda::ecmascript::JSThread*, panda::ecmascript::JSTaggedValue, unsigned int)+2032)(ac2f8c031d558352edfdc1f1e48a80da)
#01 pc 000000000021a358 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::RuntimeStubs::GetStringFromCache(unsigned long, unsigned int, unsigned long)+108)(ac2f8c031d558352edfdc1f1e48a80da)
#02 pc 0000000000e88be8 /system/lib64/module/arkcompiler/stub.an(RTStub_CallRuntime+40)
#03 pc 0000000000495c2c /system/lib64/module/arkcompiler/stub.an(BCStub_HandleLdaStrId16StwCopy+56)
#04 at anonymous entry (entry/src/main/ets/pages/tests/CppCrash.ets:105:17)
#05 pc 0000000000430e34 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+744)(ac2f8c031d558352edfdc1f1e48a80da)
#06 pc 0000000000430070 /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::CallForNapi(panda::ecmascript::EcmaVM const*, panda::JSValueRef*, panda::JSValueRef* const*, int)+512)(ac2f8c031d558352edfdc1f1e48a80da)
#07 pc 000000000007d170 /system/lib64/platformsdk/libace_napi.z.so(napi_call_function+208)(2cab84cf077802c8dfd884592bd4324c)
#08 pc 000000000000e8f0 /data/storage/el1/bundle/libs/arm64/libentry.so(75af9681c85ad20a8b6b2c7088a4428784459547)
#09 pc 0000000000068180 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2cab84cf077802c8dfd884592bd4324c)
...
Registers:
x0:0000000000000000 x1:6b6b32c1793a854b x2:0000000000000016 x3:0000005b9bc842c2
x4:0000005c16cc458f x5:000000243ff33986 x6:6f5f657461657263 x7:6163207463656a62
x8:0000000000000000 x9:0000000000000000 x10:0000000000000000 x11:0000005bc0cc7a90
x12:207463656a626f5f x13:6b6361626c6c6163 x14:0000000000353f8a x15:0000000088e112c3
x16:0000005b9c6b60b8 x17:0000005b0c911efc x18:00000000000001d0 x19:0000005bbf9f3440
x20:0000005bbfa4c020 x21:000000243ff36030 x22:000000243ff33960 x23:0000005bbfa4c028
x24:0000005c16cc4579 x25:0000000000000000 x26:000000243ff33968 x27:00000000000026d0
x28:0000005bbf91b000 x29:0000007e3364c9c0
lr:0000005b9bd1aa68 sp:0000007e3364c830 pc:0000005b9bd1ac18
pstate:0000000080001000 esr:0000000092000007
```

**故障分析**

1. 确认类型。

   通过Reason字段分析，按照案例1的分析过程，这是一个空指针解引用问题。
2. 调用栈分析。

   通过对调用栈分析，栈顶是libark\_jsruntime.so、stub.an。这里怀疑是JS对象跨线程访问导致。具体可以参考[常见多线程安全问题](bpta-stability-ark-runtime-detection.md#section19357830121120)。
3. 代码分析。

   通过DevEco Studio的跳转功能查看业务代码，04帧是dfxNapi.create\_object中参数传递的回调函数，08帧是Native层使用napi\_call\_function进行JS侧函数调用。这里都是JS对象的操作。通过对代码进行分析发现，env被跨线程使用。通过[开启方舟多线程检测](bpta-stability-ark-runtime-detection.md#section7199344111510)进行问题复现，可以明确是由运行时上下文跨线程操作导致的问题。
4. 更多日志。

   结合流水日志分析故障场景，可用于复现问题。

分析结论：该问题为JS对象跨线程访问导致的空指针解引用类崩溃。

**开发建议**

* 问题排查建议
  + 当堆栈栈顶是libark\_jsruntime.so、stub.an等会操作Js对象的库时，可以考虑是由于运行时上下文跨线程操作导致的问题，开启多线程检测进行问题复现定位。
* 编码建议
  + 检查JS对象在Native侧保存的必要性，是否会跨线程使用。应避免出现跨线程进行运行时访问的场景。

**案例八：栈不可信**

**构造故障**

使用如下代码在DevEco Studio中的Native工程中进行故障构造。

```cpp
napi_value TriggerLinkRegisterCorruption(napi_env env, napi_callback_info info)
{
    char buff[16];
    int errLen = 64;
    for (int i = 0; i < errLen; i++) {
        buff[i] = 0x41;
    }
    
    return nullptr;
}
```

上述代码生成的故障日志节选如下。

```screen
Reason:Signal:SIGSEGV(SEGV_MAPERR)@000000000000000000  probably caused by NULL pointer dereference
LastFatalMessage:Failed to unwind stack, try to get unreliable call stack from #03 by reparsing thread stack.
Fault thread info:
Tid:43116, Name:ppcrashanalysis
#00 pc 00000000000b67b8 /system/lib/ld-musl-aarch64.so.1(__stack_chk_fail+4)(5dd0bdf5d51c963c76026832aa3dc923)
#01 pc 0000000000019fd0 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+148)(ad2906eca13ac73d769c2624db5d4df3dc84efec)
#02 pc 000041414141413d Not mapped
#03 pc 00000000001c87f4 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::BaseHeap::OnAllocateEvent(panda::ecmascript::EcmaVM*, panda::ecmascript::TaggedObject*, unsigned long)+76)(6ef29d235261e68a70bf017016103242)
#04 pc 000000000024b128 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewResolvedIndexBindingRecord(panda::ecmascript::JSHandle<panda::ecmascript::SourceTextModule> const&, int)+952)(6ef29d235261e68a70bf017016103242)
#05 pc 000000000024b134 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewResolvedIndexBindingRecord(panda::ecmascript::JSHandle<panda::ecmascript::SourceTextModule> const&, int)+964)(6ef29d235261e68a70bf017016103242)
#06 pc 0000000000006608 /system/lib64/chipset-sdk-sp/libhitrace_meter.so((anonymous namespace)::AddHitraceMeterMarker((anonymous namespace)::TraceMarker&)+840)(3842f4e7841926eb2c408c7e5e70d456)
#07 pc 0000000000006724 /system/lib64/chipset-sdk-sp/libhitrace_meter.so((anonymous namespace)::AddHitraceMeterMarker((anonymous namespace)::TraceMarker&)+1124)(3842f4e7841926eb2c408c7e5e70d456)
#08 pc 00000000001bacc8 /system/lib64/platformsdk/libark_jsruntime.so(panda::JsiRuntimeCallInfo::GetData()+144)(6ef29d235261e68a70bf017016103242)
...
Registers:
x0:0000005ae7eb9100 x1:0000007f898814a0 x2:0000005ad709db70 x3:0001000000000000
x4:0000000000000003 x5:0000007f898814b0 x6:000000000000000d x7:00000000ffffffff
x8:0000000000000000 x9:4141414141414141 x10:0000000000010000 x11:00000021cff02000
x12:0000000000000008 x13:0000000000001b00 x14:00000000000001e9 x15:0000000000000018
x16:0000005afda098c0 x17:0000005a4d6ef7b4 x18:00000000000001d3 x19:0000005aec9dd000
x20:0000005ae7eb9100 x21:0000005afd9d9f3c x22:0000007f898814a0 x23:0000000000000000
x24:0000000000000136 x25:0000005ad70e6c20 x26:0000007f89881290 x27:0000005a4d858850
x28:0000000000000000 x29:0000007f898811e0
lr:0000005afd9d9fd4 sp:0000007f898811b0 pc:0000005a4d6ef7b8
pstate:0000000020001000 esr:0000000092000047
...
```

**故障分析**

1. 确认类型。

   在LastFatalMessage字段中有Failed to unwind stack, try to get unreliable call stack from #03 by reparsing thread stack.的字样。可以确定这是一个栈不可信的问题，真实原因是栈上的lr寄存器被踩导致的。
2. 调用栈分析。

   分析调用栈，由于只有00帧和01帧可信，先看下这两帧。00帧是cfi检测，并且cfi检测失败，01帧是业务代码。 对01帧通过llvm-objdump.exe -C -S -l -d libentry.so | c++filt.exe > obj.asm命令进行反编译。（在entry\build\default\intermediates\cmake\default\obj\arm64-v8a目录下获取带符号的二进制文件）

   ```screen
   0000000000019f3c <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)>:
   ; TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)():
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:111
   ; {
      19f3c: d10103ff     	sub	sp, sp, #64
      19f40: a9037bfd     	stp	x29, x30, [sp, #48]
      19f44: 9100c3fd     	add	x29, sp, #48
      19f48: 90000188     	adrp	x8, 0x49000 <UseEnv(napi_env__*, napi_callback_info__*)>
      19f4c: f943b908     	ldr	x8, [x8, #1904]
      19f50: f9400108     	ldr	x8, [x8]
      19f54: f81f83a8     	stur	x8, [x29, #-8]
      19f58: f9000be0     	str	x0, [sp, #16]
      19f5c: f90007e1     	str	x1, [sp, #8]
      19f60: 52800808     	mov	w8, #64
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:113
   ;     int errLen = 64;
      19f64: b90007e8     	str	w8, [sp, #4]
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:114
   ;     for (int i = 0; i < errLen; i++) {
      19f68: b90003ff     	str	wzr, [sp]
      19f6c: 14000001     	b	0x19f70 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x34>
      19f70: b94003e8     	ldr	w8, [sp]
      19f74: b94007e9     	ldr	w9, [sp, #4]
      19f78: 6b090108     	subs	w8, w8, w9
      19f7c: 1a9fb7e8     	cset	w8, ge
      19f80: 37000188     	tbnz	w8, #0, 0x19fb0 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x74>
      19f84: 14000001     	b	0x19f88 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x4c>
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:115
   ;         buff[i] = 0x41;
      19f88: b98003e9     	ldrsw	x9, [sp]
      19f8c: 910063e8     	add	x8, sp, #24
      19f90: 8b090109     	add	x9, x8, x9
      19f94: 52800828     	mov	w8, #65
      19f98: 39000128     	strb	w8, [x9]
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:116
   ;     }
      19f9c: 14000001     	b	0x19fa0 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x64>
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:114
   ;     for (int i = 0; i < errLen; i++) {
      19fa0: b94003e8     	ldr	w8, [sp]
      19fa4: 11000508     	add	w8, w8, #1
      19fa8: b90003e8     	str	w8, [sp]
      19fac: 17fffff1     	b	0x19f70 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x34>
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:118
   ;     return nullptr;
      19fb0: f85f83a9     	ldur	x9, [x29, #-8]
      19fb4: 90000188     	adrp	x8, 0x49000 <UseEnv(napi_env__*, napi_callback_info__*)+0x6c>
      19fb8: f943b908     	ldr	x8, [x8, #1904]
      19fbc: f9400108     	ldr	x8, [x8]
      19fc0: eb090108     	subs	x8, x8, x9
      19fc4: 1a9f17e8     	cset	w8, eq
      19fc8: 37000068     	tbnz	w8, #0, 0x19fd4 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x98>
      19fcc: 14000001     	b	0x19fd0 <TriggerLinkRegisterCorruption(napi_env__*, napi_callback_info__*)+0x94>
      19fd0: 9400b328     	bl	0x46c70 <__stack_chk_fail@plt>
      19fd4: aa1f03e0     	mov	x0, xzr
   ; D:/workspace/DevEcoStudioProjects/BestPracticeSnippets/CppCrashAnalysis/entry/src/main/cpp/sigsegv/sigsegv.cpp:118
   ;     return nullptr;
      19fd8: a9437bfd     	ldp	x29, x30, [sp, #48]
      19fdc: 910103ff     	add	sp, sp, #64
      19fe0: d65f03c0     	ret
   ```

   可以从汇编代码中可以看出19fd0是跳转到cfi检测进行cfi检测，后面紧跟着是函数结束返回。崩溃的栈顶是cfi检测失败，这里是触发了后向cfi检测失败，即返回地址不合法。印证栈上lr寄存器被踩的结论。
3. 代码分析。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具对0000000000019fd0偏移地址进行解析（本例中也可以使用DevEco Studio故障日志的直接跳转功能），代码指向函数return所在行，这也符合步骤2中分析的在进行后向cfi检查。

   继续分析函数实现，char buff[16]申请栈16字节栈内存，但是memset修改了64KB的内存。由于栈内存布局是向下生长，所以缓冲区的内存地址是小于进入函数时压栈的寄存器地址，在进行越界写操作时，修改了栈上内存导致的故障。

分析结论：不当的缓存操作，踩栈踩到了lr寄存器导致故障。结合上面步骤2中的汇编代码绘制故障时的内存布局如下：

| 内存地址 | 存放内容 |
| --- | --- |
| sp + #48 | x29,x30 |
| sp + #24 | 缓冲区buff |
| sp + #16 | 函数的参数1 |
| sp + #8 | 函数的参数2 |
| sp | 栈顶位置 |

通过这个内存布局图可以清晰的看到当操作buff及其往后64字节的空间时会覆盖栈上缓存的x29和x30寄存器的内容，导致函数栈被踩。

**开发建议**

* 问题排查建议
  + 02以及之后的栈帧都是不可信的，谨慎看待。
  + 遇到栈不可信的问题，排查故障函数是否有对栈上缓存的溢出操作。
* 编码建议
  + 数组等内存的访问需要进行边界判断，禁止越界访问。

### 常见易错代码预防建议

* 对所有外部数据进行合法性校验，常见典型场景有：
  + 作为数组索引：将不可信的数据作为数组索引，可能导致超出数组上限，从而造成非法内存访问。
  + 作为内存偏移地址：将不可信数据作为指针偏移访问内存，可能造成非法内存访问，并可以造成进一步的危害，如任意地址读写。
  + 作为内存分配的尺寸参数：使用0长度分配内存可能造成非法内存访问；未限制分配内存大小会造成过度资源消耗。
  + 作为循环条件：将不可信数据作为循环限定条件，可能会引发缓冲区溢出、内存越界读写、死循环等问题。
  + 作为内存复制长度：可能造成缓冲区溢出问题。
* 函数参数需传入单个对象时应以引用取代指针。
* 引用比指针更安全，因为它一定非空，且一定不会再指向其他目标，不需要检查空指针。
* 如果函数内不修改参数所引用的对象，应当将该参数声明为const引用。
* 在移动操作后，禁止读取已移动对象的值。
* 确保对象在使用之前已被初始化。
* 内存申请前，必须对申请内存大小进行合法性校验。
* 当申请内存大小由程序外部输入时，内存申请前，要求对申请内存大小进行合法性校验，防止申请0长度内存，或者过多地、非法地申请内存。
* 在传递数组参数时，不应单独传递指针。
* 当函数参数类型为数组（不是数组的引用）或者指针时，若调用者传入数组，则在参数传递时数组会退化为指针，其数组长度信息会丢失，容易引发越界读写等问题。
* 禁止将局部变量的地址传递到其作用域外。
* 如果对象在其生命周期之外被引用，则程序会产生未定义行为。
* 当lambda会逃逸出函数外面时，禁止按引用捕获局部变量。
* 如果一个lambda不止在局部范围内使用，禁止按引用捕获局部变量，比如它被传递到了函数的外部，或者被传递给了其他线程的时候。lambda按引用捕获就是把局部对象的引用存储起来。如果lambda的生命周期会超过局部变量生命周期，则可能导致内存不安全。
* 指向资源句柄或描述符的变量，在资源释放后立即赋予新值。
* “指向资源句柄或描述符的变量”包括：指针、文件描述符、socket描述符以及其他指向资源的变量。
* 合理选择值类型、智能指针、裸指针或引用。
* 类型系统是C++提供的重要功能，应该利用类型系统来表达意图，更清晰方便地管理资源。

## SEGV\_ACCERR不可访问的内存地址

### 根因描述

SIGSEGV是系统中进程访问无效内存时收到的信号。根据C++ siginfo\_t结构体中的si\_code字段，可分为两大类：

1. SEGV\_MAPERR：地址未映射，即虚拟地址不在任何VMA（Virtual Memory Area）范围内（如空指针、野指针）。
2. SEGV\_ACCERR：地址已映射，但当前操作违反了该内存区域的访问权限。

SEGV\_ACCERR的核心机制：

CPU的MMU（Memory Management Unit）在进行地址转换时，会检查页表项（PTE）中的权限位（如R/W、U/S、XD/NX）。当程序试图执行以下操作时，MMU会触发页故障（Page Fault），操作系统捕获后向进程发送SIGSEGV并置si\_code = SEGV\_ACCERR。

关键区别：SEGV\_ACCERR表明地址是“存在”的，只是权限不足。这通常不是由空指针直接引起，而是由类型转换错误、常量区写入、代码段踩踏、安全机制被触发等更深层逻辑错误导致。

### 问题分析思路

此类问题通常情况下，会有如下几种可能：

1. 写只读内存：如修改text段、rodata段、字符串字面量、mmap时指定为PROT\_READ的区域。
2. 执行不可执行内存：现代操作系统普遍开启NX（No-eXecute）或DEP（Data Execution Prevention）。若程序跳转至栈、堆或数据段等非可执行区域执行指令，触发此错误。
3. 访问被内核保护的内存：如mprotect已将页面权限设为PROT\_NONE后继续访问。
4. 对只读映射写入：如mmap一个文件时参数使用了MAP\_PRIVATE但修改了映射内容（触发写时复制前试图写只读页，虽然通常写时复制会处理，但如果页面本身映射为只读且没有写权限，第一次写也会触发保护）。
5. 踩内存跑飞：如内存读写越界等异常导致的程序执行异常，通常产生随机的崩溃调用栈，进程崩溃时已非问题发生的第一现场，可以借助HWASan等检测工具辅助分析，具体分析方法请参见[地址越界类问题分析方法](bpta-stability-address-illegal-way.md)。

问题分析的步骤如下：

1. **确认类型：**首先确认崩溃信号是否为SIGSEGV，且si\_code是否为SEGV\_ACCERR，这直接指明了问题的性质。重点关注**访问出错的地址**（fault addr）和**导致崩溃的代码位置**（backtrace），这是定位问题的物理出发点。
2. **调用栈分析：**找到异常内存访问的调用栈，根据栈帧崩溃文件名，转到业务代码栈帧去查看崩溃的函数。
3. **代码分析：**参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)，使用llvm-addr2line工具结合调用栈文件和地址偏移，找到具体业务代码行。根据代码上下文，分析其中可能存在的逻辑问题，从崩溃点出发逆向分析数据从何而来，是否涉及mmap映射，对应的文件是否存在并发修改，如果是硬件问题，是否有系统日志支持。
4. **更多日志：**结合崩溃日志文件中的其他信息，以及hilog日志，还原更多故障现场信息，进行定位。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* SEGV\_ACCERR

### 案例分析

**案例一：修改字符串导致崩溃**

**问题现象**

触发业务代码执行字符串修改后，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR 6.1.0.125(SP29log)cust preload version format error
   DeviceDebuggable:Yes
   Fingerprint:fe6457dbb0d76ebeeb3acbc90ff0b14d65ae5afd7cba2f4aa9c76a2769b49628
   Module name:com.samples.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.0
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     14:27:08.858 /ets/pages/Index:SegvAccerr
     14:27:07.136 /ets/pages/Index:SigSegv
     14:27:04.111 :enters foreground
   Timestamp:2026-06-09 14:27:10.674
   Pid:8180
   Uid:20020200
   Process name:com.samples.cppcrashanalysis
   Process life time:8s
   Process Memory(kB): 189358(Rss)
   Device Memory(kB): Total 15833180, Free 2103052, Available 8339456
   Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000005a34709a6a 
   Fault thread info:
   Tid:8180, Name:ppcrashanalysis
   #00 pc 0000000000012c34 /data/storage/el1/bundle/libs/arm64/libentry.so(AccessString(napi_env__*, napi_callback_info__*)+56)(bd43f4c571612e25c0819eb45ff336341094211d)
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   #04 at callback entry (entry/src/main/ets/pages/sigsegv/segv_accerr.ets:21:21)
   #05 at anonymous entry (entry/src/main/ets/component/EntryList.ets:58:24)
   #06 pc 00000000001c0098 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+268)(bcdaa6dbb0e0ac023c972db186c60b63)
   #07 pc 00000000002b3b2c /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+412)(bcdaa6dbb0e0ac023c972db186c60b63)
   #08 pc 0000000000985668 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*) const+276)(d0768bdee195ff44343b1c7006b2f0dc)
   #09 pc 00000000009ac394 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunctionBase::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*)+416)(d0768bdee195ff44343b1c7006b2f0dc)
   #10 pc 000000000112eb6c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsClickFunction::Execute(OHOS::Ace::GestureEvent&)+3392)(d0768bdee195ff44343b1c7006b2f0dc)
   Registers:
   x0:0000005a1fb9f900 x1:0000007e7cdb9630 x2:0000005a107a0340 x3:00000000000001cd
   x4:000000178ffc1b50 x5:0000007e7cdb9640 x6:000000000000000d x7:00000000000001bc
   x8:0000000000000048 x9:0000005a34709a6a x10:0000000000010000 x11:00000020bfd8ef88
   x12:0000000000001b00 x13:00000000000001e3 x14:000000000000000a x15:00000000ffffffff
   x16:0000005a107e32a8 x17:0000005a08b61ab0 x18:0000000000000001 x19:0000005a1fbf0000
   x20:0000005a1fb9f900 x21:0000005a34712bfc x22:0000007e7cdb9630 x23:0000000000000000
   x24:0000000000000136 x25:0000005a107e5e78 x26:0000007e7cdb9420 x27:0000005a0100ee00
   x28:0000000000000000 x29:0000007e7cdb9370
   lr:0000005a107a0434 sp:0000007e7cdb9340 pc:0000005a34712c34
   pstate:0000000080001000 esr:000000009200004f
   ```

   说明1：如上故障日志Reason字段，可以看到崩溃类型为Signal:SIGSEGV(SEGV\_ACCERR)@0x0000005a34709a6a。后面便为访问出错的地址。
2. 分析崩溃栈。

   证据2：

   ```screen
   Fault thread info:
   Tid:8180, Name:ppcrashanalysis
   #00 pc 0000000000012c34 /data/storage/el1/bundle/libs/arm64/libentry.so(AccessString(napi_env__*, napi_callback_info__*)+56)(bd43f4c571612e25c0819eb45ff336341094211d)  --> 业务栈帧，访问出错位置
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   ...
   ```

   说明2：通常认为标准库、系统so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。

   通常用法为llvm-addr2line -Cfie libentry.so 0000005a34709a6a，即可定位到行号，so为带符号版本。

   证据3：

   从上往下跳过C库的调用栈，找到内存访问出错的调用栈，对应#00层调用栈。

   ```cpp
   napi_value AccessString(napi_env env, napi_callback_info info)
   {
       char *p = "hello";
       p[0] = 'H';  // -> access error
       
       // Return null if no error is triggered
       napi_value result;
       napi_get_null(env, &result);
       return result;
   }
   ```

   说明3：此处可以直接定位到具体访问的变量，排查该变量的地址是否合法。

**问题结论与总结**

本案例为修改一个存储在.rodata数据段的字面量，PC指向p[0] = 'H'指令，目标地址p位于.rodata数据段，权限为r--p。

字符串字面量存储在只读数据段，任何写操作都会被MMU拦截，触发SEGV\_ACCERR类崩溃问题。

**修复建议**

使用字符数组char p[] = "hello"分配到栈上。

```cpp
napi_value AccessStringFixed(napi_env env, napi_callback_info info)
{
    char p[] = "hello";
    p[0] = 'H';
    
    napi_value result;
    napi_get_null(env, &result);
    return result;
}
```

**案例二：写只读内存触发崩溃**

**问题现象**

触发业务代码对只读内存执行写操作，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR 6.1.0.125(SP29log)cust preload version format error
   DeviceDebuggable:Yes
   Fingerprint:c69db87c880b42898027fe6f0425971d0c719e7727060b31fbcaaa7b8382eb77
   Module name:com.samples.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.0
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     14:37:59.506 /ets/pages/Index:SegvAccerr
     14:37:58.275 /ets/pages/Index:SigSegv
     14:37:54.014 :enters foreground
   Timestamp:2026-06-09 14:38:00.110
   Pid:16461
   Uid:20020200
   Process name:com.samples.cppcrashanalysis
   Process life time:8s
   Process Memory(kB): 186646(Rss)
   Device Memory(kB): Total 15833180, Free 2069204, Available 8473600
   Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000005a027f8000 
   Fault thread info:
   Tid:16461, Name:ppcrashanalysis
   #00 pc 0000000000012fd8 /data/storage/el1/bundle/libs/arm64/libentry.so(WriteReadableMem(napi_env__*, napi_callback_info__*)+164)(84331389b629ef559552827ec6e4be2ede74e6b7)
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   #04 at callback entry (entry/src/main/ets/pages/sigsegv/segv_accerr.ets:26:21)
   #05 at anonymous entry (entry/src/main/ets/component/EntryList.ets:58:24)
   #06 pc 00000000001c0098 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+268)(bcdaa6dbb0e0ac023c972db186c60b63)
   #07 pc 00000000002b3b2c /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+412)(bcdaa6dbb0e0ac023c972db186c60b63)
   #08 pc 0000000000985668 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*) const+276)(d0768bdee195ff44343b1c7006b2f0dc)
   #09 pc 00000000009ac394 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunctionBase::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*)+416)(d0768bdee195ff44343b1c7006b2f0dc)
   #10 pc 000000000112eb6c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsClickFunction::Execute(OHOS::Ace::GestureEvent&)+3392)(d0768bdee195ff44343b1c7006b2f0dc)
   Registers:
   x0:0000005a027f8000 x1:0000000000001000 x2:0000000000000001 x3:0000000000000022
   x4:ffffffffffffffff x5:0000000000000000 x6:0000000000008080 x7:7f7f7f7f7f7f7f7f
   x8:000000000000002a x9:0000005a027f8000 x10:6b6b000000000000 x11:0000000006ea2385
   x12:0000000000000000 x13:aaaaaaaa00000000 x14:000000003b9ac9ff x15:0000000000000000
   x16:0000005a344e57a8 x17:0000005a00e8c6ac x18:0000000000000001 x19:0000005a1fbf0000
   x20:0000005a1fb9f900 x21:0000005a344d2f34 x22:0000007e7cdb9630 x23:0000000000000000
   x24:0000000000000136 x25:0000005a107e5e78 x26:0000007e7cdb9420 x27:0000005a0100ee00
   x28:0000000000000000 x29:0000007e7cdb9370
   lr:0000005a344d2f94 sp:0000007e7cdb9330 pc:0000005a344d2fd8
   pstate:0000000000001000 esr:0000000092000047
   ```

   说明1：如上故障日志Reason字段，可以看到崩溃类型为Signal:SIGSEGV(SEGV\_ACCERR)@0x0000005a027f8000。后面便为访问出错的地址。
2. 分析崩溃栈。

   证据2：

   ```screen
   Fault thread info:
   Tid:16461, Name:ppcrashanalysis
   #00 pc 0000000000012fd8 /data/storage/el1/bundle/libs/arm64/libentry.so(WriteReadableMem(napi_env__*, napi_callback_info__*)+164)(84331389b629ef559552827ec6e4be2ede74e6b7)  --> 业务栈帧，访问出错位置
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   ...
   ```

   说明2：通常认为标准库、系统so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号，通常用法为llvm-addr2line -Cfie libentry.so 0000005a027f8000，即可定位到行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到内存访问出错的调用栈，对应#00层调用栈。

   ```cpp
   napi_value WriteReadableMem(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "TestTag", "Get stacks");
       const uint32_t mapLen = 4096;
       void* ptr = mmap(nullptr, mapLen, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
       if (ptr == MAP_FAILED) {
           napi_throw_error(env, nullptr, "Failed to allocate memory");
           return nullptr;
       }
       
       int* invalidPtr = static_cast<int*>(ptr);
       *invalidPtr = 42;    // 42 : value invalid access
       
       munmap(ptr, mapLen);
       
       napi_value result;
       napi_get_null(env, &result);
       return result;
   }
   ```

   说明3：此处可以直接定位到具体访问的变量，排查该变量的地址是否合法。
4. 排查访问地址的内存段创建时是否为可读。内存地址段底层均通过mmap函数创建，通过mmap函数调用传入的参数是否为PROT\_READ来判断。

**问题结论与总结**

本案例为通过mmap()函数创建了一个不可读的内存地址段，然后对该地址段进行修改触发SIGSEGV SEGV\_ACCERR类崩溃。

**修复建议**

1. 封装mmap调用，权限参数与实际操作严格匹配；
2. 对映射进行写操作前，检查并确保PROT\_WRITE已设置。

例如：

```cpp
napi_value WriteReadableMemFixed(napi_env env, napi_callback_info info)
{
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "TestTag", "Get stacks");
    const uint32_t mapLen = 4096;
    // Ensure that PROT_WRITE is configured.
    void* ptr = mmap(nullptr, mapLen, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (ptr == MAP_FAILED) {
        napi_throw_error(env, nullptr, "Failed to allocate memory");
        return nullptr;
    }
    
    int* invalidPtr = static_cast<int*>(ptr);
    *invalidPtr = 42;    // 42 : value invalid access
    
    munmap(ptr, mapLen);
    
    napi_value result;
    napi_get_null(env, &result);
    return result;
}
```

**案例三：执行不可执行内存触发崩溃**

**问题现象**

在ARM64平台上，一个计算密集型程序需要动态生成一个专用函数，用来快速计算两个整数的和，以避免重复的函数调用开销。程序在堆上构造了ARM64机器码来实现，但是触发业务代码调用后，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR 6.1.0.125(SP29log)cust preload version format error
   DeviceDebuggable:Yes
   Fingerprint:4bd23c6cf850e9e9888d76933c08f7486717b9d48416b0f0651f3bf2d0a336df
   Module name:com.samples.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.0
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     14:58:18.808 /ets/pages/Index:SegvAccerr
     14:58:17.798 /ets/pages/Index:SigSegv
     14:58:16.233 :enters foreground
     14:57:06.809 :leaves foreground
     14:56:37.014 :enters foreground
   Timestamp:2026-06-09 14:58:19.081
   Pid:28938
   Uid:20020200
   Process name:com.samples.cppcrashanalysis
   Process life time:104s
   Process Memory(kB): 195088(Rss)
   Device Memory(kB): Total 15833180, Free 2234976, Available 8511488
   Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000005a21d9a000 
   Fault thread info:
   Tid:28938, Name:ppcrashanalysis
   #00 pc 0000000002900000 [anon:native_heap:jemalloc]
   #01 pc 00000000000132ec /data/storage/el1/bundle/libs/arm64/libentry.so(RunWithJIT(napi_env__*, napi_callback_info__*)+96)(d10b3e3abc53f4af305eb776f0172e7876cc4aab)
   #02 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #03 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   #05 at callback entry (entry/src/main/ets/pages/sigsegv/segv_accerr.ets:32:21)
   #06 at anonymous entry (entry/src/main/ets/component/EntryList.ets:58:24)
   #07 pc 00000000001c0098 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+268)(bcdaa6dbb0e0ac023c972db186c60b63)
   #08 pc 00000000002b3b2c /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+412)(bcdaa6dbb0e0ac023c972db186c60b63)
   #09 pc 0000000000985668 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*) const+276)(d0768bdee195ff44343b1c7006b2f0dc)
   #10 pc 00000000009ac394 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunctionBase::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*)+416)(d0768bdee195ff44343b1c7006b2f0dc)
   Registers:
   x0:0000000000000003 x1:0000000000000004 x2:0000005a107a0340 x3:00000000000001cd
   x4:000000178ffc1b50 x5:0000007e7cdb9640 x6:000000000000000d x7:00000000000001bc
   x8:0000005a21d9a000 x9:0000005a21d9a000 x10:0000005a21d9a000 x11:0000000000000020
   x12:0000000000001b00 x13:00000000000001e3 x14:000000000000000a x15:0000000000000000
   x16:0000005a300e5b10 x17:0000005a00e8c400 x18:0000000000000001 x19:0000005a1fbf0000
   x20:0000005a1fb9f900 x21:0000005a300d328c x22:0000007e7cdb9630 x23:0000000000000000
   x24:0000000000000136 x25:0000005a107e5e78 x26:0000007e7cdb9420 x27:0000005a0100ee00
   x28:0000000000000000 x29:0000007e7cdb9370
   lr:0000005a300d32f0 sp:0000007e7cdb9320 pc:0000005a21d9a000
   pstate:0000000060001800 esr:000000008200000f
   ```

   说明1：如上故障日志Reason字段，可以看到崩溃类型为SIGSEGV(SEGV\_ACCERR)@0x0000005a21d9a000。后面便为访问出错的地址。
2. 分析崩溃栈.

   证据2：

   ```screen
   Fault thread info:
   Tid:28938, Name:ppcrashanalysis
   #00 pc 0000000002900000 [anon:native_heap:jemalloc]    --> pc执行跑到了堆上
   #01 pc 00000000000132ec /data/storage/el1/bundle/libs/arm64/libentry.so(RunWithJIT(napi_env__*, napi_callback_info__*)+96)(d10b3e3abc53f4af305eb776f0172e7876cc4aab)   --> 业务栈帧，访问出错位置
   #02 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #03 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   ...
   ```

   说明2：通常认为标准库、系统so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号，通常用法为llvm-addr2line -Cfie libentry.so 0x0000005a21d9a000，即可定位到行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到内存访问出错的调用栈，对应#01层调用栈。

   ```cpp
   using JitFunc = int (*)(int, int);

   napi_value RunWithJIT(napi_env env, napi_callback_info info)
   {
       unsigned char code[] = {
           0x00, 0x00, 0x01, 0x0b,
           0xc0, 0x03, 0x5f, 0xd6
       };
       const uint32_t mapLen = 4096;
       void *mem = malloc(mapLen);
       if (memcpy_s(mem, mapLen, code, sizeof(code)) != EOK) {
           return nullptr;
       }
       
       JitFunc add = (JitFunc)mem;
       int res = add(3, 4);   // -> Error occurred at location /no_think
       free(mem);
       
       napi_value result;
       napi_get_null(env, &result);
       return result;
   }
   ```

   说明3：此处可以直接定位到具体访问的函数，排查该函数的地址是否合法。
4. 排查访问的函数地址是否可以执行，是否为合法可访问的函数。

**问题结论与总结**

本案例为程序意图实现极简的JIT编译，但错误的使用了malloc()分配代码缓冲区。在ARM64平台上，堆内存具有可读写权限但是没有执行权限，直接跳转执行会触发访问权限错误。

**修复建议**

使用mmap分配内存并显式指定执行权限，同时建议在写完代码后调用mprotect(mem, 4096, PROT\_READ | PROT\_EXEC)移除写权限，以遵循“写或执行不可同时”安全原则。

```screen
void* mem = mmap(NULL, 4096, PROT_READ| PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
```

不过当前HarmonyOS应用开发不支持通过mmap设置可执行权限，不建议采用上述代码实现方式。

**案例四：mprotect保护页访问触发崩溃**

**问题现象**

触发业务代码访问被mprotect保护的内存页，应用触发退出，并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：

   ```screen
   Device info:HUAWEI Mate 70 Pro
   Build info:PLR 6.1.0.125(SP29log)cust preload version format error
   DeviceDebuggable:Yes
   Fingerprint:3c0431508e8a7fb278ec34337ff95cc7eba953879c0a9573cf2b117e063a7890
   Module name:com.samples.cppcrashanalysis
   ReleaseType:debug
   CpuAbi:arm64-v8a
   Version:1.0.0
   VersionCode:1000000
   IsSystemApp:No
   PreInstalled:No
   Foreground:Yes
   Page switch history:
     15:03:29.663 /ets/pages/Index:SegvAccerr
     15:03:28.545 /ets/pages/Index:SigSegv
     15:03:21.204 :enters foreground
   Timestamp:2026-06-09 15:03:30.225
   Pid:35302
   Uid:20020200
   Process name:com.samples.cppcrashanalysis
   Process life time:11s
   Process Memory(kB): 201474(Rss)
   Device Memory(kB): Total 15833180, Free 2205876, Available 8495104
   Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000005a027f8000 
   Fault thread info:
   Tid:35302, Name:ppcrashanalysis
   #00 pc 00000000000134bc /data/storage/el1/bundle/libs/arm64/libentry.so(AccessProtectedPage(napi_env__*, napi_callback_info__*)+96)(9428eb29b7186a058870d949e1dc991ef96f4d75)
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   #04 at callback entry (entry/src/main/ets/pages/sigsegv/segv_accerr.ets:38:21)
   #05 at anonymous entry (entry/src/main/ets/component/EntryList.ets:58:24)
   #06 pc 00000000001c0098 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+268)(bcdaa6dbb0e0ac023c972db186c60b63)
   #07 pc 00000000002b3b2c /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+412)(bcdaa6dbb0e0ac023c972db186c60b63)
   #08 pc 0000000000985668 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*) const+276)(d0768bdee195ff44343b1c7006b2f0dc)
   #09 pc 00000000009ac394 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunctionBase::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*)+416)(d0768bdee195ff44343b1c7006b2f0dc)
   #10 pc 000000000112eb6c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsClickFunction::Execute(OHOS::Ace::GestureEvent&)+3392)(d0768bdee195ff44343b1c7006b2f0dc)
   Registers:
   x0:0000000000000000 x1:0000000000001000 x2:0000000000000000 x3:0000000000000000
   x4:ffffffffffffffff x5:0000000000000000 x6:000000000000000d x7:00000000000001bc
   x8:0000000000000001 x9:0000005a027f8000 x10:0000005a012fa000 x11:fffffffffffff000
   x12:0000000000001b00 x13:00000000000001e3 x14:000000000000000a x15:00000000ffffffff
   x16:0000005a34425d30 x17:0000005a00fa1f50 x18:0000000000000001 x19:0000005a1fbf0000
   x20:0000005a1fb9f900 x21:0000005a3441345c x22:0000007e7cdb9630 x23:0000000000000000
   x24:0000000000000136 x25:0000005a107e5e78 x26:0000007e7cdb9420 x27:0000005a0100ee00
   x28:0000000000000000 x29:0000007e7cdb9370
   lr:0000005a344134b4 sp:0000007e7cdb9330 pc:0000005a344134bc
   pstate:0000000000001000 esr:0000000092000047
   ```

   说明1：如上故障日志Reason字段，可以看到崩溃类型为Signal:SIGSEGV(SEGV\_ACCERR)@0x0000005a027f8000 。后面便为访问出错的地址。
2. 分析崩溃栈。

   证据2：

   ```screen
   Fault thread info:
   Tid:35302, Name:ppcrashanalysis
   #00 pc 00000000000134bc /data/storage/el1/bundle/libs/arm64/libentry.so(AccessProtectedPage(napi_env__*, napi_callback_info__*)+96)(9428eb29b7186a058870d949e1dc991ef96f4d75)  --> 业务栈帧，访问出错位置
   #01 pc 0000000000060430 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(b4e45f188949f6fb66e496b653c33e6c)
   #02 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 0000000000582bf0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+396)
   ...
   ```

   说明2：通常认为标准库、系统so较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 找到上下文。

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。通常用法为llvm-addr2line -Cfie libentry.so 0x0000005a027f8000，即可定位到行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到内存访问出错的调用栈，对应#00层调用栈。

   ```cpp
   napi_value AccessProtectedPage(napi_env env, napi_callback_info info)
   {
       const uint32_t mapLen = 4096;
       char *p = (char *)mmap(nullptr, mapLen, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
       mprotect(p, mapLen, PROT_NONE);
       *p = 1;
       
       napi_value result;
       napi_get_null(env, &result);
       return result;
   }
   ```

   说明3：此处可以直接定位到具体访问的函数，排查该函数的地址是否合法。
4. 排查访问的函数地址是否可以执行，是否为合法可访问的函数。

**问题结论与总结**

本案例为程序在通过mprotect保护指定内存段不可被读写后，显式读写该地址区间导致触发SEGV\_ACCERR崩溃。

**修复建议**

1、合理使用mprotect，调整业务调用顺序。

2、结合业务评估mprotect保护的权限flag。

```screen
napi_value AccessProtectedPageFixed(napi_env env, napi_callback_info info)
{
    const uint32_t mapLen = 4096;
    char *p = (char *)mmap(nullptr, mapLen, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    mprotect(p, mapLen, PROT_WRITE);
    *p = 1;
    
    napi_value result;
    napi_get_null(env, &result);
    return result;
}
```

### 常见易错代码预防建议

|  |  |
| --- | --- |
| **错误模式** | **预防措施** |
| 修改字符串字面量 | 1. 用const char \*明确指针只读意图；2. 需要可写字符串时用char[]或std::string；3. 启用编译器警告-Wwrite-strings。 |
| mmap权限不足 | 1. 封装mmap调用，权限参数与实际操作严格匹配；2. 对映射进行写操作前，检查并确保PROT\_WRITE已设置 |
| 执行不可执行内存 | 1. 绝不将数据指针强转为函数指针并调用；2. 必须动态生成代码时，使用mmap和PROT\_EXEC并遵守“写时无执行，执行时无写”原则；3. 开启-fno-allow-store-data-races等安全编译选项。 |
| 写时复制/只读映射写 | 1. 在mmap文件时，若打算修改内容，必须映射为MAP\_PRIVATE | PROT\_WRITE；2. 使用MAP\_SHARED时确保文件可写。 |
| 内存被mprotect保护 | 1. 使用自定义内存分配器时，文档明确页面状态；2. 不要随意将页面权限设为PROT\_NONE后仍持有指针；3. 使用静态分析或运行时检查。 |
| 通用编码建议 | 1. 开启-Wall -Wextra -Werror；2. 使用 HWASan定期检测；3. 代码检视重点关注指针强转和内存权限；4. 模块涉及裸内存操作时，用断言 (assert) 检查边界和权限（如检测地址是否在可写段内）；5. 对于复杂内存布局，使用mprotect设置“守护页”捕获越界（然后正确处理信号）。 |
