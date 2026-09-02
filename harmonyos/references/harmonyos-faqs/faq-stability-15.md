---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-15
title: 应用使用卡顿，运行一段时间后出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用使用卡顿，运行一段时间后出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3f9427436f1c7fc1c6cad55e30c17561733c255919b1d583a70fa9e25d245ec1
---

## 问题现象

应用使用过程中出现卡顿，一段时间后发生闪退。

## 背景知识

* 句柄泄漏是进程在调用系统文件之后，没有释放已经打开的文件句柄。
* 句柄泄漏日志文件规格可以参考[句柄泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏日志规格)。
* 如果Leaked fd Top 10的句柄信息属于ashmem、socket、pipe、sync\_file或dmabuf这五类特殊类型，且该类型的句柄个数超过1000个，日志中会增加整机详细的维测信息。
* ashmem是一种匿名共享内存机制,允许多个进程共享同一块内存区域,而无需显式的文件系统交互。它基于Linux内核的内存映射机制(mmap)实现,通过文件描述符(File Descriptor)传递共享内存的句柄。

## 场景一

### 问题定位

1. 查看句柄泄漏日志文件，ashmem句柄个数达到5000+，存在句柄泄漏。

   ```shell
   time: 2025/06/08 12:55:50
   pid: 30687
   process: com.hx.example
   leaked fd nums: 6043
   FdCount	FileDescriptor

   *****************************
   Leaked fd Top 10:
   5727	ashmem
   72	pipe
   58	eventpoll
   55	eventfd
   45	socket
   6	/dev/urandom
   5	/data/storage/el2/database/entry/rdb/monitor_hysdk.db
   5	/data/storage/el2/database/rdb/Bugly_database.db
   5	/data/storage/el2/database/entry/rdb/huya_database.db
   5	/data/storage/el2/database/entry/rdb/monitor_harmony_instance.db
   ```
2. 搜索关键字LOGGER\_MEMCHECK\_ASHMEM\_INFO，查看整机ashmem内存的详细信息。可以看到应用占用的物理共享内存达到500M左右(515649536byte)。

   ```shell
   Process_name Virtual_size Physical_size
   Total ashmem  of [audio_server] virtual size is  140265, physical size is 163840 
   Total ashmem  of [multimodalinput] virtual size is  4096, physical size is 4096 
   Total ashmem  of [telephony] virtual size is  20480, physical size is 20480 
   Total ashmem  of [composer_host] virtual size is  303104, physical size is 303104 
   Total ashmem  of [render_service] virtual size is  239421716, physical size is 241115136 
   Total ashmem  of [foundation] virtual size is  969755, physical size is 212992 
   // ...
   Total ashmem  of [com.hx.example] virtual size is  514969880, physical size is 515649536 
   Total ashmem  of [hod:inputMethod] virtual size is  520052, physical size is 528384 
   // ...
   ```
3. 从Ashmem\_name可以看出，基本都是dev/ashmem/EXTRawData，和图片有关。目前系统采用了统一渲染架构，应用使用PixelMap解码和几何变换的时候会生成ashmem。

   ```shell
   Process_name	Process_ID	Fd	Cnode_idx	Applicant_Pid	Ashmem_name	Virtual_size	Physical_size	magic
   // ...
   com.hx.example	30687	16158	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16159	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16160	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16161	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16162	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16163	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16164	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16165	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16166	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16167	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16168	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16169	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   com.hx.example	30687	16170	328447	30687	dev/ashmem/EXTRawData	90000	90112	3956290
   // ...
   ```

### 分析结论

句柄泄漏导致应用在运行过程中持续消耗系统资源，最终出现卡死或闪退。

### 修改建议

申请句柄后必须进行释放，特别是在异常分支提前return的场景中，示例可见[优化建议1：函数各个异常分支及时增加关闭句柄的操作](../best-practices/bpta-stability-leak-opt.md#section0221141523718)。

## 场景二

### 问题定位

1. 在hilog日志中搜索关键字Kill Reason|PROCESS\_KILL，找到终止原因Kill Reason:ResourceLeak:Ashmem Leak，表示Ashmem内存泄漏。

   ```shell
   12-15 18:27:42.349  1573  1573 I C01311/foundation/AppMS: [a92ab8e29d5199d 0 0][AMSI3051]kill reason=KillApplication, 20817
   12-15 18:27:42.350  1573  1573 W C01311/foundation/AppMS: [a92ab8e29d5199d 0 0][AMSI3075]kill pid 20817, ret:0, Kill Reason:KillApplication,callingPid=933
   12-15 18:27:42.350  1573  1573 W C01311/foundation/AppMS: [a92ab8e29d5199d 0 0][AMSI3079]nullptr
   12-15 18:27:42.351   933 26981 E C01716/resource_schedule_service/RESOURCE_QUOTA_CONTROL: [a92ab8e29d5199d 0 0][KillApplication:148] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], uid=20020256, pid=20817, processName=com.hx.example, appIndex=0, KillReason=Kill Reason:ResourceLeak:Ashmem Leak,Msg=, FOREGROUND=0
   12-15 18:27:42.351   933 26981 I C01716/resource_schedule_service/RESOURCE_QUOTA_CONTROL: [a92ab8e29d5199d 0 0][ClearAppInfo:186] clear app info, uid:20020256
   ```
2. 从memory\_leak目录下查看文件名为memleak-kernel-[应用包名]-0-sample.txt的采样文件，可以看到泄漏内存的类型为ashmem，在18:23:59时超出了阈值hardThreshold:4096(MB)。

   ```shell
   memoryName:ashmem
   softThreshold:2048(MB)
   hardThreshold:4096(MB)
   topMemory:5446410(KB)

   time(s) kernelMemory(KB)realtime
   0               123659          296734          2025/12/15 16:40:36
   1               123879          289900          2025/12/15 16:44:16
   // ...
   27              129600          3569341         2025/12/15 18:20:19
   28              129820          5446410         2025/12/15 18:23:59
   ```
3. 同目录下查看内存映射文件memleak-kernel-[应用包名]-0-[timestamp].txt，搜索关键字Process ashmem overview info，找到ashmem内存概览信息，观察到应用进程虚拟内存占用约5G，物理内存占用约2G。

   ```shell
   Process_name Virtual_size Physical_size
   Total ashmem  of [audio_server] virtual size is  85509, physical size is 57344 
   Total ashmem  of [multimodalinput] virtual size is  8192, physical size is 8192 
   // ...
   Total ashmem  of [com.hx.example] virtual size is  5287611976, physical size is 2005512192 
   Total ashmem  of [hongmeng:render] virtual size is  16384, physical size is 0 
   Total ashmem  of [ExtAbility:1082] virtual size is  1675264, physical size is 1675264
   ```
4. 搜索关键字Process ashmem detail info，找到ashmem内存详细信息，观察应用进程那些ashmem内存占用较高，主要关注Process\_name、Virtual\_size和Physical\_size这几列，观察到某个ashmem资源占用高达277755556字节。

   ```shell
   Process_name	Process_ID	Fd	Cnode_idx	Applicant_Pid	Ashmem_name	Virtual_size	Physical_size	magic
   // ...
   com.hx.example	20579	39	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	192512	2186702
   com.hx.example	20579	108	328359	20579	dev/ashmem/112x112-re*ou*ce**15*99*79*.w*bp	50176	0	2108956
   com.hx.example	20579	138	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	191729664	2188915
   com.hx.example	20579	328	328359	20579	dev/ashmem/EXTRawData	277755556	262664192	2190514
   com.hx.example	20579	330	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	8699904	2187409
   com.hx.example	20579	332	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	20688896	2187423
   com.hx.example	20579	334	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	50786304	2187674
   com.hx.example	20579	336	328359	20579	dev/ashmem/srcImageSize-8333x8333-pixelMapSize-8333x8333-streamsize-3036967-mimetype-jpeg	277755556	100409344	2187706
   com.hx.example	20579	337	328359	20579	dev/ashmem/EXTRawData	277755556	264130560	2190536
   com.hx.example	20579	340	328359	1438	dev/ashmem/gralloc_shared_attr	4096	0	2189497
   com.hx.example	20579	342	328359	20579	dev/ashmem/EXTRawData	277755556	256749568	2190552
   com.hx.example	20579	345	328359	20579	dev/ashmem/EXTRawData	277755556	249798656	2190556
   com.hx.example	20579	347	328359	20579	dev/ashmem/EXTRawData	277755556	208814080	2190627
   com.hx.example	20579	351	328359	20579	dev/ashmem/EXTRawData	277755556	74665984	2191220
   com.hx.example	20579	354	328359	20579	dev/ashmem/EXTRawData	277755556	72732672	2191221
   ```

### 分析结论

应用存在ashmem图片共享内存资源泄漏。

### 修改建议

通过[setMemoryNameSync](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)或者[OH\_PixelmapNative\_SetMemoryName()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)自定义PixelMap内存标识符，快速定位泄漏的图片资源，减少加载图片资源的数量，及时释放图片共享内存。详情参考[ashmem泄漏](../best-practices/bpta-stability-leak-way.md#section2825227501)。
