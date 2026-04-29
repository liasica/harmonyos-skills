---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-4
title: ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏渲染加速服务 > ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决？
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b03119f039e12a0d737319b804712077b82a997b59a381381a09525975d134a
---

**现象描述**

以团结引擎URP管线为例，ABR对DrawOpaqueObjects绑定的Buffer进行分辨率调整时会引起SSAO shadow效果异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/jEy7T_WRSZ2N5dW5ijLbxA/zh-cn_image_0000002558765232.png?HW-CC-KV=V1&HW-CC-Date=20260429T053633Z&HW-CC-Expire=86400&HW-CC-Sign=373F8BE0283B1B0D90E4966701D825F3121153FDC648A46B01FE64386A57A197)

**原因分析**

通过上述URP管线可以看到，SSAO在渲染管线中是一个“前处理”，SSAO输出的图像会作为DrawOpaqueObjects的输入。当ABR对DrawOpaqueObjects绑定的Buffer进行自适应分辨率调整时，SSAO输出的图像为原始分辨率，而DrawOpaqueObjects绑定的Buffer使用低分辨率，分辨率不一致导致SSAO shadow效果异常。

**处理步骤**

* 仅支持渲染线程的游戏引擎处理步骤

  + **方案1**：调整渲染管线，将SSAO作为“后处理”，SSAO不受DrawOpaqueObjects绑定的Buffer分辨率影响。

    在URP资产中勾选“After Opaque”：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4LsnTCl3T5-N5_knTTcbNg/zh-cn_image_0000002558605576.png?HW-CC-KV=V1&HW-CC-Date=20260429T053633Z&HW-CC-Expire=86400&HW-CC-Sign=AA1CAA6C52D11DFB34CFE4E589C8C9E2CC728222A7773E914359302386224360)
  + **方案2**：获取实时的ABR Buffer分辨率因子，并根据Buffer分辨率因子对相关渲染数据进行同步调整。

    SSAO的shader会根据scaledScreenParams参数进行计算，该变量与渲染分辨率相关，在集成ABR后，scaledScreenParams需要根据实时的ABR Buffer分辨率因子调整。

    对于团结引擎，可在ScriptableRenderer.cs的SetPerCameraShaderVariables函数中根据Buffer分辨率因子设置scaledScreenParams参数。

    ```
    1. void SetPerCameraShaderVariables(CommandBuffer cmd, ref CameraData cameraData, bool isTargetFlipped)
    2. {
    3. Camera camera = cameraData.camera;
    4. float scaledCameraWidth = (float)cameraData.cameraTargetDescriptor.width;
    5. float scaledCameraHeight = (float)cameraData.cameraTargetDescriptor.height;
    6. // scale为通过HMS_ABR_GetScale接口获取的ABR Buffer分辨率因子
    7. scaledCameraWidth *= scale;
    8. scaledCameraHeight *= scale;
    9. cmd.SetGlobalVector(ShaderPropertyId.scaledScreenParams, new Vector4(scaledCameraWidth, scaledCameraHeight, 1.0f + 1.0f / scaledCameraWidth, 1.0f + 1.0f / scaledCameraHeight));
    10. }
    ```
* 支持渲染线程、RHI线程的游戏引擎处理步骤

  对于同时支持渲染线程、RHI线程的游戏引擎，而且RHI线程延迟于渲染线程的场景，渲染线程通过[HMS\_ABR\_GetScale](../harmonyos-references/_graphics_accelerate.md#hms_abr_getscale)接口获取的ABR Buffer分辨率因子无法解决上述问题。

  对于该场景，渲染线程在Buffer渲染后调用[HMS\_ABR\_GetNextScale](../harmonyos-references/_graphics_accelerate.md#hms_abr_getnextscale)接口获取下一帧的ABR Buffer分辨率因子，并根据Buffer分辨率因子对相关渲染数据进行同步调整。

  ```
  1. // 在Buffer渲染后调用
  2. float scale = 1.0f;
  3. errorCode = HMS_ABR_GetNextScale(context_, &scale);
  4. if (errorCode != ABR_SUCCESS) {
  5. GOLOGE("HMS_ABR_GetNextScale execution failed, error code: %d.", errorCode);
  6. }

  8. // 根据Buffer分辨率因子对渲染数据进行同步调整
  9. void SetViewUniformParameters()
  10. {
  11. ViewUniformParameters.BufferSize.X = (int)(ViewUniformParameters.BufferSize.X * scale);
  12. ViewUniformParameters.BufferSize.Y = (int)(ViewUniformParameters.BufferSize.Y * scale);
  13. ViewUniformParameters.BufferInvSize.X /= scale;
  14. ViewUniformParameters.BufferInvSize.Y /= scale;
  15. }
  ```
