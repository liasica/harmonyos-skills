---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-fdleak-fault-mode
title: 应用句柄泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 句柄泄漏故障模式说明 > 应用句柄泄漏故障模式说明
category: best-practices
scraped_at: 2026-11-14T08:54:20+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:c9bee2ad2b21c51d99837ed8ecdb36f9c72e81a301a1bc172714c941d5efcd2b
---

## 概述

应用运行期间，若存在文件句柄未正常释放、连接池参数配置不合理、IO资源关闭逻辑缺失等问题，容易导致进程句柄数量持续上涨。如果句柄总量突破系统单进程句柄上限（32768个），可能导致进程无法新建文件描述符，无法对外提供服务。本文旨在为开发者梳理句柄泄漏的各种常见根因，并结合实际故障案例，分别讲解运维态与开发态的问题分析思路。本文提供了以下五种类型的句柄泄漏问题分析说明和案例：

* [文件句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1460613474513)
* [socket句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1232317539454)
* [pipe句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section94463205454)
* [ASHMEM句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1338618214454)
* [dmabuf句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section15702142194514)

## 文件句柄泄漏

### 根因描述

文件句柄是用来访问硬盘数据的标识符。文件句柄泄漏根因包括：

* 创建文件句柄后未关闭：开发者通过open()、fopen()等接口创建文件句柄后，由于编码疏忽或业务逻辑复杂，后续流程未能调用close()、fclose()关闭句柄。
* 异常路径导致文件句柄泄漏：在异步回调、异常处理或提前返回的逻辑分支中，跳过了本该执行的close()。
* fork后的文件句柄泄漏：父进程在fork()之前已打开某些文件句柄，且没有设置O\_CLOEXEC标志，子进程即使不使用这些句柄，也被迫继承导致泄漏。
* ArkTS中的文件对象未释放资源：ArkTS的[fileIo.openSync()](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口调用之后，没有调用[fileIo.closeSync()](../harmonyos-references/js-apis-file-fs.md#fileioclosesync)关闭文件句柄。

### 问题分析思路

开发者可以参考[运维态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section71361119142017)和[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)对句柄泄漏问题进行分析。

### 案例：文件句柄泄漏

本案例模拟了因大量文件句柄未释放引发的泄漏故障。系统检测到应用发生了句柄泄漏后，在后台管控了此应用，再次打开时，应用冷启动。

**运维态问题案例分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，当应用发生句柄泄漏故障时，开发者可以在沙箱中获取到句柄泄漏相关的故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)分析以下基础维测日志，日志中显示泄漏最多的句柄为/data/storage/el2/log/fd\*ea\*\_f\*rt，可以确认泄漏的句柄类型为文件句柄。

   ```screen
   *****************************
   Summary:
   Leaked fd:/data/storage/el2/log/fd*ea*_f*rt

   Leaked fd Top 10:
   18002	/data/storage/el2/log/fd*ea*_f*rt
   9001	/data/storage/el2/log/fd*ea*_u*
   10	eventpoll
   8	eventfd
   8	pipe
   7	socket
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   ```
3. 如果获取到了句柄栈，可以按照[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)提供的步骤依次分析，通过单击下图1处导入句柄栈文件，再依次单击下图2-4处，可筛选出泄漏的调用栈如下图5、6处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SmGooHkaRe2Bb5dolUV0QQ/zh-cn_image_0000002699891782.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE74728AC7F269FD40544504A1D264AC3E22EC1652A075F230E6EDF22D17E269 "点击放大")
4. 分析调用栈指向的代码段，发现FileHandleLeakUvWork()函数正在循环申请文件句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/pxSzfJ3SS2OGIO86N5oiVA/zh-cn_image_0000002699731896.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC3E62FBE8A51A6C3B445BA4241B83AB3FCC7A15900379AAF3E382C820F3DAE "点击放大")

**开发态问题案例分析思路**

1. 按照[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)提供的步骤完成录制后，依次单击下图1、2处，可找到泄漏句柄的申请调用栈如下图3处框中所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/xqiuM-HORFKxOz52uvS63g/zh-cn_image_0000002729491151.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC4E423D49DAB6D291CD07998E27183387F62DE501470FAF87B83607C37A61C7)
2. 分析调用栈指向的代码段，发现FileHandleLeakUvWork()函数正在循环申请文件句柄，且未释放，最终导致了句柄泄漏。调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/qSlLOKzeSqK82OOZi-jNug/zh-cn_image_0000002729611111.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8B43A6BC85C140E7F104C1CB4DE7B2404E512C0F9D847A494C9B95023EA1F57 "点击放大")

**修复建议**

* 遵循RAII原则，利用对象的生命周期管理资源。
* 确保所有控制流路径都执行资源清理代码，优先使用语言特性保证资源释放。
* ArkTS开发过程中使用fileIo.openSync()获取句柄，使用完后必须调用fileIo.closeSync()释放句柄。

## socket句柄泄漏

### 根因描述

socket句柄一般为访问网卡、网络连接的标识符。socket句柄泄漏根因包括：

* 创建socket后没有关闭：开发者通过socket()等接口创建句柄后，由于编码疏忽或业务逻辑复杂，后续流程未能调用close()关闭句柄。
* select/poll/epoll中socket句柄泄漏：开发者将socket添加到多路复用器（如epoll）监听事件，但在socket关闭时忘记从epoll中移除。
* fork后的socket句柄泄漏：父进程在fork()之前已打开某些socket句柄，且没有设置O\_CLOEXEC标志，子进程即使不使用这些句柄，也被迫继承导致泄漏。

### 问题分析思路

**运维态问题分析思路**

开发者可以根据[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)对日志中的top10进行分析，如果类型为socket的句柄数量最多，那么可以将当前句柄泄漏问题定位为socket泄漏问题。

```screen
Leaked fd Top 10:
20008	socket
10	eventpoll
8	eventfd
8	pipe
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
3	/dev/null
3	/sys/kernel/debug/tracing/trace_marker
2	/dev/kmsg
```

除了使用运维态问题分析方法中展示的通用方法外，socket作为特殊类型句柄，会有进程详细的维测信息输出如下所示：

```screen
ProcessName ProcessID Fd inode PeerTid
xample.dfx_test 6611 3 7883 592
xample.dfx_test 6611 25 7883 592
xample.dfx_test 6611 29 17361 2136
xample.dfx_test 6611 31 7883 592
xample.dfx_test 6611 50 17417 927
xample.dfx_test 6611 51 17425 1657
xample.dfx_test 6611 54 17411 1657
```

开发者可以通过以下方法分析socket基础维测日志缩小排查范围：

1. 查看本应用所占用的socket句柄，日志经过pid过滤，每一行表示一个socket句柄。
2. 查看inode和对端进程，两方进程通信持有的inode相同，PeerTid一般就是对端进程的pid。如果出现大量相同PeerTid，可以通过命令行或者流水日志搜索获取该pid对应的进程，再结合业务逻辑，追踪到相应代码。
3. 关注应用代码中是否使用socket()等接口创建socket句柄，排查其生命周期是否存在泄漏。

参考[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)获取到句柄栈日志后，开发者可以参考[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)进行下一步定位。

**开发态问题分析思路**

如果应用发生了socket句柄泄漏，可以参考[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)，尝试按场景复现并使用DevEco Studio中Profiler工具的Allocation功能定位句柄泄漏问题。

### 案例：socket句柄泄漏

本案例模拟创建大量socket句柄未释放引发的句柄泄漏故障。系统检测到应用发生了句柄泄漏后，在后台管控了此应用，再次打开时，应用冷启动。

**运维态问题案例分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，当应用发生句柄泄漏故障时，开发者可以在沙箱中获取到句柄泄漏相关的故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)，根据以下基础维测日志确认泄漏的句柄类型为socket。

   ```screen
   Leaked fd Top 10:
   4990	socket
   10	eventpoll
   8	eventfd
   8	pipe
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   3	/sys/kernel/debug/tracing/trace_marker
   2	/dev/kmsg
   ```
3. 参考[问题分析思路](bpta-stability-app-fdleak-fault-mode.md#section15698629724)，分析详细日志中inode、PeerTid等数据，可进一步缩小排查范围。
4. 如果获取到了句柄栈，可以按照[运维态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section71361119142017)提供的步骤依次分析，通过单击下图1处导入句柄栈文件，再依次单击下图2-4处，可筛选出泄漏的调用栈如下图5、6处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/dN_UIhIER6uIsv4RQcQEYg/zh-cn_image_0000002699891784.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE968689E8A04F4494FED024EEB706A9ABC244E2E0067AF8733427437C3FC2D6)
5. 分析调用栈指向的代码段，发现SocketFDLeak()函数正在循环调用CreateSocketAndLeak()函数，后者会申请socket句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/L8we3dF9TOmnM4xWzLpyjA/zh-cn_image_0000002699731898.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F405C0B354A31C85B2F4163B3376E8D55E1521E02AC66C55ED995D1EC20FAFB "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/6un_V5VlRJuKlM-FCOSNiQ/zh-cn_image_0000002729491153.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC751A1E4D603DC3954511C0E2E4E7D44795F0FF57DB0123C194FE8A0A5CC273 "点击放大")

**开发态问题案例分析思路**

1. 按照[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)提供的步骤完成录制后，依次单击下图1、2处，在下图3处可找到泄漏句柄的申请调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/J6K86rQIQ4KBUlFPRqiRAQ/zh-cn_image_0000002729611113.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=75F4BC819064365917A1666E74E682D4094163360F01A6F2E4CBC86EC1DF8AAD)
2. 分析调用栈指向的代码段，发现SocketFDLeak()函数正在循环调用CreateSocketAndLeak()函数，后者会申请socket句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/JYWsVaC1Si6U18fMMwnjXg/zh-cn_image_0000002699891786.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD06881D59B6B9D980969568FE35D3BAF8F9DA29C8E9B7129099F2BBC5D9F7DA "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/b7JJcTfjQ2qaNcCSq1NFjg/zh-cn_image_0000002699731900.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=96BA56FFC012FAE804CA7309352E3539FFAFE506288FE07243F35F01E6F958FE "点击放大")

**修复建议**

* 遵循RAII原则，利用对象的生命周期管理资源。
* epoll场景的socket句柄使用结束后，应当按照顺序，先调用epoll\_ctl(epfd, EPOLL\_CTL\_DEL, fd, NULL)从事件监听器中移除，再调用close(fd)关闭句柄。
* 当参数错误或资源不足时，清理所有已分配资源。

## pipe句柄泄漏

### 根因描述

pipe句柄是一种单向通信管道，依托于内核中的环形缓冲区，常用于实现轻量级的进程间通信（IPC）。pipe句柄泄漏根因包括：

* 创建pipe后没有关闭：开发者通过pipe()、pipe2()等接口创建句柄后，因编码疏忽或业务逻辑复杂，未能在后续流程中调用close()予以释放，导致句柄残留。
* 异常路径绕过关闭逻辑：在异步回调、异常处理或提前返回等分支中，本应执行的close()意外跳过，从而造成泄漏。
* fork后的pipe句柄泄漏：父进程在fork()之前已打开某些pipe句柄，且没有设置O\_CLOEXEC标志，子进程即使不使用这些句柄，也被迫继承导致泄漏。
* popen使用后未配对pclose：通过popen()创建的管道流，若忘记调用pclose()进行清理，同样会产生句柄泄漏。

### 问题分析思路

**运维态问题分析思路**

开发者可以根据[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)对日志中的top10进行分析，如果类型为pipe的句柄数量最多，那么可以将当前句柄泄漏问题定位为pipe句柄泄漏问题。

```screen
Leaked fd Top 10:
20008	pipe
10	eventpoll
8	eventfd
7	socket
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
3	/dev/null
3	/sys/kernel/debug/tracing/trace_marker
2	/dev/urandom
```

除了使用运维态问题分析方法中展示的通用方法外，pipe作为特殊类型句柄，会有进程详细的维测信息输出如下所示：

```screen
ProcessName ProcessID Fd PipeName inode MaxUsage NumAccounted RingSize
xample.dfx_test 20767 5 / 6943 16 16 16
xample.dfx_test 20767 7 / 6943 16 16 16
xample.dfx_test 20767 12 / 8564 16 16 16
```

开发者可以通过以下方法分析pipe基础维测日志来缩小排查范围：

1. 查看本应用所占用的pipe句柄，日志经过pid过滤，每一行表示一个pipe句柄。
2. 对于命名pipe句柄，可以进行排查，如果大量句柄PipeName相同，则可以根据名称定位到主要泄漏点。
3. 关注应用代码中是否使用pipe()和pipe2()等接口创建pipe句柄，排查其生命周期是否存在泄漏。

参考[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)获取到句柄栈日志后，开发者可以参考[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)进行下一步定位。

**开发态问题分析思路**

如果应用发生了pipe句柄泄漏，可以参考[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)，尝试按场景复现并使用DevEco Studio中Profiler工具的Allocation功能定位句柄泄漏问题。

### 案例：pipe句柄泄漏

本案例模拟了因大量pipe句柄未释放引发的泄漏故障。系统检测到应用发生了句柄泄漏后，在后台管控了此应用，再次打开时，应用冷启动。

**运维态问题案例分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，当应用发生句柄泄漏故障时，开发者可以在沙箱中获取到句柄泄漏相关的故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)分析以下基础维测日志，可以确认泄漏的句柄类型为pipe。

   ```screen
   Leaked fd Top 10:
   20008	pipe
   10	eventpoll
   8	eventfd
   7	socket
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   3	/sys/kernel/debug/tracing/trace_marker
   2	/dev/urandom
   ```
3. 如果获取到了句柄栈，可以按照[运维态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section71361119142017)提供的步骤依次分析，通过下图1处导入句柄栈文件，再依次单击下图2-4处，可筛选出泄漏的调用栈如下图5、6处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/sJuXNcrbQlCszZePUxhvBw/zh-cn_image_0000002729491155.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=045DB4D7C2225AD108B79A9213B83A7FEDCD4419D4569A005B1A2B0DBD700E34)
4. 分析调用栈指向的代码段，发现PipeFDLeak()函数正在循环申请pipe句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/pJWFFplEQAW9Y1zIu-KIDg/zh-cn_image_0000002729611115.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A9250AE44B973A1C2AA2599D6D86D5B3C03E05ED3B3C5A80CD270A143DC28D2 "点击放大")

**开发态问题案例分析思路**

1. 按照[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)提供的步骤完成录制后，并依次单击下图1、2处，在下图3处可找到泄漏句柄的申请调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/DpAsxJmMQwGZ0BOGxdo9Mg/zh-cn_image_0000002699891788.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C3631C49CC868AA02F55C7BF45DBD17E4CDCA10900AF607669C7A5882972266)
2. 分析调用栈指向的代码段，发现PipeFDLeak()函数正在循环申请pipe句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/zUEy0K6JS9m4tyyY1j_lpw/zh-cn_image_0000002699731902.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=E563CA1E5BB784F0F7E36D5BA33477A68B3CBEA3FF50D6295CF43DA2EC4217FF "点击放大")

**修复建议**

* 遵循RAII原则，利用对象的生命周期管理资源。
* 确保所有控制流路径都执行资源清理代码，优先使用语言特性保证资源释放。
* 关闭事件监听之前，检查事件描述符是否已经释放。

## ASHMEM句柄泄漏

### 根因描述

ASHMEM句柄：匿名共享内存句柄，用于大量数据的跨进程通信（IPC）。ASHMEM句柄泄漏根因包括：

* 未正确关闭文件描述符：创建ASHMEM区域后未及时调用close()释放句柄，导致系统资源泄漏。
* 异常处理不完善：代码执行中发生异常或进入错误分支时，未能清理已分配的资源，致使句柄残存。
* ArkTS开发中的典型遗漏：使用Ashmem.[create()](../harmonyos-references/js-apis-rpc.md#create9-2)后未调用[closeAshmem()](../harmonyos-references/js-apis-rpc.md#closeashmem8)，或使用[createPixelMap()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)后未执行对应的释放操作（如[release()](../harmonyos-references/arkts-apis-image-pixelmap.md#release7)），从而造成内存与句柄双重泄漏。

### 问题分析思路

**运维态问题分析思路**

开发者可以根据[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)对日志中的top10进行分析，如果类型为ASHMEM的句柄数量最多，那么可以将当前句柄泄漏问题定位为ASHMEM句柄泄漏问题。

```screen
Leaked fd Top 10:
20001	ashmem
10	eventpoll
8	eventfd
8	pipe
7	socket
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
3	/dev/null
3	/sys/kernel/debug/tracing/trace_marker
```

除了使用运维态问题分析方法中展示的通用方法外，ASHMEM作为特殊类型句柄，会有进程详细的维测信息输出如下所示，分析方法可参考[ASHMEM内存基础维测日志分析方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section170311436201)。

```screen
Process ashmem detail info:
---------------------------------------------------------------------------------
Process_name	Process_ID	Fd	Cnode_idx	Applicant_Pid	Ashmem_name	Virtual_size	Physical_size	magic
audio_server	832	17	328231	832	dev/ashmem/PolicyVolumeMap	722	4096	2
composer_host	1467	20	328281	1659	dev/ashmem/hdi_smq	135168	135168	20
composer_host	1467	21	328281	1467	dev/ashmem/hdi_smq	135168	135168	21
composer_host	1467	41	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	131
composer_host	1467	47	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	23
composer_host	1467	48	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	32
composer_host	1467	50	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	25
composer_host	1467	53	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	22
composer_host	1467	60	328281	1465	dev/ashmem/gralloc_shared_attr	4096	4096	4392
```

此外，针对ASHMEM句柄泄漏问题，可参考[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)提取句柄申请调用栈日志，进而结合[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)定位到申请句柄的具体代码位置。

**开发态问题分析思路**

如果应用发生了ASHMEM句柄泄漏，可以参考[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)，尝试按场景复现并使用DevEco Studio中Profiler工具的Allocation功能定位句柄泄漏问题。

### 案例：ASHMEM句柄泄漏

本案例模拟了因大量ASHMEM句柄未释放引发的泄漏故障。系统检测到应用发生了句柄泄漏后，在后台管控了此应用，再次打开时，应用冷启动。

**运维态问题案例分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，当应用发生句柄泄漏故障时，开发者可以在沙箱中获取到句柄泄漏相关的故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)，根据以下基础维测日志，可以确认泄漏的句柄类型为ASHMEM。

   ```screen
   Leaked fd Top 10:
   20001	ashmem
   10	eventpoll
   8	eventfd
   8	pipe
   7	socket
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   3	/sys/kernel/debug/tracing/trace_marker
   ```
3. ASHMEM基础维测日志提供了申请的各个节点信息，可参考[问题分析思路](bpta-stability-app-fdleak-fault-mode.md#section17564184819411)分析ASHMEM句柄的具体使用业务，缩小排查范围。
4. 如果获取到了句柄栈，可以按照[运维态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section71361119142017)提供的步骤依次分析，通过单击下图1处导入句柄栈文件，再依次单击下图2-4处，筛选出泄漏的调用栈如下图5、6处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/MZ7KE0-WRFqcssUxhjN_sA/zh-cn_image_0000002729491157.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=F24216539B2A872710048C672446EF507BCC49996D1050F52A040FBE1B9A8062)
5. 分析调用栈指向的代码段，发现AshmemFDLeak()函数正在循环调用AshmemCreate()函数，之后又进入AshmemOpenLocked()函数申请ASHMEM句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/X33PMHofTgeW1F_bj-LjLw/zh-cn_image_0000002729611117.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=546FC5B2A4F92B82BA23EA40B349447BA816B41772EE10A4B67BEA695BEB77D0 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/VbwNwVVhT1aSy19brG4H1Q/zh-cn_image_0000002699891790.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BA2BE0F114E9AE617F31BF90FD3A3928399B833121A2782C0F607E51C3DF1A2 "点击放大")

**开发态问题案例分析思路**

1. 按照[开发态分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section4840142124519)提供的步骤完成录制后，依次单击下图1、2处，可找到泄漏句柄的申请调用栈如下图3处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/cjVQ8kPWSHymrplWZuhoAA/zh-cn_image_0000002699731904.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=E82CE8C40A09A75DE8EE91F9E80C7286EAA9493744390AADA7F89C558FA4F573)
2. 分析调用栈指向的代码段，发现AshmemFDLeak()函数正在循环调用AshmemCreate()函数，之后又进入AshmemOpenLocked()函数申请ASHMEM句柄，且未释放，最终导致了句柄泄漏，调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/nntTesfITOWQdWjOaMgSsw/zh-cn_image_0000002729491159.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=38ADDF966E6E415A429892CBABEF85183717FF2757BF0EF3D048606ECF86D519 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/xi5lkEfWQ0ez2tE4XNYR8Q/zh-cn_image_0000002729611119.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BE597BE874562EBEEAAED25A7E25ABBCA4C002EF96A1253A26DB01B2541FADE "点击放大")

**修复建议**

* 遵循RAII原则，利用对象的生命周期管理资源。
* 确保所有控制流路径都执行资源清理代码，优先使用语言特性保证资源释放。
* 规范使用Ashmem.create()函数，在调用该函数创建共享内存区域后，必须建立严格的配对机制及时释放。
* 使用完毕后及时释放PixelMap资源，PixelMap通常使用量较大，因此在不再需要渲染或处理图像数据时，应立即调用其释放接口。

## dmabuf句柄泄漏

### 根因描述

dmabuf句柄：硬件直接访问内存的句柄。dmabuf句柄泄漏根因包括：

* 未正确关闭文件描述符：创建dmabuf区域后未及时调用close()释放句柄，导致系统资源泄漏。
* 异常处理不完善：代码执行中发生异常或进入错误分支时，未能清理已分配的资源，致使句柄残留。
* ArkTS开发中的典型遗漏：使用[OH\_NativeBuffer\_Alloc()](../harmonyos-references/capi-native-buffer-h.md#oh_nativebuffer_alloc)后未调用[OH\_NativeBuffer\_Unreference()](../harmonyos-references/capi-native-buffer-h.md#oh_nativebuffer_unreference)，或使用[createPixelMap()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)后未及时释放，导致dmabuf句柄大量堆积，造成资源泄漏。

### 问题分析思路

**运维态问题分析思路**

开发者可以根据[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)对日志中的top10进行分析，如果类型为dmabuf的句柄数量最多，那么可以将当前句柄泄漏问题定位为dmabuf句柄泄漏问题。

```screen
Leaked fd Top 10:
32698	dmabuf
10	eventpoll
8	eventfd
8	pipe
7	socket
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
3	/dev/null
3	/sys/kernel/debug/tracing/trace_marker
```

dmabuf作为特殊类型句柄，会有进程详细的维测信息输出如下所示：

```screen
Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
xample.dfx_test	28812   	67      	130965504	7899    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	69      	130965504	5397    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	71      	130965504	7900    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	73      	130965504	7901    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	76      	147456  	7902    	28812   	xample.dfx_test	srcImageSize-192x192-pixelMapSize-192x192-streamsize-5386-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	77      	131563520	5398    	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	80      	130965504	8829    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
```

开发者可以先参考[DMA内存基础日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section170311436201)找到可疑的dmabuf句柄，并分析对应的组件以及关联的业务场景，以缩小排查范围。

通过[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)获取到栈日志后，开发者还可以按照以下步骤进行分析，定位至泄漏点：

1. 单击下图1处Open File按钮导入句柄栈日志。
2. 选择VM:others泳道，如下图2处，其对应的是dmabuf句柄信息。
3. 单击下图3处Call Trees查看句柄申请调用栈。
4. 单击下图4处选择Created & Existing，筛选申请并且未释放的句柄及其调用栈。
5. 找到申请异常的dmabuf句柄及其调用栈，如下图5、6处框选的内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/0p7RbWYaTYOmStApiW7pFQ/zh-cn_image_0000002699891792.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=48996128C887A4BC519C7F208B031DD2C6202A41A01B0216A99B5AF1098BCF81)

**开发态问题分析思路**

如果应用发生了dmabuf句柄泄漏，推荐开发者使用DevEco Studio中Profiler工具的Allocation功能抓取句柄的异常增长点。

1. 确认问题为句柄泄漏后，开发者可以使用DevEco Studio中Profiler工具的Allocation功能抓取句柄数量和申请调用栈，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。
2. 启动录制后，不断尝试复现发生过句柄泄漏的场景。
3. 录制完成后，可参考上文运维态分析思路对句柄泄漏点进行定位。

### 案例：dmabuf句柄泄漏

本案例模拟了因大量dmabuf句柄未释放引发的泄漏故障。系统检测到应用发生了句柄泄漏后，在后台管控了此应用，再次打开时，应用冷启动。

**运维态问题案例分析思路**

如果开发者在运维态遇到此问题，可以按照如下步骤进行分析：

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，当应用发生句柄泄漏故障时，开发者可以在沙箱中获取到句柄泄漏相关的故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)分析以下基础维测日志，可以确认泄漏的句柄类型为dmabuf。

   ```screen
   Leaked fd Top 10:
   32698	dmabuf
   10	eventpoll
   8	eventfd
   8	pipe
   7	socket
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   3	/sys/kernel/debug/tracing/trace_marker
   ```
3. 如果获取到了句柄栈，可以按照[问题分析思路](bpta-stability-app-fdleak-fault-mode.md#section158103411211)中的运维态分析思路提供的步骤依次分析，通过下图1处导入句柄栈文件，再依次单击下图2-4处，可筛选出泄漏的调用栈如下图5、6处所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/vgelGpFsRx28_Sr6szI9sA/zh-cn_image_0000002699731906.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D328294951AA3AA72F41839B55782CF051A8CEA0A0388DFAC43675A91F959BA)
4. 分析调用栈指向的代码段，发现应用InitLeak()函数正在循环调用ResourceFactory::CreateResource()函数，之后又进入DmaBufResource::Acquire()函数，申请dmabuf句柄，且未释放，最终导致了句柄泄漏。调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jz9OFm_2SLOwl3adwIP4dQ/zh-cn_image_0000002729491161.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=63159C619B054555534221F25014DD40A05B925CF1EA2F6E1E69BEF70101B75B "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/g-EV-VjNQLqwbn1y2Pbo1A/zh-cn_image_0000002729611121.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BA2C844CA3D8BC953559FA0FE1566D2E148A281E81EED44E5EF71CE24E5C103 "点击放大")

**开发态问题案例分析思路**

如果开发者在开发态遇到此问题，可以按照如下步骤进行分析：

1. 按照[问题分析思路](bpta-stability-app-fdleak-fault-mode.md#section158103411211)中开发态问题分析思路提供的步骤完成录制，并依次单击下图1、2处，在下图3处可找到泄漏句柄的申请调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/9XSskk6lQXOVGSTl0ClfUw/zh-cn_image_0000002699891794.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F4EDD68534033AEAF58D59ED40B2DD8C4FF9AF3724452B52CBB2B5F317C34A0)
2. 分析调用栈指向的代码段，发现应用InitLeak()函数正在循环调用ResourceFactory::CreateResource()函数，之后又进入DmaBufResource::Acquire()函数，申请dmabuf句柄，且未释放，最终导致了句柄泄漏。调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/SvualtAST42JurlyZ-wipA/zh-cn_image_0000002699731908.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AE495D7750E55C74F2D79197EBE41A5B4C192203B7BFE4706F3BDECE5D94E70 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/HuiCF1YyQVyyn2J1V8AYdQ/zh-cn_image_0000002729491163.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D4263E23328B2FAC58C6B4FE55CED0CFE7A4E485E017F2DB934D872316BC105 "点击放大")

**修复建议**

* 遵循RAII原则，利用对象的生命周期管理资源。
* 确保所有控制流路径都执行资源清理代码，优先使用语言特性保证资源释放。
* 规范使用NativeBuffer类的相关函数，在创建NativeBuffer实例后，严格对应其生命周期进行管理，确保在不再需要缓冲区数据时，正确调用销毁或释放接口。
* 使用完毕后及时释放PixelMap资源，PixelMap通常使用量较大，因此在不再需要渲染或处理图像数据时，应立即调用其释放接口。
