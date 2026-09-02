---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/purgeable-memory-guidelines
title: 内存管理 Purgeable Memory 开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > 内存管理 Purgeable Memory 开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7c775b926de8a7dae20038793f9b810f77b907421acd17f29c801d311bcc60f0
---

Purgeable Memory指可以随时丢弃的内存，此内存区域用于存放那些很容易通过重新计算构建出来的数据，该数据在系统低内存时可以被直接释放，用户访问的时候再重新构建。Purgeable Memory适用于存放大块（至少4KB）且恢复代价较小的数据，它在系统压力较大时优先回收（这里指对匿名页采用类似文件页的drop的形式，而不是压缩），再次使用时需要用户自己恢复数据再使用。

## 场景介绍

HarmonyOS提供Purgeable Memory管理机制，开发者可以使用相关接口创建PurgeableMemory对象，从而管理Purgeable Memory。

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native层相关接口操作Purgeable Memory。功能包括Purgeable Memory的申请、释放等。

针对Purgeable Memory内存管理机制，常见的开发场景如下：

1. 通过该机制提供的Native层相关接口申请并管理PurgeableMemory对象，并将数据内容写入该对象。
2. 使用完毕后释放PurgeableMemory对象。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_PurgeableMemory \*OH\_PurgeableMemory\_Create(size\_t size, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | 创建PurgeableMemory对象，每次调用都会产生一个新的PurgeableMemory对象。 |
| bool OH\_PurgeableMemory\_Destroy(OH\_PurgeableMemory \*purgObj) | 销毁PurgeableMemory对象。 |
| bool OH\_PurgeableMemory\_BeginRead(OH\_PurgeableMemory \*purgObj) | 对PurgeableMemory对象进行读访问，将读引用计数加1。 |
| void OH\_PurgeableMemory\_EndRead(OH\_PurgeableMemory \*purgObj) | 读操作结束，将PurgeableMemory对象的读引用计数减1。 |
| bool OH\_PurgeableMemory\_BeginWrite(OH\_PurgeableMemory \*purgObj) | 对PurgeableMemory对象进行写访问，将写引用计数加1。 |
| void OH\_PurgeableMemory\_EndWrite(OH\_PurgeableMemory \*purgObj) | 写操作结束，将PurgeableMemory对象的写引用计数减1。 |
| void \*OH\_PurgeableMemory\_GetContent(OH\_PurgeableMemory \*purgObj) | 获取PurgeableMemory对象内存数据指针，返回void\*类型，使用时需根据实际数据类型进行转换。 |
| size\_t OH\_PurgeableMemory\_ContentSize(OH\_PurgeableMemory \*purgObj) | 获取PurgeableMemory对象内存数据大小。 |
| bool OH\_PurgeableMemory\_AppendModify(OH\_PurgeableMemory \*purgObj, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | 添加PurgeableMemory对象的修改方法。 |

## Purgeable Memory应用开发步骤

以下步骤描述了在**HarmonyOS**中如何使用Purgeable Memory提供的Native层相关接口，申请PurgeableMemory对象，并将内容写入PurgeableMemory对象后，对该对象进行读写访问。

1. 声明PurgeableMemory对象创建规则。

   ```
   // 声明构建函数的参数
   struct ParaData{
       int start;
       int end;
   };

   // 声明一个使用ModifyFunc的函数（示例：阶乘函数）
   bool FactorialFunc(void* data, size_t size, void* param){
       bool ret = true;
       ParaData *pdata = (ParaData*) param;
       int* oriData = (int*)data;
       // 初始化为1，准备计算阶乘
       *oriData = 1;
       int i = pdata->start;
       while (i <= pdata->end) {
           *oriData *= i;
           i++;
       }
       return ret;
   }

   // 声明修改PurgeableMemory对象扩展函数的参数
   struct AppendParaData{
       int newPara;
   };

   // 声明修改PurgeableMemory对象的扩展函数
   bool AddFunc(void* data, size_t size, void* param){
       bool ret = true;
       int *oriDatap = (int*) data;
       AppendParaData* apData = (AppendParaData*)param;
       *oriDatap += apData->newPara;
       return ret;
   }
   ```
2. 创建PurgeableMemory对象。

   ```
   // 声明一个4MB的PurgeableMemory对象大小
   #define DATASIZE (4 * 1024 * 1024)

   // 声明创建函数的参数
   struct ParaData pdata = {1,2};

   // 创建一个PurgeableMemory对象
   OH_PurgeableMemory* pPurgmem = OH_PurgeableMemory_Create(DATASIZE, FactorialFunc, &pdata);
   ```
3. 读访问PurgeableMemory对象。

   ```
   // 业务自定义对象类型，需在业务代码中补充成员变量和方法
   class ReqObj {
   };

   // 读取对象
   if(OH_PurgeableMemory_BeginRead(pPurgmem)) {
       // 获取PurgeableMemory对象大小
       size_t size = OH_PurgeableMemory_ContentSize(pPurgmem);

       // 获取PurgeableMemory对象内容，使用前需确保对象内容已初始化
       ReqObj* pReqObj = reinterpret_cast<ReqObj*>(OH_PurgeableMemory_GetContent(pPurgmem));

       // 读取PurgeableMemory对象结束
       OH_PurgeableMemory_EndRead(pPurgmem);
   }
   ```
4. 写访问PurgeableMemory对象。

   ```
   // 业务自定义对象类型，需在业务代码中补充成员变量和方法
   class ReqObj {
   };

   // 修改PurgeableMemory对象
   if(OH_PurgeableMemory_BeginWrite(pPurgmem)) {
       // 获取PurgeableMemory对象数据
       ReqObj* pReqObj = reinterpret_cast<ReqObj*>(OH_PurgeableMemory_GetContent(pPurgmem));

       // 定义并初始化扩展修改函数的参数
       struct AppendParaData apdata = {1};

       // 更新PurgeableMemory对象重建规则
       OH_PurgeableMemory_AppendModify(pPurgmem, AddFunc, &apdata);

       // 修改PurgeableMemory对象结束
       OH_PurgeableMemory_EndWrite(pPurgmem);
   }
   ```
5. 销毁PurgeableMemory对象。

   ```
   // 销毁对象
   OH_PurgeableMemory_Destroy(pPurgmem);
   // 置空指针防止悬空指针访问
   pPurgmem = nullptr;
   ```

* **[高负载场景线程优先级设置](high-load-thread-priority.md)**
