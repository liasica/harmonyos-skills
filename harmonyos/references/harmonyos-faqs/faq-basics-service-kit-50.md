---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-50
title: 大数据量下载过程中会中断下载
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 大数据量下载过程中会中断下载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ed18ede49650728f1c63479ded31cd22e506acb06dffce7ff8aa5af2076f2d7
---

## 问题现象

用户使用应用通过共享文件的方式进行复制下载操作。当下载文件总量较大时，下载到某个文件可能会中断，导致下载进度停滞。

## 背景知识

[GC垃圾回收](../harmonyos-guides/gc-introduction.md)：GC（全称Garbage Collection），即垃圾回收。在计算机领域，GC是指识别并释放内存中的不再使用的对象，以回收内存空间。

## 问题定位

根据HiLog日志进行分析，日志信息如下：

```shell
07-08 13:24:39.893   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Speed: merge dataList usedTime = 0
07-08 13:24:39.896   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-SMB: smb2.read off=135168000, len=614400
07-08 13:24:39.896   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Read: doRead at 1751952279896
07-08 13:24:39.896   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-SMB: created header={"protocol_":"SMB","structureSize_":64,"creditCharge_":10,"channelSequence_":0,"status_":0,"command_":8,"creditsRequested_":10,"creditsGranted_":0,"flags_":0,"chainOffset_":0,"messageId_":"2214","asyncId_":"0","treeId_":1,"sessionId_":"46576497963565095","signature_":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0}}
07-08 13:24:39.896   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-SMB: signing[true] for command: 8
07-08 13:24:39.896   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-SMB: Header.write.sessionId_=46576497963565095, messageId_=2214, command=8
07-08 13:24:39.897   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Write: signing data[113] cost time 0
07-08 13:24:39.897   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Read: doRead created readPacket at 1751952279897
07-08 13:24:39.897   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Read[2214]: doRead: offset=135168000, length=614400, startWritePacket at 1751952279897
07-08 13:24:39.897   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-SMB: communication.writePacket isConnected=true, messageId=2214
07-08 13:24:39.898   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Read[2214]: writedPacket usedTime=1, time=1751952279898
07-08 13:24:39.918   9100-9100     C01406/com.example.hmos/OHOS::RS  com.com.example.hmos  I     RSUIDirector::ProcessMessages messageId:30903, cmdCount:1, instanceId:100000
07-08 13:24:39.919   9100-9100     C01406/com.example.hmos/OHOS::RS  com.com.example.hmos  I     RSUIDirector::PostTask messageId:30903, cmdCount:1, instanceId:100000
07-08 13:24:39.929   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received data[2896]
07-08 13:24:39.929   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received packet begin, length=614480  at 1751952279929
07-08 13:24:39.929   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: wait receive more data
07-08 13:24:39.938   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received data[8192]
07-08 13:24:39.938   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received packet begin, length=614480  at 1751952279938
07-08 13:24:39.938   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: wait receive more data
07-08 13:24:39.938   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received data[496]
07-08 13:24:39.938   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received packet begin, length=614480  at 1751952279938
07-08 13:24:39.939   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: wait receive more data
07-08 13:24:39.949   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received data[8192]
07-08 13:24:39.950   9100-10545    A03D00/com.example.hmos/JSAPP  com.com.example.hmos  I     LiuZh-Socket: received packet begin, length=614480  at 1751952279950
```

根据上述日志，可以分析得到：在应用下载某个文件时，会创建一个data的数组，用来缓存接收到的二进制数据。

紧接着往下分析日志，如下日志信息：

```shell
07-08 13:24:56.183   9100-35708    C01203/com.example.hmos/Ans  com.com.example.hmos  I     [ans_notification.cpp(PublishNotification:194)]PublishNotification,notificationId:0
07-08 13:24:56.776   9100-9100     C03F00/com.example.hmos/ArkCompiler  com.com.example.hmos  I     [gc] IdleGCTrigger: trigger full gc
07-08 13:24:56.807   9100-9100     C03F00/com.example.hmos/ArkCompiler  com.com.example.hmos  I     [gc] IdleGCTrigger: trigger shared full gc
07-08 13:24:57.182   9100-9100     C01203/com.example.hmos/Ans  com.com.example.hmos  I     [common_convert_request.cpp(GetNotificationId:944)]notificationId = 0
07-08 13:24:57.182   9100-9100     C01203/com.example.hmos/Ans  com.com.example.hmos  I     [common_convert_request.cpp(GetNotificationSlotType:978)]notificationSlotType = 4
07-08 13:24:57.182   9100-35708    C01203/com.example.hmos/Ans  com.com.example.hmos  I     [ans_notification.cpp(PublishNotification:194)]PublishNotification,notificationId:0
```

通过上述日志可以判断此时触发了full gc，导致应用线程因触发GC垃圾回收而被中断。

## 分析结论

由于需要缓存的数据不断增加，触发了full gc的机制，导致应用的线程被中断。

## 修改建议

* 可以限制一次允许下载文件数量和大小。
* 做好内存申请和相应的清理处理，避免触发full gc。
