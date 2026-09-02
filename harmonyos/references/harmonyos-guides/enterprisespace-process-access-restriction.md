---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-process-access-restriction
title: 进程访问限制
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 进程访问限制
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:76819c3f6d66f686be6abfbe20f807aecf4727e2ad25f60561932211da679ac5
---

从API版本6.0.1(21)开始，支持应用配置系统服务进程对后台用户数据的访问控制。

## 场景介绍

Enterprise Space Kit支持应用设置系统服务进程不可访问后台用户数据的能力，同时支持获取系统服务进程管控不可访问后台用户数据的状态。另外，支持应用提供获取、新增和删除不可访问后台用户数据的系统服务进程列表的能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [setRestrictedAccessBackgroundUserdata](../harmonyos-references/enterprisespace-spacemanager.md#setrestrictedaccessbackgrounduserdata)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum), enable: boolean): Promise<void> | 设置系统服务进程不可访问后台用户数据。 |
| [getRestrictedAccessBackgroundUserdataStatus](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdatastatus)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum)): Promise<boolean> | 获取系统服务进程管控不可访问后台用户数据的状态。 |
| [getRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdataprocesslist)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum)): Promise<[ProcessConfigInfo](../harmonyos-references/enterprisespace-spacemanager.md#processconfiginfo)[]> | 获取不可访问后台用户数据的系统服务进程列表。 |
| [addRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#addrestrictedaccessbackgrounduserdataprocesslist)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum), processName: string, disallowPaths?: string[]): Promise<void> | 新增系统服务进程不可访问后台用户数据路径列表。 |
| [deleteRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#deleterestrictedaccessbackgrounduserdataprocesslist)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum), processName: string): Promise<void> | 删除系统服务进程不可访问后台用户数据路径列表。 |

## 开发步骤

1.导入进程访问限制API模块相关依赖。

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.进程访问限制API接口封装。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class RestrictedAccessProcessApi {
  static async setRestrictedAccessBackgroundUserdata(
    userData: spaceManager.UserDataEnum, enable: boolean): Promise<number> {
    try {
      await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
      hilog.info(DOMAIN, TAG,
        `Succeeded in setting restricted access background user data. userData:${userData},enable:${enable}`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to set restricted access background user data. Code:${err.code},message:${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async getRestrictedAccessBackgroundUserdataStatus(
    userData: spaceManager.UserDataEnum): Promise<boolean | undefined> {
    try {
      const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
      hilog.info(DOMAIN, TAG, `Succeeded in getting restricted access background user data status. status:${status}`);
      return status;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to get restricted access background user data status. Code:${err.code},message:${err.message}`);
      return undefined;
    }
  }

  static async getRestrictedAccessBackgroundUserdataProcessList(
    userData: spaceManager.UserDataEnum): Promise<spaceManager.ProcessConfigInfo[]> {
    try {
      let processConfigInfo: spaceManager.ProcessConfigInfo[] =
        await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
      hilog.info(DOMAIN, TAG, 'Succeeded in getting restricted access background user data process list.');
      return processConfigInfo;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get restricted access background user data process list.
        Code:${err.code},message:${err.message}`);
      return [];
    }
  }

  static async addRestrictedAccessBackgroundUserdataProcessList(
    userData: spaceManager.UserDataEnum, processName: string, disallowPaths: string[]): Promise<number> {
    try {
      await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
      hilog.info(DOMAIN, TAG, `Succeeded in adding restricted access background user data process list`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to add restricted access background user data process list.Code:${err.code},message:${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async deleteRestrictedAccessBackgroundUserdataProcessList(
    userData: spaceManager.UserDataEnum, processName: string): Promise<number> {
    try {
      await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
      hilog.info(DOMAIN, TAG, `Succeeded in deleting restricted access background user data process list`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to delete restricted access background user data process list.Code:${err.code},message:${err.message}`);
      return ErrCode.ERR;
    }
  }
}
```

3.导入进程访问限制业务实现相关依赖。

```typescript
import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { ErrCode } from '../../common/ErrCode';
import { RestrictedAccessProcessApi } from '../api/RestrictedAccessprocessApi'
import { hilog } from '@kit.PerformanceAnalysisKit';
```

4.进程访问限制业务相关实现。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct RestrictedAccessProcessPage {
  async setRestrictedAccessBackgroundUserdata() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const enable: boolean = false;
    if (await RestrictedAccessProcessApi.setRestrictedAccessBackgroundUserdata(userData, enable) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set restricted access background user data!');
      return;
    }
    // 处理后置逻辑
  }

  async getRestrictedAccessBackgroundUserdataStatus() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    let enable: boolean | undefined =
      await RestrictedAccessProcessApi.getRestrictedAccessBackgroundUserdataStatus(userData);
    if (enable === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to get restricted access background user data status!');
      return;
    }
    // 处理后置逻辑
  }

  async addRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 限制进程名，由用户传入
    const disallowPaths: string[] = ['path']; // 限制访问路径，由用户传入
    if (await RestrictedAccessProcessApi.addRestrictedAccessBackgroundUserdataProcessList(
        userData, processName, disallowPaths) !== ErrCode.OK) {
      // 处理异常逻辑
      hilog.error(DOMAIN, TAG, 'Failed to add restricted access background user data process list!');
      return;
    }
    // 处理后置逻辑
  }

  async getRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    let processConfigInfo: spaceManager.ProcessConfigInfo[] =
      await RestrictedAccessProcessApi.getRestrictedAccessBackgroundUserdataProcessList(userData);
    // 处理后置逻辑
  }

  async deleteRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 限制进程名，由用户传入
    if (await RestrictedAccessProcessApi.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName) !==
        ErrCode.OK) {
      // 处理异常逻辑
      hilog.error(DOMAIN, TAG, 'Failed to delete restricted access background user data process list!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setRestrictedAccessBackgroundUserdata'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setRestrictedAccessBackgroundUserdata();
          })
      }

      Row() {
        Button($r('app.string.getRestrictedAccessBackgroundUserdataStatus'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataStatus();
          })
      }

      Row() {
        Button($r('app.string.getRestrictedAccessBackgroundUserdataProcessList'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button($r('app.string.addRestrictedAccessBackgroundUserdataProcessList'))
          .buttonCommonStyle()
          .onClick(() => {
            this.addRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button($r('app.string.deleteRestrictedAccessBackgroundUserdataProcessList'))
          .buttonCommonStyle()
          .onClick(() => {
            this.deleteRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button($r('app.string.back'))
          .buttonCommonStyle()
          .onClick(() => {
            router.back();
          })
      }
    }
  }
}

@Extend(Button)
function buttonCommonStyle() {
  .width(400)
  .height(50)
  .backgroundColor('#6366F1')
  .fontColor('#FFFFFF')
  .fontSize(14)
  .margin({ left: 20, bottom: 5 })
}
```
