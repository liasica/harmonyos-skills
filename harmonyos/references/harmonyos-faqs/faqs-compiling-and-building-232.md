---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-232
title: 编译构建时报错：权限错误问题汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建时报错：权限错误问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7058aa90e4c681923b07ab396d6a11b519cc064c7b3d2be386b2aa415c50e8d1
---

## 问题现象

**应用权限问题：**

* 场景一：应用中集成毕昇编译器，使用clang编译代码文件时报错找不到文件，调试时发现添加ohos.permission.READ\_WRITE\_USER\_FILE后正常，但是该权限无法申请，请问如何解决编译找不到文件的错误？
* 场景二：用SaveButton安全控件保存图片，用到createAsset，警告提示需要申请ohos.permission.WRITE\_IMAGEVIDEO。

**环境权限问题：**

* 场景三：无文件权限。
  + 问题1：复制文件失败。

    ```txt
    hvigor ERROR: EPERM: operation not permitted, copyfile 'D:\xxx\entry\src\main\ets\pages' -> 'D:\xxx\entry\build\default\intermediates\loader_out\default\ets\pages'
    ```
  + 问题2：传输文件失败。

    ```txt
    FileTransfer Failed: [Fail]Error opening file: operation not permitted
    ```
  + 问题3：移动字体文件失败。

    ```txt
    Tools execution failed.Error: remove file'E:\harmony_example\calendar-harmony\entry\build\default\intermediates\res\default\resources\rawfile\font\avenir_regular.ttf' failed, reason: Permission denied Detail: Please check the message from tools.avenir_regular.ttf
    ```
  + 问题4：文件被占用。

    ```txt
    hvigor ERROR: EBUSY: resource busy or locked, unlink xxx.abc
    ```

## 背景知识

[构建报错排查](../harmonyos-guides/ide-hvigor-faq.md)：提供如何使用日志记录以及常见问题和错误码，协助开发者快速解决编译阶段问题。

## 问题定位

* 场景一：[ohos.permission.READ\_WRITE\_USER\_FILE](../harmonyos-guides/restricted-permissions.md#ohospermissionread_write_user_file)允许应用访问并修改用户目录下的文件，是受限权限。排查代码发现，访问文件路径存在问题，未通过指定接口获取。
* 场景二：createAsset实际上从接口层面是需要权限的，只是SaveButton进行权限豁免，参考：[createAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#createasset)。
* 场景三：operation not permitted报错，文件操作失败。
  + 文件占用锁定：pages目录或其内部文件被其他进程占用（如IDE未释放/杀毒软件扫描）。
  + 权限不足：当前用户对目标缺乏读/写权限。
  + 路径冲突：特殊字符路径或超长路径触发Windows权限限制（常见于Windows系统）。

## 分析结论

* 场景一：访问文件路径错误。
* 场景二：权限实际被使用，仅通过特定组件豁免。
* 场景三：文件无操作权限。

## 修改建议

* 场景一：通过[Environment.getUserDocumentDir](../harmonyos-references/js-apis-file-environment.md#environmentgetuserdocumentdir)获取公共目录路径后再访问。
* 场景二：告警提示使用相关权限，如果确认无影响可忽略。
* 场景三：
  + 文件占用锁定：关闭占用进程或者重启设备。
  + 权限不足：
    - 右键文件选择属性，常规页签中取消勾选只读，常规中授予当前用户读写和执行权限（读写相关）。
    - 选择"完全磁盘访问权限"，在左侧的列表中，找到"完全磁盘访问权限"并点击，以此来手动为编译器授予完全访问权限（传输相关）。
  + 路径冲突：修改文件路径。
