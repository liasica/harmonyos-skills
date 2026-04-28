---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-errorcode
title: 错误码
breadcrumb: 指南 > 优化应用性能 > 附录 > 错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:67aac1b1536667c284b101a789fd57dcc72fcf44f61a11f9d731ecc1fe01ac8d
---

## 00701101 应用拉起失败

**错误信息**

Failed to start this app. If the app is of the release type, make sure you have enabled it to be started. For more details, see the logs.

**错误描述**

应用无法正常拉起。

**可能原因**

录制Launch等模板时会自动拉起应用，应用在拉起过程中设备断开连接。

**处理步骤**

重新连接设备后再次录制。

## 00701102 应用启动失败

**错误信息**

App not started correctly. Start a new session and try again.

**错误描述**

应用程序启动失败。

**可能原因**

录制Launch模板时，手动点击应用图标启动应用过程中，设备断开连接。

**处理步骤**

重新连接设备后再次录制。

## 00701202 数据文件导入失败

**错误信息**

Failed to import data file. Please check file version or storage space.

**错误描述**

数据文件导入失败，请检查数据文件版本和磁盘空间。

**可能原因**

1. 版本不匹配。导入的数据文件版本与当前使用的DevEco Studio版本不匹配。
2. 磁盘空间不足。

**处理步骤**

1. 尝试使用数据文件导出时或更高版本的DevEco Studio导入数据。
2. 清理磁盘空间。

## 00702101 离线符号解析失败

**错误信息**

Failed to import offline symbols. Verify the offline symbol files.

**错误描述**

离线符号解析失败。

**可能原因**

导入的so库与抓取到的so库不匹配。

**处理步骤**

导入对应的携带符号表信息的so库进行解析。

## 00702102 导入文件大小超出限制

**错误信息**

The imported file exceeds maximum size limit.

**错误描述**

导入文件大小超出限制。

**可能原因**

导入的文件过大。

**处理步骤**

重新导入符合大小限制的文件。

## 00702103 导入的.jsleaklist文件格式不正确

**错误信息**

Invalid files: {0}.

**错误描述**

导入的.jsleaklist文件格式不正确。

**可能原因**

导入的.jsleaklist文件格式不正确。

**处理步骤**

导入格式正确的.jsleaklist文件。

## 00702104 导入的.jsleaklist文件与导入的 .heapsnapshot或.rawheap文件不匹配

**错误信息**

Unmatched files: {0}.

**错误描述**

导入的.jsleaklist文件与导入的 .heapsnapshot或.rawheap文件不匹配。

**可能原因**

导入的.jsleaklist文件与导入的 .heapsnapshot或.rawheap文件不匹配。

**处理步骤**

导入与.heapsnapshot 或 .rawheap文件匹配的.jsleaklist文件。

## 00702106 CodeGenie授权登录已过期

**错误信息**

The authentication information has expired. Please sign in again.

**错误描述**

CodeGenie授权登录已过期，请重新登录。

**可能原因**

CodeGenie授权登录已过期。

**处理步骤**

重新登录。

## 00702201 离线符号解析失败

**错误信息**

Failed to import offline symbols.

**错误描述**

离线符号解析失败。

**可能原因**

导入未携带符号表信息的so库。

**处理步骤**

导入正确携带符号表信息的so库。

## 00702203 无法启动录制

**错误信息**

Since no Running Application is selected, recording cannot be started. Please select a Running Application first.

**错误描述**

要调测的应用处于非运行状态，无法启动录制。请先选择一个运行中的应用。

**可能原因**

调测应用未运行。

**处理步骤**

调测的应用开始运行后，再启动录制。

## 00702204 点击跳转按钮失败

**错误信息**

The corresponding slice is not available in the current view.

**错误描述**

点击跳转按钮失败。

**可能原因**

跳转的目标泳道在当前文件中不存在。

**处理步骤**

重新录制，录制文件中需包含跳转的目标泳道。

## 00702205 创建的会话达到了会话个数的最大限制

**错误信息**

Maximum number of sessions reached. Delete some sessions and try again.

**错误描述**

创建的会话达到了会话个数的最大限制，请清理会话。

**可能原因**

创建的会话达到了会话个数的最大限制。

**处理步骤**

清理创建的会话。

## 00702206 泳道不存在

**错误信息**

The lane does not exist. Please upgrade the DevEco Studio.

**错误描述**

导入的数据文件中包含的泳道在前版本的DevEco Studio中不存在。

**可能原因**

版本不匹配。导入的数据文件中包含的泳道在当前版本的DevEco Studio中不存在。

**处理步骤**

尝试使用数据文件导出时或更高版本的DevEco Studio导入数据。

## 00702208 设备锁屏

**错误信息**

Unlock the device and try again.

**错误描述**

解锁被调优的设备后，重新录制。

**可能原因**

设备设置了锁屏密码，且处于锁屏状态，录制Launch等模板时应用无法被拉起。

**处理步骤**

解锁设备后重新录制。

## 00702209 不能同时导入.heapsnapshot和.rawheap文件

**错误信息**

The .heapsnapshot and .rawheap files cannot be imported at the same time.

**错误描述**

不能同时导入.heapsnapshot和.rawheap文件。

**可能原因**

同时导入.heapsnapshot 和.rawheap 文件。

**处理步骤**

.heapsnapshot 文件和.rawheap 文件分开导入。

## 00702210 数据导出时，没有足够的权限访问需要保存文件的目录

**错误信息**

The selected directory has no permissions.

**错误描述**

没有足够的权限访问需要保存文件的目录。

**可能原因**

数据导出时，没有足够的权限访问需要保存文件的目录。

**处理步骤**

选择一个有权限访问的目录进行数据导出。

## 00702211 导入的文件数量超出限制

**错误信息**

Only a single .insight/.ftrace/.htrace/.nas/.txt/.perfdata/.data/.sys file or 1-10 .heapsnapshot/.jsleaklist/.rawheap files are allowed to be imported.

**错误描述**

只允许导入一个.insight/.ftrace/.htrace/.nas/.txt/.perfdata/.data/.sys文件，或者导入10个以内的.heapsnapshot/.jsleaklist/.rawheap文件。

**可能原因**

导入的文件数量超出限制。

**处理步骤**

导入单个.insight/.ftrace/.htrace/.nas/.txt/.perfdata/.data/.sys文件，或者导入10个以内的.heapsnapshot/.jsleaklist/.rawheap文件。

## 00702212 导出文件时文件名使用了不允许的字符

**错误信息**

Make sure the file name does not contain the following characters:\* : ? " < > |

**错误描述**

请确保文件名不包含以下字符： \* : ? " < > |。

**可能原因**

导出文件时，文件名使用了不允许的字符，如 \* : ? " < > |。

**处理步骤**

导出文件时，文件名中不包含以下字符：\* : ? " < > |。

## 00702213 导出文件时文件名超过238个字符

**错误信息**

Make sure that the file name does not exceed 238 characters.

**错误描述**

确保文件名不超过238个字符。

**可能原因**

导出文件时，文件名超过238个字符的限制。

**处理步骤**

导出文件时，文件名不超过238个字符。

## 00702214 保存路径不存在

**错误信息**

Invalid save path: {0}

**错误描述**

保存路径不存在。

**可能原因**

保存路径不存在。

**处理步骤**

确认保存路径存在后，再保存。

## 00703201 录制文件过大导致解析失败

**错误信息**

The recording file is too large and cannot be parsed. Restart a new recording session with shorter duration.

**错误描述**

因录制文件较大，导致解析失败。请减少录制时间重新录制。

**可能原因**

录制文件过大，导致解析失败。

**处理步骤**

减少录制时间，重新录制。

## 00703202 Profiler分配的内存已超出限制

**错误信息**

The memory allocated to Profiler has reached the upper limit. To maintain normal operation, consider increasing the heap size.

**错误描述**

Profiler分配的内存已超出限制，请考虑增加可用堆内存容量以确保正常运行。

**可能原因**

Profiler分配的内存已达到上限，导致无法正常运行。

**处理步骤**

在DevEco Studio的配置文件中手动修改虚拟机可使用的最大内存，具体请参考[内存占用率过高导致DevEco Studio无法正常运行](../harmonyos-faqs/faqs-profiler-3.md)。

## 00703204 录制的数据与当前DevEco Studio窗口打开的源码工程不匹配

**错误信息**

Unable to navigate to source code. Make sure the SymbolTable file exists in the corresponding module directory and the recorded data matches the source code project, and then rebuild the project.

**错误描述**

录制的数据与当前DevEco Studio窗口打开的源码工程不匹配。

**可能原因**

录制的数据与当前DevEco Studio窗口打开的源码工程不匹配，导致无法正确跳转到源代码。

**处理步骤**

检查被录制的应用与当前DevEco Studio窗口打开的应用工程是否匹配。

## 00703205 跳转至对应工程源码失败

**错误信息**

Source file not found.

**错误描述**

跳转至对应工程源码失败。

**可能原因**

录制的数据需要跳转的源码不存在。

**处理步骤**

检查被录制的应用与当前DevEco Studio窗口打开的应用工程是否匹配。

## 00703301 结束录制失败

**错误信息**

Failed to stop the session.

**错误描述**

结束录制失败。

**可能原因**

插件在停止录制过程中出现错误，导致无法正常结束录制。

**处理步骤**

本次录制结束后，需重新录制。
