---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-mv-gles
title: OpenGL ES平台
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 顶点标记 > OpenGL ES平台
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0c0b35cb8c5f30164819eba5d8fe222ff13b739e4d88b5d9d8be30097a1135d3
---

## 业务流程

基于OpenGL ES图形API平台，超帧顶点标记的主要业务流程如下：

* 增强模式运动估计原理

  开发阶段，开发者需要使用系统的图形驱动库提供的OpenGL ES接口，在期望被标记的物体绘制前后添加上开始标记指令和结束标记指令。运行阶段，基于OpenGL ES的Transform Feedback（变换反馈）特性，被标记的所有Draw Call处理的顶点数据将被缓存，再通过顶点匹配、运动估计、屏幕空间投影等过程，得到高精度运动向量，最终绘制出预测帧。运行阶段流程如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/tFSUxwFJSJufGnl77a1fgA/zh-cn_image_0000002589245015.png?HW-CC-KV=V1&HW-CC-Date=20260429T053625Z&HW-CC-Expire=86400&HW-CC-Sign=91405361FD4D120496FFD9B79CD54354AB820461EE8D1F0053178D7F46112E3A)
* 顶点标记原则

  被标记的物体能在运动估计阶段得到更高精度的运动向量图（MV，Motion Vector），但需要付出额外的性能代价，开发者需要在这之间做出平衡。**建议只标记画面中相对场景运动的物体**，因为相对场景运动的物体的顶点数量较少，但运动预测却最为困难，这样的标记方式能以少量的性能代价换取较明显的超帧画质收益。

  注意

  **请在会影响最终深度缓冲区写入的渲染Pass中，标记对应的Draw Call**。比如对于延迟管线，建议在gbuffer pass中标记；对于有pre depth的前向管线，建议在pre depth pass标记；对于无pre depth的前向管线，建议在base pass（也叫forward pass）中进行标记。并且注意，不要在生成shadowmap pass中的动态物体Draw Call进行标记。

## 开发步骤

本节阐述基于OpenGL ES图形API平台的超帧调用示例。详细代码请参考[图形开发Sample（超帧GLES）](https://gitcode.com/harmonyos_samples/frame-generation-gles-samplecode-clientdemo-cpp)。

1. 设置meta-data。设置GraphicsAccelerateKit\_VBMV为true，来通知系统支持顶点标记。

   ```
   1. {
   2. "module": {
   3. /*
   4. 其他的配置项
   5. ...
   6. */
   7. "metadata": [
   8. {
   9. "name": "GraphicsAccelerateKit_VBMV",
   10. "value": "true"
   11. }
   12. ]
   13. }
   14. }
   ```
2. 定义glHint扩展宏，标记需要得到更高精度MV的物体顶点。

   ```
   1. // 引用头文件
   2. #include <GLES3/gl32.h>
   3. // 定义glHint的拓展宏
   4. #define GL_DRAWCALL_HINT 0x8193
   5. #define GL_START 0x8194
   6. #define GL_END 0x8195

   8. // 声明动态物体的顶点数量
   9. GLsizei vertices;

   11. // 循环渲染帧
   12. void UpdateAndRenderOpaqueScene()
   13. {
   14. // Do something prepare ...
   15. glHint(GL_DRAWCALL_HINT, GL_START);       // 绘制动态物体前，开始记录顶点数据
   16. glDrawArrays(GL_TRIANGLES, 0, vertices);  // 被记录的动态物体顶点绘制
   17. glHint(GL_DRAWCALL_HINT, GL_END);         // 绘制动态物体后，结束记录顶点数据
   18. // Do something post process...
   19. }
   ```

   说明

   宏名GL\_DRAWCALL\_HINT 、GL\_START 、GL\_END均为HarmonyOS 5.0.x及以上版本独有的拓展宏，且仅在马良910 GPU及以上的手机平板设备上被HarmonyOS的系统实现和定义，在其他芯片平台上运行时标记无效，但不会影响应用的正常运行。
