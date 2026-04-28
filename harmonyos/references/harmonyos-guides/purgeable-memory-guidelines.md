---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/purgeable-memory-guidelines
title: 内存管理purgeable内存开发指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 内存管理 > 内存管理purgeable内存开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e19d0cf17ccda52f187f38ce35f1e9bb72c86ae97043aa546c8bad5582785d29
---

Purgeable Memory指可以随时丢弃的内存，此内存区域用于存放那些很容易通过重新计算构建出来的数据，该数据在系统低内存时可以被直接释放，用户访问的时候再重新构建。Purgeable Memory适用于存放大块（至少4K）且恢复代价较小的数据，它在系统压力较大时优先回收（这里指对匿名页采用类似文件页的drop的形式，而不是压缩），再次使用时需要用户自己恢复数据再使用。

## 场景介绍

HarmonyOS提供Purgeable Memory内存管理机制，开发者可以使用相关接口创建PurgeableMemory对象，从而管理purgeable内存。

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native层相关接口操作purgeable内存。功能包括purgeable内存的申请、释放等。

针对Purgeable Memory内存管理机制，常见的开发场景如下：

* 通过该机制提供的NAPI接口申请管理PurgeableMemory对象，并将数据内容写入该对象。
* 使用完毕后释放。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_PurgeableMemory \*OH\_PurgeableMemory\_Create(size\_t size, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | 创建PurgeableMemory对象，每次调用都会产生一个新的PurgeableMemory对象。 |
| bool OH\_PurgeableMemory\_Destroy(OH\_PurgeableMemory \*purgObj) | 对PurgeableMemory对象进行析构操作。 |
| bool OH\_PurgeableMemory\_BeginRead(OH\_PurgeableMemory \*purgObj) | 对PurgeableMemory对象进行读访问。 |
| void OH\_PurgeableMemory\_EndRead(OH\_PurgeableMemory \*purgObj) | 读操作结束，将PurgeableMemory对象的引用计数减1，当引用计数为0的时候， 该PurgeableMemory对象可以被系统回收。 |
| bool OH\_PurgeableMemory\_BeginWrite(OH\_PurgeableMemory \*purgObj) | 对PurgeableMemory对象进行写访问。 |
| void OH\_PurgeableMemory\_EndWrite(OH\_PurgeableMemory \*purgObj) | 写操作结束，将PurgeableMemory对象的引用计数减1，当引用计数为0的时候，该PurgeableMemory对象可以被系统回收。 |
| void \*OH\_PurgeableMemory\_GetContent(OH\_PurgeableMemory \*purgObj) | 获取PurgeableMemory对象内存数据。 |
| size\_t OH\_PurgeableMemory\_ContentSize(OH\_PurgeableMemory \*purgObj) | 获取PurgeableMemory对象内存数据大小。 |
| bool OH\_PurgeableMemory\_AppendModify(OH\_PurgeableMemory \*purgObj, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara) | 添加PurgeableMemory对象的修改方法。 |

## Purgeable Memory应用开发步骤

以下步骤描述了在**HarmonyOS**中如何使用Purgeable Memory提供的NAPI接口，申请PurgeableMemory对象，并将内容写入PurgeableMemory对象后，对相应对象进行读写访问。

1. 声明PurgeableMemory对象创建规则。

   ```
   1. // 声明构建函数的参数
   2. struct ParaData{
   3. int start;
   4. int end;
   5. };

   7. // 声明一个使用ModifyFunc
   8. bool FactorialFunc(void* data, size_t size, void* param){
   9. bool ret = true;
   10. ParaData *pdata = (ParaData*) param;
   11. int* oriData = (int*)data;
   12. int i = pdata->start;
   13. while (i < pdata->end) {
   14. *oriData *= i;
   15. i++;
   16. }
   17. return ret;
   18. }

   20. // 声明修改PurgeableMemory对象扩展函数的参数
   21. struct AppendParaData{
   22. int newPara;
   23. };

   25. // 声明修改PurgeableMemory对象的扩展函数
   26. bool AddFunc(void* data, size_t size, void* param){
   27. bool ret = true;
   28. int *oriDatap = (int*) data;
   29. AppendParaData* apData = (AppendParaData*)param;
   30. *oriDatap += apData->newPara;
   31. return ret;
   32. }
   ```
2. 创建PurgeableMemory对象。

   ```
   1. // 声明一个4MB的PurgeableMemory对象大小
   2. #define DATASIZE (4 * 1024 * 1024)

   4. // 声明创建函数的参数
   5. struct ParaData pdata = {1,2};

   7. // 创建一个PurgeableMemory对象
   8. OH_PurgeableMemory* pPurgmem = OH_PurgeableMemory_Create(DATASIZE, FactorialFunc, &pdata);
   ```
3. 读访问PurgeableMemory对象。

   ```
   1. //业务定义对象类型
   2. class ReqObj;

   4. // 读取对象
   5. if(OH_PurgeableMemory_BeginRead(pPurgmem)) {
   6. // 获取PurgeableMemory对象大小
   7. size_t size = OH_PurgeableMemory_ContentSize(pPurgmem);

   9. // 获取PurgeableMemory对象内容
   10. ReqObj* pReqObj = (ReqObj*) OH_PurgeableMemory_GetContent(pPurgmem);

   12. // 读取PurgeableMemory对象结束
   13. OH_PurgeableMemory_EndRead(pPurgmem);
   14. }
   ```
4. 写访问PurgeableMemory对象。

   ```
   1. //业务定义对象类型
   2. class ReqObj;

   4. // 修改PurgeableMemory对象
   5. if(OH_PurgeableMemory_BeginWrite(pPurgmem)) {
   6. // 获取PurgeableMemory对象数据
   7. ReqObj* pReqObj = (ReqObj*) OH_PurgeableMemory_GetContent(pPurgmem);

   9. // 声明扩展创建函数的参数
   10. struct AppendParaData apdata = {1};

   12. // 更新PurgeableMemory对象重建规则
   13. OH_PurgeableMemory_AppendModify(pPurgmem, AddFunc, &apdata);

   15. // 修改PurgeableMemory对象结束
   16. OH_PurgeableMemory_EndWrite(pPurgmem);
   17. }
   ```
5. 销毁PurgeableMemory对象。

   ```
   1. // 销毁对象
   2. OH_PurgeableMemory_Destroy(pPurgmem);
   3. // 置空指针防止UAF
   4. pPurgmem = nullptr;
   ```
