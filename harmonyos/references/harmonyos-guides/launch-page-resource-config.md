---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page-resource-config
title: 启动页资源分类配置
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 应用启动页的配置与使用 > 启动页资源分类配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c4e05b0907e158a7f5ef97c21684b4cccdf19fdc9de5ba8bbcd4edecc0e9fb27
---

启动页资源配置与其他资源配置相同，支持资源分类配置，可针对不同的场景配置不同资源，常用于在深色模式或不同设备类型上配置不同的启动页内容。

## 配置深色模式启动页

* 在API version 20之前，启动页深浅色模式仅支持跟随系统深浅色模式。
* 从API version 20开始，支持通过[增强启动页](launch-page-config.md#配置增强启动页)的startWindowColorModeType字段配置同进程下拉起的UIAbility的启动页深浅色模式跟随应用深浅色模式。对于未配置场景，启动页深浅色模式跟随系统深浅色模式。

以[配置增强启动页](launch-page-config.md#配置增强启动页)的背景色为例：startWindowBackgroundColor字段值为"$color:start\_window\_background"，按如下方式在resources目录下分别配置字段值对应的颜色值，即可对深色模式生效。其他字段配置方式与背景色相同，在resources目录中配置其字段值对应的资源即可。

1. 修改resources/base/element/color.json中，对应配置项start\_window\_background的颜色值，对应一般情况下的默认启动页背景色，示例如下：

   ```
   1. {
   2. "color": [
   3. {
   4. "name": "start_window_background",
   5. "value": "#FFFFFFFF"
   6. }
   7. ]
   8. }
   ```
2. 修改resources/dark/element/color.json中，对应配置项start\_window\_background的颜色值，对应深色模式下的默认启动页背景色，示例如下：

   ```
   1. {
   2. "color": [
   3. {
   4. "name": "start_window_background",
   5. "value": "#FF000000"
   6. }
   7. ]
   8. }
   ```

## 配置不同设备启动页

与深色模式类似，通过在resources目录新建car、tablet等资源目录，配置上述字段对应的资源，则可在对应设备上配置显示不同的启动页内容，参考[创建资源目录和资源文件](resource-categories-and-access.md#创建资源目录和资源文件)。

如未针对特定场景的启动页字段配置资源文件，则该场景下默认以base目录中的对应资源文件为准。
