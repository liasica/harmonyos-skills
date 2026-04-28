---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-catagory
title: 地址越界经典问题类型
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 地址越界类问题检测 > 地址越界经典问题类型
category: best-practices
scraped_at: 2026-04-28T08:22:49+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c9a6c89bf5fadd185ceb8ecb9ab88b2ea9a9146d77ab090f2d59f833ede42414
---

## heap-use-after-free

**定义**

heap-use-after-free：当堆内存被释放后，仍然使用该内存地址进行读写操作。这种行为可能导致未定义行为、数据损坏或远程代码执行等严重后果。其成因是开发者未能正确管理内存的生命周期，导致“野指针”留存，并在后续代码执行中继续被使用。

想要检测UseAfterFree的错误，需要有两点保证：

1. 已经free掉的内存区域需要被标记成特殊的状态。
2. 已经free掉的内存区域需要放入隔离区一段时间，防止发生错误时该区域已经通过malloc重新分配给其他人使用。一旦分配给其他人使用，则可能漏掉UseAfterFree的错误。

**影响**

导致程序存在安全漏洞，存在功能异常甚至崩溃的风险。

**代码示例**

以下为heap-use-after-free代码示例

```
1. int HeapUseAfterFree()
2. {
3. int *array = new int[100];
4. delete[] array;
5. return array[5];
6. }
```

[address\_problems.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/address_problems.cpp#L24-L29)

**ASan日志示例**

对这类日志，重点关注三个核心信息：分配位置、释放位置以及再次访问的位置。首先，要先找到程序再次访问已释放内存的现场，这部分一般在日志开头，通过READ of size ...或WRITE of size ...来标明本次非法访问的类型和字节大小，并附带触发时的调用栈信息。紧接着往下查看previously allocated by，可以定位这块内存最初是在何处分配的；再往下看freed by，则可以确认这块内存在何时被释放。

为了进一步确认内存状态是否与预期一致，ASan还提供了shadow memory的辅助信息。如日志所示，=>指向的那行有一个byte数值被中括号标记，例如：[fd]。它表示的是此次出错的内存地址对应的shadow memory的值。而其之前的fa表示heap left redzone，它是之前该区域有效时的遗留产物。连续的fd总共有50个，每一个shadow memory的byte和8个normal memory byte对应，所以可以知道此次free的内存总共是50×8=400bytes。

```
1. =================================================================
2. ==6254== ERROR: AddressSanitizer: heap-use-after-free on address 0x603e0001fc64 at pc 0x417f6a bp 0x7fff626b3250 sp 0x7fff626b3248
3. READ of size 4 at 0x603e0001fc64 thread T0
4. #0 0x417f69 in main example_UseAfterFree.cc:5
5. #1 0x7fae62b5076c (/lib/x86_64-linux-gnu/libc.so.6+0x2176c)
6. #2 0x417e54 (a.out+0x417e54)
7. 0x603e0001fc64 is located 4 bytes inside of 400-byte region [0x603e0001fc60,0x603e0001fdf0)
8. freed by thread T0 here:
9. #0 0x40d4d2 in operator delete[](void*) /home/kcc/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:61
10. #1 0x417f2e in main example_UseAfterFree.cc:4
11. previously allocated by thread T0 here:
12. #0 0x40d312 in operator new[](unsigned long) /home/kcc/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:46
13. #1 0x417f1e in main example_UseAfterFree.cc:3
14. Shadow bytes around the buggy address:
15. 0x1c07c0003f30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
16. 0x1c07c0003f40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
17. 0x1c07c0003f50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
18. 0x1c07c0003f60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
19. 0x1c07c0003f70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
20. =>0x1c07c0003f80: fa fa fa fa fa fa fa fa fa fa fa fa[fd]fd fd fd
21. 0x1c07c0003f90: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
22. 0x1c07c0003fa0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
23. 0x1c07c0003fb0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fa fa
24. 0x1c07c0003fc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
25. 0x1c07c0003fd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
```

## stack-use-after-return

**定义**

stack-use-after-return：在并发场景下，A线程栈内存被释放后，栈上内存仍传递到B线程继续对该内存地址进行读写操作。这种行为可能导致B线程使用时异常，触发CPP\_CRASH。

**影响**

导致程序存在安全漏洞，存在功能异常甚至崩溃的风险。

**代码示例**

以下为stack-use-after-return代码示例

```
1. int *ptr;

3. __attribute__((noinline))
4. void FunctionThatEscapesLocalObject()
5. {
6. int local[100];
7. ptr = &local[0];
8. printf("address: %p", local);
9. }

11. int StackUseAfterReturn(int argc)
12. {
13. FunctionThatEscapesLocalObject();
14. return ptr[argc];
15. }
```

[address\_problems.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/address_problems.cpp#L37-L51)

**ASan日志示例**

如下，可以看到最终出错的shadow memory值为f5，表示这是一个函数返回后仍被访问的内存区域

```
1. =================================================================
2. ==52583==ERROR: AddressSanitizer: stack-use-after-return on address 0x007a50590c2c at pc 0x007bfe89a5d8 bp 0x007fe7bfd590 sp 0x007fe7bfd588
3. READ of size 4 at 0x007a50590c2c thread T0 (e.myapplication)
4. #0 0x7bfe89a5d4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x5a5d4) (BuildId: 7bd557d1f1104b6d2201c007074c00b2d049f2fa)
5. #1 0x7adafcc4a4  (/system/lib64/platformsdk/libace_napi.z.so+0x4c4a4) (BuildId: 885449edb5de58e60c275a3b46d06982)
6. #2 0x7af82232c8  (/system/lib64/module/arkcompiler/stub.an+0x5c82c8)
7. #3 0x7af7c6bae0  (/system/lib64/module/arkcompiler/stub.an+0x10ae0)

9. Address 0x007a50590c2c is located in stack of thread T0 (e.myapplication) at offset 44 in frame
10. #0 0x7bfe896f10  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x56f10) (BuildId: 7bd557d1f1104b6d2201c007074c00b2d049f2fa)

12. This frame has 1 object(s):
13. [32, 432) 'local' (line 345) <== Memory access at offset 44 is inside this variable
14. HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
15. (longjmp and C++ exceptions *are* supported)
16. SUMMARY: AddressSanitizer: stack-use-after-return (/data/storage/el1/bundle/libs/arm64/libentry.so+0x5a5d4) (BuildId: 7bd557d1f1104b6d2201c007074c00b2d049f2fa)
17. Shadow bytes around the buggy address:
18. 0x001f4a0b2130: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
19. 0x001f4a0b2140: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
20. 0x001f4a0b2150: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
21. 0x001f4a0b2160: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
22. 0x001f4a0b2170: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
23. =>0x001f4a0b2180: f5 f5 f5 f5 f5[f5]f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
24. 0x001f4a0b2190: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
25. 0x001f4a0b21a0: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
26. 0x001f4a0b21b0: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
27. 0x001f4a0b21c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
28. 0x001f4a0b21d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

## overflow

**定义**

overflow：数据超出其分配的内存空间或数据类型所能表示的范围时，产生的一种错误或异常情况。溢出问题在多个领域中都有体现，包括但不限于整数溢出、堆栈溢出等。

* 整数溢出：当一个整数变量的值超过了它所能表示的范围时，会发生整数溢出。例如，当一个有符号的8位整数变量的值超过了-128到127的范围时，会发生溢出。
* 堆栈溢出：当程序在调用函数时，递归过深或输入数据过长，导致栈空间不足，从而引发堆栈溢出。

想要检测HeapBufferOverflow的问题，只需要保证一点：

* 正常的Heap前后需要插入一定长度的安全区，而且此安全区对应的shadow memory需要被标记为特殊的状态。在ASAN的实现里，安全区被标记为0xfa。

**影响**

溢出问题的影响主要体现在以下几个方面：

1. **数据错误：**当变量无法容纳超出其范围的数值时，存储在变量中的内容将被截断或改变，导致数据的错误计算。
2. **程序崩溃：**当程序试图分配超出可用内存范围的空间时，操作系统可能会强制关闭程序，导致程序崩溃或异常终止。
3. **性能问题：**在处理大量数据时，溢出问题可能导致程序运行缓慢或资源占用过高。

**代码示例**

以下为heap-buffer-overflow代码示例

```
1. int HeapBufferOverflow()
2. {
3. char* buffer;
4. buffer = (char *)malloc(100);
5. *(buffer + 101) = 'n';
6. *(buffer + 102) = 'n';
7. free(buffer);
8. printf("address: %p", buffer);
9. return buffer[1];
10. }
```

[address\_problems.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/address_problems.cpp#L59-L68)

**ASan日志示例**

如下，可以看到最终出错的shadow memory值为0x4，表示该shadow memory对应的normal memory中只有前4个bytes是可寻址的。0x4的shadow memory前还有12个0x0，表示其前面的12个memory region（每个region有8个byte）都是完全可寻址的。因此所有可寻址的大小=12×8+4=100，正是代码中malloc的size。之所以此次访问会出错，是因为地址0x00609ee303e5意图访问最后一个region的第五个byte，而该region只有前四个byte可寻址。由于0x4后面是0xfa，因此此次错误属于HeapBufferOverflow。

```
1. =================================================================
2. ==appspawn==7656==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x00609ee303e5 at pc 0x007bb8897c18 bp 0x007e02723fa0 sp 0x007e02723f98
3. WRITE of size 1 at 0x00609ee303e5 thread T0 (e.myapplication)
4. #0 0x7bb8897c14  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x57c14) (BuildId: 9e7ce7cc7ace9cc03f6720335ea2147c140eff23)
5. #1 0x7b2966afcc  (/system/lib64/platformsdk/libace_napi.z.so+0x6afcc) (BuildId: 24e2a6bc2f2ee3af0a8e42bd42959091)
6. #2 0x7badbd710c  (/system/lib64/module/arkcompiler/stub.an+0xdd710c)
7. #3 0x7bace19d20  (/system/lib64/module/arkcompiler/stub.an+0x19d20)

9. 0x00609ee303e5 is located 1 bytes to the right of 100-byte region [0x00609ee30380,0x00609ee303e4)
10. allocated by thread T0 (e.myapplication) here:
11. #0 0x5a9d912678  (/system/lib64/libclang_rt.asan.so+0xd2678) (BuildId: 41a3c185ba5b0e795c1b5cc5f6d5680c5c523d3c)
12. #1 0x7bb8897bb8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x57bb8) (BuildId: 9e7ce7cc7ace9cc03f6720335ea2147c140eff23)
13. #2 0x7b2966afcc  (/system/lib64/platformsdk/libace_napi.z.so+0x6afcc) (BuildId: 24e2a6bc2f2ee3af0a8e42bd42959091)
14. #3 0x7badbd710c  (/system/lib64/module/arkcompiler/stub.an+0xdd710c)
15. #4 0x7bace19d20  (/system/lib64/module/arkcompiler/stub.an+0x19d20)

17. SUMMARY: AddressSanitizer: heap-buffer-overflow (/data/storage/el1/bundle/libs/arm64/libentry.so+0x57c14) (BuildId: 9e7ce7cc7ace9cc03f6720335ea2147c140eff23)
18. Shadow bytes around the buggy address:
19. 0x001c13dc6020: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
20. 0x001c13dc6030: 00 00 00 00 00 00 00 00 fa fa fa fa fa fa fa fa
21. 0x001c13dc6040: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fa fa
22. 0x001c13dc6050: fa fa fa fa fa fa fa fa fd fd fd fd fd fd fd fd
23. 0x001c13dc6060: fd fd fd fd fd fd fa fa fa fa fa fa fa fa fa fa
24. =>0x001c13dc6070: 00 00 00 00 00 00 00 00 00 00 00 00[04]fa fa fa
25. 0x001c13dc6080: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
26. 0x001c13dc6090: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
27. 0x001c13dc60a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
28. 0x001c13dc60b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
29. 0x001c13dc60c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
```
