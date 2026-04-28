---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileio
title: @ohos.fileio (文件管理)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > 已停止维护的接口 > @ohos.fileio (文件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec13ad36faf0ad436f24f0c32b01a9d7e61072030e971f6d072ad2bcd404fa53
---

该模块提供文件存储管理能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块从API version 9开始废弃，建议使用[@ohos.file.fs](js-apis-file-fs.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import fileio from '@ohos.fileio';
```

## 使用说明

PhonePC/2in1TabletTVWearable

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import window from '@ohos.window';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let context = this.context;
7. let pathDir = context.filesDir;
8. }
9. }
```

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：[应用上下文Context-获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)

## fileio.stat

PhonePC/2in1TabletTVWearable

stat(path: string): Promise<Stat>

获取文件信息，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.stat](js-apis-file-fs.md#fileiostat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stat](js-apis-fileio.md#stat)> | Promise对象。返回文件的具体信息。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "test.txt";
3. fileio.stat(filePath).then((stat: fileio.Stat) => {
4. console.info("getFileInfo succeed, the size of file is " + stat.size);
5. }).catch((err: BusinessError) => {
6. console.error("getFileInfo failed with error:" + err);
7. });
```

## fileio.stat

PhonePC/2in1TabletTVWearable

stat(path: string, callback: AsyncCallback<Stat>): void

获取文件信息，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.stat](js-apis-file-fs.md#fileiostat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |
| callback | AsyncCallback<[Stat](js-apis-fileio.md#stat)> | 是 | 异步获取文件的信息之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. fileio.stat(pathDir, (err: BusinessError, stat: fileio.Stat) => {
3. // example code in Stat
4. });
```

## fileio.statSync

PhonePC/2in1TabletTVWearable

statSync(path: string): Stat

以同步方法获取文件的信息。

说明

从API version 9开始废弃，请使用[fileIo.statSync](js-apis-file-fs.md#fileiostatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待获取文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stat](js-apis-fileio.md#stat) | 表示文件的具体信息。 |

**示例：**

```
1. let stat = fileio.statSync(pathDir);
2. // example code in Stat
```

## fileio.opendir

PhonePC/2in1TabletTVWearable

opendir(path: string): Promise<Dir>

打开文件目录，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Dir](js-apis-fileio.md#dir)> | Promise对象。返回Dir对象。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let dirPath = pathDir + "/testDir";
3. fileio.opendir(dirPath).then((dir: fileio.Dir) => {
4. console.info("opendir succeed");
5. }).catch((err: BusinessError) => {
6. console.error("opendir failed with error:" + err);
7. });
```

## fileio.opendir

PhonePC/2in1TabletTVWearable

opendir(path: string, callback: AsyncCallback<Dir>): void

打开文件目录，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |
| callback | AsyncCallback<[Dir](js-apis-fileio.md#dir)> | 是 | 异步打开文件目录之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. fileio.opendir(pathDir, (err: BusinessError, dir: fileio.Dir) => {
3. // example code in Dir struct
4. // use read/readSync/close
5. });
```

## fileio.opendirSync

PhonePC/2in1TabletTVWearable

opendirSync(path: string): Dir

以同步方法打开文件目录。

说明

从API version 9开始废弃，请使用[fileIo.listFileSync](js-apis-file-fs.md#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Dir](js-apis-fileio.md#dir) | 返回Dir对象。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. // example code in Dir struct
3. // use read/readSync/close
```

## fileio.access

PhonePC/2in1TabletTVWearable

access(path: string, mode?: number): Promise<void>

检查当前进程是否可访问某文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.access](js-apis-file-fs.md#fileioaccess)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。  确认当前进程是否具有对应权限：  - 0：确认文件是否存在。  - 1：确认当前进程是否具有可执行权限。  - 2：确认当前进程是否具有写权限。  - 4：确认当前进程是否具有读权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.access(filePath).then(() => {
4. console.info("access succeed");
5. }).catch((err: BusinessError) => {
6. console.error("access failed with error:" + err);
7. });
```

## fileio.access

PhonePC/2in1TabletTVWearable

access(path: string, mode?: number, callback: AsyncCallback<void>): void

检查当前进程是否可访问某文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.access](js-apis-file-fs.md#fileioaccess-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。  确认当前进程是否具有对应权限：  - 0：确认文件是否存在。  - 1：确认当前进程是否具有可执行权限。  - 2：确认当前进程是否具有写权限。  - 4：确认当前进程是否具有读权限。 |
| callback | AsyncCallback<void> | 是 | 异步检查当前进程是否可访问某文件之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.access(filePath, (err: BusinessError) => {
4. // do something
5. });
```

## fileio.accessSync

PhonePC/2in1TabletTVWearable

accessSync(path: string, mode?: number): void

以同步方法检查当前进程是否可访问某文件。

说明

从API version 9开始废弃，请使用[fileIo.accessSync](js-apis-file-fs.md#fileioaccesssync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待访问文件的应用沙箱路径。 |
| mode | number | 否 | 访问文件时的选项，可给定如下选项，以按位或的方式使用多个选项，默认给定0。  确认当前进程是否具有对应权限：  - 0：确认文件是否存在。  - 1：确认当前进程是否具有可执行权限。  - 2：确认当前进程是否具有写权限。  - 4：确认当前进程是否具有读权限。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. try {
4. fileio.accessSync(filePath);
5. } catch(error) {
6. let err: BusinessError = error as BusinessError;
7. console.error("accessSync failed with error:" + err);
8. }
```

## fileio.close7+

PhonePC/2in1TabletTVWearable

close(fd: number): Promise<void>

关闭文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.close](js-apis-file-fs.md#fileioclose)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.close(fd).then(() => {
5. console.info("close file succeed");
6. }).catch((err: BusinessError) => {
7. console.error("close file failed with error:" + err);
8. });
```

## fileio.close7+

PhonePC/2in1TabletTVWearable

close(fd: number, callback: AsyncCallback<void>): void

关闭文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.close](js-apis-file-fs.md#fileioclose-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步关闭文件之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.close(fd, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.closeSync

PhonePC/2in1TabletTVWearable

closeSync(fd: number): void

以同步方法关闭文件。

说明

从API version 9开始废弃，请使用[fileIo.closeSync](js-apis-file-fs.md#fileioclosesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. fileio.closeSync(fd);
```

## fileio.copyFile

PhonePC/2in1TabletTVWearable

copyFile(src: string|number, dest: string|number, mode?: number): Promise<void>

复制文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.copyFile](js-apis-file-fs.md#fileiocopyfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcPath = pathDir + "srcDir/test.txt";
3. let dstPath = pathDir + "dstDir/test.txt";
4. fileio.copyFile(srcPath, dstPath).then(() => {
5. console.info("copyFile succeed");
6. }).catch((err: BusinessError) => {
7. console.error("copyFile failed with error:" + err);
8. });
```

## fileio.copyFile

PhonePC/2in1TabletTVWearable

copyFile(src: string|number, dest: string|number, mode: number, callback: AsyncCallback<void>): void

复制文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.copyFile](js-apis-file-fs.md#fileiocopyfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcPath = pathDir + "srcDir/test.txt";
3. let dstPath = pathDir + "dstDir/test.txt";
4. fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.copyFileSync

PhonePC/2in1TabletTVWearable

copyFileSync(src: string|number, dest: string|number, mode?: number): void

以同步方法复制文件。

说明

从API version 9开始废弃，请使用[fileIo.copyFileSync](js-apis-file-fs.md#fileiocopyfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string|number | 是 | 待复制文件的路径或待复制文件的描述符。 |
| dest | string|number | 是 | 目标文件路径或目标文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**示例：**

```
1. let srcPath = pathDir + "srcDir/test.txt";
2. let dstPath = pathDir + "dstDir/test.txt";
3. fileio.copyFileSync(srcPath, dstPath);
```

## fileio.mkdir

PhonePC/2in1TabletTVWearable

mkdir(path: string, mode?: number): Promise<void>

创建目录，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.mkdir](js-apis-file-fs.md#fileiomkdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。  - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let dirPath = pathDir + '/testDir';
3. fileio.mkdir(dirPath).then(() => {
4. console.info("mkdir succeed");
5. }).catch((error: BusinessError) => {
6. console.error("mkdir failed with error:" + error);
7. });
```

## fileio.mkdir

PhonePC/2in1TabletTVWearable

mkdir(path: string, mode: number, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.mkdir](js-apis-file-fs.md#fileiomkdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。  - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let dirPath = pathDir + '/testDir';
3. fileio.mkdir(dirPath, (err: BusinessError) => {
4. console.info("mkdir succeed");
5. });
```

## fileio.mkdirSync

PhonePC/2in1TabletTVWearable

mkdirSync(path: string, mode?: number): void

以同步方法创建目录。

说明

从API version 9开始废弃，请使用[fileIo.mkdirSync](js-apis-file-fs.md#fileiomkdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待创建目录的应用沙箱路径。 |
| mode | number | 否 | 创建目录的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o775。  - 0o775：所有者具有读、写及可执行权限，其余用户具有读及可执行权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**示例：**

```
1. let dirPath = pathDir + '/testDir';
2. fileio.mkdirSync(dirPath);
```

## fileio.open7+

PhonePC/2in1TabletTVWearable

open(path: string, flags?: number, mode?: number): Promise<number>

打开文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.open](js-apis-file-fs.md#fileioopen)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：  - 0o0：只读打开。  - 0o1：只写打开。  - 0o2：读写打开。  同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：  - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。  - 0o200：如果追加了0o100选项，且文件已经存在，则出错。  - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - 0o2000：以追加方式打开，后续写将追加到文件末尾。  - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - 0o200000：如果path不指向目录，则出错。  - 0o400000：如果path指向符号链接，则出错。  - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。  - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回打开文件的文件描述符。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.open(filePath, 0o1, 0o0200).then((number: number) => {
4. console.info("open file succeed");
5. }).catch((err: BusinessError) => {
6. console.error("open file failed with error:" + err);
7. });
```

## fileio.open7+

PhonePC/2in1TabletTVWearable

open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void

打开文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.open](js-apis-file-fs.md#fileioopen-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：  - 0o0：只读打开。  - 0o1：只写打开。  - 0o2：读写打开。  同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：  - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。  - 0o200：如果追加了0o100选项，且文件已经存在，则出错。  - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - 0o2000：以追加方式打开，后续写将追加到文件末尾。  - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - 0o200000：如果path不指向目录，则出错。  - 0o400000：如果path指向符号链接，则出错。  - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。  - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |
| callback | AsyncCallback<number> | 是 | 异步打开文件之后的回调，返回打开文件的文件描述符。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.open(filePath, 0, (err: BusinessError, fd: number) => {
4. // do something
5. });
```

## fileio.openSync

PhonePC/2in1TabletTVWearable

openSync(path: string, flags?: number, mode?: number): number

以同步方法打开文件。

说明

从API version 9开始废弃，请使用[fileIo.openSync](js-apis-file-fs.md#fileioopensync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| flags | number | 否 | 打开文件的选项，必须指定如下选项中的一个，默认以只读方式打开：  - 0o0：只读打开。  - 0o1：只写打开。  - 0o2：读写打开。  同时，也可给定如下选项，以按位或的方式追加，默认不给定任何额外选项：  - 0o100：若文件不存在，则创建文件。使用该选项时必须指定第三个参数 mode。  - 0o200：如果追加了0o100选项，且文件已经存在，则出错。  - 0o1000：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - 0o2000：以追加方式打开，后续写将追加到文件末尾。  - 0o4000：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - 0o200000：如果path不指向目录，则出错。  - 0o400000：如果path指向符号链接，则出错。  - 0o4010000：以同步IO的方式打开文件。 |
| mode | number | 否 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限，默认给定0o660。  - 0o660：所有者具有读、写权限，所有用户组具有读、写权限。  - 0o640：所有者具有读、写权限，所有用户组具有读权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。  创建出的文件权限受umask影响，umask随进程启动确定，其修改当前不开放。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 打开文件的文件描述符。 |

## fileio.read

PhonePC/2in1TabletTVWearable

read(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): Promise<ReadOut>

从文件读取数据，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.read](js-apis-file-fs.md#fileioread)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。  - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReadOut](js-apis-fileio.md#readout)> | Promise对象。返回读取的结果。 |

## fileio.read

PhonePC/2in1TabletTVWearable

read(fd: number, buffer: ArrayBuffer, options: { offset?: number; length?: number; position?: number; }, callback: AsyncCallback<ReadOut>): void

从文件读取数据，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.read](js-apis-file-fs.md#fileioread-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，单位为Byte，即相对于缓冲区首地址的偏移。可选，默认为0。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<[ReadOut](js-apis-fileio.md#readout)> | 是 | 异步读取数据之后的回调。 |

## fileio.readSync

PhonePC/2in1TabletTVWearable

readSync(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): number

以同步方法从文件读取数据。

说明

从API version 9开始废弃，请使用[fileIo.readSync](js-apis-file-fs.md#fileioreadsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。  - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath, 0o2);
3. let buf = new ArrayBuffer(4096);
4. let num = fileio.readSync(fd, buf);
```

## fileio.rmdir7+

PhonePC/2in1TabletTVWearable

rmdir(path: string): Promise<void>

删除目录，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.rmdir](js-apis-file-fs.md#fileiormdir)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let dirPath = pathDir + '/testDir';
3. fileio.rmdir(dirPath).then(() => {
4. console.info("rmdir succeed");
5. }).catch((err: BusinessError) => {
6. console.error("rmdir failed with error:" + err);
7. });
```

## fileio.rmdir7+

PhonePC/2in1TabletTVWearable

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.rmdir](js-apis-file-fs.md#fileiormdir-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除目录之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let dirPath = pathDir + '/testDir';
3. fileio.rmdir(dirPath, (err: BusinessError) => {
4. // do something
5. console.info("rmdir succeed");
6. });
```

## fileio.rmdirSync7+

PhonePC/2in1TabletTVWearable

rmdirSync(path: string): void

以同步方法删除目录。

说明

从API version 9开始废弃，请使用[fileIo.rmdirSync](js-apis-file-fs.md#fileiormdirsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除目录的应用沙箱路径。 |

**示例：**

```
1. let dirPath = pathDir + '/testDir';
2. fileio.rmdirSync(dirPath);
```

## fileio.unlink

PhonePC/2in1TabletTVWearable

unlink(path: string): Promise<void>

删除文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.unlink](js-apis-file-fs.md#fileiounlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.unlink(filePath).then(() => {
4. console.info("remove file succeed");
5. }).catch((error: BusinessError) => {
6. console.error("remove file failed with error:" + error);
7. });
```

## fileio.unlink

PhonePC/2in1TabletTVWearable

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.unlink](js-apis-file-fs.md#fileiounlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除文件之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.unlink(filePath, (err: BusinessError) => {
4. console.info("remove file succeed");
5. });
```

## fileio.unlinkSync

PhonePC/2in1TabletTVWearable

unlinkSync(path: string): void

以同步方法删除文件。

说明

从API version 9开始废弃，请使用[fileIo.unlinkSync](js-apis-file-fs.md#fileiounlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待删除文件的应用沙箱路径。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. fileio.unlinkSync(filePath);
```

## fileio.write

PhonePC/2in1TabletTVWearable

write(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.write](js-apis-file-fs.md#fileiowrite)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
4. fileio.write(fd, "hello, world").then((number: number) => {
5. console.info("write data to file succeed and size is:" + number);
6. }).catch((err: BusinessError) => {
7. console.error("write data to file failed with error:" + err);
8. });
```

## fileio.write

PhonePC/2in1TabletTVWearable

write(fd: number, buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.write](js-apis-file-fs.md#fileiowrite-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<number> | 是 | 异步将数据写入完成后执行的回调函数。返回实际写入的长度，单位为Byte。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
4. fileio.write(fd, "hello, world", (err: BusinessError, bytesWritten: number) => {
5. if (bytesWritten) {
6. console.info("write data to file succeed and size is:" + bytesWritten);
7. }
8. });
```

## fileio.writeSync

PhonePC/2in1TabletTVWearable

writeSync(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入文件。

说明

从API version 9开始废弃，请使用[fileIo.writeSync](js-apis-file-fs.md#fileiowritesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
3. let num = fileio.writeSync(fd, "hello, world");
```

## fileio.hash

PhonePC/2in1TabletTVWearable

hash(path: string, algorithm: string): Promise<string>

计算文件的哈希值，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[hash.write](js-apis-file-hash.md#hashhash)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回文件的哈希值。表示为十六进制数字串，所有字母均大写。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.hash(filePath, "sha256").then((str: string) => {
4. console.info("calculate file hash succeed:" + str);
5. }).catch((err: BusinessError) => {
6. console.error("calculate file hash failed with error:" + err);
7. });
```

## fileio.hash

PhonePC/2in1TabletTVWearable

hash(path: string, algorithm: string, callback: AsyncCallback<string>): void

计算文件的哈希值，使用callback异步回调。

说明

从API version 9开始废弃，请使用[hash.write](js-apis-file-hash.md#hashhash-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待计算哈希值文件的应用沙箱路径。 |
| algorithm | string | 是 | 哈希计算采用的算法。可选 "md5"、"sha1" 或 "sha256"。建议采用安全强度更高的 "sha256"。 |
| callback | AsyncCallback<string> | 是 | 异步计算文件哈希操作之后的回调函数（其中给定文件哈希值表示为十六进制数字串，所有字母均大写）。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.hash(filePath, "sha256", (err: BusinessError, hashStr: string) => {
4. if (hashStr) {
5. console.info("calculate file hash succeed:" + hashStr);
6. }
7. });
```

## fileio.chmod7+

PhonePC/2in1TabletTVWearable

chmod(path: string, mode: number): Promise<void>

改变文件权限，使用Promise异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.chmod(filePath, 0o700).then(() => {
4. console.info("chmod succeed");
5. }).catch((err: BusinessError) => {
6. console.error("chmod failed with error:" + err);
7. });
```

## fileio.chmod7+

PhonePC/2in1TabletTVWearable

chmod(path: string, mode: number, callback: AsyncCallback<void>): void

改变文件权限，使用callback异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件权限之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.chmod(filePath, 0o700, (err: BusinessError) => {
4. // do something
5. });
```

## fileio.chmodSync7+

PhonePC/2in1TabletTVWearable

chmodSync(path: string, mode: number): void

以同步方法改变文件权限。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 所需变更权限的文件的应用沙箱路径。 |
| mode | number | 是 | 改变文件权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. fileio.chmodSync(filePath, 0o700);
```

## fileio.fstat7+

PhonePC/2in1TabletTVWearable

fstat(fd: number): Promise<Stat>

基于文件描述符获取文件状态信息，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.stat](js-apis-file-fs.md#fileiostat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stat](js-apis-fileio.md#stat)> | Promise对象。返回表示文件状态的具体信息。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fstat(fd).then((stat: fileio.Stat) => {
5. console.info("fstat succeed, the size of file is " + stat.size);
6. }).catch((err: BusinessError) => {
7. console.error("fstat failed with error:" + err);
8. });
```

## fileio.fstat7+

PhonePC/2in1TabletTVWearable

fstat(fd: number, callback: AsyncCallback<Stat>): void

基于文件描述符获取文件状态信息，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.stat](js-apis-file-fs.md#fileiostat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |
| callback | AsyncCallback<[Stat](js-apis-fileio.md#stat)> | 是 | 异步获取文件状态信息之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fstat(fd, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.fstatSync7+

PhonePC/2in1TabletTVWearable

fstatSync(fd: number): Stat

以同步方法基于文件描述符获取文件状态信息。

说明

从API version 9开始废弃，请使用[fileIo.statSync](js-apis-file-fs.md#fileiostatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待获取文件状态的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stat](js-apis-fileio.md#stat) | 表示文件状态的具体信息。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let stat = fileio.fstatSync(fd);
```

## fileio.ftruncate7+

PhonePC/2in1TabletTVWearable

ftruncate(fd: number, len?: number): Promise<void>

基于文件描述符截断文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.truncate](js-apis-file-fs.md#fileiotruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.ftruncate(fd, 5).then(() => {
5. console.info("truncate file succeed");
6. }).catch((err: BusinessError) => {
7. console.error("truncate file failed with error:" + err);
8. });
```

## fileio.ftruncate7+

PhonePC/2in1TabletTVWearable

ftruncate(fd: number, len?: number, callback: AsyncCallback<void>): void

基于文件描述符截断文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.truncate](js-apis-file-fs.md#fileiotruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. let len = 5;
5. fileio.ftruncate(fd, 5, (err: BusinessError) => {
6. // do something
7. });
```

## fileio.ftruncateSync7+

PhonePC/2in1TabletTVWearable

ftruncateSync(fd: number, len?: number): void

以同步方法基于文件描述符截断文件。

说明

从API version 9开始废弃，请使用[fileIo.truncateSync](js-apis-file-fs.md#fileiotruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待截断文件的文件描述符。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let len = 5;
4. fileio.ftruncateSync(fd, len);
```

## fileio.truncate7+

PhonePC/2in1TabletTVWearable

truncate(path: string, len?: number): Promise<void>

基于文件路径截断文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.truncate](js-apis-file-fs.md#fileiotruncate)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let len = 5;
4. fileio.truncate(filePath, len).then(() => {
5. console.info("truncate file succeed");
6. }).catch((err: BusinessError) => {
7. console.error("truncate file failed with error:" + err);
8. });
```

## fileio.truncate7+

PhonePC/2in1TabletTVWearable

truncate(path: string, len?: number, callback: AsyncCallback<void>): void

基于文件路径截断文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.truncate](js-apis-file-fs.md#fileiotruncate-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let len = 5;
4. fileio.truncate(filePath, len, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.truncateSync7+

PhonePC/2in1TabletTVWearable

truncateSync(path: string, len?: number): void

以同步方法基于文件路径截断文件。

说明

从API version 9开始废弃，请使用[fileIo.truncateSync](js-apis-file-fs.md#fileiotruncatesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待截断文件的应用沙箱路径。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let len = 5;
3. fileio.truncateSync(filePath, len);
```

## fileio.readText7+

PhonePC/2in1TabletTVWearable

readText(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.readText](js-apis-file-fs.md#fileioreadtext)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项：  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回读取文件的内容。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.readText(filePath).then((str: string) => {
4. console.info("readText succeed:" + str);
5. }).catch((err: BusinessError) => {
6. console.error("readText failed with error:" + err);
7. });
```

## fileio.readText7+

PhonePC/2in1TabletTVWearable

readText(filePath: string, options: { position?: number; length?: number; encoding?: string; }, callback: AsyncCallback<string>): void

基于文本方式读取文件（即直接读取文件的文本内容），使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.readText](js-apis-file-fs.md#fileioreadtext-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项：  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回读取文件的内容。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. class Option {
4. length: number = 4096;
5. position: number = 0;
6. encoding: string = 'utf-8';
7. }
8. let option = new Option();
9. option.position = 1;
10. option.encoding = 'utf-8';
11. fileio.readText(filePath, option, (err: BusinessError, str: string) => {
12. // do something
13. });
```

## fileio.readTextSync7+

PhonePC/2in1TabletTVWearable

readTextSync(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

说明

从API version 9开始废弃，请使用[fileIo.readTextSync](js-apis-file-fs.md#fileioreadtextsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 待读取文件的应用沙箱路径。 |
| options | Object | 否 | 支持如下选项：  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取文件的内容。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. class Option {
3. length: number = 4096;
4. position: number = 0;
5. encoding: string = 'utf-8';
6. }
7. let option = new Option();
8. option.position = 1;
9. option.length = 3;
10. let str = fileio.readTextSync(filePath, option);
```

## fileio.lstat7+

PhonePC/2in1TabletTVWearable

lstat(path: string): Promise<Stat>

获取链接信息，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.lstat](js-apis-file-fs.md#fileiolstat)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stat](js-apis-fileio.md#stat)> | promise对象，返回文件对象，表示文件的具体信息，详情见stat。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.lstat(filePath).then((stat: fileio.Stat) => {
4. console.info("get link status succeed, the size of file is" + stat.size);
5. }).catch((err: BusinessError) => {
6. console.error("get link status failed with error:" + err);
7. });
```

## fileio.lstat7+

PhonePC/2in1TabletTVWearable

lstat(path: string, callback: AsyncCallback<Stat>): void

获取链接信息，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.lstat](js-apis-file-fs.md#fileiolstat-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback<[Stat](js-apis-fileio.md#stat)> | 是 | 回调函数，返回文件的具体信息。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.lstat(filePath, (err: BusinessError, stat: fileio.Stat) => {
4. // do something
5. });
```

## fileio.lstatSync7+

PhonePC/2in1TabletTVWearable

lstatSync(path: string): Stat

以同步方法获取链接信息。

说明

从API version 9开始废弃，请使用[fileIo.lstatSync](js-apis-file-fs.md#fileiolstatsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目标文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stat](js-apis-fileio.md#stat) | 表示文件的具体信息。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stat = fileio.lstatSync(filePath);
```

## fileio.rename7+

PhonePC/2in1TabletTVWearable

rename(oldPath: string, newPath: string): Promise<void>

重命名文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.rename](js-apis-file-fs.md#fileiorename)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcFile = pathDir + "/test.txt";
3. let dstFile = pathDir + '/new.txt';
4. fileio.rename(srcFile, dstFile).then(() => {
5. console.info("rename succeed");
6. }).catch((err: BusinessError) => {
7. console.error("rename failed with error:" + err);
8. });
```

## fileio.rename7+

PhonePC/2in1TabletTVWearable

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.rename](js-apis-file-fs.md#fileiorename-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步重命名文件之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcFile = pathDir + "/test.txt";
3. let dstFile = pathDir + '/new.txt';
4. fileio.rename(srcFile, dstFile, (err: BusinessError) => {
5. });
```

## fileio.renameSync7+

PhonePC/2in1TabletTVWearable

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件。

说明

从API version 9开始废弃，请使用[fileIo.renameSync](js-apis-file-fs.md#fileiorenamesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 目标文件的当前应用沙箱路径。 |
| newPath | string | 是 | 目标文件的新应用沙箱路径。 |

**示例：**

```
1. let srcFile = pathDir + "/test.txt";
2. let dstFile = pathDir + '/new.txt';
3. fileio.renameSync(srcFile, dstFile);
```

## fileio.fsync7+

PhonePC/2in1TabletTVWearable

fsync(fd: number): Promise<void>

同步文件数据，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fsync](js-apis-file-fs.md#fileiofsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fsync(fd).then(() => {
5. console.info("sync data succeed");
6. }).catch((err: BusinessError) => {
7. console.error("sync data failed with error:" + err);
8. });
```

## fileio.fsync7+

PhonePC/2in1TabletTVWearable

fsync(fd: number, callback: AsyncCallback<void>): void

同步文件数据，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fsync](js-apis-file-fs.md#fileiofsync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件数据同步之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fsync(fd, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.fsyncSync7+

PhonePC/2in1TabletTVWearable

fsyncSync(fd: number): void

以同步方法同步文件数据。

说明

从API version 9开始废弃，请使用[fileIo.fsyncSync](js-apis-file-fs.md#fileiofsyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. fileio.fsyncSync(fd);
```

## fileio.fdatasync7+

PhonePC/2in1TabletTVWearable

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fdatasync](js-apis-file-fs.md#fileiofdatasync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fdatasync(fd).then(() => {
5. console.info("sync data succeed");
6. }).catch((err: BusinessError) => {
7. console.error("sync data failed with error:" + err);
8. });
```

## fileio.fdatasync7+

PhonePC/2in1TabletTVWearable

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fdatasync](js-apis-file-fs.md#fileiofdatasync-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件内容数据同步之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fdatasync (fd, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.fdatasyncSync7+

PhonePC/2in1TabletTVWearable

fdatasyncSync(fd: number): void

以同步方法实现文件内容数据同步。

说明

从API version 9开始废弃，请使用[fileIo.fdatasyncSync](js-apis-file-fs.md#fileiofdatasyncsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待同步文件的文件描述符。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let stat = fileio.fdatasyncSync(fd);
```

## fileio.symlink7+

PhonePC/2in1TabletTVWearable

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.symlink](js-apis-file-fs.md#fileiosymlink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcFile = pathDir + "/test.txt";
3. let dstFile = pathDir + '/test';
4. fileio.symlink(srcFile, dstFile).then(() => {
5. console.info("symlink succeed");
6. }).catch((err: BusinessError) => {
7. console.error("symlink failed with error:" + err);
8. });
```

## fileio.symlink7+

PhonePC/2in1TabletTVWearable

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.symlink](js-apis-file-fs.md#fileiosymlink-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建符号链接信息之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let srcFile = pathDir + "/test.txt";
3. let dstFile = pathDir + '/test';
4. fileio.symlink(srcFile, dstFile, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.symlinkSync7+

PhonePC/2in1TabletTVWearable

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

说明

从API version 9开始废弃，请使用[fileIo.symlinkSync](js-apis-file-fs.md#fileiosymlinksync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**示例：**

```
1. let srcFile = pathDir + "/test.txt";
2. let dstFile = pathDir + '/test';
3. fileio.symlinkSync(srcFile, dstFile);
```

## fileio.chown7+

PhonePC/2in1TabletTVWearable

chown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，使用Promise异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID（UserID）。 |
| gid | number | 是 | 新的GID（GroupID）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let stat = fileio.statSync(filePath);
4. fileio.chown(filePath, stat.uid, stat.gid).then(() => {
5. console.info("chown succeed");
6. }).catch((err: BusinessError) => {
7. console.error("chown failed with error:" + err);
8. });
```

## fileio.chown7+

PhonePC/2in1TabletTVWearable

chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，使用callback异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let stat = fileio.statSync(filePath)
4. fileio.chown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.chownSync7+

PhonePC/2in1TabletTVWearable

chownSync(path: string, uid: number, gid: number): void

以同步的方法基于文件路径改变文件所有者。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待改变文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stat = fileio.statSync(filePath)
3. fileio.chownSync(filePath, stat.uid, stat.gid);
```

## fileio.mkdtemp7+

PhonePC/2in1TabletTVWearable

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.mkdtemp](js-apis-file-fs.md#fileiomkdtemp)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回生成的唯一目录路径。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. fileio.mkdtemp(pathDir + "/XXXXXX").then((pathDir: string) => {
3. console.info("mkdtemp succeed:" + pathDir);
4. }).catch((err: BusinessError) => {
5. console.error("mkdtemp failed with error:" + err);
6. });
```

## fileio.mkdtemp7+

PhonePC/2in1TabletTVWearable

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.mkdtemp](js-apis-file-fs.md#fileiomkdtemp-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |
| callback | AsyncCallback<string> | 是 | 异步创建临时目录之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. fileio.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
3. // do something
4. });
```

## fileio.mkdtempSync7+

PhonePC/2in1TabletTVWearable

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

说明

从API version 9开始废弃，请使用[fileIo.mkdtempSync](js-apis-file-fs.md#fileiomkdtempsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 产生的唯一目录路径。 |

**示例：**

```
1. let res = fileio.mkdtempSync(pathDir + "/XXXXXX");
```

## fileio.fchmod7+

PhonePC/2in1TabletTVWearable

fchmod(fd: number, mode: number): Promise<void>

基于文件描述符改变文件权限，使用Promise异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. let mode: number = 0o700;
5. fileio.fchmod(fd, mode).then(() => {
6. console.info("chmod succeed");
7. }).catch((err: BusinessError) => {
8. console.error("chmod failed with error:" + err);
9. });
```

## fileio.fchmod7+

PhonePC/2in1TabletTVWearable

fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件权限，使用callback异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件权限之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. let mode: number = 0o700;
5. fileio.fchmod(fd, mode, (err: BusinessError) => {
6. // do something
7. });
```

## fileio.fchmodSync7+

PhonePC/2in1TabletTVWearable

fchmodSync(fd: number, mode: number): void

以同步方法基于文件描述符改变文件权限。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| mode | number | 是 | 若创建文件，则指定文件的权限，可给定如下权限，以按位或的方式追加权限。  - 0o700：所有者具有读、写及可执行权限。  - 0o400：所有者具有读权限。  - 0o200：所有者具有写权限。  - 0o100：所有者具有可执行权限。  - 0o070：所有用户组具有读、写及可执行权限。  - 0o040：所有用户组具有读权限。  - 0o020：所有用户组具有写权限。  - 0o010：所有用户组具有可执行权限。  - 0o007：其余用户具有读、写及可执行权限。  - 0o004：其余用户具有读权限。  - 0o002：其余用户具有写权限。  - 0o001：其余用户具有可执行权限。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let mode: number = 0o700;
4. fileio.fchmodSync(fd, mode);
```

## fileio.createStream7+

PhonePC/2in1TabletTVWearable

createStream(path: string, mode: string): Promise<Stream>

基于文件路径打开文件流，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.createStream](js-apis-file-fs.md#fileiocreatestream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stream](js-apis-fileio.md#stream)> | Promise对象。返回文件流的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.createStream(filePath, "r+").then((stream: fileio.Stream) => {
4. console.info("createStream succeed");
5. }).catch((err: BusinessError) => {
6. console.error("createStream failed with error:" + err);
7. });
```

## fileio.createStream7+

PhonePC/2in1TabletTVWearable

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径打开文件流，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.createStream](js-apis-file-fs.md#fileiocreatestream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<[Stream](js-apis-fileio.md#stream)> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. fileio.createStream(filePath, "r+", (err: BusinessError, stream: fileio.Stream) => {
4. // do something
5. });
```

## fileio.createStreamSync7+

PhonePC/2in1TabletTVWearable

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径打开文件流。

说明

从API version 9开始废弃，请使用[fileIo.createStreamSync](js-apis-file-fs.md#fileiocreatestreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stream](js-apis-fileio.md#stream) | 返回文件流的结果。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let ss = fileio.createStreamSync(filePath, "r+");
```

## fileio.fdopenStream7+

PhonePC/2in1TabletTVWearable

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fdopenStream](js-apis-file-fs.md#fileiofdopenstream)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stream](js-apis-fileio.md#stream)> | Promise对象。返回文件流的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fdopenStream(fd, "r+").then((stream: fileio.Stream) => {
5. console.info("openStream succeed");
6. }).catch((err: BusinessError) => {
7. console.error("openStream failed with error:" + err);
8. });
```

## fileio.fdopenStream7+

PhonePC/2in1TabletTVWearable

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.fdopenStream](js-apis-file-fs.md#fileiofdopenstream-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<[Stream](js-apis-fileio.md#stream)> | 是 | 异步打开文件流之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. fileio.fdopenStream(fd, "r+", (err: BusinessError, stream: fileio.Stream) => {
5. // do something
6. });
```

## fileio.fdopenStreamSync7+

PhonePC/2in1TabletTVWearable

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。

说明

从API version 9开始废弃，请使用[fileIo.fdopenStreamSync](js-apis-file-fs.md#fileiofdopenstreamsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待打开文件的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stream](js-apis-fileio.md#stream) | 返回文件流的结果。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let ss = fileio.fdopenStreamSync(fd, "r+");
```

## fileio.fchown7+

PhonePC/2in1TabletTVWearable

fchown(fd: number, uid: number, gid: number): Promise<void>

基于文件描述符改变文件所有者，使用Promise异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. let stat = fileio.statSync(filePath);
5. fileio.fchown(fd, stat.uid, stat.gid).then(() => {
6. console.info("chown succeed");
7. }).catch((err: BusinessError) => {
8. console.error("chown failed with error:" + err);
9. });
```

## fileio.fchown7+

PhonePC/2in1TabletTVWearable

fchown(fd: number, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件描述符改变文件所有者，使用callback异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let fd = fileio.openSync(filePath);
4. let stat = fileio.statSync(filePath);
5. fileio.fchown(fd, stat.uid, stat.gid, (err: BusinessError) => {
6. // do something
7. });
```

## fileio.fchownSync7+

PhonePC/2in1TabletTVWearable

fchownSync(fd: number, uid: number, gid: number): void

以同步方法基于文件描述符改变文件所有者。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待改变文件的文件描述符。 |
| uid | number | 是 | 文件所有者的UID。 |
| gid | number | 是 | 文件所有组的GID。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let fd = fileio.openSync(filePath);
3. let stat = fileio.statSync(filePath);
4. fileio.fchownSync(fd, stat.uid, stat.gid);
```

## fileio.lchown7+

PhonePC/2in1TabletTVWearable

lchown(path: string, uid: number, gid: number): Promise<void>

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是符号链接所指向的实际文件，使用Promise异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let stat = fileio.statSync(filePath);
4. fileio.lchown(filePath, stat.uid, stat.gid).then(() => {
5. console.info("chown succeed");
6. }).catch((err: BusinessError) => {
7. console.error("chown failed with error:" + err);
8. });
```

## fileio.lchown7+

PhonePC/2in1TabletTVWearable

lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件，使用callback异步回调。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |
| callback | AsyncCallback<void> | 是 | 异步改变文件所有者之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let stat = fileio.statSync(filePath);
4. fileio.lchown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
5. // do something
6. });
```

## fileio.lchownSync7+

PhonePC/2in1TabletTVWearable

lchownSync(path: string, uid: number, gid: number): void

以同步方法基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待打开文件的应用沙箱路径。 |
| uid | number | 是 | 新的UID。 |
| gid | number | 是 | 新的GID。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stat = fileio.statSync(filePath);
3. fileio.lchownSync(filePath, stat.uid, stat.gid);
```

## fileio.createWatcher7+

PhonePC/2in1TabletTVWearable

createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher

监听文件或者目录的变化，使用callback异步回调。

说明

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filename | string | 是 | 待监视文件的应用沙箱路径。 |
| events | number | 是 | - 1: 监听文件或者目录是否发生重命名。  - 2：监听文件或者目录内容的是否修改。  - 3：两者都有。 |
| callback | AsyncCallback<number> | 是 | 每发生变化一次，调用一次此函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Watcher](js-apis-fileio.md#watcher7) | Promise对象。返回文件变化监听的实例。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
3. console.info("event: " + event + "errmsg: " + JSON.stringify(err));
4. });
```

## Readout

PhonePC/2in1TabletTVWearable

仅用于read方法，获取文件的读取结果。

说明

从API version 9开始废弃。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| bytesRead | number | 是 | 是 | 实际读取长度，单位为Byte。 |
| offset | number | 是 | 是 | 读取数据相对于缓冲区首地址的偏移，单位为Byte。 |
| buffer | ArrayBuffer | 是 | 是 | 保存读取数据的缓冲区。 |

## Stat

PhonePC/2in1TabletTVWearable

文件具体信息，在调用Stat的方法前，需要先通过[stat()](js-apis-fileio.md#fileiostat)方法（同步或异步）来构建一个Stat实例。

说明

从API version 9开始废弃，请使用[fileIo.Stat](js-apis-file-fs.md#stat)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

### 属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| dev | number | 是 | 否 | 标识包含该文件的主设备号。 |
| ino | number | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 表示文件类型及权限，其首 4 位表示文件类型，后 12 位表示权限。各特征位的含义如下：  - 0o170000：可用于获取文件类型的掩码。  - 0o140000：文件是套接字。  - 0o120000：文件是符号链接。  - 0o100000：文件是一般文件。  - 0o060000：文件属于块设备。  - 0o040000：文件是目录。  - 0o020000：文件是字符设备。  - 0o010000：文件是命名管道，即FIFO。  - 0o0700：可用于获取用户权限的掩码。  - 0o0400：用户读，对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。  - 0o0200：用户写，对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。  - 0o0100：用户执行，对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。  - 0o0070：可用于获取用户组权限的掩码。  - 0o0040：用户组读，对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。  - 0o0020：用户组写，对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。  - 0o0010：用户组执行，对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。  - 0o0007：可用于获取其他用户权限的掩码。  - 0o0004：其他读，对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。  - 0o0002：其他写，对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。  - 0o0001：其他执行，对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。 |
| nlink | number | 是 | 否 | 文件的硬链接数。 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| rdev | number | 是 | 否 | 标识包含该文件的从设备号。 |
| size | number | 是 | 否 | 文件的大小，单位为Byte。仅对普通文件有效。 |
| blocks | number | 是 | 否 | 文件占用的块数，计算时块大小按512B计算。 |
| atime | number | 是 | 否 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| mtime | number | 是 | 否 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |

### isBlockDevice

PhonePC/2in1TabletTVWearable

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isBlockDevice](js-apis-file-fs.md#isblockdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是块特殊设备。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isBLockDevice = fileio.statSync(filePath).isBlockDevice();
```

### isCharacterDevice

PhonePC/2in1TabletTVWearable

isCharacterDevice(): boolean

用于判断文件是否是字符特殊文件。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isCharacterDevice](js-apis-file-fs.md#ischaracterdevice)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isCharacterDevice = fileio.statSync(filePath).isCharacterDevice();
```

### isDirectory

PhonePC/2in1TabletTVWearable

isDirectory(): boolean

用于判断文件是否是目录。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isDirectory](js-apis-file-fs.md#isdirectory)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是目录。true为是，false为不是。 |

**示例：**

```
1. let dirPath = pathDir + "/test";
2. let isDirectory = fileio.statSync(dirPath).isDirectory();
```

### isFIFO

PhonePC/2in1TabletTVWearable

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isFIFO](js-apis-file-fs.md#isfifo)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是 FIFO。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isFIFO = fileio.statSync(filePath).isFIFO();
```

### isFile

PhonePC/2in1TabletTVWearable

isFile(): boolean

用于判断文件是否是普通文件。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isFile](js-apis-file-fs.md#isfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是普通文件。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isFile = fileio.statSync(filePath).isFile();
```

### isSocket

PhonePC/2in1TabletTVWearable

isSocket(): boolean

用于判断文件是否是套接字。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isSocket](js-apis-file-fs.md#issocket)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是套接字。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isSocket = fileio.statSync(filePath).isSocket();
```

### isSymbolicLink

PhonePC/2in1TabletTVWearable

isSymbolicLink(): boolean

用于判断文件是否是符号链接。

说明

从API version 9开始废弃，请使用[fileIo.Stat.isSymbolicLink](js-apis-file-fs.md#issymboliclink)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是符号链接。true为是，false为不是。 |

**示例：**

```
1. let filePath = pathDir + "/test";
2. let isSymbolicLink = fileio.statSync(filePath).isSymbolicLink();
```

## Watcher7+

PhonePC/2in1TabletTVWearable

Watcher是文件变化监听的实例，调用Watcher.stop()方法（同步或异步）来停止文件监听。

说明

从API version 10开始废弃。

### stop7+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

关闭watcher监听，使用Promise异步回调。

说明

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
3. console.info("event: " + event + "errmsg: " + JSON.stringify(err));
4. });
5. watcher.stop().then(() => {
6. console.info("close watcher succeed");
7. });
```

### stop7+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

关闭watcher监听，使用callback异步回调。

说明

从API version 10开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 以异步方法关闭watcher监听之后的回调。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
3. console.info("event: " + event + "errmsg: " + JSON.stringify(err));
4. });
5. watcher.stop(() => {
6. console.info("close watcher succeed");
7. })
```

## Stream

PhonePC/2in1TabletTVWearable

文件流，在调用Stream的方法前，需要先通过createStream()方法（同步或异步）来构建一个Stream实例。

说明

从API version 9开始废弃，请使用[fileIo.Stream](js-apis-file-fs.md#stream)替代。

### close7+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭文件流，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.close](js-apis-file-fs.md#close)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。返回表示异步关闭文件流的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. ss.close().then(() => {
5. console.info("close fileStream succeed");
6. }).catch((err: BusinessError) => {
7. console.error("close fileStream  failed with error:" + err);
8. });
```

### close7+

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.close](js-apis-file-fs.md#close-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步关闭文件流之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. ss.close((err: BusinessError) => {
5. // do something
6. });
```

### closeSync

PhonePC/2in1TabletTVWearable

closeSync(): void

同步关闭文件流。

说明

从API version 9开始废弃，请使用[fileIo.Stream.closeSync](js-apis-file-fs.md#closesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let ss = fileio.createStreamSync(filePath, "r+");
3. ss.closeSync();
```

### flush7+

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

刷新文件流，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.flush](js-apis-file-fs.md#flush)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。返回表示异步刷新文件流的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. ss.flush().then(() => {
5. console.info("flush succeed");
6. }).catch((err: BusinessError) => {
7. console.error("flush failed with error:" + err);
8. });
```

### flush7+

PhonePC/2in1TabletTVWearable

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.flush](js-apis-file-fs.md#flush-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步刷新文件流后的回调函数。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. ss.flush((err: BusinessError) => {
5. // do something
6. });
```

### flushSync7+

PhonePC/2in1TabletTVWearable

flushSync(): void

同步刷新文件流。

说明

从API version 9开始废弃，请使用[fileIo.Stream.flushSync](js-apis-file-fs.md#flushsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let ss = fileio.createStreamSync(filePath, "r+");
3. ss.flushSync();
```

### write7+

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

将数据写入流文件，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.write](js-apis-file-fs.md#write)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. class Option {
5. offset: number = 0;
6. length: number = 4096;
7. position: number = 0;
8. encoding: string = 'utf-8';
9. }
10. let option = new Option();
11. option.offset = 1;
12. option.length = 5;
13. option.position = 5;
14. ss.write("hello, world", option).then((number: number) => {
15. console.info("write succeed and size is:" + number);
16. }).catch((err: BusinessError) => {
17. console.error("write failed with error:" + err);
18. });
```

### write7+

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.write](js-apis-file-fs.md#write-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数，返回实际写入的长度，单位为Byte。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let filePath = pathDir + "/test.txt";
3. let ss = fileio.createStreamSync(filePath, "r+");
4. class Option {
5. offset: number = 0;
6. length: number = 4096;
7. position: number = 0;
8. encoding: string = 'utf-8';
9. }
10. let option = new Option();
11. option.offset = 1;
12. option.length = 5;
13. option.position = 5;
14. ss.write("hello, world", option, (err: BusinessError, bytesWritten: number) => {
15. if (bytesWritten) {
16. // do something
17. console.info("write succeed and size is:" + bytesWritten);
18. }
19. });
```

### writeSync7+

PhonePC/2in1TabletTVWearable

writeSync(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

以同步方法将数据写入流文件。

说明

从API version 9开始废弃，请使用[fileIo.Stream.writeSync](js-apis-file-fs.md#writesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer|string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望写入数据的长度。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let ss = fileio.createStreamSync(filePath,"r+");
3. class Option {
4. offset: number = 0;
5. length: number = 4096;
6. position: number = 0;
7. encoding: string = 'utf-8';
8. }
9. let option = new Option();
10. option.offset = 1;
11. option.length = 5;
12. option.position = 5;
13. let num = ss.writeSync("hello, world", option);
```

### read7+

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): Promise<ReadOut>

从流文件读取数据，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.read](js-apis-file-fs.md#read)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。  - position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReadOut](js-apis-fileio.md#readout)> | Promise对象。返回读取的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. import buffer from '@ohos.buffer';
3. let filePath = pathDir + "/test.txt";
4. let ss = fileio.createStreamSync(filePath, "r+");
5. let arrayBuffer = new ArrayBuffer(4096);
6. class Option {
7. offset: number = 0;
8. length: number = 4096;
9. position: number = 0;
10. }
11. let option = new Option();
12. option.offset = 1;
13. option.length = 5;
14. option.position = 5;
15. ss.read(arrayBuffer, option).then((readResult: fileio.ReadOut) => {
16. console.info("read data succeed");
17. let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
18. console.info(`The content of file: ${buf.toString()}`);
19. }).catch((err: BusinessError) => {
20. console.error("read data failed with error:" + err);
21. });
```

### read7+

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options: { position?: number; offset?: number; length?: number; }, callback: AsyncCallback<ReadOut>): void

从流文件读取数据，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.Stream.read](js-apis-file-fs.md#read-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  约束：offset+length<=buffer.size。 |
| callback | AsyncCallback<[ReadOut](js-apis-fileio.md#readout)> | 是 | 异步从流文件读取数据之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. import buffer from '@ohos.buffer';
3. let filePath = pathDir + "/test.txt";
4. let ss = fileio.createStreamSync(filePath, "r+");
5. let arrayBuffer = new ArrayBuffer(4096);
6. class Option {
7. offset: number = 0;
8. length: number = 4096;
9. position: number = 0;
10. }
11. let option = new Option();
12. option.offset = 1;
13. option.length = 5;
14. option.position = 5;
15. ss.read(arrayBuffer, option, (err: BusinessError, readResult: fileio.ReadOut) => {
16. if (readResult.bytesRead) {
17. console.info("read data succeed");
18. let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
19. console.info(`The content of file: ${buf.toString()}`);
20. }
21. });
```

### readSync7+

PhonePC/2in1TabletTVWearable

readSync(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): number

以同步方法从流文件读取数据。

说明

从API version 9开始废弃，请使用[fileIo.Stream.readSync](js-apis-file-fs.md#readsync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | Object | 否 | 支持如下选项：  - offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。  - length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。  - position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  约束：offset+length<=buffer.size。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let ss = fileio.createStreamSync(filePath, "r+");
3. class Option {
4. offset: number = 0;
5. length: number = 4096;
6. position: number = 0;
7. }
8. let option = new Option();
9. option.offset = 1;
10. option.length = 5;
11. option.position = 5;
12. let buf = new ArrayBuffer(4096)
13. let num = ss.readSync(buf, option);
```

## Dir

PhonePC/2in1TabletTVWearable

管理目录，在调用Dir的方法前，需要先通过opendir方法（同步或异步）来构建一个Dir实例。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

### read

PhonePC/2in1TabletTVWearable

read(): Promise<Dirent>

读取下一个目录项，使用Promise异步回调。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Dirent](js-apis-fileio.md#dirent)> | Promise对象。返回表示异步读取目录项的结果。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. dir.read().then((dirent: fileio.Dirent) => {
3. console.info("read succeed, the name of dirent is " + dirent.name);
4. }).catch((err: BusinessError) => {
5. console.error("read failed with error:" + err);
6. });
```

### read

PhonePC/2in1TabletTVWearable

read(callback: AsyncCallback<Dirent>): void

读取下一个目录项，使用callback异步回调。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Dirent](js-apis-fileio.md#dirent)> | 是 | 异步读取下一个目录项之后的回调。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. dir.read((err: BusinessError, dirent: fileio.Dirent) => {
3. if (dirent) {
4. // do something
5. console.info("read succeed, the name of file is " + dirent.name);
6. }
7. });
```

### readSync

PhonePC/2in1TabletTVWearable

readSync(): Dirent

同步读取下一个目录项。

说明

从API version 9开始废弃，请使用[fileIo.listFileSync](js-apis-file-fs.md#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Dirent](js-apis-fileio.md#dirent) | 表示一个目录项。 |

**示例：**

```
1. let dirent = dir.readSync();
```

### close7+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

异步关闭目录，使用promise形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. dir.close().then(() => {
3. console.info("close dir successfully");
4. });
```

### close7+

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

异步关闭目录，使用callback形式返回结果。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile-1)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. dir.close((err: BusinessError) => {
3. console.info("close dir successfully");
4. });
```

### closeSync

PhonePC/2in1TabletTVWearable

closeSync(): void

用于关闭目录。目录被关闭后，Dir中持有的文件描述将被释放，后续将无法从Dir中读取目录项。

说明

从API version 9开始废弃，请使用[fileIo.listFileSync](js-apis-file-fs.md#fileiolistfilesync)替代。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**示例：**

```
1. dir.closeSync();
```

## Dirent

PhonePC/2in1TabletTVWearable

在调用Dirent的方法前，需要先通过[dir.read()](js-apis-fileio.md#read)方法（同步或异步）来构建一个Dirent实例。

说明

从API version 9开始废弃，请使用[fileIo.listFile](js-apis-file-fs.md#fileiolistfile)替代。

**系统能力**：以下各项对应的系统能力均为SystemCapability.FileManagement.File.FileIO。

### 属性

| 名称 | 类型 | 只读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 目录项的名称。 |

### isBlockDevice

PhonePC/2in1TabletTVWearable

isBlockDevice(): boolean

用于判断当前目录项是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是块特殊设备。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isBLockDevice = dir.readSync().isBlockDevice();
```

### isCharacterDevice

PhonePC/2in1TabletTVWearable

isCharacterDevice(): boolean

用于判断当前目录项是否是字符特殊设备。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是字符特殊设备。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isCharacterDevice = dir.readSync().isCharacterDevice();
```

### isDirectory

PhonePC/2in1TabletTVWearable

isDirectory(): boolean

用于判断当前目录项是否是目录。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是目录。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isDirectory = dir.readSync().isDirectory();
```

### isFIFO

PhonePC/2in1TabletTVWearable

isFIFO(): boolean

用于判断当前目录项是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是FIFO。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isFIFO = dir.readSync().isFIFO();
```

### isFile

PhonePC/2in1TabletTVWearable

isFile(): boolean

用于判断当前目录项是否是普通文件。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是普通文件。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isFile = dir.readSync().isFile();
```

### isSocket

PhonePC/2in1TabletTVWearable

isSocket(): boolean

用于判断当前目录项是否是套接字。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是套接字。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isSocket = dir.readSync().isSocket();
```

### isSymbolicLink

PhonePC/2in1TabletTVWearable

isSymbolicLink(): boolean

用于判断当前目录项是否是符号链接。

说明

从API version 9开始废弃。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前目录项是否是符号链接。true为是，false为不是。 |

**示例：**

```
1. let dir = fileio.opendirSync(pathDir);
2. let isSymbolicLink = dir.readSync().isSymbolicLink();
```
