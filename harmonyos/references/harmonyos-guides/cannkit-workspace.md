---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-workspace
title: 如何申请workspace作为临时内存
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 如何申请workspace作为临时内存
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34a3f7ee81b148c8596ccbcf278dbb2b362a4e8d2787e53ffd889cebb8169d28
---

workspace是设备侧Global Memory上的一块内存。workspace内存分为两部分：系统workspace和开发者workspace。

* 系统workspace：AscendC API需要预留的workspace内存

  API在计算过程需要一些workspace内存作为缓存，因此算子需要为API预留workspace内存，预留内存大小通过[GetLibApiWorkSpaceSize](cannkit-getlibapiworkspacesize.md)接口获取。
* 开发者workspace：算子实现使用到的workspace内存

  算子内部需要通过额外的device内存进行数据交换或者缓存的时候才需要分配，根据实际情况自行分配。使用场景如下。

  + 需要使用Unified Buffer和L1 Buffer上空间且空间不够用时，可以将数据暂存至workspace上。
  + 其他需要使用Global Memory上内存空间的场景。

不同开发方式下，具体的使用方法如下。

* 工程化算子开发方式

  在tiling函数中先通过[GetWorkspaceSizes](cannkit-getworkspacesizes.md)接口获取workspace大小的存放位置，再设置workspace的大小，框架侧会为其在申请对应大小的设备侧Global Memory，在对应的算子kernel侧实现时可以使用这块workspace内存。在使用[Matmul](cannkit-matmul-usage-description.md)等需要系统workspace的高阶API时，设置的workspace空间大小为系统workspace和开发者workspace之和。

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

  在device侧kernel入口处的workspace为开发者的workspace指针：

  ```
  1. // 开发者写的Kernel函数，核函数必须包括GM_ADDR workspace入参，位置需要放在tiling之前
  2. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
  3. {
  4. // ...

  6. }
  ```
