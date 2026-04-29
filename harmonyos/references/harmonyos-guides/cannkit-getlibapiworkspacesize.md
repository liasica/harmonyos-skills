---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getlibapiworkspacesize
title: GetLibApiWorkSpaceSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetLibApiWorkSpaceSize
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a99cbe6199a0008cf8376d715ab396a79ce32cac5501b585f175d898241a901
---

## 函数功能

获取AscendC API需要的workspace空间大小。

## 函数原型

```
1. uint32_t GetLibApiWorkSpaceSize(void) const;
```

## 参数说明

无

## 返回值

返回uint32\_t数据类型的结果，该结果代表当前系统workspace的大小。

## 约束说明

无

## 调用示例

```
1. // 开发者自定义的tiling函数
2. static ge::graphStatus TilingFunc(gert::TilingContext* context)
3. {
4. AddApiTiling tiling;
5. // ...
6. size_t usrSize = 256; // 设置开发者需要使用的workspace大小。
7. // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。
8. auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());
9. uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();
10. size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。
11. currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。
12. // ...
13. }
```
