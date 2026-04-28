---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fdsan
title: fdsan使用指导
breadcrumb: 指南 > NDK开发 > 代码开发 > C/C++标准库 > fdsan使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:58+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:badf5ad681a6843b5dcdab16559837b07349933cc7af1b6b3aa30d2179f3398c
---

## 功能介绍

fdsan主要用于检测不同使用者对相同文件描述符的错误操作，如多次关闭（double-close）和关闭后使用（use-after-close）。这些文件描述符可以是操作系统中的文件、目录、网络套接字或其他I/O设备等。在程序中，打开文件或套接字会生成一个文件描述符。如果此文件描述符在使用后出现反复关闭或关闭后使用等情形，会导致内存泄露或文件句柄泄露等安全隐患。这类问题非常隐蔽，难以排查。为此，引入了fdsan这种检测工具。

## 实现原理

设计思路：当打开已有文件或创建一个新文件的时候，在得到返回fd后，设置一个关联的tag，来标记fd的属主信息；关闭文件前，检测fd关联的tag，判断是否符合预期(属主信息一致)，符合就继续走正常文件关闭流程；如果不符合就是检测到异常，根据设置，调用对应的异常处理。

tag由两部分组成，最高位的8-bit构成type，后面的56-bit构成value。

type标识fd通过何种封装形式进行管理，例如FDSAN\_OWNER\_TYPE\_FILE表示fd通过普通文件进行管理。类型在fdsan\_owner\_type中定义。

value用于标识实际的owner tag。

tag构成图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/n4CVtsIBSMecTI8U-NyKlA/zh-cn_image_0000002583439413.png?HW-CC-KV=V1&HW-CC-Date=20260427T235357Z&HW-CC-Expire=86400&HW-CC-Sign=7AFEB360701FF683D5C3A4F2AB1C97006C25F10EEF48C2CDFC7FD49D1137226C)

## 接口说明

### fdsan\_set\_error\_level

```
1. enum fdsan_error_level fdsan_set_error_level(enum fdsan_error_level new_level);
```

**描述：** 可以通过fdsan\_set\_error\_level设定error\_level，error\_level用于控制检测到异常后的处理行为。默认error\_level为FDSAN\_ERROR\_LEVEL\_WARN\_ALWAYS。

**参数：** fdsan\_error\_level

| 名称 | 说明 |
| --- | --- |
| FDSAN\_ERROR\_LEVEL\_DISABLED | disabled，此level代表什么都不处理。 |
| FDSAN\_ERROR\_LEVEL\_WARN\_ONCE | warn-once，第一次出现错误时在hilog中发出警告，然后将级别降低为disabled(FDSAN\_ERROR\_LEVEL\_DISABLED)。 |
| FDSAN\_ERROR\_LEVEL\_WARN\_ALWAYS | warn-always，每次出现错误时都在hilog中发出警告。 |
| FDSAN\_ERROR\_LEVEL\_FATAL | fatal，出现错误时调用abort异常退出。 |

**返回值：** 返回旧的error\_level。

### fdsan\_get\_error\_level

```
1. enum fdsan_error_level fdsan_get_error_level();
```

**描述：** 可以通过fdsan\_get\_error\_level获取error level。

**返回值：** 当前的error\_level。

### fdsan\_create\_owner\_tag

```
1. uint64_t fdsan_create_owner_tag(enum fdsan_owner_type type, uint64_t tag);
```

**描述：** 通过传入的type和tag字段，拼接成一个有效的文件描述符的关闭tag。

**参数：** fdsan\_owner\_type

| 名称 | 说明 |
| --- | --- |
| FDSAN\_OWNER\_TYPE\_GENERIC\_00 | 默认未使用fd对应的type值。 |
| FDSAN\_OWNER\_TYPE\_GENERIC\_FF | 默认非法fd对应的type值。 |
| FDSAN\_OWNER\_TYPE\_FILE | 默认普通文件对应的type值，使用fopen或fdopen打开的文件具有该类型。 |
| FDSAN\_OWNER\_TYPE\_DIRECTORY | 默认文件夹对应的type值，使用opendir或fdopendir打开的文件具有该类型。 |
| FDSAN\_OWNER\_TYPE\_UNIQUE\_FD | 默认unique\_fd对应的type值，保留暂未使用。 |
| FDSAN\_OWNER\_TYPE\_ZIPARCHIVE | 默认zip压缩文件对应的type值，保留暂未使用。 |

**返回值：** 返回创建的tag，可以用于fdsan\_exchange\_owner\_tag函数的输入。

### fdsan\_exchange\_owner\_tag

```
1. void fdsan_exchange_owner_tag(int fd, uint64_t expected_tag, uint64_t new_tag);
```

**描述：** 修改文件描述符的关闭tag。

通过fd找到对应的FdEntry，判断close\_tag值与expected\_tag是否一致。如果一致，说明符合预期，可以使用new\_tag值重新设定对应的FdEntry。

如果不符合，说明检测到异常，后续进行对应的异常处理。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| fd | int | fd句柄，作为FdEntry的索引。 |
| expected\_tag | uint64\_t | 期望的ownership tag值。 |
| new\_tag | uint64\_t | 设置新的ownership tag值。 |

### fdsan\_close\_with\_tag

```
1. int fdsan_close_with_tag(int fd, uint64_t tag);
```

**描述：** 根据tag描述符关闭文件描述符。

通过fd找到匹配的FdEntry。如果close\_tag与tag相同，则符合预期，可以继续执行文件描述符关闭流程；否则，表示检测到异常。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| fd | int | 待关闭的fd句柄。 |
| tag | uint64\_t | 期望的ownership tag。 |

**返回值：** 0或者-1，0表示close成功，-1表示close失败。

### fdsan\_get\_owner\_tag

```
1. uint64_t fdsan_get_owner_tag(int fd);
```

**描述：** 根据文件描述符获取tag信息。

通过fd找到匹配的FdEntry，并获取其close\_tag。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| fd | int | 文件描述符。 |

**返回值：** 返回对应fd的tag。

### fdsan\_get\_tag\_type

```
1. const char* fdsan_get_tag_type(uint64_t tag);
```

**描述：** 根据tag计算出对应的type类型。

获取tag信息后，计算并获取对应tag的type信息。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| tag | uint64\_t | ownership tag。 |

**返回值：** 返回对应tag的type。

### fdsan\_get\_tag\_value

```
1. uint64_t fdsan_get_tag_value(uint64_t tag);
```

**描述：** 根据tag计算出对应的owner value。

通过获取到的tag信息，通过偏移计算获取对应tag中的value信息。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| tag | uint64\_t | ownership tag。 |

**返回值：** 返回对应tag的value。

## 使用示例

如何使用fdsan？这是一个简单的double-close问题：

```
1. #include <unistd.h>
2. #include <fcntl.h>
3. #include <hilog/log.h>
4. #include <vector>
5. #include <thread>

7. void good_write()
8. {
9. sleep(1);
10. int fd = open("log", O_WRONLY | O_APPEND);
11. sleep(3);
12. ssize_t ret = write(fd, "fdsan test", 11);
13. if (ret == -1) {
14. OH_LOG_ERROR(LOG_APP, "good write but failed?!");
15. }
16. close(fd);
17. }

19. void bad_close()
20. {
21. int fd = open("/dev/null", O_RDONLY);
22. close(fd);
23. sleep(2);
24. // This close expected to be detect by fdsan
25. close(fd);
26. }

28. void functional_test()
29. {
30. std::vector<std::thread> threads;
31. for (auto function : { good_write, bad_close }) {
32. threads.emplace_back(function);
33. }
34. for (auto& thread : threads) {
35. thread.join();
36. }
37. }

39. int main()
40. {
41. functional_test();
42. return 0;
43. }
```

上述代码中的good\_write函数会打开一个文件并写入一些字符串，而bad\_close函数中也会打开一个文件同时包含double-close问题，这两个线程同时运行执行情况如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/zDBeJKfdT4y9Z9LrS8kxDg/zh-cn_image_0000002552959368.png?HW-CC-KV=V1&HW-CC-Date=20260427T235357Z&HW-CC-Expire=86400&HW-CC-Sign=67BD6EEFB84B38E3623AC51C5A29A529A419872081728B64F80E4D79F64AFC91)

由于每次open返回的文件描述符（fd）是顺序分配的，进入主函数后第一个可用的fd是43。在bad\_close 函数中，第一次open返回的fd也是43。关闭之后，43变成可用的fd。在good\_write函数中，open返回了第一个可用的fd，即43。然而，由于bad\_close函数中存在重复关闭问题，错误地关闭了另一个线程中打开的文件，导致写入失败。

引入fdsan后，有两种检测方法：使用标准库接口或实现带有fdsan的函数接口。

### 使用标准库接口

标准库接口中，fopen、fdopen、opendir、fdopendir已集成fdsan。使用这些接口而非直接使用open有助于检测问题。例如，可以使用fopen替代open。

```
1. #include <stdio.h>
2. #include <errno.h>
3. #define TEMP_FILE "/data/local/tmp/test.txt"

5. void good_write()
6. {
7. // fopen is protected by fdsan, replace open with fopen
8. // int fd = open(TEMP_FILE, O_RDWR);
9. FILE *f = fopen(TEMP_FILE, "w+");
10. if (f == NULL) {
11. printf("fopen failed errno=%d\n", errno);
12. return;
13. }
14. // ssize_t ret = write(fd, "fdsan test\n", 11);
15. int ret = fprintf(f, "fdsan test %d\n", 11);
16. if (ret < 0) {
17. printf("fprintf failed errno=%d\n", errno);
18. }
19. // close(fd);
20. fclose(f);
21. }
```

### 日志信息

使用fopen打开的每个文件描述符都需要有一个与之对应的 tag 。fdsan 在 close 时会检查关闭的 fd 是否与 tag 匹配，不匹配就会默认提示相关日志信息。下面是上述代码的日志信息：

```
1. # hilog | grep MUSL-FDSAN
2. 04-30 15:03:41.760 10933  1624 E C03f00/MUSL-FDSAN: attempted to close file descriptor 43,                             expected to be unowned, actually owned by FILE* 0x00000000f7b90aa2
```

从这里的错误信息中可以看出，FILE接口的文件被其他人错误地关闭了。FILE接口的地址可以协助进一步定位。

此外，可以在代码中使用fdsan\_set\_error\_level设置错误等级error\_level。设置为Fatal之后，如果fdsan检测到错误，会提示日志信息并crash生成堆栈信息，用于定位。下面是 error\_level 设置为Fatal之后生成的crash堆栈信息：

```
1. Reason:Signal:SIGABRT(SI_TKILL)@0x0000076e from:1902:20010043
2. Fault thread info:
3. Tid:15312, Name:e.myapplication
4. #00 pc 000e65bc /system/lib/ld-musl-arm.so.1(raise+176)(3de40c79448a2bbced06997e583ef614)
5. #01 pc 0009c3bc /system/lib/ld-musl-arm.so.1(abort+16)(3de40c79448a2bbced06997e583ef614)
6. #02 pc 0009de4c /system/lib/ld-musl-arm.so.1(fdsan_error+116)(3de40c79448a2bbced06997e583ef614)
7. #03 pc 0009e2e8 /system/lib/ld-musl-arm.so.1(fdsan_close_with_tag+836)(3de40c79448a2bbced06997e583ef614)
8. #04 pc 0009e56c /system/lib/ld-musl-arm.so.1(close+20)(3de40c79448a2bbced06997e583ef614)
9. #05 pc 000055d8 /data/storage/el1/bundle/libs/arm/libentry.so(bad_close()+96)(f3339aac824c099f449153e92718e1b56f80b2ba)
10. #06 pc 00006cf4 /data/storage/el1/bundle/libs/arm/libentry.so(decltype(std::declval<void (*)()>()()) std::__n1::__invoke[abi:v15004]<void (*)()>(void (*&&)())+24)(f3339aac824c099f449153e92718e1b56f80b2ba)
11. #07 pc 00006c94 /data/storage/el1/bundle/libs/arm/libentry.so(f3339aac824c099f449153e92718e1b56f80b2ba)
12. #08 pc 000067b8 /data/storage/el1/bundle/libs/arm/libentry.so(void* std::__n1::__thread_proxy[abi:v15004]<std::__n1::tuple<std::__n1::unique_ptr<std::__n1::__thread_struct, std::__n1::default_delete<std::__n1::__thread_struct>>, void (*)()>>(void*)+100)(f3339aac824c099f449153e92718e1b56f80b2ba)
13. #09 pc 00105a6c /system/lib/ld-musl-arm.so.1(start+248)(3de40c79448a2bbced06997e583ef614)
14. #10 pc 000700b0 /system/lib/ld-musl-arm.so.1(3de40c79448a2bbced06997e583ef614)
```

此时，从crash信息中可以看到bad\_close存在问题，同时crash中包含所有打开的文件，协助定位问题，提升效率。

OpenFiles列出所有打开的文件

**字段说明：**

fd->对象描述：文件描述符fd关联的内核对象标识。

[方括号内容]：对象内部标识：

* 对于socket/pipe：内核分配的伪文件系统ID；
* 对于普通文件：文件系统inode编号（操作系统用于管理该文件元数据及数据块的数据结构）；
* 对于anon\_inode：对象类型名称。

native object of unknown type 0：该fd对应的tag标签值为0。

```
1. OpenFiles:
2. 0->/dev/null native object of unknown type 0
3. 1->/dev/null native object of unknown type 0
4. 2->/dev/null native object of unknown type 0
5. 3->socket:[28102] native object of unknown type 0
6. 4->socket:[28103] native object of unknown type 0
7. 5->anon_inode:[eventpoll] native object of unknown type 0
8. 6->/sys/kernel/debug/tracing/trace_marker native object of unknown type 0
9. 7->anon_inode:[eventpoll] native object of unknown type 0
10. 8->anon_inode:[eventpoll] native object of unknown type 0
11. 9->/dev/console native object of unknown type 0
12. 10->pipe:[95598] native object of unknown type 0
13. 11->pipe:[95598] native object of unknown type 0
14. 12->socket:[18542] native object of unknown type 0
15. 13->pipe:[96594] native object of unknown type 0
16. 14->socket:[18545] native object of unknown type 0
17. 15->pipe:[96594] native object of unknown type 0
18. 16->anon_inode:[eventfd] native object of unknown type 0
19. 17->/dev/binder native object of unknown type 0
20. 18->/data/storage/el1/bundle/entry.hap native object of unknown type 0
21. 19->anon_inode:[eventpoll] native object of unknown type 0
22. 20->anon_inode:[signalfd] native object of unknown type 0
23. 21->socket:[29603] native object of unknown type 0
24. 22->anon_inode:[eventfd] native object of unknown type 0
25. 23->anon_inode:[eventpoll] native object of unknown type 0
26. 24->anon_inode:[eventfd] native object of unknown type 0
27. 25->anon_inode:[eventpoll] native object of unknown type 0
28. 26->anon_inode:[eventfd] native object of unknown type 0
29. 27->anon_inode:[eventpoll] native object of unknown type 0
30. 28->anon_inode:[eventfd] native object of unknown type 0
31. 29->anon_inode:[eventpoll] native object of unknown type 0
32. 30->anon_inode:[eventfd] native object of unknown type 0
33. 31->anon_inode:[eventpoll] native object of unknown type 0
34. 32->anon_inode:[eventfd] native object of unknown type 0
35. 33->anon_inode:[eventpoll] native object of unknown type 0
36. 34->anon_inode:[eventfd] native object of unknown type 0
37. 35->socket:[97409] native object of unknown type 0
38. 36->socket:[94716] native object of unknown type 0
39. 38->socket:[94720] native object of unknown type 0
40. 40->/data/storage/el1/bundle/entry_test.hap native object of unknown type 0
41. 41->socket:[95617] native object of unknown type 0
42. 42->/sys/kernel/debug/tracing/trace_marker native object of unknown type 0
43. 43->/dev/null FILE* 4155724704
44. 44->socket:[94737] native object of unknown type 0
45. 45->pipe:[95634] native object of unknown type 0
46. 46->pipe:[95634] native object of unknown type 0
47. 47->pipe:[95635] native object of unknown type 0
48. 49->pipe:[95636] native object of unknown type 0
49. 50->pipe:[95636] native object of unknown type 0
```

### 实现具有fdsan的函数接口

除了使用标准库函数，还可以实现具有fdsan的函数接口。fdsan机制通过fdsan\_exchange\_owner\_tag和fdsan\_close\_with\_tag实现。fdsan\_exchange\_owner\_tag设置fd的tag，fdsan\_close\_with\_tag检查关闭文件时的tag。

下面是一个实现具有fdsan功能的函数接口的示例：

```
1. #include <errno.h>
2. #include <stdio.h>
3. #include <fcntl.h>
4. #include <unistd.h>

6. #include <utility>

8. struct fdsan_fd {
9. fdsan_fd() = default;

11. explicit fdsan_fd(int fd)
12. {
13. reset(fd);
14. }

16. fdsan_fd(const fdsan_fd& copy) = delete;
17. fdsan_fd(fdsan_fd&& move)
18. {
19. *this = std::move(move);
20. }

22. ~fdsan_fd()
23. {
24. reset();
25. }

27. fdsan_fd& operator=(const fdsan_fd& copy) = delete;
28. fdsan_fd& operator=(fdsan_fd&& move)
29. {
30. if (this == &move) {
31. return *this;
32. }
33. reset();
34. if (move.fd_ != -1) {
35. fd_ = move.fd_;
36. move.fd_ = -1;
37. // Acquire ownership from the moved-from object.
38. exchange_tag(fd_, move.tag(), tag());
39. }
40. return *this;
41. }

43. int get()
44. {
45. return fd_;
46. }

48. void reset(int new_fd = -1)
49. {
50. if (fd_ != -1) {
51. close(fd_, tag());
52. fd_ = -1;
53. }
54. if (new_fd != -1) {
55. fd_ = new_fd;
56. // Acquire ownership of the presumably unowned fd.
57. exchange_tag(fd_, 0, tag());
58. }
59. }

61. private:
62. int fd_ = -1;

64. // Use the address of object as the file tag
65. uint64_t tag()
66. {
67. return reinterpret_cast<uint64_t>(this);
68. }

70. static void exchange_tag(int fd, uint64_t old_tag, uint64_t new_tag)
71. {
72. if (&fdsan_exchange_owner_tag) {
73. fdsan_exchange_owner_tag(fd, old_tag, new_tag);
74. }
75. }

77. static int close(int fd, uint64_t tag)
78. {
79. if (&fdsan_close_with_tag) {
80. return fdsan_close_with_tag(fd, tag);
81. }
82. }
83. };
```

这里的实现中使用fdsan\_exchange\_owner\_tag在开始时将fd与结构体对象地址绑定，然后在关闭文件时使用fdsan\_close\_with\_tag进行检测，预期tag是结构体对象地址。

在实现具有fdsan的函数接口后，可以使用该接口包装fd。

```
1. #define TEMP_FILE "/data/local/tmp/test.txt"

3. void good_write()
4. {
5. // int fd = open(DEV_NULL_FILE, O_RDWR);
6. fdsan_fd fd(open(TEMP_FILE, O_CREAT | O_RDWR));
7. if (fd.get() == -1) {
8. printf("fopen failed errno=%d\n", errno);
9. return;
10. }
11. ssize_t ret = write(fd.get(), "fdsan test\n", 11);
12. if (ret == -1) {
13. printf("write failed errno=%d\n", errno);
14. }
15. fd.reset();
16. }
```

此时运行该程序可以检测到另一个线程的double-close问题，详细信息可以[参考日志](fdsan.md#日志信息)。同样也可以设置error\_level为fatal，这样可以使fdsan在检测到crash之后主动crash以获取更多信息。

## 多线程场景下的注意事项

在多线程环境中使用fdsan时，由于文件描述符（fd）的分配和回收是全局性的，fdsan检测到的tag不匹配错误信息可能存在与实际根因不一致的情况。开发者需要注意以下场景：

**fd快速回收导致报错指向错误属主：** 当线程A关闭一个fd后，该fd可能立即被线程B回收并绑定新的tag。此时如果线程A（或系统中其他模块）对该fd执行了非法close或double close，fdsan报错信息中显示的owner将是线程B的tag，而非原始属主的信息。这并不意味着线程B的tag设置有误，而是当前进程内其他业务逻辑存在非法close或double close的问题。

**检测与执行的竞态窗口：** fdsan\_close\_with\_tag内部在"校验tag"与"执行close"之间存在极小的时间窗口。在多线程并发场景下，fd可能在该窗口内被回收并重新分配给其他线程，导致校验结果指向的属主并非当前fd的实际使用者。

**排查建议：** 当看到fdsan报错时，不应直接认定日志中显示的owner就是问题的直接责任方。建议结合fd的生命周期、调用栈信息以及系统中其他模块对fd的使用情况进行综合排查，确认是否存在其他模块的非法close或double close行为。

## close函数信号安全性说明

在POSIX标准中，close函数原本被定义为信号安全函数（async-signal-safe），这意味着它可以安全地在信号处理函数（signal handler）中调用。然而，在集成了fdsan（File Descriptor Sanitizer）机制的系统实现中，这一性质发生了变化。

由于fdsan的实现依赖于mmap系统调用，而mmap本身不是信号安全函数，这会导致close函数也不再是信号安全的。因此，在信号处理函数中避免使用 close，可以通过其他系统调用来实现相同功能。
